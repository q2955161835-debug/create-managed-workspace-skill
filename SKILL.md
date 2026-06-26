---
name: create-managed-workspace
description: Create and validate managed workspaces for recurring project work. Use when Codex needs to create a multi-task workspace with AGENTS.md rules, doc/task indexes, progress records, tasks/YYYYMMDD-slug task folders, task project maps, task acceptance criteria, per-task try folders, environment ledger files, or a specialized task-type workspace that also needs root skills storage. Also use when planning alignment of existing CAD, scraping, automation, research, or multi-output workspaces to this structure.
---

# Create Managed Workspace

## Overview

Use this skill to create a repeatable workspace for projects that will produce files, span sessions, or contain many small tasks. Choose the workspace kind before creation:

- `multi-task`: default for general workspaces that hold unrelated or loosely related projects. Do not create root `skills/`.
- `specialized`: use for a dedicated task-type workspace such as CAD, scraping, automation, or research where the workspace should keep common skills or skill entrypoints. Create root `skills/`.

Do not choose CAD or scraping profiles; use one structure plus the task-type adjustment notes.

## First Actions

- Read the target repository or parent folder rules before creating files.
- Run `git status --short --branch` in the target folder if it is already under Git.
- Before broad generation inside an existing Git-managed folder, create a checkpoint commit according to the local `AGENTS.md`.
- Use `scripts/new_workspace.py` for a new workspace root.
- Use `scripts/new_task.py` for a new small project under an existing managed workspace.
- Use `scripts/validate_workspace.py` after creation or before claiming the workspace is ready.

## Standard Multi-Task Workspace

Create this root structure by default:

```text
<workspace-root>/
├─ AGENTS.md
├─ .gitignore
├─ .env.example
├─ doc/
│  ├─ 任务索引.md
│  └─ 进展记录/
│     └─ YYYY-M-D.md
├─ tasks/
│  ├─ README.md
│  └─ YYYYMMDD-短任务名/
│     ├─ README.md
│     ├─ doc/
│     │  ├─ 项目地图.md
│     │  ├─ 验收标准.md
│     │  └─ 进展记录/
│     │     └─ YYYY-M-D.md
│     ├─ input/
│     ├─ work/
│     ├─ output/
│     └─ try/
├─ output/
└─ try/
```

For a specialized task-type workspace, add:

```text
<workspace-root>/
└─ skills/
   └─ .gitkeep
```

Rules:

- Do not create root `skills/` for a general multi-task workspace.
- Create root `skills/` only for a specialized task-type workspace. Keep it empty except `.gitkeep` at creation time, then store commonly used workspace-specific skills or documented entrypoints there.
- Do not create root `doc/项目地图.md`; root-level long-lived workspace information, directory responsibilities, core entry points, and operating rules belong in `AGENTS.md`.
- Keep root `try/` for workspace-level experiments only.
- Give every task directory its own `try/`; clearing a task `try/` must not affect formal results.
- Put task context in `tasks/YYYYMMDD-slug/README.md`.
- Put task long-lived structure and directory responsibilities in `tasks/YYYYMMDD-slug/doc/项目地图.md`.
- Put task acceptance steps, expected results, verification commands, manual checks, and final conclusion in `tasks/YYYYMMDD-slug/doc/验收标准.md`.
- Put task progress in `tasks/YYYYMMDD-slug/doc/进展记录/YYYY-M-D.md`, based on the record completion date.
- Put task final deliverables in `tasks/YYYYMMDD-slug/output/`.

## Scripts

Create a workspace:

```powershell
python D:\2Folder\skills\create-managed-workspace\scripts\new_workspace.py "D:\path\workspace" --name "工作区名称"
```

Create a specialized task-type workspace with root `skills/`:

```powershell
python D:\2Folder\skills\create-managed-workspace\scripts\new_workspace.py "D:\path\cad-workspace" --name "CAD 工作区" --workspace-kind specialized
```

PowerShell wrapper:

```powershell
D:\2Folder\skills\create-managed-workspace\scripts\New-Workspace.ps1 -Path "D:\path\workspace" -Name "工作区名称"
```

Specialized wrapper:

```powershell
D:\2Folder\skills\create-managed-workspace\scripts\New-Workspace.ps1 -Path "D:\path\cad-workspace" -Name "CAD 工作区" -WorkspaceKind specialized
```

Create a task:

```powershell
python D:\2Folder\skills\create-managed-workspace\scripts\new_task.py "D:\path\workspace" "短任务名"
```

Validate:

```powershell
python D:\2Folder\skills\create-managed-workspace\scripts\validate_workspace.py "D:\path\workspace"
```

Validate specialized mode explicitly:

```powershell
python D:\2Folder\skills\create-managed-workspace\scripts\validate_workspace.py "D:\path\cad-workspace" --workspace-kind specialized
```

## References

- Read `references/task-type-adjustments.md` when the user wants to adapt the standard structure for CAD, scraping, research, automation, or other task families.
- Read `references/existing-workspace-alignment.md` before planning to organize an existing workspace. This reference is guidance only; it does not authorize automatic migration.
- Read `references/rule-checklist.md` before editing generated workspace rules or checking whether a workspace is complete.
