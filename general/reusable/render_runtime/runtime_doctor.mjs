#!/usr/bin/env node
import { accessSync, constants } from 'node:fs';
import { execFileSync } from 'node:child_process';
import process from 'node:process';

function cmd(name, args = ['--version']) {
  try {
    return execFileSync(name, args, { encoding: 'utf8', stdio: ['ignore', 'pipe', 'pipe'] }).trim();
  } catch {
    return null;
  }
}

const major = Number(process.versions.node.split('.')[0]);
const ffmpeg = cmd('ffmpeg', ['-version']);
const ffprobe = cmd('ffprobe', ['-version']);
let producer = false;
let cli = false;
let shaders = false;
for (const [key, path] of [
  ['producer', './node_modules/@hyperframes/producer/package.json'],
  ['cli', './node_modules/@hyperframes/cli/package.json'],
  ['shaders', './node_modules/@hyperframes/shader-transitions/package.json'],
]) {
  try {
    accessSync(new URL(path, import.meta.url), constants.R_OK);
    if (key === 'producer') producer = true;
    if (key === 'cli') cli = true;
    if (key === 'shaders') shaders = true;
  } catch {}
}

const result = {
  schema: 'aivideoedit.scene-runtime-doctor.v1',
  node: process.version,
  node_ok: major >= 22,
  ffmpeg_ok: Boolean(ffmpeg),
  ffprobe_ok: Boolean(ffprobe),
  dependencies: { producer, cli, shaders },
  ready: major >= 22 && Boolean(ffmpeg) && Boolean(ffprobe) && producer && cli && shaders,
};
console.log(JSON.stringify(result, null, 2));
process.exit(result.ready ? 0 : 2);
