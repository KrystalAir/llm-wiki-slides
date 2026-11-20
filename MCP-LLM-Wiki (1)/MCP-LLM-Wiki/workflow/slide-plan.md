# 從 Wiki 生成教學 HTML：檢索策略與大綱

## 需求

- 主題：什麼是 MCP？
- 受眾：沒有 MCP 背景、知道基本 AI 概念的初學者
- 格式：能直接在瀏覽器開啟的 HTML／CSS／JS，非圖片或只提供 PPT。
- 限制：事實資訊需出自 Wiki 和可追溯的來源 ID；統一 `2026-07-28`。

## 頁面規劃（12 頁）

| 頁 | 主題 | 優先讀取 Wiki | 資料 ID |
|---|---|---|---|
| 1 | 什麼是 MCP？ | [[overview]] | S01 |
| 2 | AI 無法憑空存取工具 | [[why-mcp]] | S01 |
| 3 | 整合上的重複工作 | [[why-mcp]] | S01、S02 |
| 4 | Host / Client / Server | [[architecture]] | S02 |
| 5 | 本機與遠端架構 | [[architecture]] | S02 |
| 6 | Tools / Resources / Prompts | [[primitives]] | S03 |
| 7 | 什麼是 JSON-RPC？ | [[protocol-2026]] | S02、S04 |
| 8 | 一次 Tool Call 的七步驟 | [[call-sequence]] | S02、S03 |
| 9 | MCP vs API / Function Calling | [[compare]] | S01、S04（教學推論） |
| 10 | MCP vs RAG | [[compare]] | S01、S04（教學推論） |
| 11 | 為何要注意安全？ | [[security]] | S05 |
| 12 | 總結 + 三題測驗 | [[faq]]、[[glossary]] | S01–S05 |

## 對 LLM 的簡報生成 Prompt

> 先閱讀 `AGENTS.md`、`index.md`、`workflow/slide-plan.md`。依照表格逐頁閱讀所需 Wiki，設計一份 12 頁繁體中文教學 HTML，適合零基礎大學生；每頁要有主要概念、一個例子／圖示或提問，以及資料來源的 S 編號及可點擊原文 URL。不可擅自加入 Wiki 未支持的技術事實；在 2026-07-28 版的通訊示意，不要使用舊版 `initialize`。輸出單檔 `index.html`（CSS/JS 內嵌），支援上一頁下一頁和鍵盤箭頭。生成後完成 `workflow/quality-checklist.md` 的檢查並將真實結果寫到新的 experiment-log 檔案。若檢查失敗，修正受影響的頁面再驗證，最多重試 3 次，不可捏造結果。

## 檢索流程

1. **路由**：依投影片主題，從 `index.md` 或上表選 Wiki 頁。
2. **讀頁**：只讀相關 Wiki 頁並記下 S 來源 IDs。
3. **查回原文**：對易混淆／版本敏感資訊，連回 `raw/Sxx` 的官方 URL。
4. **驗證**：要求每張投影片的技術重點至少有一個來源 ID；比較性推論額外標記「教學推論」。
5. **輸出**：生成 HTML，後續實際在瀏覽器開啟測試。

## 本次執行狀態

- 已依上表生成 `presentation/index.html`，12 頁均附 Wiki 對應標籤與 S01–S05 官方來源。
- 已在 Chromium + Playwright 測試切頁、互動及桌面／手機橫向溢出；詳見 `experiment-log-2026-11-20.md`。
- 尚待使用者 Windows Chrome／Edge 直開檔案驗收，及發布為可分享的網頁連結。
