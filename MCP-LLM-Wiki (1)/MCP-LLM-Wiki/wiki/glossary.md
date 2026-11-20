# MCP 詞彙表

| 名詞 | 中文直觀解釋 | 連結／來源 |
|---|---|---|
| MCP | AI 應用與外部工具／資料的開放對接協定 | [[overview]] · [S01](../raw/s01-introduction.md) |
| Host | 管理 AI 模型與連接的應用程式 | [[architecture]] · [S02](../raw/s02-architecture.md) |
| Client | Host 內對應特定 Server 的協定連線元件 | [[architecture]] · [S02](../raw/s02-architecture.md) |
| Server | 向 Client 提供 Tools、Resources 或 Prompts 的程式 | [[architecture]] · [S03](../raw/s03-server-concepts.md) |
| Tool | 可以被呼叫執行的功能 | [[primitives]] · [S03](../raw/s03-server-concepts.md) |
| Resource | 供讀取的上下文資料 | [[primitives]] · [S03](../raw/s03-server-concepts.md) |
| Prompt | 預先定義的互動模板 | [[primitives]] · [S03](../raw/s03-server-concepts.md) |
| JSON-RPC | 以 JSON 表達請求／結果／通知的 RPC 訊息協定 | [[protocol-2026]] · [S04](../raw/s04-specification.md) |
| stdio | 本機程式透過標準輸入與輸出傳輸資料 | [[protocol-2026]] · [S02](../raw/s02-architecture.md) |
| Streamable HTTP | MCP 可用的 HTTP 遠端傳輸方式 | [[protocol-2026]] · [S02](../raw/s02-architecture.md) |
| `server/discover` | 發現 Server 支援哪些版本與能力的操作 | [[protocol-2026]] · [S02](../raw/s02-architecture.md) |
| `tools/list` | 取得可用工具的定義 | [[primitives]] · [S03](../raw/s03-server-concepts.md) |
| `tools/call` | 呼叫某個工具並帶入參數 | [[call-sequence]] · [S03](../raw/s03-server-concepts.md) |
| stateless | 核心請求攜帶處理所需版本與能力資訊的無狀態模式 | [[protocol-2026]] · [S04](../raw/s04-specification.md) |
| Scope | Token 被授予的權限範圍 | [[security]] · [S05](../raw/s05-security.md) |
| Token Audience | Token 是發給哪個資源／服務使用 | [[security]] · [S05](../raw/s05-security.md) |
