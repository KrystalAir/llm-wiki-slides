---
id: S03
type: source-note
status: ingested
source_title: Understanding MCP servers
source_publisher: Model Context Protocol
source_url: https://modelcontextprotocol.io/docs/2026-07-28/learn/server-concepts
spec_baseline: 2026-07-28
accessed: 2026-11-20
copyright_note: 原文網址與中文整理，非原文全文副本
---
# S03｜Server 能暴露的三大功能

**[閱讀官方全文](https://modelcontextprotocol.io/docs/2026-07-28/learn/server-concepts)**

## 關鍵摘記（中文轉述）

- **Tools** 是可由模型選擇使用的動作介面，例如查詢 API 或修改資料；每個工具使用 schema 描述輸入／輸出。
- **Resources** 提供上下文資料，例如文件、結構描述或資料內容，常由應用選擇讀取。
- **Prompts** 提供可重用的互動模板，通常由使用者主動選擇。
- `tools/list` 用來取得可用工具的名稱及定義；`tools/call` 送出實際的工具名稱與參數。
- 三種能力的目的不同，不應把 Server 理解成只有工具呼叫。

## 可導出的概念頁

[[primitives]]、[[call-sequence]]、[[glossary]]

## 核查問題

- 「誰控制功能」是設計上的典型用法，不是表示程式永遠不能用其他方式存取。
