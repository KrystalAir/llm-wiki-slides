# MCP 是什麼？一分鐘總覽

> **MCP（Model Context Protocol）是一種讓 AI 應用以一致方式與外部資料及工具溝通的開放協定。** 它界定的是「怎麼對接」，不是「模型怎麼思考」。本文依 `2026-07-28` 規範整理。[S01](../raw/s01-introduction.md) [S04](../raw/s04-specification.md)

## 從問題看它的價值

想像你要求 AI：「從我的工作專案找最新 issue，再幫我整理摘要。」語言模型本身不會自動擁有 GitHub 登入權限，也不知道哪些 API 可以調用。AI 應用必須有一套方式：找到可用的工具、知道工具的參數、把動作交給外部系統，最後把結果帶回對話。MCP 將這類連接的規則標準化。

## 最重要的三個角色

- **Host**：你實際使用的 AI 應用。
- **Client**：Host 內專責和某個 Server 溝通的連接元件。
- **Server**：對外提供工具、上下文資料與提示模板的程式。

詳見 [[architecture]]。[S02](../raw/s02-architecture.md)

## 最重要的三種能力

- **Tools**：呼叫可執行動作，例如搜尋或更新一筆資料。
- **Resources**：取得模型可參考的資訊，例如資料庫 schema。
- **Prompts**：取用預設好的互動模板。

詳見 [[primitives]]。[S03](../raw/s03-server-concepts.md)

## 一句話避免誤解

MCP **不是**模型本身、不是大型語言模型訓練技術，也不是「把所有 API 取代」。它是讓 AI 應用對接外部能力的一種標準；底層服務仍可使用既有 API。[S01](../raw/s01-introduction.md) [S04](../raw/s04-specification.md)

## 下一步

[[why-mcp]] → [[architecture]] → [[call-sequence]] → [[security]]。
