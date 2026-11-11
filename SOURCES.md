# 方法来源与取舍

调研日期：2026-11-11。

本项目将公开技能中的方法思路进行比较、取舍，并独立编写自己的流程、中文说明、模板、示例与脚本。下面的链接固定到调研时核对的提交，便于以后复查。

没有打包上游技能文件、代码、小说语料、案例摘录或商业服务接口。MIT 许可只覆盖本仓库自己的内容，不改变任何上游项目的许可。若未来直接纳入第三方文件，需要单独核对许可并保留所要求的声明。

| 来源快照 | 参考的思路 | 本项目的选择 |
|---|---|---|
| [Tomsawyerhu/Chinese-WebNovel-Skill](https://github.com/Tomsawyerhu/Chinese-WebNovel-Skill/tree/96709f477f4b59be856ebb10bec052dd0452b846) | 剧情、人物、转场和对白分别诊断 | 拆成按任务选择的方法，不沿用固定开篇字数与语料检索要求 |
| [deedeekong07-alt/fiction-humanizer-zh](https://github.com/deedeekong07-alt/fiction-humanizer-zh/tree/859a3fda0ddb03cafe2fc08455c9865c62f033c6) | 场景过程、情绪与事件余波；修改力度分层 | 不采用固定转折间隔、强制失败或篇幅配额 |
| [orange4664/chinese-grammar-proofreader](https://github.com/orange4664/chinese-grammar-proofreader/tree/91ac03c119ec6ecb8a7f2d2180aef56658c07cc3) | 语病与风格分开、依语境判断、最小修改 | 不把句式清单当自动判错规则 |
| [wgwtest/novel-writing](https://github.com/wgwtest/novel-writing/tree/838729695148008d42c01bd7c3c0c1a5c15de830) | 人物信息边界、场景因果、作者声音与修改反馈 | 项目规则优先，保留笔法证据与版本依据 |
| [Elowwwen/Fanfic-background-assistant](https://github.com/Elowwwen/Fanfic-background-assistant/tree/0b5da382b5f5d0150b406bc66bfbc0c4aaa11e3f) | 有来源的背景研究与作者创作边界 | 扩展为同人与原创均可使用的资料模块，不自动创建手册 |
| [XTmingyue/wenfeng-skill](https://github.com/XTmingyue/wenfeng-skill/tree/aed604e9f1e97bd275dc9a4151179e854431797a) | 从文本样本提炼可复用笔法 | 偏好留在单书档案，不默认生成新的作者人格技能 |
| [Calliope-Editor/writing-skills](https://github.com/Calliope-Editor/writing-skills/tree/2fad031982cbbcb00c4da14c2fc9712d2daa78da) | 连续性证据、只评不改、读者体验视角 | 不依赖 Calliope 服务，明确模拟读者不是市场数据 |
| [jwynia/agent-skills](https://github.com/jwynia/agent-skills/tree/e02ec7e226a6e4f8419fd3b88a1d8e472d421b32) | 新物种或技术的社会连锁后果 | 只在题材需要时使用，不强迫全部作品写实化 |
| [jiaw-Zh/long-novel-writer](https://github.com/jiaw-Zh/long-novel-writer/tree/ec1604e414bfafece8142f469b05a960d21b3a9a) | 分层摘要、人物档案、知情范围与原文回查 | 按实际规模增量建档，不采用固定字数门和自动扩缩写 |
| [xiaofeng-928/chinese-longnovel-skill](https://github.com/xiaofeng-928/chinese-longnovel-skill/tree/1277f1e886ad1263562b0d85d828ece675c97417) | 计划与事实隔离、状态来源与受影响范围 | 保留轻量 Markdown 工作流，不搬运事务脚本或固定规划窗口 |
| [chaserr/novel-craft](https://github.com/chaserr/novel-craft/tree/cd9d308d46b4d19286db03e1082f2e2c3064b1b2) | 写后同步、按编辑职责划分审阅 | 默认单代理可用，不要求 RTK 文件或重新初始化已有工程 |
| [haowjy/creative-writing-skills](https://github.com/haowjy/creative-writing-skills/tree/0fb3c580a4e20435ddb0c0a744629b42a63c7307) | 分层编辑、读者模拟、风格证据 | 本轮任务决定审阅层级，不默认整套 agent 与知识库 |
| [danjdewhurst/story-skills](https://github.com/danjdewhurst/story-skills/tree/3c0e0346ee09ded32546d9481ac18ec5324f02c3) | 结构化连续性、设定与状态可追溯 | 不要求其 CLI 或目录契约，不声称自动理解全部正文 |
| [zenstory-ai/oh-story-claudecode](https://github.com/zenstory-ai/oh-story-claudecode/tree/41d28fcde00bc60956f9fa432a569478c43a217e) | 依创作阶段组织、拆书证据、作者偏好 | 不加入扫榜、抓取、封面或自动发布依赖 |

## 主要整合决定

- 把篇幅、创作阶段、题材、文风和合作方式作为不同维度，避免一个题材标签决定全部写法。
- 首次只问影响下一步的内容；已有大纲与正文直接接入，作者意向可以在后续对话修改。
- 公开入口保持轻量，专门方法按需读取。无需安装所有来源技能，也无需额外 API。
- 用作品内部证据评价连续性，把读者感受与确定错误分开。
- 保留草稿状态和作者接受状态，允许已授权的连续草稿链，又不把试写偷偷提升为事实。
- 不采用固定字距反转、每章强冲突、必败一次、感官配额、强制碎句、模板化 AI 检测分数等通用门槛。
- 长篇需要分层记忆，短篇保持简洁；已有工程的文件与版本约定优先。

## 如何贡献

报告问题时提供最小虚构例子、作者本轮请求和实际偏差。先判断是单书偏好还是通用方法问题，再决定改偏好档案、模块规则或脚本。不要提交未获准公开的书稿和个人资料。
