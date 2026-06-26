"""Create a managed workspace."""

from __future__ import annotations

import argparse
import subprocess
from datetime import datetime
from pathlib import Path


ROOT_DIRS = ["doc", "tasks", "output", "try"]
ROOT_KEEP_DIRS = ["output", "try"]
WORKSPACE_KINDS = ("multi-task", "specialized")


def now_minute() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M")


def today_progress_file() -> str:
    now = datetime.now()
    return f"{now.year}-{now.month}-{now.day}.md"


def write_file(path: Path, content: str, overwrite: bool) -> None:
    if path.exists() and not overwrite:
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def touch_keep(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)
    keep = path / ".gitkeep"
    if not keep.exists():
        keep.write_text("", encoding="utf-8")


def maybe_git_init(root: Path) -> None:
    if (root / ".git").exists():
        return
    subprocess.run(["git", "init"], cwd=root, check=True)
    subprocess.run(["git", "add", "-A"], cwd=root, check=True)
    subprocess.run(["git", "commit", "-m", "chore: baseline managed workspace"], cwd=root, check=True)


def workspace_agents(name: str, workspace_kind: str) -> str:
    skills_rule = (
        "- `skills/`：本专一任务类型工作区常用 Skill（技能）、包装脚本或外部入口；新建时只保留 `.gitkeep`。\n"
        if workspace_kind == "specialized"
        else "- `skills/`：多任务通用工作区默认不创建；只有转换为专一任务类型工作区时才新增并在本文件记录用途。\n"
    )
    return f"""# {name} 工作区规则

## 工作区概览
- `{name}` 是托管工作区，用于管理跨会话任务、小项目、产物和规则。
- 工作区类型：`{workspace_kind}`。
- 根目录 `doc/项目地图.md` 已废弃；工作区长期信息、目录职责、核心入口、运行/维护规则统一维护在本文件。

## 任务归属
- 开始处理会产生文件、需要跨会话继续、或会留下多个产物的任务前，先检查 `doc/任务索引.md` 是否已有对应任务。
- 若属于已有任务，继续使用该任务目录；若是新复杂任务，创建 `tasks/YYYYMMDD-短任务名/` 并登记到任务索引。
- 简单问答、一次性搜索、无文件产出的会话不登记任务。

## 任务目录
- 每个小项目目录默认包含 `README.md`、`doc/项目地图.md`、`doc/验收标准.md`、`doc/进展记录/`、`input/`、`work/`、`output/`、`try/`。
- `README.md` 记录任务目标、当前状态、关键决策、下一步。
- `doc/项目地图.md` 记录该小项目的长期信息、目录职责、入口、依赖和数据流。
- `doc/验收标准.md` 记录功能、交互、测试、人工验收流程、结果记录和最终结论。
- `doc/进展记录/YYYY-M-D.md` 记录该小项目阶段进展，按记录完成日期落入当天文件。
- `try/` 只放该小项目的测试、调试、临时验证文件，清空后不得影响正式结果。

## 工作区目录
- `AGENTS.md`：工作区规则、目录职责、长期维护信息和 Agent（智能代理）执行约束。
- `.env.example`：环境变量示例账本，只写变量名、占位值和说明。
- `doc/任务索引.md`：跨会话任务总索引。
- `doc/进展记录/`：工作区级阶段总览，按记录完成日期每日一份。
{skills_rule.rstrip()}
- `tasks/`：小项目目录。
- `output/`：历史成品或工作区级交付物；新任务产物优先放入对应 `tasks/.../output/`。
- `try/`：工作区级一次性调试和测试。

## 进展记录
- 有任务目录的会话，在对应任务目录 `doc/进展记录/YYYY-M-D.md` 记录阶段细节、文件清单和错误汇报。
- 根目录 `doc/进展记录/YYYY-M-D.md` 只保留简短总览：会话时间、任务名/路径、核心产出或结论。
- 高风险操作前必须更新进展记录，并写清回退方案。

## 环境账本
- `.env` 是真账本，只能存真实敏感配置，必须被 `.gitignore` 忽略，禁止提交。
- `.env.example` 是假账本，只能写变量名、占位值、示例值和必要说明。
"""


def create_workspace(root: Path, name: str, overwrite: bool, init_git: bool, workspace_kind: str) -> Path:
    root.mkdir(parents=True, exist_ok=True)
    root_dirs = list(ROOT_DIRS)
    root_keep_dirs = list(ROOT_KEEP_DIRS)
    if workspace_kind == "specialized":
        root_dirs.append("skills")
        root_keep_dirs.append("skills")

    for folder in root_dirs:
        (root / folder).mkdir(parents=True, exist_ok=True)
    for folder in root_keep_dirs:
        touch_keep(root / folder)

    stamp = now_minute()
    write_file(root / "AGENTS.md", workspace_agents(name, workspace_kind), overwrite)
    write_file(
        root / ".gitignore",
        """.env
.venv/
__pycache__/
*.pyc
.pytest_cache/
try/**
!try/
!try/.gitkeep
tasks/*/try/**
!tasks/*/try/
!tasks/*/try/.gitkeep
""",
        overwrite,
    )
    write_file(
        root / ".env.example",
        """# 环境变量示例账本
# 只记录变量名、占位值和说明；禁止写入真实密钥、token、cookie、数据库密码或私有地址。
""",
        overwrite,
    )
    write_file(
        root / "doc" / "任务索引.md",
        """# 任务索引

本文件用于快速回答：当前有哪些跨会话任务、进展到哪里、产物在哪里、下一步是什么。简单问答、一次性搜索、无文件产出的会话不登记。

| 任务 ID | 任务名 | 状态 | 最近会话时间 | 任务目录 | 最终产物 | 下一步 |
| --- | --- | --- | --- | --- | --- | --- |

## 状态说明
- `进行中`：当前正在推进，下一次会话应优先查看任务目录 README。
- `待确认`：需要用户选择、补充材料或确认范围。
- `已完成`：阶段目标完成，最终产物或结论已记录。
- `暂停`：暂不处理，但保留上下文以便恢复。
""",
        overwrite,
    )
    write_file(
        root / "doc" / "进展记录" / today_progress_file(),
        f"""# 进展记录

## {stamp} ~ {stamp}
- 本阶段完成内容：创建标准托管工作区结构。
- 新增/修改/生成的文件清单与用途说明：`AGENTS.md`、`.gitignore`、`.env.example`、`doc/任务索引.md`、`doc/进展记录/`、{"`skills/`、" if workspace_kind == "specialized" else ""}`tasks/`、`output/`、`try/`。
- 错误汇报：无。
""",
        overwrite,
    )
    write_file(
        root / "tasks" / "README.md",
        """# tasks

每个小项目使用 `YYYYMMDD-短任务名/` 命名，并包含 `README.md`、`doc/项目地图.md`、`doc/验收标准.md`、`doc/进展记录/`、`input/`、`work/`、`output/`、`try/`。
""",
        overwrite,
    )
    if init_git:
        maybe_git_init(root)
    return root


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", help="Workspace root path to create")
    parser.add_argument("--name", help="Human-readable workspace name")
    parser.add_argument(
        "--workspace-kind",
        choices=WORKSPACE_KINDS,
        default="multi-task",
        help="multi-task creates no root skills directory; specialized creates root skills directory",
    )
    parser.add_argument(
        "--specialized",
        action="store_true",
        help="Shortcut for --workspace-kind specialized",
    )
    parser.add_argument("--overwrite", action="store_true", help="Overwrite existing managed files")
    parser.add_argument("--init-git", action="store_true", help="Initialize Git and create a baseline commit if needed")
    args = parser.parse_args()

    root = Path(args.path).resolve()
    name = args.name or root.name
    workspace_kind = "specialized" if args.specialized else args.workspace_kind
    created = create_workspace(root, name, args.overwrite, args.init_git, workspace_kind)
    print(created)


if __name__ == "__main__":
    main()
