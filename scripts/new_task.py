"""Create a standard task folder inside a managed workspace."""

from __future__ import annotations

import argparse
import re
from datetime import datetime
from pathlib import Path


TASK_DIRS = ["doc", "input", "work", "output", "try"]
KEEP_DIRS = ["input", "work", "output", "try"]


def now_minute() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M")


def today() -> str:
    return datetime.now().strftime("%Y%m%d")


def slugify(name: str) -> str:
    cleaned = re.sub(r"[\\/:*?\"<>|]+", "-", name.strip())
    cleaned = re.sub(r"\s+", "-", cleaned)
    cleaned = cleaned.strip(".-")
    if not cleaned:
        raise ValueError("Task name cannot be empty after sanitizing")
    return cleaned


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


def create_task(workspace: Path, name: str, task_id: str | None, overwrite: bool) -> Path:
    root = workspace.resolve()
    if not (root / "tasks").exists():
        raise FileNotFoundError(f"Missing tasks directory: {root / 'tasks'}")

    slug = slugify(name)
    final_id = task_id or f"{today()}-{slug}"
    task = root / "tasks" / final_id
    task.mkdir(parents=True, exist_ok=True)
    for folder in TASK_DIRS:
        (task / folder).mkdir(parents=True, exist_ok=True)
    for folder in KEEP_DIRS:
        touch_keep(task / folder)

    stamp = now_minute()
    write_file(
        task / "README.md",
        f"""# {name}

## 任务目标
- 待填写。

## 当前状态
- 待确认。

## 关键决策
- 待填写。

## 下一步
- 待填写。
""",
        overwrite,
    )
    write_file(
        task / "doc" / "项目地图.md",
        f"""# 项目地图

## 任务目标
- 待填写：`{name}` 的目标、范围和交付物。

## 目录职责
- `README.md`：任务目标、当前状态、关键决策和下一步。
- `doc/项目地图.md`：本小项目长期维护信息。
- `doc/进展记录.md`：本小项目阶段进展。
- `input/`：输入资料。
- `work/`：处理中间文件、草稿和脚本。
- `output/`：最终交付物。
- `try/`：测试、调试、临时验证文件，可清理。

## 创建时间
- {stamp}
""",
        overwrite,
    )
    write_file(
        task / "doc" / "进展记录.md",
        f"""# 进展记录

## {stamp} ~ {stamp}
- 本阶段完成内容：创建小项目目录骨架。
- 新增/修改/生成的文件清单与用途说明：`README.md`、`doc/项目地图.md`、`doc/进展记录.md`、`input/`、`work/`、`output/`、`try/`。
- 错误汇报：无。
""",
        overwrite,
    )
    return task


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("workspace", help="Managed workspace root")
    parser.add_argument("name", help="Task display name")
    parser.add_argument("--task-id", help="Explicit task directory name")
    parser.add_argument("--overwrite", action="store_true", help="Overwrite existing managed files")
    args = parser.parse_args()

    task = create_task(Path(args.workspace), args.name, args.task_id, args.overwrite)
    print(task)


if __name__ == "__main__":
    main()
