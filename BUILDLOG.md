# WorkbuddyLink Build Log

> 每一次构建决策，都是 FDE 方法论的实际应用记录。

---

## 2026-08-23 — v1.0.0 首版上线

**版本**: v1.0.0

### 决策背景
海角 WorkBuddy 生态业务需要一个独立的前端增长入口站，承接企业合作咨询、渠道合作申请、预约演示与商务线索。复刻 NexFDE.com 已验证的落地路径（纯静态 HTML + GitHub Pages + Actions workflow + GEO/AI 基础设施），快速上线可转化的首页。

### 具体变更
- 新建 `ActionThinker/workbuddylink` 仓库，纯静态单页站（15 区块）
- Hero 双 CTA：预约沟通 / 申请渠道合作
- 双受众内容架构：企业客户价值 + 渠道伙伴价值 + 双轨合作路径
- 联系区：企业合作/渠道合作双 tab 表单（mailto 组装 + 线索来源标记 + 感谢态）+ 微信二维码
- 设计系统：深青墨 `#101E26` + 品牌青绿 `#28b894`（借鉴 WorkBuddy 官方 workbuddy.cn 实测色板）+ 珊瑚橙 `#E8590C`（区隔）
- GEO/AI 基础设施：llms.txt / llms-full.txt / robots.txt / sitemap.xml / .well-known/ai / JSON-LD @graph
- 合规口径对齐 WorkBuddy 业务 Brief：商务 3 禁、信通院认证、SaaS 1 席起、One PC One Buddy、案例脱敏

### 设计决策
- **借鉴官方色系做区隔**：品牌青绿直接采用官方 Workbuddy 色 `#28b894`（生态识别），深色基调换成青色墨黑、CTA 换成官方没有的珊瑚橙，避免与官方站混淆
- **转化导向**：每个区块都收口到一个 CTA，线索来源下拉 + mailto 预填 + 感谢态，纯静态下实现可用的线索收集
- **双轨叙事**：企业（Toolkit→Result 断层）与渠道（Opportunity→Delivery 断层）分列痛点，路径双轨展示

### 待办（用户侧）
- workbuddylink.com 域名 A 记录配置（185.199.108.153 等 4 条）→ 生效后自动切自定义域名
