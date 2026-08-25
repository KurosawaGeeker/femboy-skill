# 参与贡献

感谢你帮助 Femboy Skill 变得更准确、安全和包容。贡献者不需要公开自己的性别身份、性取向、医疗经历或任何私密信息。

## 适合贡献的内容

- 修正危险、过时或证据不足的建议；
- 补充伪音、女性化表达与成人性健康的权威来源；
- 改善对 MTF、crossdresser、femboy、非二元及其他性别多元人群的措辞；
- 提交新的低风险实践主题或更清晰的停止信号；
- 向分类案例库提交完成脱敏的成年人第一手真实经历；
- 修正文档、链接、安装说明和 Agent 兼容性问题。

## 提交真实案例

案例库位于 [`femboy-guide/cases/`](femboy-guide/cases/README.md)。投稿步骤：

1. 阅读案例库的分类、18+ 与脱敏要求；
2. 复制 [`_template.md`](femboy-guide/cases/_template.md) 到最匹配的主题目录；
3. 选择 `experience_level` 和 `outcome`，如实保留无效、停止或不良反应结果；
4. 删除本人、伴侣、医生和机构的可识别信息；
5. 在 [`INDEX.md`](femboy-guide/cases/INDEX.md) 的对应分类增加一行；
6. 发起 PR，并勾选 PR 模板中的案例确认项。

只接收投稿者本人在成年后发生的真实经历。可以用 AI 整理语言，但不能虚构、拼接、转载或代投；维护者可以要求进一步脱敏。模板刻意保持宽松，除标记“必填”的部分外，可以根据经历删改。

## 内容要求

1. 成人露骨内容必须明确限定 18+，不得描述或暗示未成年人参与。
2. 医学、药物、疾病、解剖或急症主张应附当前权威来源；优先指南、政府/大学医疗机构与同行评议研究。
3. 个人或社区体验要明确标注，不得承诺普遍结果。
4. 不提交 DIY 激素、处方药剂量、危险插入、疼痛训练、非自愿实践或规避医疗监管的指导。
5. 沿用当事人的自称和代词，不把某种表达、性实践或身体特征绑定为身份标准。
6. 不在 Issue、PR、截图或样例中泄露本人或他人的私密影像、病历与可识别信息。
7. 案例投稿不得包含具体处方剂量、绕过处方的购药渠道或鼓励自行停药；不良反应应优先说明停止与专业求助。

## 工作流

1. 先搜索现有 Issue，避免重复。
2. 从 `main` 创建符合 Conventional Commits 语义的分支，例如 `docs/safety-source-update`。
3. 修改后运行校验：

   ```bash
   python3 /path/to/skill-creator/scripts/quick_validate.py femboy-guide
   python3 scripts/validate_cases.py
   git diff --check
   ```

4. Commit 使用 `type(scope): subject`，例如 `docs(safety): clarify adult-content boundary`。
5. 提交 PR，说明改动、来源、风险与验证结果。

来自生如夏花 Wiki 的改编内容必须保留来源链接，并以 CC BY-SA 4.0 相同方式共享。
