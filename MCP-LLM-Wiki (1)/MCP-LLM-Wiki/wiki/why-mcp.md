# 為什麼需要 MCP？

> MCP 想降低 AI 應用與外部服務彼此整合的碎片化成本，而不是取代服務端本身的業務邏輯。[S01](../raw/s01-introduction.md)

## 沒有共通介面時

假設有 A、B 兩個 AI 助理，都需要接 GitHub、資料庫與行事曆。若每個助理都必須自行摸索每項服務的工具描述、參數格式及回傳資料的接收方式，會產生許多重複工作。對接仍然可行，但每個組合都需要額外管理。

## 有 MCP 後

服務端可以藉由 MCP Server 暴露一致規範下的能力描述。支援 MCP 的 Host 透過自己的 MCP Client 探索並使用這些能力。這不是「一鍵萬能」；使用者授權、認證設定、Server 安裝／託管、業務 API 適配仍然存在。[S01](../raw/s01-introduction.md) [S02](../raw/s02-architecture.md)

## 後端工程師視角

重要的是**介面契約（contract）**：Server 明確告知「我有哪些工具」、「參數需要什麼型別」、「能取得哪些資料」；Host 遵循協定完成對接。不同產品得以共享協定層，但真正連到資料庫的 SQL 查詢與權限設計仍是後端系統的工作。

## 常見誤解

- 不是 MCP 就不能 Tool Calling：錯；沒有 MCP 的專用整合仍能做工具呼叫。
- 有 MCP 就不需要 API：錯；MCP Server 可以在背後調用 API。
- 有 MCP 就表示工具值得信任：錯；工具仍需控制權限與驗證輸入。

## 延伸

[[compare]]、[[security]]、[[architecture]]。來源：[S01](../raw/s01-introduction.md)、[S02](../raw/s02-architecture.md)。
