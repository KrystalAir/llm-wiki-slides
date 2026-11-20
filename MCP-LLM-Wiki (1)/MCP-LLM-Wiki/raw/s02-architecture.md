---
id: S02
type: source-note
status: ingested
source_title: Architecture overview
source_publisher: Model Context Protocol
source_url: https://modelcontextprotocol.io/docs/2026-07-28/learn/architecture
spec_baseline: 2026-07-28
accessed: 2026-11-20
copyright_note: 原文網址與中文整理，非原文全文副本
---
# S02｜架構與訊息交換

**[閱讀官方全文](https://modelcontextprotocol.io/docs/2026-07-28/learn/architecture)**

## 關鍵摘記（中文轉述）

- MCP Host 是 AI 應用，會為連接的各 Server 建立 MCP Client；Client 管理與對應 Server 的連線。
- Server 可在本機或遠端執行：常見傳輸包含本機 stdio 與遠端 Streamable HTTP。
- 協定分 Data Layer（JSON-RPC、功能與能力）和 Transport Layer（傳輸與連線）。
- 2026-07-28 說明了無狀態請求、`_meta` 內的版本／能力資訊、可選的 `server/discover` 查詢、`tools/list` 與 `tools/call`。
- 舊文件常見初始化順序與新版不同，教學不可混用。

## 可導出的概念頁

[[architecture]]、[[primitives]]、[[protocol-2026]]、[[call-sequence]]

## 核查問題

- `server/discover` 是 Server 應支援的操作；Client 不一定每次都先發出此請求，不能寫成每次工具呼叫必經之步驟。
