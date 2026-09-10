(() => {
  let boardState = null;

  function durationFromProject(){
    const candidates=(assetsCache||[]).map(a=>Number(a?.metadata?.duration_seconds||0)).filter(x=>x>0);
    return candidates.length?Math.max(...candidates):0;
  }
  function rowHtml(index,start='',end=''){
    return `<fieldset class="story-row" data-story-row>
      <legend>Shot ${index}</legend>
      <div class="toolbar"><label>Start seconds<input data-story-start type="number" min="0" step="0.001" value="${start}"></label><label>End seconds<input data-story-end type="number" min="0" step="0.001" value="${end}"></label><button type="button" class="secondary" data-story-remove>Remove</button></div>
      <label>Story action<textarea data-story-action rows="2" placeholder="What happens in this shot"></textarea></label>
      <label>Visual media<textarea data-story-visual rows="2" placeholder="Image/footage/composite and framing"></textarea></label>
      <label>Animation / camera behavior<textarea data-story-motion rows="2" placeholder="Movement, depth, camera, particles, etc."></textarea></label>
      <label>Music cue<input data-story-music placeholder="Beat, section, energy change, instrument cue"></label>
      <label>Lyric cue (only when active)<input data-story-lyric placeholder="Exact lyric/meaning cue, or leave blank"></label>
      <label>Transition<input data-story-transition placeholder="Cut, dissolve, morph, match move, etc."></label>
    </fieldset>`;
  }
  function renumber(){ [...document.querySelectorAll('[data-story-row]')].forEach((r,i)=>r.querySelector('legend').textContent=`Shot ${i+1}`); }
  function bindRemovers(){
    document.querySelectorAll('[data-story-remove]').forEach(b=>b.onclick=()=>{ b.closest('[data-story-row]').remove(); renumber(); });
  }
  function addRow(start='',end=''){
    const host=$('storyboardRows');
    const n=host.querySelectorAll('[data-story-row]').length+1;
    host.insertAdjacentHTML('beforeend',rowHtml(n,start,end)); bindRemovers();
  }
  function seedRows(){
    $('storyboardRows').innerHTML='';
    const duration=durationFromProject();
    const count=4;
    for(let i=0;i<count;i++){
      const start=duration?Number((duration*i/count).toFixed(3)):'';
      const end=duration?Number((duration*(i+1)/count).toFixed(3)):'';
      addRow(start,end);
    }
  }
  function entries(){
    return [...document.querySelectorAll('[data-story-row]')].map((r,i)=>({
      shot_id:`shot-${String(i+1).padStart(3,'0')}`,
      start_seconds:Number(r.querySelector('[data-story-start]').value),
      end_seconds:Number(r.querySelector('[data-story-end]').value),
      story_action:r.querySelector('[data-story-action]').value.trim(),
      visual_media:r.querySelector('[data-story-visual]').value.trim(),
      animation_behavior:r.querySelector('[data-story-motion]').value.trim(),
      music_cues:[r.querySelector('[data-story-music]').value.trim()].filter(Boolean),
      lyric_cue:r.querySelector('[data-story-lyric]').value.trim(),
      transition:r.querySelector('[data-story-transition]').value.trim(),
    }));
  }
  function validate(rows){
    if(!rows.length) return 'Add at least one storyboard shot.';
    for(let i=0;i<rows.length;i++){
      const r=rows[i];
      if(!Number.isFinite(r.start_seconds)||!Number.isFinite(r.end_seconds)||r.end_seconds<=r.start_seconds) return `Shot ${i+1} needs a valid start and end time.`;
      if(i===0 && Math.abs(r.start_seconds)>0.001) return 'The storyboard must begin at 0 seconds.';
      if(i>0 && Math.abs(r.start_seconds-rows[i-1].end_seconds)>0.002) return `Shot ${i+1} must start exactly where shot ${i} ends.`;
      if(!r.story_action||!r.visual_media||!r.animation_behavior||!r.music_cues.length||!r.transition) return `Complete story, visual, motion, music cue, and transition for shot ${i+1}.`;
    }
    const duration=durationFromProject();
    if(duration && Math.abs(rows.at(-1).end_seconds-duration)>0.05) return `The final shot must end at the project duration (${duration.toFixed(3)}s).`;
    return null;
  }
  async function saveBoard(){
    const rows=entries(),problem=validate(rows);
    if(problem){ $('productionStatus').textContent=problem; return false; }
    const fps=Number($('storyboardFps').value||30);
    try{
      boardState=await toolCall('storyboard.set',{project_id:projectId(),entries:rows,target_fps:fps,summary:$('storyboardSummary').value.trim(),authority:'studio_current_user'});
      $('productionStatus').textContent=`Storyboard draft saved · ${boardState.entry_count||rows.length} shots · full frame coverage.`;
      await refreshBoardStatus();
      return true;
    }catch(e){ $('productionStatus').textContent=e.message; return false; }
  }
  async function lockBoard(){
    if(!await saveBoard()) return;
    const instruction=$('storyboardLockInstruction').value.trim();
    if(!instruction){ $('productionStatus').textContent='Record the instruction approving this storyboard before locking it.'; return; }
    $('lockStoryboard').disabled=true;
    try{
      boardState=await toolCall('storyboard.lock',{project_id:projectId(),recorded_instruction:instruction});
      const guard=await toolCall('storyboard.guard',{project_id:projectId()});
      if(!guard.ok){ $('productionStatus').textContent=`Storyboard locked, but narrative verification failed: ${guard.stdout||guard.stderr||'needs attention'}`; }
      else $('productionStatus').textContent='Storyboard and production script locked. Canonical narrative guard PASS.';
      $('storyboardDialog').close();
      await refreshBoardStatus(); await loadProductionStatus();
    }catch(e){ $('productionStatus').textContent=e.message; }
    finally{ $('lockStoryboard').disabled=false; }
  }
  async function openBoard(){
    try{ boardState=await toolCall('storyboard.status',{project_id:projectId()}); }
    catch(e){ $('productionStatus').textContent=e.message; return; }
    $('storyboardFps').value=boardState.target_fps||30;
    seedRows();
    $('storyboardDialog').showModal();
  }
  async function refreshBoardStatus(){
    const button=$('storyboardEditor'),status=$('storyboardStatus');
    if(!button||!status) return;
    const stage=productionState?.stage;
    const relevant=['APPROACH_ESTABLISHED','STORYBOARD_LOCKED'].includes(stage);
    button.hidden=stage!=='APPROACH_ESTABLISHED';
    if(!relevant){ status.hidden=true; boardState=null; return; }
    try{
      boardState=await toolCall('storyboard.status',{project_id:projectId()});
      status.hidden=false;
      status.textContent=boardState.storyboard_exists
        ? `Storyboard: ${boardState.entry_count} shots · ${boardState.total_frames||'—'} frames · ${boardState.storyboard_locked&&boardState.script_locked?'locked':'draft'}.`
        : 'Storyboard: not authored yet.';
    }catch(e){ status.hidden=false; status.textContent=e.message; }
  }

  $('storyboardEditor')?.addEventListener('click',openBoard);
  $('addStoryboardRow')?.addEventListener('click',()=>addRow());
  $('saveStoryboard')?.addEventListener('click',saveBoard);
  $('lockStoryboard')?.addEventListener('click',lockBoard);
  setInterval(refreshBoardStatus,2500);
  setTimeout(refreshBoardStatus,500);
})();
