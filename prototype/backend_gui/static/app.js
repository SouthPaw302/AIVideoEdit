const $ = id => document.getElementById(id);
let currentAssetId = null;
let assetsCache = [];
let systemState = null;
let coreState = null;
let productionState = null;

async function api(url, options) {
  const res = await fetch(url, options);
  let body = null;
  try { body = await res.json(); } catch (_) {}
  if (!res.ok) throw new Error(body?.error || `${res.status} ${res.statusText}`);
  return body;
}
async function toolCall(name, arguments_ = {}) {
  const d = await api('/api/tools/call', {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({name, arguments: arguments_})
  });
  return d.result;
}
const esc = v => String(v ?? '').replace(/[&<>'"]/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;',"'":'&#39;','"':'&quot;'}[c]));
const projectId = () => $('project').value || 'prototype';

function formatBytes(n) {
  n = Number(n); if (!Number.isFinite(n)) return '—';
  const u=['B','KB','MB','GB','TB']; let i=0; while(n>=1024&&i<u.length-1){n/=1024;i++;}
  return `${n.toFixed(i?1:0)} ${u[i]}`;
}
function formatDuration(n) { n=Number(n); if(!Number.isFinite(n)) return '—'; const m=Math.floor(n/60), s=Math.round(n%60); return `${m}:${String(s).padStart(2,'0')}`; }
function formatTime(ts) { return ts ? new Date(ts*1000).toLocaleTimeString() : '—'; }
function friendlyJob(type){ return ({analyze_media:'Reading media',make_proxy:'Making preview copy',extract_review_frames:'Creating review snapshots',qc_media:'Checking media',ffmpeg_check:'Testing video engine',sync_project:'Backing up project'})[type] || type.replaceAll('_',' '); }
function friendlyStatus(status){ return ({complete:'Done',failed:'Needs attention',running:'Working',queued:'Waiting',interrupted:'Stopped'})[status] || status; }
function friendlyStage(stage){ return ({INITIALIZED:'Project started',SOURCE_INGESTED:'Source media added',REFERENCES_ANALYZED:'Media analyzed',APPROACH_ESTABLISHED:'Creative approach set',STORYBOARD_LOCKED:'Storyboard locked',SHOT_PACKAGES_BUILT:'Shots prepared',SHOT_PROOFS_ACCEPTED:'Shot proofs accepted',FX_LOCKED:'Effects locked',ASSEMBLED:'Video assembled',FINAL_QC_PASSED:'Final check passed',ARCHIVED:'Archived'})[stage] || String(stage||'').replaceAll('_',' ').toLowerCase(); }

async function loadHealth(){
  try { await api('/api/health'); $('health').textContent='Ready'; $('health').classList.add('online'); }
  catch(_){ $('health').textContent='Offline'; $('health').classList.remove('online'); }
}
async function loadCapabilities(){
  const d=await api('/api/capabilities');
  const caps=d.capabilities.map(c=>c.name==='Python'&&!c.available?{...c,available:true,detail:'Running this app'}:c);
  $('capabilities').innerHTML=caps.map(c=>`<div class="cap"><span class="dot ${c.available?'ok':'bad'}"></span><div><strong>${esc(c.name)}</strong><small>${esc(c.available?'Ready':c.detail)}</small></div></div>`).join('');
}
async function loadCoreStatus(){
  try {
    coreState = await api('/api/core');
    if(coreState.bootstrapped){
      $('coreStatus').textContent='Current-main production engine loaded and attested.';
      $('coreDetails').textContent=`main ${String(coreState.main_commit||'').slice(0,12)} · ${coreState.capability_count||0} media capabilities · ${coreState.fx_count||0} reusable FX · guard ${coreState.guard_result||'unknown'}`;
      $('loadCore').textContent='Refresh current core';
    } else {
      $('coreStatus').textContent='Canonical production engine is not loaded yet.';
      $('coreDetails').textContent='Load it to use the production contracts, capability matrix and reusable FX from current main.';
      $('loadCore').textContent='Load current core';
    }
  } catch (_) {
    coreState = null;
    $('coreStatus').textContent='Start the full stack to use the canonical production engine.';
    $('coreDetails').textContent='';
  }
  updateProductionButtons();
}
async function bootstrapCore(){
  $('loadCore').disabled=true;
  $('coreStatus').textContent='Loading and verifying current main…';
  $('coreDetails').textContent='This can take a moment the first time.';
  try {
    const d=await api('/api/core/bootstrap',{method:'POST',headers:{'Content-Type':'application/json'},body:'{}'});
    coreState=d;
    $('uploadMessage').textContent=d.bootstrapped?'Production engine loaded.':'Production engine could not be loaded.';
  } catch(e) {
    $('coreStatus').textContent='Production engine needs attention.';
    $('coreDetails').textContent=e.message;
  } finally {
    $('loadCore').disabled=false;
    await Promise.allSettled([loadCoreStatus(),loadSystem(),loadProductionStatus()]);
  }
}
function updateProductionButtons(){
  const initialized=!!productionState?.initialized;
  $('startProjectEngine').hidden=initialized;
  $('verifyProjectEngine').hidden=!initialized;
  $('syncProductionAssets').hidden=!initialized;
  $('advanceProduction').hidden=!initialized || !productionState?.next_stage;
  $('startProjectEngine').disabled=!coreState?.bootstrapped;
  if(productionState?.next_stage){ $('advanceProduction').textContent=`Continue: ${friendlyStage(productionState.next_stage)}`; }
}
async function loadProductionStatus(){
  if(!$('project').value){ return; }
  try {
    productionState = await toolCall('production.status',{project_id:projectId()});
    if(!productionState.initialized){
      $('productionStatus').textContent=coreState?.bootstrapped?'This project is not connected to the production engine yet.':'Load the canonical core first, then start the project engine.';
    } else {
      const media = productionState.workstation_asset_sync_complete ? ` · ${productionState.workstation_ready_asset_count}/${productionState.workstation_asset_count} media synced` : ' · media not synced';
      const verify = productionState.guard_pass ? 'verified' : 'needs verification';
      $('productionStatus').textContent=`${friendlyStage(productionState.stage||'INITIALIZED')} · ${verify}${media}${productionState.next_stage?` · next: ${friendlyStage(productionState.next_stage)}`:''}.`;
    }
  } catch(e) {
    productionState=null;
    $('productionStatus').textContent=e.message;
  }
  updateProductionButtons();
}
async function startProjectEngine(){
  $('startProjectEngine').disabled=true;
  $('productionStatus').textContent='Creating an isolated production workspace and verifying it…';
  try {
    if(!coreState?.bootstrapped){ await bootstrapCore(); }
    if(!coreState?.bootstrapped) throw new Error('Canonical core is not loaded.');
    productionState=await toolCall('production.initialize',{project_id:projectId()});
    $('productionStatus').textContent=productionState.guard_pass?`Production workspace ready · ${friendlyStage(productionState.stage||'INITIALIZED')}.`:'Production workspace was created but the canonical guard did not pass.';
  } catch(e){
    $('productionStatus').textContent=e.message;
  } finally {
    $('startProjectEngine').disabled=false;
    await loadProductionStatus();
  }
}
async function syncProductionAssets(){
  $('syncProductionAssets').disabled=true;
  $('productionStatus').textContent='Syncing workstation media into the canonical project manifests…';
  try {
    productionState=await toolCall('production.sync_assets',{project_id:projectId()});
    $('productionStatus').textContent=`Synced ${productionState.asset_count||0} media items to the production engine. Run Verify project before relying on this state.`;
  } catch(e){
    $('productionStatus').textContent=e.message;
  } finally {
    $('syncProductionAssets').disabled=false;
    await loadProductionStatus();
  }
}
async function advanceProduction(){
  if(!productionState?.next_stage) return;
  const target=productionState.next_stage;
  $('advanceProduction').disabled=true;
  $('productionStatus').textContent=`Checking whether the project can continue to ${friendlyStage(target)}…`;
  try {
    const result=await toolCall('production.advance',{project_id:projectId(),target_stage:target});
    productionState=result;
    if(result.advanced){
      $('productionStatus').textContent=`Continued to ${friendlyStage(result.stage)}. Canonical guard PASS.`;
    } else {
      $('productionStatus').textContent=`Could not continue. ${result.guard_stderr||result.error||'Required production evidence is still missing.'}`;
    }
  } catch(e){
    $('productionStatus').textContent=e.message;
  } finally {
    $('advanceProduction').disabled=false;
    await loadProductionStatus();
  }
}
async function verifyProjectEngine(){
  $('verifyProjectEngine').disabled=true;
  $('productionStatus').textContent='Running the canonical production guard…';
  try {
    productionState=await toolCall('production.guard',{project_id:projectId()});
    $('productionStatus').textContent=productionState.guard_pass?`Verified · ${friendlyStage(productionState.stage||'INITIALIZED')} · guard PASS.`:`Verification failed. ${productionState.stderr||'Project state needs attention.'}`;
  } catch(e){
    $('productionStatus').textContent=e.message;
  } finally {
    $('verifyProjectEngine').disabled=false;
    await loadProductionStatus();
  }
}
async function loadSystem(){
  try {
    systemState = await api('/api/system');
    const s = systemState;
    const coreLabel=s.core?.bootstrapped?'core loaded':'core not loaded';
    $('systemStats').textContent = `${s.workers} workers · ${s.queue_depth} waiting · ${formatBytes(s.disk?.free)} free · storage: ${s.storage?.mode || 'local'} · ${coreLabel} · ${s.tool_count||0} agent tools`;
    $('syncProject').hidden = !s.storage?.configured;
  } catch (_) {
    systemState = null;
    $('systemStats').textContent = 'Run stack.py or the platform launcher to enable queued workers and storage telemetry.';
    $('syncProject').hidden = true;
  }
}
async function loadProjects(selectId){
  const d=await api('/api/projects');
  $('project').innerHTML=d.projects.map(p=>`<option value="${esc(p.id)}">${esc(p.name)}</option>`).join('');
  if(selectId && d.projects.some(p=>p.id===selectId)) $('project').value=selectId;
}
function updateNextAction(){
  const title=$('nextActionTitle'), text=$('nextActionText'), button=$('nextActionButton');
  button.hidden=true; button.onclick=null;
  if(!assetsCache.length){ title.textContent='Add your first media file'; text.textContent='Choose a video, song, or image above, then click “Add to project”.'; return; }
  const a=assetsCache.find(x=>x.id===currentAssetId) || assetsCache[0];
  if(!currentAssetId){ title.textContent='Choose a file from Your media'; text.textContent='Pick the video or audio you want to work on next, or prepare the whole project at once.'; return; }
  if(a.status==='analyzing'||a.status==='uploaded'){ title.textContent='Reading your media…'; text.textContent='The app is checking the file and preparing its basic information.'; return; }
  if(a.status==='failed'){ title.textContent='This file needs attention'; text.textContent=a.error||'The app could not prepare this media.'; return; }
  if(!a.proxy_url&&a.metadata?.video_codec){ title.textContent='Make a smooth preview copy'; text.textContent='This creates a smaller version that is easier to play while you work.'; button.textContent='Make preview copy'; button.hidden=false; button.onclick=()=>operation('make_proxy'); return; }
  if(!(a.review_frames||[]).length&&a.metadata?.video_codec){ title.textContent='Create review snapshots'; text.textContent='Generate six frames across the video so you can quickly inspect the whole piece.'; button.textContent='Create snapshots'; button.hidden=false; button.onclick=()=>operation('extract_review_frames'); return; }
  if(a.qc?.status!=='pass'){ title.textContent='Check the media'; text.textContent='Verify that the file can be decoded cleanly before you continue editing.'; button.textContent='Check media'; button.hidden=false; button.onclick=()=>operation('qc_media'); return; }
  title.textContent='This media is ready'; text.textContent='Preview copy, review snapshots, and media check are complete.';
}
async function loadAssets(){
  const d=await api(`/api/assets?project=${encodeURIComponent(projectId())}`); assetsCache=d.assets;
  if(!d.assets.length){ $('assets').innerHTML='<div class="empty-list"><strong>No media yet</strong><small>Add a file above to get started.</small></div>'; currentAssetId=null; showInspector(null); updateNextAction(); return; }
  $('assets').innerHTML=d.assets.map(a=>{
    const m=a.metadata||{}; const selected=a.id===currentAssetId?' selected':'';
    const thumb=a.thumbnail_url?`<img src="${esc(a.thumbnail_url)}" alt="">`:`<div class="mini-placeholder">${esc(a.status==='ready'?'media':a.status)}</div>`;
    const qc=a.qc?.status||'unchecked'; const label=qc==='pass'?'checked':qc==='fail'?'issue':'';
    return `<button class="asset-row${selected}" data-asset="${esc(a.id)}">${thumb}<span><strong>${esc(a.filename)}</strong><small>${esc([m.width&&m.height?`${m.width}×${m.height}`:'',formatDuration(m.duration_seconds),formatBytes(a.size_bytes)].filter(Boolean).join(' · '))}</small></span><em class="mini-qc ${esc(qc)}">${esc(label)}</em></button>`;
  }).join('');
  document.querySelectorAll('[data-asset]').forEach(el=>el.addEventListener('click',()=>selectAsset(el.dataset.asset)));
  if(currentAssetId){ const a=d.assets.find(x=>x.id===currentAssetId); showInspector(a||null); }
  updateNextAction();
}
function selectAsset(id){ currentAssetId=id; const a=assetsCache.find(x=>x.id===id); showInspector(a); loadAssets(); }
function showInspector(a){
  $('emptyInspector').hidden=!!a; $('assetInspector').hidden=!a; if(!a)return;
  const m=a.metadata||{}; $('assetTitle').textContent=a.filename; $('assetSubtitle').textContent=`${formatBytes(a.size_bytes)} · ${a.status==='ready'?'Ready to work with':a.status}`;
  const qc=a.qc?.status||'unchecked'; $('qcBadge').textContent=qc==='pass'?'CHECKED':qc==='fail'?'CHECK FAILED':'NOT CHECKED'; $('qcBadge').className=`pill ${qc}`;
  const url=a.proxy_url||a.source_url;
  if(url&&m.video_codec) $('preview').innerHTML=`<video controls preload="metadata" poster="${esc(a.thumbnail_url||'')}"><source src="${esc(url)}"></video>`;
  else if(url&&m.audio_codec) $('preview').innerHTML=`<audio controls src="${esc(url)}"></audio>`;
  else if(a.thumbnail_url) $('preview').innerHTML=`<img src="${esc(a.thumbnail_url)}" alt="Preview">`;
  else $('preview').innerHTML='<div class="preview-placeholder">Preparing preview…</div>';
  const rows=[['Length',formatDuration(m.duration_seconds)],['Video',m.video_codec||'—'],['Size',m.width&&m.height?`${m.width} × ${m.height}`:'—'],['Frame rate',m.fps||'—'],['Audio',m.audio_codec||'—'],['File size',formatBytes(a.size_bytes)],['Preview copy',a.proxy_url?'Ready':'Not made yet'],['Media check',qc==='pass'?'Passed':qc==='fail'?'Failed':'Not checked']];
  $('metadata').innerHTML=rows.map(([k,v])=>`<div><small>${esc(k)}</small><strong>${esc(v)}</strong></div>`).join('');
  $('reviewFrames').innerHTML=(a.review_frames||[]).map(u=>`<img src="${esc(u)}" alt="Review snapshot">`).join('');
}
async function loadJobs(){
  const d=await api(`/api/jobs?project=${encodeURIComponent(projectId())}`);
  if(!d.jobs.length){$('jobs').innerHTML='<p class="muted">No background work yet.</p>';return;}
  $('jobs').innerHTML=d.jobs.slice(0,20).map(j=>`<div class="job"><div><strong>${esc(friendlyJob(j.type))}</strong><small>${formatTime(j.created_at)}</small></div><span class="job-state ${esc(j.status)}">${esc(friendlyStatus(j.status))}</span><div class="progress"><i style="width:${Number(j.progress||0)}%"></i></div><small class="job-result">${esc(j.result||'Working…')}</small></div>`).join('');
}
async function uploadMedia(){
  const file=$('mediaFile').files[0]; if(!file){$('uploadMessage').textContent='Choose a file first.';return;}
  $('upload').disabled=true; $('uploadMessage').textContent=`Adding ${file.name}…`;
  try{ const d=await api(`/api/assets?filename=${encodeURIComponent(file.name)}&project=${encodeURIComponent(projectId())}`,{method:'POST',headers:{'Content-Type':file.type||'application/octet-stream'},body:file}); currentAssetId=d.asset.id; $('uploadMessage').textContent='Added. Preparing media…'; await refreshAll(); }
  catch(e){$('uploadMessage').textContent=e.message;} finally{$('upload').disabled=false;}
}
async function operation(type){
  if(!currentAssetId)return;
  try{ await api('/api/jobs',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({type,project:projectId(),asset_id:currentAssetId})}); await loadJobs(); updateNextAction(); }
  catch(e){$('uploadMessage').textContent=e.message;}
}
async function prepareProject(){
  $('prepareProject').disabled=true; $('uploadMessage').textContent='Preparing everything that still needs work…';
  try { const d=await api(`/api/projects/${encodeURIComponent(projectId())}/prepare`,{method:'POST'}); $('uploadMessage').textContent=d.count?`${d.count} background tasks added.`:'Everything is already prepared.'; await loadJobs(); }
  catch(e){ $('uploadMessage').textContent=e.message; }
  finally { $('prepareProject').disabled=false; }
}
async function syncProject(){
  $('syncProject').disabled=true; $('uploadMessage').textContent='Starting project backup…';
  try { await api(`/api/projects/${encodeURIComponent(projectId())}/sync`,{method:'POST'}); $('uploadMessage').textContent='Backup queued.'; await loadJobs(); }
  catch(e){ $('uploadMessage').textContent=e.message; }
  finally { $('syncProject').disabled=false; }
}
async function deleteAsset(){
  if(!currentAssetId||!confirm('Remove this media and its local preview files from this project?')) return;
  await api(`/api/assets/${encodeURIComponent(currentAssetId)}`,{method:'DELETE'}); currentAssetId=null; await refreshAll();
}
async function createProject(){
  const name=$('newProjectName').value.trim(); if(!name)return;
  const d=await api('/api/projects',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({name})}); await loadProjects(d.project.id); $('newProjectName').value=''; productionState=null; await refreshAll();
}
async function refreshAll(){ await Promise.allSettled([loadAssets(),loadJobs(),loadSystem(),loadCoreStatus(),loadProductionStatus()]); }

$('upload').addEventListener('click',uploadMedia);
$('project').addEventListener('change',()=>{currentAssetId=null;productionState=null;refreshAll();});
$('refreshAssets').addEventListener('click',loadAssets);
$('refreshJobs').addEventListener('click',loadJobs);
$('runJob').addEventListener('click',()=>api('/api/jobs',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({type:'ffmpeg_check',project:projectId()})}).then(loadJobs));
$('prepareProject').addEventListener('click',prepareProject);
$('syncProject').addEventListener('click',syncProject);
$('loadCore').addEventListener('click',bootstrapCore);
$('startProjectEngine').addEventListener('click',startProjectEngine);
$('syncProductionAssets').addEventListener('click',syncProductionAssets);
$('advanceProduction').addEventListener('click',advanceProduction);
$('verifyProjectEngine').addEventListener('click',verifyProjectEngine);
$('deleteAsset').addEventListener('click',deleteAsset);
document.querySelectorAll('[data-op]').forEach(b=>b.addEventListener('click',()=>operation(b.dataset.op)));
$('newProject').addEventListener('click',()=>$('projectDialog').showModal());
$('createProject').addEventListener('click',e=>{e.preventDefault();createProject().then(()=>$('projectDialog').close());});

(async()=>{ await Promise.allSettled([loadHealth(),loadCapabilities(),loadProjects(),loadSystem(),loadCoreStatus()]); await refreshAll(); })();
setInterval(()=>refreshAll(),2500);
