# Rule Checklist（规则检查清单）

Use this checklist before finishing workspace creation or editing generated rules.

## Root（根目录）

- `AGENTS.md` describes workspace purpose, directory responsibilities, task ownership, task folders, workspace kind, root `try/`, progress records, and environment ledgers.
- Root `doc/项目地图.md` is deprecated; do not create it. Move any root project-map content into `AGENTS.md`.
- `.gitignore` ignores `.env`, caches, root `try/` contents, and task `try/` contents while preserving `.gitkeep`.
- `.env.example` contains placeholders only and no real secrets.
- `doc/任务索引.md` exists for cross-session tasks.
- `doc/进展记录/YYYY-M-D.md` records workspace-level summaries, one file per record completion date.
- For `multi-task` workspaces, root `skills/` is absent by default.
- For `specialized` task-type workspaces, root `skills/` exists and is empty except `.gitkeep` at creation unless the user asked for skill entrypoints.
- `try/` exists and contains no required project result.

## Task（小项目）

- Directory name uses `YYYYMMDD-短任务名`.
- `README.md` records goal, current status, key decisions, and next step.
- `doc/项目地图.md` records the task purpose, directory responsibilities, entry points, dependencies, and output flow.
- `doc/验收标准.md` records test environment, acceptance steps, expected results, evidence method, result record, feedback/issues, and final conclusion.
- `doc/进展记录/YYYY-M-D.md` records time ranges to the minute.
- `input/` holds input material.
- `work/` holds drafts, scripts, and intermediate files.
- `output/` holds final deliverables.
- `try/` holds disposable tests and can be cleared safely.

## Safety（安全）

- For existing Git-managed folders, check status before structural edits.
- For broad changes, create a checkpoint commit first.
- For high-risk local operations, use a timestamped backup under `D:\0文件夹\备份`.
