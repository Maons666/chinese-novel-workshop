<p align="center">
  <img src="assets/readme-banner.svg" alt="中文小说工坊。按你的要求写小说：构思与大纲、正文与续写、审稿与修改。" width="900">
</p>

一套随作者调整的中文小说写作 Skill。支持原创与同人、短篇到长篇，可以从构思写成完整正文，也能接着已有作品续写、重写或审阅。

[安装与调用](#安装与第一次调用)　[作者定制](#按你的书来合作)　[写作样例](#写作样例)　[审阅](#写完之后检查这些)

## 安装与第一次调用

需要一个能读取 Skill 的 AI 工具。核心是 Markdown 指令与参考资料，**无需额外配置模型 API，也不需要 Python**。

将整个仓库安装到 Skills 目录，保留其中的参考资料、模板和脚本。

**Codex · Windows PowerShell**

```powershell
git clone https://github.com/Maons666/chinese-novel-workshop.git "$env:USERPROFILE\.codex\skills\chinese-novel-workshop"
```

**Codex · macOS / Linux**

```sh
git clone https://github.com/Maons666/chinese-novel-workshop.git ~/.codex/skills/chinese-novel-workshop
```

目录已存在时，先检查原安装与本地改动。安装后开启新会话，输入：

```text
请用 $chinese-novel-workshop 先了解我的写作意向，再决定怎么合作。
```

已有大纲，可以直接起稿：

```text
用 $chinese-novel-workshop 按我们确认的大纲写第一章。
直接给完整正文，保持第三人称限知和朴素语言，写后检查连续性。
```

<details>
<summary>其他工具、项目内安装与已有作品</summary>

也可安装在项目的 `.agents/skills/chinese-novel-workshop`，由支持该目录的工具发现。其他 agent 可将完整目录放入其支持的 Skills 目录，或显式读取 [SKILL.md](SKILL.md)；发现机制以工具文档为准。

接着已有作品写：

```text
用 $chinese-novel-workshop 读取项目说明、大纲与进度。
沿用已确认的设定，准备下一章，先给场景安排。
```

只做审稿：

```text
只审第七章，不改文件。
分别说明硬伤、可选建议与阅读感受。
```

用法示例：[从一个想法开始](examples/short-original.md) · [接入已有长篇](examples/existing-long-project.md)。

</details>

## 按你的书来合作

先读已有材料，再问会影响下一步的问题。你可以让它代拟初稿，也可以自己执笔，只请它做规划与审稿。

| 你来决定 | 据此调整 |
| --- | --- |
| 从哪里开始 | 一个念头、已有大纲或现成书稿；短篇、中篇或长篇 |
| 写什么 | 原创或同人、题材、世界观、人物关系与不能改变的内容 |
| 怎么写 | 文风、视角、节奏与目标阅读体验；结合样章和作者修改理解笔法 |
| 怎样合作 | 提问陪写、共同规划、起草、续写、重写或只做审阅 |

[作者访谈](references/interview.md)每轮最多三个简短问题，可回答“不确定”“你推荐”或“先跳过”。同人先确认原作版本，分清官方事实、作者改动与待定设定。

短篇围绕主要变化展开；长篇按当前卷和近期章节推进；想边写边探索，也可以先小范围试写。偏好会影响写法与审阅标准，随时可以调整。

作品与偏好保存在**自己的小说项目里**，已有工程沿用原有结构。硬约束、软偏好、暂定方案与本轮修改范围分别记录，候选方向不会自动定案。详见 [定制方法](references/customization.md) · [作者偏好模板](templates/author-profile.md)。

## 写作样例

[阅读独立样例《搬家前的晚饭》](examples/prose-sample.md)

附写作要求与完整片段。

## 写完之后，检查这些

| 检查范围 | 具体内容 |
| --- | --- |
| 事实与结构 | 因果、人物信息、时间、物品、世界规则及题材相关问题 |
| 表达与体验 | 中文语病、节奏、情绪、人物声音、理解难点与继续阅读的动力 |
| 问题与建议 | 引用实际读过的原文，区分确定问题、待核实事项和可选优化，指出值得保留的表达 |

**只要求审稿时，不修改正文。** 修订限于授权范围；候选稿、活跃草稿与作者接受的正文保持区分。模型自查通过不等于作者接受，未执行的检查不会记成已完成。

不设统一的“好小说分数”，不保证通过 AI 检测或获得平台流量。

## 资料与验证

| 资料 | 入口 |
| --- | --- |
| 技能入口、方法与模板 | [SKILL.md](SKILL.md) · [参考资料](references/) · [模板](templates/) |
| 使用方式与实际验证 | [用法示例](examples/) · [行为场景](evals/scenarios.md) · [验证记录](evals/validation.md) |
| 方法来源、版本与取舍 | [SOURCES.md](SOURCES.md) |
| 开源许可 | [MIT License](LICENSE) |

包结构和脚本可自动检查，写作行为按场景验证；结构校验不代表写作效果实测。

<details>
<summary>可选工具与目录说明</summary>

```text
SKILL.md             入口与任务路由
references/          访谈、规划、正文、审阅、连续性与定制
templates/           偏好、简报、章节任务、状态与报告
examples/            独立编写的虚构示例
agents/openai.yaml   Codex 显示信息
scripts/             只读统计与技能包校验
tests/               脚本测试
evals/               行为场景、实际输出与验证记录
```

可选脚本使用 **Python 3.10+ 标准库**，无第三方依赖：

```sh
python scripts/text_stats.py path/to/chapter.md --skip-headings
python scripts/validate.py
python -m unittest discover -s tests -v
```

统计脚本报告汉字、非空白字符和 SHA-256，只按选项排除 ATX 标题，批注与占位仍计入。汉字识别依据当前 Python 的 Unicode 数据库，口径不等同于任意写作平台。脚本不改稿、不补字，也不判断文学质量。

</details>

公开仓库只保存方法与虚构示例。欢迎提交具体使用场景、可复现问题与改进建议。
