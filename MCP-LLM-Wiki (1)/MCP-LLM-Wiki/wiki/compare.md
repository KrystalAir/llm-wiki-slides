# MCP vs API、Function Calling、RAG

> 這是**教學性概念比較**，用途是避免初學者混淆層次；部分判讀基於系統設計的合理推論，並非官方規範提供的正式對照表。[S01](../raw/s01-introduction.md) [S04](../raw/s04-specification.md)

| 概念 | 最核心的問題 | 與 MCP 的關係 |
|---|---|---|
| API | 服務提供哪些資料／功能，程式如何使用？ | MCP Server 背後常會調用現有 API；MCP 不取代服務本身。 |
| Function Calling / Tool Calling | 模型如何選擇、描述、要求呼叫函式？ | MCP 提供跨 Host–Server 的能力探索與執行協定；模型側的 Tool Calling 可與 MCP 協作。 |
| RAG | 回答時如何檢索相關外部知識？ | RAG 是知識檢索與生成策略；可透過 MCP Tool / Resource 取得知識，但彼此獨立。 |
| MCP | AI 應用與外部工具／資料源如何標準化連接？ | 處理不同系統間的協定層介面。 |

## 生活化理解

- API：餐廳的後廚能力。
- Function Calling：模型決定「要點哪道菜、需哪些參數」。
- MCP：讓不同 AI 助理用一致的方式查看菜單、送出訂單並取得結果的溝通協定。
- RAG：為回答問題而翻閱菜單與相關資料的檢索策略。

這是**比喻**，不是嚴格的一對一技術等價。

## 最實用的結論

一個系統可以**同時使用四者**：模型利用 Tool Calling 決定要找資料，Host 經 MCP Client 呼叫 MCP Server，Server 透過 API 存取後端；回傳的資料可能被納入 RAG 的回答脈絡。這是可能的設計組合，不表示 MCP 必定搭配 RAG。[S01](../raw/s01-introduction.md) [S02](../raw/s02-architecture.md)

## 延伸

[[why-mcp]]、[[call-sequence]]、[[primitives]]。
