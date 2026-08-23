# CLAUDE.md — workbuddylink.com

> **WorkBuddyLink**: WorkBuddy 生态前端增长入口
> **母品牌**: NexFDE
> **部署**: GitHub Pages（纯静态 HTML，push 即部署）

## 项目信息

- **站点**: workbuddylink.com v1.1.1
- **类型**: 单页转化站（企业客户 + 渠道伙伴双受众），纯静态 HTML + CSS + JS
- **部署**: GitHub Pages（`ActionThinker/workbuddylink`），无构建步骤
- **设计系统**: 深青墨 `#101E26` + 品牌青绿 `#28b894`（借鉴 WorkBuddy 官方）+ 珊瑚橙 `#E8590C`（区隔强调），Inter 字体，浅青白 `#F6F8F7` 背景
- **AI 构建**: Claude (Anthropic) 辅助，FDE-style AI Deployment 方法

## 关键路径

| 路径 | 用途 |
|:---|:---|
| `index.html` | 主落地页（自包含 CSS/JS，8 模块：Hero/企业服务/问题/落地/信任/渠道/FAQ/CTA） |
| `assets/` | 静态资源（微信二维码、OG 图片） |
| `BUILDLOG.md` | 构建日志（每次迭代记录） |
| `CLAUDE.md` | GEO 规则 + 构建指令（本文件） |
| `llms.txt` | AI Agent 站点摘要 |
| `llms-full.txt` | 完整内容 Markdown 摘要 |

## 品牌约束（最高优先级）

1. **页面主角永远是 WorkBuddyLink**；对外不展示品牌体系层级与战略意图（页脚已移除品牌体系区块）
2. **主 CTA**: 企业客户「获取落地建议」/「获取启动建议」 | **次 CTA**: 合作伙伴「申请合作沟通」/「申请成为合作伙伴」
3. **语气**: 专业、清晰、有商业感。不空泛、不夸张承诺、不堆 AI 概念
4. **视觉**: 现代 B2B 增长站。深青墨+青绿+珊瑚橙，不用紫色/霓虹/粒子动效
5. **品牌关系**: NexFDE（总品牌）→ WorkBuddyLink（前端入口）→ FDE（交付底座）→ WorkBuddyMesh（伙伴网络，规划中）
6. **叙事**: 客户优先结构（企业结果 → 问题 → 落地 → 信任 → 渠道），削减「前端入口/后端交付/业务系统/生态能力」等内部术语的密集使用

## 合规口径（不能错，来自 workbuddy-business-brief.md）

- **商务 3 禁**: 不送免费试用 / 不送代金券 / 不打折 → 替代话术「先买 1 月/1 季，先开 1 坐席跑」
- **版本**: SaaS 企业版 1 席起 / 专有云 100 席起；专有云 ≠ 本地私有化
- **认证**: 说「信通院认证」不说「工信部认证」
- **署名**: One PC, One Buddy
- **脱敏**: 客户名 → 行业+规模；不暴露商业敏感信息
- **竞品**: 不点名、不贬低
- 不提及悦智分销协议细节（brief 未要求，避免渠道规则越界）

---

## GEO 自动化规则（每次修改页面强制执行）

> **目标渠道**: 豆包、DeepSeek、元宝、Kimi
> **核心原则**: AI 搜索不点链接，直接给答案。你的页面必须成为答案里被引用的那个来源。

### A. 页面标题
标题必须包含目标用户会搜索的问题或关键词。
格式: `[核心问题/关键词] | WorkBuddyLink`
当前: `WorkBuddy 企业导入、落地与持续运营 | WorkBuddyLink` ✅

### B. 页面描述
描述是 AI 生成答案时的摘要来源，必须包含：做什么 + 为谁做 + 独特价值。
当前: `基于 WorkBuddy 官方产品能力，结合 FDE 交付支持，帮助企业完成 AI 认知对齐、办公提效培训、业务场景评估、企业版采购与部署实施、定制化方案设计与持续应用陪跑；对合作伙伴提供销售赋能、联合获客、方案支撑与交付承接。` ✅

### C. 结构化数据（JSON-LD Schema）
页面必须包含 @graph 模式的 JSON-LD:
- Organization（含 sameAs, logo, contactPoint, parentOrganization）
- Service（含 offers, provider 引用）
- FAQPage（至少 8 个 FAQ）
- Article（含 datePublished, dateModified）
- BreadcrumbList

### D. 内容结构
1. 页面必须有清晰的 H1/H2/H3 层级
2. 每个 H2 段落必须能独立回答一个问题
3. 列表和表格优于大段文字
4. 关键术语首次出现时加 `<strong>` 标记（WorkBuddy、FDE、渠道伙伴、AI 认知对齐、业务场景评估、部署实施、持续陪跑）

### E. 内部链接
链接锚文本必须是描述性的:
✅ `<a href="#channel">申请渠道合作</a>`
❌ `<a href="#channel">点击这里</a>`

### F. AI 基础设施检查清单
每次部署前检查:
- [ ] llms.txt 反映最新页面结构
- [ ] robots.txt AI 爬虫指令正确
- [ ] sitemap.xml 日期更新
- [ ] JSON-LD @graph 完整
- [ ] .well-known/ai 可访问
- [ ] BUILDLOG.md 记录本次变更

### G. 渠道差异化

| 渠道 | 针对性动作 |
|------|-----------|
| 豆包 | Hero 首段可被截取为短答案 |
| DeepSeek | FAQ Schema + 结构化深度 |
| 元宝 | 标题含「导入」「落地」「持续运营」关键词 |
| Kimi | 页面保持足够深度和结构化 |

### H. 构建记录规则
每次对站点做实质性修改后:
1. 更新 BUILDLOG.md（时间倒序，记录决策原因）
2. 提交信息写「为什么」，不写「改了什么」
3. 版本号递增（MAJOR.MINOR.PATCH）

---

## 禁止操作

- ❌ 不要将 NexFDE 放到 Hero 主叙事中（WorkBuddyLink 才是主角）
- ❌ 不要使用紫色系、霓虹渐变、大面积纯黑背景
- ❌ 不要添加粒子、3D、复杂滚动动效
- ❌ 不要使用「颠覆」「革命」「重新定义」等夸张文案
- ❌ 不要承诺免费试用/代金券/折扣
- ❌ 不要在页面上使用 Jekyll 或任何构建框架（保持纯静态 HTML）
- ❌ 不要跳过 GEO 检查清单
- ❌ 不要跳过 BUILDLOG.md 记录
- ❌ 不要点名竞品、不要暴露客户身份
