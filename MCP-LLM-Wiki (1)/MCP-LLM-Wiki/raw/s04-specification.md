---
id: S04
type: source-note
status: ingested
source_title: MCP Specification
source_publisher: Model Context Protocol
source_url: https://modelcontextprotocol.io/specification/2026-07-28
spec_baseline: 2026-07-28
accessed: 2026-11-20
copyright_note: 原文網址與中文整理，非原文全文副本
---
# S04｜MCP 2026-07-28 正式規範（入口）

**[閱讀官方規範入口](https://modelcontextprotocol.io/specification/2026-07-28)**

## 關鍵摘記（中文轉述）

- MCP 是 AI Host／Client 與提供資訊或操作的 Server 之間的開放協定，採 JSON-RPC 2.0 作為訊息基礎。
- 2026-07-28 核心請求採無狀態設計，相關版本和能力資訊隨請求傳送；規範入口連結到各個子規格。
- Server 的三大核心能力是 Resources、Prompts、Tools，還有授權、取消、進度、錯誤等概念。
- 部分功能被規劃為需雙方支援的擴充，例如長任務與應用內互動元件。不可把擴充等同所有 MCP 實作必備功能。
- 設計原則明確強調使用者授權與隱私；協定具備機制不代表應用自行實現了安全。

## 可導出的概念頁

[[protocol-2026]]、[[architecture]]、[[security]]

## 核查問題

- 這是**規範入口**而非所有子章節的逐字封存。需精確實作細節時，應循官方子規範查驗。
