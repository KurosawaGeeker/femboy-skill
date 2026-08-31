<p align="center">
  <img src="assets/femboy-skill-banner.svg" alt="Femboy Skill — 一朵由跨性别旗帜色花瓣、开放书页和星光组成的包容性图形" width="100%">
</p>

<h1 align="center">Femboy Skill · 男娘成长指南</h1>

<p align="center">
  面向女性化表达与成年人身体探索的中文 Agent Skill<br>
  尊重每一种自我称呼，也尊重不被任何标签定义的你
</p>

<p align="center">
  <a href="#安装">安装</a> ·
  <a href="#能回答什么">能力</a> ·
  <a href="#使用示例">示例</a> ·
  <a href="#社区真实案例库">案例</a> ·
  <a href="#社区消费指南">消费指南</a> ·
  <a href="#安全原则">安全</a> ·
  <a href="#知识来源与许可">来源</a> ·
  <a href="CONTRIBUTING.md">参与贡献</a>
</p>

<p align="center">
  <img alt="License: CC BY-SA 4.0" src="https://img.shields.io/badge/license-CC%20BY--SA%204.0-8F6FC7?style=flat-square">
  <img alt="Language: Chinese" src="https://img.shields.io/badge/language-%E4%B8%AD%E6%96%87-5BCEFA?style=flat-square">
  <img alt="Audience: Adults only" src="https://img.shields.io/badge/audience-18%2B-F5A9B8?style=flat-square">
  <img alt="Community: Inclusive" src="https://img.shields.io/badge/community-inclusive-7657A6?style=flat-square">
</p>

> [!CAUTION]
> **仅限年满 18 周岁的成年人阅读和使用。未成年人勿看勿用，后果自负。**
> 本项目包含成人性健康与身体探索内容，不构成医疗诊断、处方或结果保证。身体状况、当地法律和个体风险各不相同；使用者应自行判断并承担使用本项目所产生的后果。出现疼痛、出血、持续不适或其他危险信号时，应停止尝试并及时就医。

## 前言

发现了一个开源社区漏洞 —— 居然没有给男娘进化和养成用的 skill！

本着“如果没有的话，那我就搞一个” 的行动原则，先把坑开了，不定期维护。大家可以自由地提交 pr。

Owner 本人已有三年的女装龄，目前已经实现日常女装（包括上班，居家，出行和社交），应该还算比较权威吧（大概），但本人顺性别性取向直，只是爱穿好看衣服罢了，请不要网暴我呜呜。

**须知：** 想要更加自由地以女性化的状态在社会生存，需要付出巨大的努力，跨越心理障碍，甚至要付出远超顺直男性日常开销的金钱。**绝不只是**从拼多多，淘宝上买几件几十块钱的女装，套个十几块钱的丝袜这么简单。

**须知：** 女性化是一种审美偏好，可以是嗓音、穿搭、妆容、身体感受，也可以只是更自在地成为自己想成为的样子。它不自动等于某种性别身份、性取向、身体改造或性实践。

**须知：** 一套可传递的不等式：男孩子穿女装 != Gay != 男娘 != 跨性别者 != 长发男 != 想被草 != 喜欢男的 != 吃药。

**须知：** 生理男性有权成为任何 TA 想要成为的样子，有权探索身体的变化和反馈。

Femboy Skill 希望给中文用户一个温和、直接、去羞耻化的问答入口。它欢迎 MTF/跨性别女性、crossdresser、femboy/男娘、非二元、性别不顺从、仍在探索身份的人，以及任何希望了解相关主题的成年人。项目名是安装标识，不是强加给使用者的身份标签；你可以使用自己认同的称呼和代词。

这个 skill 以社区经验提供练习思路，同时为医疗与身体风险设置更严格的证据边界：社区经验不会被包装成普遍事实，高风险建议以当前权威医学资料为准。

## 安装

### 使用 Skills CLI

```bash
npx skills add https://github.com/KurosawaGeeker/femboy-skill --skill femboy-skill
```

### 手动安装到 Codex

```bash
git clone https://github.com/KurosawaGeeker/femboy-skill.git
cp -R femboy-skill/femboy-skill ~/.codex/skills/femboy-skill
```

安装后重新开启一个 Codex 任务，即可显式调用 `$femboy-skill`；支持自动发现 skill 的 Agent 也可根据问题自动选择它。

## 能回答什么

| 主题 | 可以提供 | 关键边界 |
|---|---|---|
| 伪音与嗓音女性化 | 音高、共鸣、重量、语调、录音反馈 | 不把疼痛、嘶哑或挤喉视为进步 |
| 护肤、妆容与胡青 | 低风险入门、校色、产品选择原则 | 处方药和医美由专业人士评估 |
| 穿搭、身材与日常表达 | 轮廓、比例、姿态、低可见度表达 | 不把女性化等同于消瘦或刻板风格 |
| Cosplay 准备与拍摄 | 服化道、拍摄形式、沟通、保存与活动安全 | 不把外貌评价当作唯一标准，眼部和皮肤问题由专业人士评估 |
| 脚、鞋与袜子 | 脚部测量、鞋型选择、袜子材质与穿着安全 | 不盲目放大鞋码，疼痛、麻木或皮肤损伤时停止穿着 |
| 前列腺与后庭安全 | 成人探索、润滑、工具、停止信号 | 不保证高潮，不指导危险插入或强行扩张 |
| 其他成人性健康 | 乳首、非射精高潮、潮吹、催眠音声 | 只面向成年人，强调同意和身体安全 |

涉及跨性别医疗、激素、手术、处方减重药、疾病诊断或持续症状时，本 skill 只提供一般信息与就医分流，不提供个体处方、剂量或 DIY 医疗方案。

## 使用示例

```text
$femboy-skill 如何练习自然、可长期使用的伪音？

$femboy-skill 我总是遮不住胡青，应该先调整哪一步？

$femboy-skill 如何更安全地探索前列腺高潮？

$femboy-skill 我不方便公开女装，怎样增加低可见度的女性氛围？
```

skill 会尽量先给直接结论，再提供可执行的小步骤、观察指标、停止条件和最相关的来源链接。它不会承诺“通过”、高潮、固定训练周期或某种身体变化。

## 社区真实案例库

[`femboy-skill/cases/`](femboy-skill/cases/README.md) 用于收录成年贡献者提交、完成个人信息脱敏的第一手真实经历。案例按主题目录、经验阶段和结果分类，既收录有效经验，也保留部分有效、无效、停止和不良反应案例。

案例是帮助理解个体差异的社区经验，不是医学证据或效果保证。贡献者可以复制宽松的 [`_template.md`](femboy-skill/cases/_template.md)，放入对应类别目录并发起 PR；只需保留少量必填字段，其他章节可以根据经历自由删改。

投稿前必须删除本人及第三人的可识别信息，不提交私密照片、录音、病历号、精确地址、联系方式或涉及未成年人的露骨内容。详细规则与分类见[案例库说明](femboy-skill/cases/README.md)。

## 社区消费指南

[`femboy-skill/consumer/`](femboy-skill/consumer/README.md) 收录社区成员亲自购买、使用或到店体验过的商品、服务和店面，覆盖情趣用品、化妆和医美及女装配饰。每份记录至少包含名称、类型、链接、消费方式、推荐理由、缺点以及商业关系披露。

消费记录是个人体验，不是广告、医学背书或效果保证。贡献者可以复制简单的[消费记录模板](femboy-skill/consumer/_template.md)，放入对应[主题分类](femboy-skill/consumer/README.md)并发起 PR；商品、服务或店面链接必须是无短链、返利或联盟追踪的完整 HTTPS 页面。

## 安全原则

- **成年人限定：** 露骨性技巧只面向 18 岁及以上成年人；明确未满 18 岁时不提供插入、玩具或高潮训练步骤。
- **尊重身份：** 沿用使用者的自称与代词，不把表达方式、性取向、性实践和性别身份捆绑。
- **证据分层：** 社区经验用于启发练习，解剖、药物、疾病与急症以当前权威医学来源为准。
- **最低风险起步：** 给出小步、可逆的尝试，并明确疼痛、出血、嘶哑等停止信号。
- **不替代医疗：** 不诊断、不处方、不指导自行使用激素、GLP-1 减重药、麻醉剂或手术。
- **隐私与同意：** 不要求私密照片或录音；涉及伴侣时强调知情同意、可随时撤回和屏障防护。

完整边界见 [`femboy-skill/SKILL.md`](femboy-skill/SKILL.md) 与 [`medical-boundaries.md`](femboy-skill/references/medical-boundaries.md)。

## 项目结构

```text
femboy-skill/
├── femboy-skill/
│   ├── SKILL.md
│   ├── agents/openai.yaml
│   ├── cases/              # 分类案例、索引与投稿模板
│   ├── consumer/           # 社区消费指南与投稿模板
│   └── references/         # 主题知识与安全边界
├── assets/
├── .github/
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
├── LICENSE.md
└── NOTICE.md
```

## 知识来源与许可

本项目的主要社区知识底稿为 **[生如夏花知识库](https://wiki.viva-la-vita.org)**，并参考其公开源码仓库 **[viva-la-vita/wiki2](https://github.com/viva-la-vita/wiki2)**。截至 2026-08-25，本项目核对的 Wiki 源码提交为 `b48baf2173e5ee4409d68b8a0665d715df148309`。

生如夏花 Wiki 声明其内容混合国外互联网资料翻译与社区实践总结，除特别注明外采用 [Creative Commons Attribution-ShareAlike 4.0 International](https://creativecommons.org/licenses/by-sa/4.0/deed.zh-hans) 许可。本项目从该 Wiki 提炼的主题结构与摘要沿用 **CC BY-SA 4.0**，归属生如夏花开发者及相关原作者；再分发与改编时请保留署名、来源链接并以相同许可共享。

本项目并非生如夏花官方项目，也不代表其维护者立场。Wiki 中的社区经验经过风险筛选；医疗安全内容会尽量使用权威资料校正。详细来源映射见 [`source-map.md`](femboy-skill/references/source-map.md)，完整署名见 [`NOTICE.md`](NOTICE.md)。

README 的信息组织参考了 [Taste Skill](https://github.com/Leonxlnx/taste-skill) 的开源项目呈现方式，视觉与文案均为本项目原创。

## 参与社区

**我们最推荐的社区参与方式，是提交一份经过脱敏的成年人第一手真实案例。**真实的有效、无效、停止和不良反应经历，都能帮助后来者理解个体差异，也能让 Agent 的回答更贴近真实处境。

从宽松的[案例模板](femboy-skill/cases/_template.md)开始，选择最接近的[案例分类](femboy-skill/cases/README.md)，完成脱敏后直接发起 PR。你不需要公开真实姓名、账号、精确年龄、所在地、医疗机构、私密照片或录音；项目同样欢迎没有成功、主动停止或出现不良反应的经历。

也可以向[社区消费指南](femboy-skill/consumer/README.md)提交亲自购买、使用或到店体验过的商品、服务和店面，写清链接、消费方式、推荐理由、缺点和商业关系。

我们尤其欢迎来自 MTF、crossdresser、femboy、非二元及其他性别多元成年人的投稿。案例和消费记录之外，也欢迎安全修正、来源更新、术语改进和新的低风险主题。参与前请阅读 [`CONTRIBUTING.md`](CONTRIBUTING.md) 与 [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md)；医学主张需附权威来源，个人体验应明确标注为个人或社区经验。

发现可能导致身体伤害、错误用药或隐私泄露的问题时，请按照 [`SECURITY.md`](SECURITY.md) 的方式报告。

## 常见问题

<details>
<summary><strong>这是跨性别医疗指南吗？</strong></summary>

不是。项目尊重并支持跨性别者，但不以“男娘”概括跨性别女性，也不把医疗转变视为女性化表达的必经之路。涉及性别肯定医疗时，应转向合格、性别友善的医疗专业人士和循证指南。
</details>

<details>
<summary><strong>社区经验可信吗？</strong></summary>

它可以帮助理解体验和设计练习，但不能替代医学证据。skill 会标注社区经验，并在药物、疾病、解剖和急症方面优先采用权威来源。
</details>

<details>
<summary><strong>为什么限制未成年人使用？</strong></summary>

仓库包含露骨的成人身体探索内容，因此明确限定 18+。一般性的嗓音保护、基础护肤、穿搭、同意与身体边界教育，应从适合未成年人的专业资源获取。
</details>

## License

本项目采用 [CC BY-SA 4.0](LICENSE.md) 许可。使用、改编或再分发前，请同时阅读 [`NOTICE.md`](NOTICE.md) 中的第三方来源与署名要求。
