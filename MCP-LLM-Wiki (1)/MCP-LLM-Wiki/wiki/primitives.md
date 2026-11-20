# MCP Server 三大能力：Tools、Resources、Prompts

> 它們解決不同需求：**動作**、**資料**、**互動模板**。三者不是同義詞。[S03](../raw/s03-server-concepts.md) [S04](../raw/s04-specification.md)

| 能力 | 典型使用者 | 做什麼 | 例子 | 常見操作 |
|---|---|---|---|---|
| Tool | 模型依情境選擇呼叫 | 執行功能，可能有副作用 | `get_issue`, `create_issue` | `tools/list`, `tools/call` |
| Resource | 應用決定讀取 | 提供上下文資料 | GitHub 專案 README、資料庫 schema | `resources/list`, `resources/read` |
| Prompt | 使用者選擇 | 可重用的互動流程模板 | 「用固定格式摘要 issue」 | `prompts/list`, `prompts/get` |

**提醒**：「模型／應用／使用者控制」是官方對典型交互方式的說明，不代表硬性禁止程式以其他方式使用這些能力。[S03](../raw/s03-server-concepts.md)

## Tool 的資料契約

一個 Tool 通常至少有名稱、描述及輸入 schema。模型可看到這個描述、決定是否提出工具使用；Host 負責透過 MCP Client 執行。安全敏感工具可能需要使用者核准。[S03](../raw/s03-server-concepts.md)

## 用 GitHub 案例區分

- Tool：執行「列出尚未關閉的 Issues」。
- Resource：提供「專案 README」作為背景知識。
- Prompt：提供「依重要性整理 Issues 的格式模板」。

這是教學性範例，不代表每個 GitHub MCP Server 都必定暴露這三項。

## FAQ

**Tools 和 Resources 不都是資料嗎？** Tool 可以查回資料，但它的核心是「請求執行某個功能」；Resource 更像提供可讀的資訊入口。實際設計有重疊，需要看 Server 的介面。

## 延伸

[[architecture]]、[[call-sequence]]、[[security]]、[[glossary]]。來源：[S03](../raw/s03-server-concepts.md)、[S02](../raw/s02-architecture.md)。
