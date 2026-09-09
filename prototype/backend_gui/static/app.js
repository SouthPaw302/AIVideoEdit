const $ = (id) => document.getElementById(id);

async function getJSON(url, options) {
  const res = await fetch(url, options);
  if (!res.ok) throw new Error(`${res.status} ${res.statusText}`);
  return res.json();
}

function badge(ok, label, detail) {
  return `<div class="cap"><span class="dot ${ok ? 'ok' : 'bad'}"></span><div><strong>${label}</strong><small>${detail}</small></div></div>`;
}

async function loadHealth() {
  try {
    const data = await getJSON('/api/health');
    $('health').textContent = data.ok ? 'Backend online' : 'Backend issue';
    $('health').classList.toggle('online', data.ok);
  } catch (err) {
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

async function loadJobs() {
  const data = await getJSON('/api/jobs');
  if (!data.jobs.length) {
    $('jobs').innerHTML = '<p class="muted">No jobs yet.</p>';
    return;
  }
  $('jobs').innerHTML = data.jobs.map(job => `
    <div class="job">
      <div><strong>${job.project}</strong><small>${job.type} · ${job.id}</small></div>
      <div class="job-status ${job.status}">${job.status}</div>
      <div class="result">${job.result || 'Waiting…'}</div>
      <small>${formatTime(job.created_at)}</small>
    </div>`).join('');
}

async function runJob() {
  $('runJob').disabled = true;
  $('jobMessage').textContent = 'Queueing…';
  try {
    const job = await getJSON('/api/jobs', {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({type: 'ffmpeg_check', project: $('project').value.trim() || 'prototype'})
    });
    $('jobMessage').textContent = `Queued ${job.id}`;
    await loadJobs();
    setTimeout(loadJobs, 600);
  } catch (err) {
    $('jobMessage').textContent = err.message;
  } finally {
    $('runJob').disabled = false;
  }
}

$('runJob').addEventListener('click', runJob);
$('refresh').addEventListener('click', loadJobs);

Promise.allSettled([loadHealth(), loadCapabilities(), loadJobs()]);
setInterval(loadJobs, 3000);
