# Existing Workspace Alignment（既有工作区对齐）

Use this reference only when the user asks to plan or perform organization of an existing workspace. Do not migrate existing CAD or scraping workspaces automatically just because this skill was used.

## Alignment Policy（对齐策略）

- First inspect current `AGENTS.md`、`doc/项目地图.md`、`doc/进展记录/`、Git status, and top-level directories.
- Preserve existing useful conventions when they do not conflict with the standard managed workspace.
- Prefer adding missing documentation, `try/` folders, task maps, and indexes before moving historical files.
- Do not rename or move large historical output trees without explicit user confirmation.
- For Git-managed folders, create a checkpoint commit before structural edits.
- Decide whether the workspace is `multi-task` or `specialized` before adding root-level support folders.

## Minimum Alignment（最低对齐）

- Root has `AGENTS.md`、`.gitignore`、`.env.example`、`doc/项目地图.md`、`doc/进展记录/`、`try/`.
- General `multi-task` workspaces do not need root `skills/`.
- Dedicated `specialized` task-type workspaces should have root `skills/` when common skills or skill entrypoints are part of the workflow.
- Cross-session small projects are represented in `tasks/` or documented as existing first-level equivalents.
- Every small project has `doc/项目地图.md`、`doc/进展记录/` and `try/`.
- Each special-purpose output folder has a clear owner and purpose in a project map.

## CAD Workspace Notes（CAD 工作区说明）

- Existing CAD workspaces may already use `output/<任务名>/` as the small-project layer.
- When aligning, either keep `output/<任务名>/` as a documented legacy task layer or create future tasks under `tasks/` and leave old output folders in place.
- Do not split source/export/screenshot sets that already belong together.
- Treat CAD workspaces as `specialized` only when they need reusable CAD skills, wrappers, or skill entrypoints inside the workspace. Otherwise document external skill paths without adding root `skills/`.

## Scraping Workspace Notes（爬虫工作区说明）

- Existing scraping workspaces may already use first-level target folders.
- Keep scaffold/tooling directories such as `scaffolding/` separate from real data targets.
- Align each target by adding `doc/项目地图.md`、`doc/进展记录/` and `try/` when missing.
- Add root `skills/` only for a dedicated scraping workspace that maintains reusable scraping skills or entrypoints.
