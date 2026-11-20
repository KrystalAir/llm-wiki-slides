---
id: S05
type: source-note
status: ingested
source_title: Security Best Practices
source_publisher: Model Context Protocol
source_url: https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices
spec_baseline: 2026-07-28
accessed: 2026-11-20
copyright_note: 原文網址與中文整理，非原文全文副本
---
# S05｜官方 MCP 安全最佳實務

**[閱讀官方全文](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices)**

## 關鍵摘記（中文轉述）

- 官方將 MCP 安全議題具體分成多種攻擊情境，包括 Confused Deputy、Token Passthrough、SSRF 與本機 Server 受入侵等。
- Proxy 在授權鏈中的身分、client ID、redirect URI、token audience 不可含糊，否則可能繞過使用者意圖或跨服務濫用憑證。
- 權限應最小化；涉及檔案修改、敏感資訊與外部 API 的工具，應審查實際資料流及授權。
- 2026-07-28 已廢止 Dynamic Client Registration 作為推薦流程；仍支援舊機制的相容性實作可能承擔額外風險。

## 可導出的概念頁

[[security]]、[[faq]]

## 核查問題

- 任何「MCP 預設安全」的說法都不成立，必須評估 Host、Server、授權層與實際操作權限。
