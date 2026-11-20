# MCP 初學者常見問題

## 1. MCP 是不是 AI 模型？

不是。MCP 是應用與外部系統之間的連接協定，不是模型權重或訓練演算法。[S01](../raw/s01-introduction.md)

## 2. MCP Client 就是 ChatGPT／IDE 本身嗎？

嚴格來說 Host 才是使用者操作的 AI 應用；Client 是 Host 內連接特定 Server 的元件。詳見 [[architecture]]。[S02](../raw/s02-architecture.md)

## 3. 一定需要建立自己的 MCP Server 嗎？

沒有。若目標是理解協定，可以先閱讀架構、呼叫流程並觀察既有 Server。若要向外提供自有資料或工具，才需要建置自己的 Server。這是學習建議，不是協定限制。

## 4. MCP 是不是和 Function Calling 一模一樣？

不是。Function Calling 常指模型選擇要執行哪個工具；MCP 則規範 Host 的 Client 如何與外部 Server 探索、請求與接收結果。詳見 [[compare]]。[S02](../raw/s02-architecture.md)

## 5. MCP 是不是 RAG？

不是。RAG 偏重「檢索資訊再生成答案」，MCP 偏重「系統之間的對接」。兩者可以搭配。詳見 [[compare]]。

## 6. 2026-07-28 還需要 initialize 嗎？

這份 Wiki 的新版本流程不把舊式 `initialize` 握手當成必要流程，採 per-request `_meta` 和可選的 `server/discover`。詳見 [[protocol-2026]]。[S02](../raw/s02-architecture.md)

## 7. 安裝 MCP Server 就完全安全嗎？

不會。需要看 Server 來源、擁有哪些權限、Token 使用、網路存取、是否得到使用者同意。詳見 [[security]]。[S05](../raw/s05-security.md)
