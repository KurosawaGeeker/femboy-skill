# 参与贡献

感谢你帮助 Femboy Skill 变得更准确、安全和包容。贡献者不需要公开自己的性别身份、性取向、医疗经历或任何私密信息。

## 适合贡献的内容

- 修正危险、过时或证据不足的建议；
- 补充伪音、女性化表达与成人性健康的权威来源；
- 改善对 MTF、crossdresser、femboy、非二元及其他性别多元人群的措辞；
- 提交新的低风险实践主题或更清晰的停止信号；
- 修正文档、链接、安装说明和 Agent 兼容性问题。

## 内容要求

1. 成人露骨内容必须明确限定 18+，不得描述或暗示未成年人参与。
2. 医学、药物、疾病、解剖或急症主张应附当前权威来源；优先指南、政府/大学医疗机构与同行评议研究。
3. 个人或社区体验要明确标注，不得承诺普遍结果。
4. 不提交 DIY 激素、处方药剂量、危险插入、疼痛训练、非自愿实践或规避医疗监管的指导。
5. 沿用当事人的自称和代词，不把某种表达、性实践或身体特征绑定为身份标准。
6. 不在 Issue、PR、截图或样例中泄露本人或他人的私密影像、病历与可识别信息。

## 工作流

1. 先搜索现有 Issue，避免重复。
2. 从 `main` 创建符合 Conventional Commits 语义的分支，例如 `docs/safety-source-update`。
3. 修改后运行校验：

   ```bash
   python3 /path/to/skill-creator/scripts/quick_validate.py femboy-guide
   git diff --check
   ```

4. Commit 使用 `type(scope): subject`，例如 `docs(safety): clarify adult-content boundary`。
5. 提交 PR，说明改动、来源、风险与验证结果。

来自生如夏花 Wiki 的改编内容必须保留来源链接，并以 CC BY-SA 4.0 相同方式共享。
