---
name: create-managed-workspace
description: Create and validate a standard managed workspace for recurring project work. Use when Codex needs to create a new workspace with AGENTS.md rules, doc/ project records, tasks/YYYYMMDD-slug task folders, per-task try folders, root skills storage, environment ledger files, or when planning alignment of existing CAD, scraping, automation, research, or multi-output workspaces to this structure.
---

# Create Managed Workspace

## Overview

Use this skill to create a repeatable workspace for projects that will produce files, span sessions, or contain many small tasks. The first version creates a single standard structure; do not choose CAD or scraping profiles.

## First Actions

- Read the target repository or parent folder rules before creating files.
- Run `git status --short --branch` in the target folder if it is already under Git.
- Before broad generation inside an existing Git-managed folder, create a checkpoint commit according to the local `AGENTS.md`.
- Use `scripts/new_workspace.py` for a new workspace root.
- Use `scripts/new_task.py` for a new small project under an existing managed workspace.
- Use `scripts/validate_workspace.py` after creation or before claiming the workspace is ready.

## Standard Workspace

Create this root structure:

```text
<workspace-root>/
├─ AGENTS.md
├─ .gitignore
├─ .env.example
├─ doc/
│  ├─ 项目地图.md
│  ├─ 任务索引.md
│  └─ 进展记录.md
├─ skills/
│  └─ .gitkeep
├─ tasks/
│  ├─ README.md
│  └─ YYYYMMDD-短任务名/
│     ├─ README.md
│     ├─ doc/
│     │  ├─ 项目地图.md
│     │  └─ 进展记录.md
│     ├─ input/
│     ├─ work/
│     ├─ output/
│     └─ try/
├─ output/
└─ try/
```

Rules:

- Keep root `skills/` empty except `.gitkeep` at creation time. Later store commonly used workspace-specific skills there.
- Keep root `try/` for workspace-level experiments only.
- Give every task directory its own `try/`; clearing a task `try/` must not affect formal results.
- Put task context in `tasks/YYYYMMDD-slug/README.md`.
- Put task long-lived structure and directory responsibilities in `tasks/YYYYMMDD-slug/doc/项目地图.md`.
- Put task progress in `tasks/YYYYMMDD-slug/doc/进展记录.md`.
- Put task final deliverables in `tasks/YYYYMMDD-slug/output/`.

## Scripts

Create a workspace:

```powershell
python D:\2Folder\skills\create-managed-workspace\scripts\new_workspace.py "D:\path\workspace" --name "工作区名称"
```

PowerShell wrapper:

```powershell
D:\2Folder\skills\create-managed-workspace\scripts\New-Workspace.ps1 -Path "D:\path\workspace" -Name "工作区名称"
```

Create a task:

```powershell
python D:\2Folder\skills\create-managed-workspace\scripts\new_task.py "D:\path\workspace" "短任务名"
```

Validate:

```powershell
python D:\2Folder\skills\create-managed-workspace\scripts\validate_workspace.py "D:\path\workspace"
```

## References

- Read `references/task-type-adjustments.md` when the user wants to adapt the standard structure for CAD, scraping, research, automation, or other task families.
- Read `references/existing-workspace-alignment.md` before planning to organize an existing workspace. This reference is guidance only; it does not authorize automatic migration.
- Read `references/rule-checklist.md` before editing generated workspace rules or checking whether a workspace is complete.
