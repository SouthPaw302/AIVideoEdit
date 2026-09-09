const $ = id => document.getElementById(id);
let currentAssetId = null;
let assetsCache = [];

async function api(url, options) {
  const res = await fetch(url, options);
  let body = null;
  try { body = await res.json(); } catch (_) {}
  if (!res.ok) throw new Error(body?.error || `${res.status} ${res.statusText}`);
  return body;
}
const esc = v => String(v ?? '').replace(/[&<>'"]/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;',"'":'&#39;','"':'&quot;'}[c]));
const projectId = () => $('project').value || 'prototype';

function formatBytes(n) {
  n = Number(n); if (!Number.isFinite(n)) return '—';
  const u=['B','KB','MB','GB']; let i=0; while(n>=1024&&i<u.length-1){n/=1024;i++;}
  return `${n.toFixed(i?1:0)} ${u[i]}`;
}
function formatDuration(n) { n=Number(n); if(!Number.isFinite(n)) return '—'; const m=Math.floor(n/60), s=Math.round(n%60); return `${m}:${String(s).padStart(2,'0')}`; }
function formatTime(ts) { return ts ? new Date(ts*1000).toLocaleTimeString() : '—'; }

async function loadHealth(){
  try { const d=await api('/api/health'); $('health').textContent=`Backend online · ${d.version}`; $('health').classList.add('online'); }
  catch(_){ $('health').textContent='Backend offline'; $('health').classList.remove('online'); }
}
async function loadCapabilities(){
  const d=await api('/api/capabilities');
  const caps=d.capabilities.map(c=>{
    if(c.name==='Python' && !c.available){
      return {...c,available:true,detail:'Backend is running under Python; Windows PATH alias does not expose python3.'};
    }
    return c;
  });
  $('capabilities').innerHTML=caps.map(c=>`<div class="cap"><span class="dot ${c.available?'ok':'bad'}"></span><div><strong>${esc(c.name)}</strong><small>${esc(c.detail)}</small></div></div>`).join('');
}
async function loadProjects(selectId){
  const d=await api('/api/projects');
  $('project').innerHTML=d.projects.map(p=>`<option value="${esc(p.id)}">${esc(p.name)}</option>`).join('');
  if(selectId && d.projects.some(p=>p.id===selectId)) $('project').value=selectId;
}
async function loadAssets(){
  const d=await api(`/api/assets?project=${encodeURIComponent(projectId())}`); assetsCache=d.assets;
  if(!d.assets.length){ $('assets').innerHTML='<p class="muted">No media yet.</p>'; currentAssetId=null; showInspector(null); return; }
  $('assets').innerHTML=d.assets.map(a=>{
    const m=a.metadata||{}; const selected=a.id===currentAssetId?' selected':'';
    const thumb=a.thumbnail_url?`<img src="${esc(a.thumbnail_url)}" alt="">`:`<div class="mini-placeholder">${esc(a.status)}</div>`;
    const qc=a.qc?.status||'unchecked';
    return `<button class="asset-row${selected}" data-asset="${esc(a.id)}">${thumb}<span><strong>${esc(a.filename)}</strong><small>${esc([m.width&&m.height?`${m.width}×${m.height}`:'',formatDuration(m.duration_seconds),formatBytes(a.size_bytes)].filter(Boolean).join(' · '))}</small></span><em class="mini-qc ${esc(qc)}">${esc(qc)}</em></button>`;
  }).join('');
  document.querySelectorAll('[data-asset]').forEach(el=>el.addEventListener('click',()=>selectAsset(el.dataset.asset)));
  if(currentAssetId){ const a=d.assets.find(x=>x.id===currentAssetId); showInspector(a||null); }
}
function selectAsset(id){ currentAssetId=id; const a=assetsCache.find(x=>x.id===id); showInspector(a); loadAssets(); }
function showInspector(a){
  $('emptyInspector').hidden=!!a; $('assetInspector').hidden=!a; if(!a)return;
  const m=a.metadata||{}; $('assetTitle').textContent=a.filename; $('assetSubtitle').textContent=`${a.id} · ${formatBytes(a.size_bytes)} · ${a.status}`;
  const qc=a.qc?.status||'unchecked'; $('qcBadge').textContent=qc.toUpperCase(); $('qcBadge').className=`pill ${qc}`;
  const url=a.proxy_url||a.source_url;
  if(url && m.video_codec) $('preview').innerHTML=`<video controls preload="metadata" poster="${esc(a.thumbnail_url||'')}"><source src="${esc(url)}"></video>`;
  else if(url && m.audio_codec) $('preview').innerHTML=`<audio controls src="${esc(url)}"></audio>`;
  else if(a.thumbnail_url) $('preview').innerHTML=`<img src="${esc(a.thumbnail_url)}" alt="Preview">`;
  else $('preview').innerHTML=`<div class="preview-placeholder">${esc(a.status)}</div>`;
  const rows=[['Duration',formatDuration(m.duration_seconds)],['Video',m.video_codec||'—'],['Resolution',m.width&&m.height?`${m.width} × ${m.height}`:'—'],['FPS',m.fps||'—'],['Audio',m.audio_codec||'—'],['SHA-256',a.sha256?`${a.sha256.slice(0,16)}…`:'—'],['Proxy',a.proxy_url?'Ready':'Not built'],['QC',qc]];
  $('metadata').innerHTML=rows.map(([k,v])=>`<div><small>${esc(k)}</small><strong>${esc(v)}</strong></div>`).join('');
  $('reviewFrames').innerHTML=(a.review_frames||[]).map(u=>`<img src="${esc(u)}" alt="Review frame">`).join('');
}
async function loadJobs(){
  const d=await api(`/api/jobs?project=${encodeURIComponent(projectId())}`);
  if(!d.jobs.length){$('jobs').innerHTML='<p class="muted">No jobs yet.</p>';return;}
  $('jobs').innerHTML=d.jobs.slice(0,20).map(j=>`<div class="job"><div><strong>${esc(j.type.replaceAll('_',' '))}</strong><small>${esc(j.id)} · ${formatTime(j.created_at)}</small></div><span class="job-state ${esc(j.status)}">${esc(j.status)}</span><div class="progress"><i style="width:${Number(j.progress||0)}%"></i></div><small class="job-result">${esc(j.result||'Working…')}</small></div>`).join('');
}
async function uploadMedia(){
  const file=$('mediaFile').files[0]; if(!file){$('uploadMessage').textContent='Choose a file first.';return;}
  $('upload').disabled=true; $('uploadMessage').textContent=`Uploading ${file.name}…`;
  try{ const d=await api(`/api/assets?filename=${encodeURIComponent(file.name)}&project=${encodeURIComponent(projectId())}`,{method:'POST',headers:{'Content-Type':file.type||'application/octet-stream'},body:file}); currentAssetId=d.asset.id; $('uploadMessage').textContent='Stored. Analysis started.'; await refreshAll(); }
  catch(e){$('uploadMessage').textContent=e.message;} finally{$('upload').disabled=false;}
}
async function operation(type){
  if(!currentAssetId)return;
  try{ await api('/api/jobs',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({type,project:projectId(),asset_id:currentAssetId})}); await loadJobs(); }
  catch(e){$('uploadMessage').textContent=e.message;}
}
async function deleteAsset(){
  if(!currentAssetId || !confirm('Delete this asset and its local derivatives?')) return;
  await api(`/api/assets/${encodeURIComponent(currentAssetId)}`,{method:'DELETE'}); currentAssetId=null; await refreshAll();
}
async function createProject(){
  const name=$('newProjectName').value.trim(); if(!name)return;
  const d=await api('/api/projects',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({name})}); await loadProjects(d.project.id); $('newProjectName').value=''; await refreshAll();
}
async function refreshAll(){ await Promise.allSettled([loadAssets(),loadJobs()]); }

$('upload').addEventListener('click',uploadMedia);
$('project').addEventListener('change',()=>{currentAssetId=null;refreshAll();});
$('refreshAssets').addEventListener('click',loadAssets);
$('refreshJobs').addEventListener('click',loadJobs);
$('runJob').addEventListener('click',()=>api('/api/jobs',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({type:'ffmpeg_check',project:projectId()})}).then(loadJobs));
$('deleteAsset').addEventListener('click',deleteAsset);
document.querySelectorAll('[data-op]').forEach(b=>b.addEventListener('click',()=>operation(b.dataset.op)));
$('newProject').addEventListener('click',()=>$('projectDialog').showModal());
$('createProject').addEventListener('click',e=>{e.preventDefault();createProject().then(()=>$('projectDialog').close());});

(async()=>{ await Promise.allSettled([loadHealth(),loadCapabilities(),loadProjects()]); await refreshAll(); })();
setInterval(()=>refreshAll(),2500);
