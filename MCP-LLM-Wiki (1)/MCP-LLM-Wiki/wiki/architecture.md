# MCP 架構：Host、Client、Server

> `2026-07-28` 文件將 MCP 描述為 Host 管理一個或多個 Client，每個 Client 與某個 Server 互動的架構。[S02](../raw/s02-architecture.md)

## 角色

| 角色 | 工作 | 記憶法 |
|---|---|---|
| Host | AI 應用的協調者，整合模型輸出與連接 | 使用者看到的程式 |
| Client | 依 MCP 協定與一個 Server 通訊 | 協定的客戶端元件 |
| Server | 公開工具、資料或 Prompt 等能力 | 功能提供者 |

## 路徑示意

```text
使用者
   │
   ▼
AI Host (例如支援 MCP 的開發工具)
   ├── MCP Client A ──MCP── MCP Server A ── 內部 GitHub API
   └── MCP Client B ──MCP── MCP Server B ── 本機檔案／資料庫
```

圖中兩個 Server 只是例子。Host 可以動態連接多個 Server。MCP Server 不一定是雲端網路服務；本機程式也是 Server。[S02](../raw/s02-architecture.md)

## 兩層協定

- **Data Layer**：採 JSON-RPC 2.0 的請求、結果、方法名，定義能探索與使用哪些能力。
- **Transport Layer**：讓訊息實際傳遞；常見本機 `stdio` 與遠端 `Streamable HTTP`，遠端傳輸應處理認證與安全。

MCP 不決定模型內部如何推理，也不規定 AI 一定要怎樣消化取得的資料。[S02](../raw/s02-architecture.md)

## 常見誤解

1. MCP Client **不等於使用者 UI**，它是 Host 裡負責協定的元件。
2. MCP Server 不一定在另一台電腦；可與 Host 同機執行。
3. MCP 不代表 Host 無條件信任任何 Server，詳見 [[security]]。

## 延伸

[[overview]]、[[protocol-2026]]、[[call-sequence]]、[[primitives]]。

## 來源

[S02](../raw/s02-architecture.md) · [S04](../raw/s04-specification.md)
