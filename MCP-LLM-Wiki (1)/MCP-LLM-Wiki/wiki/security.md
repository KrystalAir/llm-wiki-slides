# MCP 安全與信任邊界

> MCP 能讓 AI 接觸真實資料與操作，因此每一次 Tool 呼叫都可能涉及權限、外部服務與使用者資料；協定標準化**不等於**自動安全。[S05](../raw/s05-security.md) [S04](../raw/s04-specification.md)

## 為什麼風險比一般聊天高？

如果 AI 只能回答文字，錯誤影響多半在答案內容；當它能呼叫工具修改檔案、查資料庫、發 API 請求，就可能產生可持續的副作用。Host、Server 與外部資源應各自評估最小權限與是否需要使用者核准。

## 官方明列的風險類型

| 類型 | 基本理解 | 防護方向 |
|---|---|---|
| Confused Deputy | 某個具權限的代理被其他方誘導濫用授權 | 每個客戶端獨立同意與嚴格驗證授權流程 |
| Token Passthrough | Server 盲目接受／轉送不屬於自己的 Token | 驗證 Token audience，避免直接轉交下游 |
| SSRF | 藉由 Server／授權流程導向非預期內部網址 | 驗證目標網址、限制網路可達範圍 |
| Local Server Compromise | 本機 MCP Server 被入侵或具有過高權限 | 限制 OS 權限、只安裝可信來源 |

詳見 [S05 官方安全指引](../raw/s05-security.md)，尤其授權伺服器與 Proxy 的不同角色。[S05](../raw/s05-security.md)

## 實務設計檢查

1. 是否確定 MCP Server 的來源與維護者？
2. 是否只授予完成任務所需的最小權限？
3. 是否有機會讓模型在使用者未預期時做出破壞性寫入？
4. 遇到敏感 Tool 是否有明確同意、審計與拒絕路徑？
5. 若涉及 OAuth，是否正確驗證對象、redirect、scope 與 token 用途？

## 容易忽略的版本問題

官方 `2026-07-28` 安全指南特別提醒：Dynamic Client Registration 已被標記為 deprecated，但仍支援舊流程的相容性實作可能受到歷史攻擊模式影響。[S05](../raw/s05-security.md)

## 延伸

[[call-sequence]]、[[protocol-2026]]、[[faq]]。來源：[S05](../raw/s05-security.md)、[S04](../raw/s04-specification.md)。
