# Task Type Adjustments（任务类型调整）

Use the standard workspace and task structure first. Add task-specific folders only when the task needs them, then document each folder in the task `doc/项目地图.md` and its verification flow in `doc/验收标准.md`.

## Workspace Kind（工作区类型）

- Use `multi-task` for general workspaces that contain many unrelated projects. Do not create or require root `skills/`.
- Use `specialized` for a dedicated task-type workspace such as CAD, scraping, automation, or research when common skills, wrappers, or skill entrypoints should live with the workspace. Only this kind gets root `skills/`.
- If a specialized workspace uses external skills instead of copied skills, root `skills/` may contain junctions, wrappers, README files, or `.gitkeep`; document the real external paths in root `AGENTS.md` or in the relevant task `doc/项目地图.md`.
- Root `doc/项目地图.md` is deprecated. Keep workspace-level long-term structure and directory responsibilities in `AGENTS.md`; keep task-level structure in task `doc/项目地图.md`.

## CAD（计算机辅助设计）

- Keep each CAD task inside `tasks/YYYYMMDD-短任务名/`.
- Put reference drawings, photos, PDFs, and measurement input in `input/`.
- Put CAD source scripts, intermediate models, and draft geometry checks in `work/`.
- Put final source, STEP/STL/3MF/GLB/DXF/DWG exports, screenshots, and verification notes in `output/`.
- Record CAD export checks, geometry checks, screenshot/manual review, and final acceptance in `doc/验收标准.md`.
- Use the task `try/` for disposable geometry experiments.
- Use root `skills/` only when the CAD workspace is a specialized task-type workspace. Store workspace-specific copies, wrappers, or junction entrypoints there; otherwise record external paths in `AGENTS.md` or the relevant task `doc/项目地图.md`.

## Scraping（爬虫数据采集）

- Keep each scraping target inside `tasks/YYYYMMDD-短任务名/`.
- Add `原始数据/`、`原始文件/`、`旧数据/`、`清洗数据/`、`截图证据/`、`导出报告/` only when needed.
- Put variable confirmation tables and field definitions under the task `doc/` or task root.
- Maintain `doc/任务清单.md` when multiple URLs, files, APIs, or source channels need dedupe tracking.
- Keep raw structured crawl outputs in `原始数据/` and downloaded files or snapshots in `原始文件/`.
- Record source coverage, dedupe checks, output file checks, and manual review items in `doc/验收标准.md`.
- Put temporary fetch tests and parser experiments in the task `try/`.
- Use root `skills/` only for a specialized scraping workspace with reusable crawlers, extraction skills, or documented entrypoints. General multi-task workspaces that happen to include scraping tasks should not add root `skills/`.

## Research, Writing, and Automation（研究、写作与自动化）

- Put source files and prompts in `input/`.
- Put drafts, scripts, notebooks, and intermediate reports in `work/`.
- Put final deliverables in `output/`.
- Put throwaway probes, one-off conversion tests, and temporary scripts in `try/`.
- Record repeatable commands, manual review criteria, output file checks, and final conclusion in `doc/验收标准.md`.
