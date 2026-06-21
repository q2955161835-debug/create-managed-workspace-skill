# Task Type Adjustments（任务类型调整）

Use the standard workspace and task structure first. Add task-specific folders only when the task needs them, then document each folder in the task `doc/项目地图.md`.

## CAD（计算机辅助设计）

- Keep each CAD task inside `tasks/YYYYMMDD-短任务名/`.
- Put reference drawings, photos, PDFs, and measurement input in `input/`.
- Put CAD source scripts, intermediate models, and draft geometry checks in `work/`.
- Put final source, STEP/STL/3MF/GLB/DXF/DWG exports, screenshots, and verification notes in `output/`.
- Use the task `try/` for disposable geometry experiments.
- Store commonly used CAD skills in root `skills/` only when they are workspace-specific copies; otherwise record external paths in the task or root `doc/项目地图.md`.

## Scraping（爬虫数据采集）

- Keep each scraping target inside `tasks/YYYYMMDD-短任务名/`.
- Add `原始数据/`、`原始文件/`、`旧数据/`、`清洗数据/`、`截图证据/`、`导出报告/` only when needed.
- Put variable confirmation tables and field definitions under the task `doc/` or task root.
- Maintain `doc/任务清单.md` when multiple URLs, files, APIs, or source channels need dedupe tracking.
- Keep raw structured crawl outputs in `原始数据/` and downloaded files or snapshots in `原始文件/`.
- Put temporary fetch tests and parser experiments in the task `try/`.

## Research, Writing, and Automation（研究、写作与自动化）

- Put source files and prompts in `input/`.
- Put drafts, scripts, notebooks, and intermediate reports in `work/`.
- Put final deliverables in `output/`.
- Put throwaway probes, one-off conversion tests, and temporary scripts in `try/`.
