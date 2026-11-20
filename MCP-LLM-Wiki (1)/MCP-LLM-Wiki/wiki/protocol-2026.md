# MCP 2026-07-28 通訊重點

> **重要版本註記**：本頁只以官方 `2026-07-28` 文檔為基準，不能用較早版本常見的初始化握手流程代替。[S02](../raw/s02-architecture.md) [S04](../raw/s04-specification.md)

## JSON-RPC 2.0

MCP 的資料層採 JSON-RPC 2.0。你會看到 `method`（要呼叫的操作）、`params`（參數）、`id`（將回覆對應到請求）等欄位。這是**協定訊息格式**，不是讓 LLM 自己「說出 JSON」就等於實作 MCP。[S04](../raw/s04-specification.md)

## 2026-07-28 的關鍵演進

- 請求採 **stateless（無狀態）** 核心模型，隨請求帶上版本與能力相關 `_meta`；不應假設伺服器必須靠先前的長連線初始化狀態才能理解後續請求。
- Server 要支援 `server/discover` 來提供版本與能力資訊，但 **Client 可選擇不先呼叫 discover**；因此不應聲稱 discover 是每個請求前的必要握手。
- `tools/list` 可以發現工具，`tools/call` 可呼叫工具。
- 回應結果型態包含 `resultType`，避免將舊版範例直接貼到新版程式中。

本頁提供概念，確切 JSON 欄位結構與 MUST/SHOULD 語義請以 [正式規範](https://modelcontextprotocol.io/specification/2026-07-28) 及 [架構範例](https://modelcontextprotocol.io/docs/2026-07-28/learn/architecture) 為準。[S02](../raw/s02-architecture.md) [S04](../raw/s04-specification.md)

## Transport：資料如何移動？

1. **stdio**：適合同一台機器上互相啟動／溝通的本機程式。
2. **Streamable HTTP**：適合透過網路存取的 MCP Server，可能包含額外的認證、安全與串流設計。

傳輸方式與 Tool 定義是不同層次：即使 transport 不同，Data Layer 仍保留核心訊息語義。[S02](../raw/s02-architecture.md)

## 不要混淆

- MCP ≠ HTTP：MCP 可以用 HTTP 傳輸，但也可用 stdio。
- MCP ≠ 一個 API URL：它規範了能力探索、呼叫與回傳的資料層互動。
- 「無狀態」≠ 服務完全沒有資料或快取；是針對核心請求的處理約定。

## 延伸

[[call-sequence]]、[[architecture]]、[[security]]。來源：[S02](../raw/s02-architecture.md)、[S04](../raw/s04-specification.md)。
