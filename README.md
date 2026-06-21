# 创建托管工作区

![创建托管工作区封面](assets/cover.png)

Create Managed Workspace 是一个面向 Codex、Claude Code、opencode 等 Agent 的 Skill，用于快速创建可长期维护的标准工作区。它适合那些会反复发生、但每次目标不同的任务类型，例如 CAD 建模、爬虫数据采集、研究写作、自动化脚本、文件转换和多产物项目。

它的目标不是生成某一种业务代码，而是先把工作区治理结构搭好：规则入口、项目地图、任务索引、进展记录、临时测试区、最终产物区，以及每个小项目自己的 `try/` 调试目录。只有专一任务类型工作区才额外创建常用 Skill 收纳位。

## 为什么需要它

很多 Agent 任务不是一次性问答，而是跨会话、跨文件、跨产物推进的项目。如果没有固定结构，常见问题包括：

- 产物散落在根目录，过几天不知道哪个是最新版。
- 临时测试脚本和正式交付物混在一起。
- 多个任务共用一个进展记录，后续接手困难。
- CAD 源码、导出文件、截图和核验记录无法对应。
- 爬虫项目缺少变量确认表、来源记录和任务清单，重复抓取同一来源。
- 专一任务类型工作区的常用 Skill 没有固定收纳位置，每次都要重新寻找。

这个 Skill 把这些约束变成可执行脚本和可校验结构。

## 生成的标准结构

新工作区默认按 `multi-task`（多任务）模式创建，不包含根目录 `skills/`：

```text
<workspace-root>/
├─ AGENTS.md
├─ .gitignore
├─ .env.example
├─ doc/
│  ├─ 项目地图.md
│  ├─ 任务索引.md
│  └─ 进展记录.md
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

如果创建 `specialized`（专一任务类型）工作区，才会额外生成：

```text
<workspace-root>/
└─ skills/
   └─ .gitkeep
```

核心约定：

- `AGENTS.md`：工作区级规则入口，告诉 Agent 如何登记任务、放置产物、更新记录。
- `doc/项目地图.md`：长期维护信息，记录工作区目标、目录职责、核心入口和环境账本。
- `doc/任务索引.md`：跨会话任务总看板，记录每个任务的状态、目录、产物和下一步。
- `doc/进展记录.md`：工作区级阶段总览，只记录简短摘要。
- `skills/`：仅专一任务类型工作区创建，用于常用 Skill 收纳位、包装脚本或外部技能入口；新建时只放 `.gitkeep`。
- `tasks/`：每个小项目的主目录。
- `tasks/.../doc/项目地图.md`：小项目自己的长期结构说明。
- `tasks/.../doc/进展记录.md`：小项目自己的阶段进展记录。
- `tasks/.../try/`：小项目自己的测试、调试、临时验证目录，清空后不得影响正式结果。
- `output/`：工作区级历史成品或全局交付物，新任务优先使用 `tasks/.../output/`。
- 根目录 `try/`：只放工作区级一次性调试内容。

## 安装方式

把本仓库放到 Codex、Claude Code、opencode 等 Agent 可读取的 Skill 目录中。例如：

```powershell
git clone https://github.com/q2955161835-debug/create-managed-workspace-skill.git D:\2Folder\skills\create-managed-workspace
```

如果你维护自己的外部 Skills 库，可以把目录复制到该库，并在你的路由 Skill 或说明书中登记：

```text
D:\2Folder\skills\create-managed-workspace\SKILL.md
```

## 快速开始

创建一个新托管工作区：

```powershell
python D:\2Folder\skills\create-managed-workspace\scripts\new_workspace.py "D:\Projects\MyWorkspace" --name "我的工作区"
```

创建专一任务类型工作区，并生成根目录 `skills/`：

```powershell
python D:\2Folder\skills\create-managed-workspace\scripts\new_workspace.py "D:\Projects\CadWorkspace" --name "CAD 工作区" --workspace-kind specialized
```

使用 PowerShell 包装器：

```powershell
D:\2Folder\skills\create-managed-workspace\scripts\New-Workspace.ps1 -Path "D:\Projects\MyWorkspace" -Name "我的工作区"
```

PowerShell 创建专一任务类型工作区：

```powershell
D:\2Folder\skills\create-managed-workspace\scripts\New-Workspace.ps1 -Path "D:\Projects\CadWorkspace" -Name "CAD 工作区" -WorkspaceKind specialized
```

在已有托管工作区中创建一个小项目：

```powershell
python D:\2Folder\skills\create-managed-workspace\scripts\new_task.py "D:\Projects\MyWorkspace" "CAD支架建模"
```

校验工作区结构：

```powershell
python D:\2Folder\skills\create-managed-workspace\scripts\validate_workspace.py "D:\Projects\MyWorkspace"
```

显式校验专一任务类型工作区：

```powershell
python D:\2Folder\skills\create-managed-workspace\scripts\validate_workspace.py "D:\Projects\CadWorkspace" --workspace-kind specialized
```

如果希望脚本为新工作区初始化 Git 并创建基线提交：

```powershell
python D:\2Folder\skills\create-managed-workspace\scripts\new_workspace.py "D:\Projects\MyWorkspace" --name "我的工作区" --init-git
```

## 脚本说明

| 脚本 | 用途 |
| --- | --- |
| `scripts/new_workspace.py` | 创建托管工作区根目录；默认多任务模式不建 `skills/`，专一任务类型模式才建 `skills/`。 |
| `scripts/New-Workspace.ps1` | Windows PowerShell 包装器，调用 `new_workspace.py`。 |
| `scripts/new_task.py` | 在 `tasks/` 下创建标准小项目目录。 |
| `scripts/validate_workspace.py` | 检查工作区根目录和每个小项目是否符合结构要求。 |

脚本默认不覆盖已有文件。需要覆盖时显式传入 `--overwrite`。

## 适用任务类型

### CAD

建议每个 CAD 任务都放在 `tasks/YYYYMMDD-短任务名/` 中：

- `input/`：图纸、照片、PDF、参考尺寸。
- `work/`：参数化建模源码、草稿、临时检查脚本。
- `output/`：最终源码、STEP/STL/3MF/GLB/DXF/DWG、截图和核验记录。
- `try/`：可随时清理的几何试验。

如果 CAD Skill 存放在外部路径，只在 `doc/项目地图.md` 中记录路径，不必复制进工作区。只有 CAD 工作区被定义为专一任务类型，并且确实需要工作区私有版本、包装脚本或外部入口时，才放入根目录 `skills/`。

### 爬虫数据采集

建议每个爬虫目标都作为一个小项目：

- 变量确认表和字段说明放在小项目 `doc/` 或小项目根目录。
- 多来源采集时维护 `doc/任务清单.md`。
- `原始数据/`、`原始文件/`、`旧数据/`、`清洗数据/` 等目录按需新增。
- 新增目录必须在小项目 `doc/项目地图.md` 中说明用途、可删除性和是否承载最终数据。
- 抓取测试、解析器试验和一次性探针放入小项目 `try/`。

### 研究、写作、自动化

- `input/`：题目、素材、参考资料、用户输入。
- `work/`：草稿、脚本、Notebook、中间报告。
- `output/`：最终文档、表格、脚本包或交付文件。
- `try/`：一次性转换测试、命令探针、临时验证。

## 对既有工作区的整理原则

本 Skill 第一版只创建新工作区，不自动迁移旧工作区。整理既有工作区时，应先阅读：

- `references/existing-workspace-alignment.md`
- `references/task-type-adjustments.md`
- `references/rule-checklist.md`

推荐策略：

- 先补齐缺失文档和 `try/`，再考虑移动历史文件。
- 已经组织良好的旧产物目录不要强行拆散。
- Git 管理下的大规模整理前先创建检查点提交。
- 目录改名、批量移动、删除历史产物前需要明确确认。

## 安全和环境变量

生成的 `.env.example` 只用于记录变量名、占位值和说明。真实敏感配置必须放在 `.env`，并确保 `.env` 被 `.gitignore` 忽略。

禁止把真实密钥、token、cookie、数据库密码或私有地址写入：

- `.env.example`
- README
- `doc/进展记录.md`
- 聊天中可复制的代码块

## 校验

校验 Skill 本身：

```powershell
$env:PYTHONUTF8='1'
python C:\Users\29551\.codex\skills\.system\skill-creator\scripts\quick_validate.py D:\2Folder\skills\create-managed-workspace
```

说明：如果 `SKILL.md` 包含中文，在部分 Windows Python 环境中需要设置 `PYTHONUTF8=1`，否则默认 GBK 编码可能导致解码失败。

校验生成的工作区：

```powershell
python D:\2Folder\skills\create-managed-workspace\scripts\validate_workspace.py "D:\Projects\MyWorkspace"
```

通过时会输出：

```text
OK    工作区结构检查通过
```

## 项目文件

```text
.
├─ SKILL.md
├─ README.md
├─ agents/
│  └─ openai.yaml
├─ assets/
│  ├─ cover.png
│  └─ templates/
├─ references/
│  ├─ existing-workspace-alignment.md
│  ├─ rule-checklist.md
│  └─ task-type-adjustments.md
└─ scripts/
   ├─ New-Workspace.ps1
   ├─ new_task.py
   ├─ new_workspace.py
   └─ validate_workspace.py
```

## 许可证

本项目使用 MIT License。详见 [LICENSE](LICENSE)。
