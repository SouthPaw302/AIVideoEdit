const $ = (id) => document.getElementById(id);

async function getJSON(url, options) {
  const res = await fetch(url, options);
  let body = null;
  try { body = await res.json(); } catch (_) {}
  if (!res.ok) throw new Error(body?.error || `${res.status} ${res.statusText}`);
  return body;
}

function esc(value) {
  return String(value ?? '').replace(/[&<>'"]/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;',"'":'&#39;','"':'&quot;'}[c]));
}

function badge(ok, label, detail) {
  return `<div class="cap"><span class="dot ${ok ? 'ok' : 'bad'}"></span><div><strong>${esc(label)}</strong><small>${esc(detail)}</small></div></div>`;
}

async function loadHealth() {
  try {
    const data = await getJSON('/api/health');
    $('health').textContent = data.ok ? 'Backend online' : 'Backend issue';
    $('health').classList.toggle('online', data.ok);
  } catch (_) {
    $('health').textContent = 'Backend offline';
  }
}

async function loadCapabilities() {
  const data = await getJSON('/api/capabilities');
  $('capabilities').innerHTML = data.capabilities.map(c => badge(c.available, c.name, c.detail)).join('');
}

function formatTime(ts) {
  return ts ? new Date(ts * 1000).toLocaleTimeString() : '—';
}

function formatBytes(n) {
  if (!Number.isFinite(Number(n))) return '—';
  const units = ['B','KB','MB','GB'];
  let value = Number(n), i = 0;
  while (value >= 1024 && i < units.length - 1) { value /= 1024; i++; }
  return `${value.toFixed(i ? 1 : 0)} ${units[i]}`;
}

async function loadJobs() {
  const data = await getJSON('/api/jobs');
  if (!data.jobs.length) {
    $('jobs').innerHTML = '<p class="muted">No jobs yet.</p>';
    return;
  }
  $('jobs').innerHTML = data.jobs.map(job => `
    <div class="job">
      <div><strong>${esc(job.project)}</strong><small>${esc(job.type)} · ${esc(job.id)}</small></div>
      <div class="job-status ${esc(job.status)}">${esc(job.status)}</div>
      <div class="result">${esc(job.result || 'Waiting…')}</div>
      <small>${formatTime(job.created_at)}</small>
    </div>`).join('');
}

async function loadAssets() {
  const data = await getJSON('/api/assets');
  if (!data.assets.length) {
    $('assets').innerHTML = '<p class="muted">No media in the workspace yet.</p>';
    return;
  }
  $('assets').innerHTML = data.assets.map(asset => {
    const m = asset.metadata || {};
    const dims = m.width && m.height ? `${m.width}×${m.height}` : '';
    const duration = m.duration_seconds != null ? `${m.duration_seconds}s` : '';
    const info = [dims, duration, m.video_codec, formatBytes(asset.size_bytes)].filter(Boolean).join(' · ');
    const thumb = asset.thumbnail_url
      ? `<img class="thumb" src="${esc(asset.thumbnail_url)}?t=${Date.now()}" alt="Preview" />`
      : `<div class="thumb placeholder">${esc(asset.status)}</div>`;
    return `<article class="asset">${thumb}<div class="asset-copy"><strong>${esc(asset.filename)}</strong><small>${esc(asset.project)} · ${esc(asset.id)}</small><p>${esc(info || 'Analyzing media…')}</p><span class="asset-state ${esc(asset.status)}">${esc(asset.status)}</span></div></article>`;
  }).join('');
}

async function runJob() {
  $('runJob').disabled = true;
  try {
    await getJSON('/api/jobs', {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({type: 'ffmpeg_check', project: $('project').value.trim() || 'prototype'})
    });
    await loadJobs();
  } catch (err) {
    $('uploadMessage').textContent = err.message;
  } finally {
    $('runJob').disabled = false;
  }
}

async function uploadMedia() {
  const file = $('mediaFile').files[0];
  if (!file) {
    $('uploadMessage').textContent = 'Choose a media file first.';
    return;
  }
  $('upload').disabled = true;
  $('uploadMessage').textContent = `Uploading ${file.name} (${formatBytes(file.size)})…`;
  const project = $('project').value.trim() || 'prototype';
  try {
    const url = `/api/assets?filename=${encodeURIComponent(file.name)}&project=${encodeURIComponent(project)}`;
    const data = await getJSON(url, {
      method: 'POST',
      headers: {'Content-Type': file.type || 'application/octet-stream'},
      body: file
    });
    $('uploadMessage').textContent = `Stored ${data.asset.filename}; analysis job ${data.job.id} started.`;
    await Promise.all([loadAssets(), loadJobs()]);
    setTimeout(() => Promise.all([loadAssets(), loadJobs()]), 1200);
  } catch (err) {
    $('uploadMessage').textContent = err.message;
  } finally {
    $('upload').disabled = false;
  }
}

$('upload').addEventListener('click', uploadMedia);
$('runJob').addEventListener('click', runJob);
$('refresh').addEventListener('click', loadJobs);
$('refreshAssets').addEventListener('click', loadAssets);

Promise.allSettled([loadHealth(), loadCapabilities(), loadJobs(), loadAssets()]);
setInterval(() => Promise.allSettled([loadJobs(), loadAssets()]), 3000);
