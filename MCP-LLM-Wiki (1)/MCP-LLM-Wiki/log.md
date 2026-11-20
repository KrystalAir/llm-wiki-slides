# LLM Wiki 維護日誌（append-only）

## [2026-11-20] discuss | 主題及設計取捨

- 使用者指定「什麼是 MCP」作為教學專題，要求參考 Karpathy LLM Wiki；先前已討論作業的至少五篇 ingest、Wiki→HTML、Loop/Graph、實驗紀錄需求。
- 設計選擇：以 Karpathy 的 raw/wiki/schema + index/log 作為知識庫骨架；選用 MCP 官方五個主題頁；統一 2026-07-28 版本。

## [2026-11-20] ingest | S01–S05 official MCP documents

- 五個官方 URL 在建置時已可讀取，建立五份 `raw/` 來源紀錄與中文重點筆記（**不是原文全文備份**）。
- 整合概念頁：動機、架構、基本能力、通訊、工具呼叫、比較、安全、詞彙表、FAQ，並建跨頁連結及來源對照表。
- 來源原文的內容分析與中文編寫已完成；未進行 API 呼叫或 MCP Server 實作。

## [2026-11-20] design | 後續 HTML 簡報工作流程

- 新增流程圖、建議頁面大綱、品質檢查、測試紀錄範本。
- 狀態：**設計完成；尚未執行簡報生成及簡報驗證**。

## [2026-11-20] lint | 檔案與來源連結靜態檢查

- 見 `workflow/quality-checklist.md` 的本地靜態檢查執行欄。初次建立時不宣稱網頁內容與幻燈片已人工逐項驗證；Wiki 事實仍需讀者與官方文件對照。

## 2026-11-20 · Wiki → HTML 教學簡報 v1

- 依 12 頁大綱與 S01–S05 來源對照建立 `presentation/index.html`。
- 加入第 8 頁七步互動、第 12 頁測驗，並標明教學模擬不等於真實 MCP Server 呼叫。
- 執行 Playwright DOM、互動與佈局測試：桌面 1440×900、手機 390×844，未發現 JS 例外或橫向溢出。
- 真實限制：沙盒 Chromium 禁止 file:// 和 localhost，改用 `set_content()` 驗證。首次截圖遇淡入動畫尚未結束，修正擷取時機後重跑。
- 新增 `workflow/experiment-log-2026-11-20.md`、`workflow/browser-test-result.json`、截圖證據及 Windows 手動驗收清單。
- 公開網頁連結與使用者 Windows 本機開啟驗收尚待完成。

- 針對單檔發布檢查，發現 `../wiki/*.md` 相對連結可能失效；改為不可點擊的 Wiki 頁名標籤，保留官方來源 URL 並重跑測試，通過。
