# WorkbuddyLink.com — 生态增长入口

> WorkBuddy 生态前端入口 + FDE 定制化交付网络。企业落地合作 × 渠道伙伴合作 × 交付支撑。
> 本项目由 Claude 辅助构建，本身就是 FDE-style AI Deployment 方法的一个活案例。

## 这个站点是什么

`WorkbuddyLink.com` 是海角旗下 WorkBuddy 生态业务的前端增长入口，承接：

- 企业合作咨询（产品咨询 / 培训 / 解决方案 / 运营陪跑）
- 渠道合作申请
- 预约演示 / 商务合作线索

它**不是**总品牌官网（那是 `NexFDE.com`），也**不是**交付能力专题站，而是一个明确服务于获客、合作转化、渠道招商的连接型入口站。

## 商业模式一句话

> 前端依托 WorkBuddy 产品能力与生态势能连接客户和伙伴，后端通过 FDE 定制化交付网络承接培训、销售转化、方案落地与持续运营——把产品分销、方案设计、定制交付与渠道赋能组织成可复制的网络。

## 技术栈与部署

| 项 | 说明 |
|---|---|
| 技术 | 纯静态 HTML + CSS + 原生 JS，零框架、零构建 |
| 部署 | GitHub Pages + GitHub Actions workflow（push master 即部署） |
| 域名 | workbuddylink.com（CNAME，A 记录待配置） |
| 设计系统 | 深青墨 #101E26 + 品牌青绿 #28b894（借鉴 WorkBuddy 官方）+ 珊瑚橙 #E8590C（区隔） |

## 目录结构

```
site/
├── index.html            # 主落地页（15 区块，自包含 CSS/JS/JSON-LD）
├── assets/               # OG 图、微信二维码
├── .well-known/ai        # AI 发现端点
├── llms.txt              # AI Agent 站点摘要
├── llms-full.txt         # 完整内容（RAG）
├── robots.txt            # AI 爬虫策略
├── sitemap.xml           # 站点地图
├── CLAUDE.md             # GEO 规则 + 品牌约束 + 合规口径
└── BUILDLOG.md           # 构建日志
```

## 构建方法（活案例）

本站点遵循 FDE 三步方法构建：**判断**（确认定位与受众）→ **试点**（快速上线可用的首页）→ **上线**（一次部署并验证）。每个区块都服务一个转化目标。

## 合规

- 商务口径对齐 WorkBuddy 业务 Brief（不送试用/不打折、信通院认证、SaaS 1 席起等）
- AI 构建透明：页面含 `ai-disclosure` meta，符合 EU AI Act Article 50

---

© 2026 WorkbuddyLink · NexFDE 生态入口
