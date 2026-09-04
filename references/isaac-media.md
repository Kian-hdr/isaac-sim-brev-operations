# Isaac visible runs and media

Read this reference for visible simulation, WebRTC streaming, camera validation,
screen recording, clean rendering, or final video production.

## Execution modes

- Bulk training, sweeps, and unattended throughput runs are headless by default.
- Use a visible stream for integration smoke inspection, policy playback, evaluation,
  camera validation, demonstrations, debugging, and explicit user requests to watch.
- Keep the simulation job independent of the viewer where practical. A viewer failure
  should not silently terminate a healthy headless job.
- If streaming fails, preserve the job and obtain offline frames or footage while
  repairing the viewing path.

## Configure and verify the viewer

Choose window dimensions, renderer dimensions, client resolution, UI visibility, and
DPI scaling for the current host, client, display, network, and deliverable. Use the
installed version's documented settings. No previously tested personal profile is
included as a default.

A client resolution selector is not proof of server renderer resolution. Inspect
Isaac's live diagnostic or the actual rendered output for the intended dimensions.
Revalidate when the simulator, client, image, GPU, display, or network changes.

## Viewport recording versus clean rendering

- A viewport recording includes the Isaac application UI and is useful for development
  evidence or simulator demonstrations.
- A clean rendering contains only the simulated camera or animation and is appropriate
  for polished presentation footage.
- Label the output truthfully. Do not call a viewport capture a clean rendering.

## Video defaults

- Produce true 16:9 media, normally `1920 x 1080` or `3840 x 2160`.
- Crop a 16:10 display capture to the streamed 16:9 image.
- Never stretch the image or retain black bars as a substitute for a correct frame.
- Preserve raw footage and failed or rejected candidates.
- Promote only a uniquely named master that passes the project's acceptance criteria.

## Media validation

For every promoted master verify:

- container, codec, pixel format, frame rate, frame count, dimensions, and duration
- full decode without errors
- representative beginning, middle, and end frames
- visual correctness, crop, overlays, labels, and absence of unintended UI
- audio integrity when audio is present
- local playback and a verified backup copy
- source run, telemetry, configuration, controller or policy identity, and checksum

An edited video is not autonomy or policy evidence by itself. Preserve the uninterrupted
supporting run and claims boundary.
