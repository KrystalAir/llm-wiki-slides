# 什麼是 MCP？｜LLM Wiki

> 一套以 Karpathy 的 **LLM Wiki** 模式編排的、可持續維護的 MCP 學習知識庫（繁體中文）。

**主題**：Model Context Protocol (MCP) 的目的、架構、功能、協定、應用與安全。  
**內容範圍**：五份 MCP 官方資料，統一採用 **2026-07-28** 規範／文件版本。  
**建立日期**：2026-11-20  
**狀態**：五個來源已閱讀、整理為來源筆記並併入 Wiki；不代表已進行 MCP Server 實機連線；**HTML 簡報已產生，但使用者 Windows 本機驗收仍待完成**。

## 如何使用（最快路徑）

1. 從 [知識索引](index.md) 開始選主題，閱讀 `wiki/` 下的概念頁。
2. 每個重要概念附有 `[S01]`～`[S05]` 來源連結，可以追溯到 `raw/` 的來源筆記與官方全文網址。
3. 將整個 `MCP-LLM-Wiki/` 資料夾用 **Obsidian → Open folder as vault** 開啟，可使用 `[[wiki links]]` 及 Graph view。
4. 在 **Codex / CLI** 中以此資料夾為工作目錄，AI 先讀 `AGENTS.md`、`index.md`，再選擇性讀取 `wiki/`。
5. 可用 `python scripts/search_wiki.py 'tools/list'` 搜尋文字，或 `python scripts/wiki_check.py` 檢查結構。上述腳本只使用 Python 標準函式庫。

## Karpathy 模式與本作業如何對應

| 概念 | 本專案 | 用途 |
|---|---|---|
| Raw sources（不修改的證據） | `raw/` | 五篇官方文件的永久 URL、閱讀筆記與來源資訊；**不是官方逐字全文備份** |
| Wiki（LLM 維護的合成知識） | `wiki/` | 主題化、交叉連結、可被查詢的知識頁 |
| Schema（AI 操作規約） | `AGENTS.md` | 定義 ingest / query / lint、引用、版本、更新規則 |
| Index | `index.md` | 從問題快速定位知識頁 |
| Append-only log | `log.md` | 可追溯的建立及測試活動紀錄 |

Karpathy 原始方法：<https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f>。

## 來源完整性說明

本資料夾**收錄五篇來源的連結、元資料與逐篇整理筆記**，並非逐字保存五篇文章全文。因為原始資料是官方網站上的持續更新文件，完整細節需要點擊來源連結回查。Wiki 內容是作者化的中文理解與統整，不能替代 MCP 規範原文。每一篇都在 `raw/` 建立獨立來源頁，已完成整理（ingest into wiki）。

這份 Markdown Wiki 已完成建置，並已產生 [`presentation/index.html`](presentation/index.html)。尚未連接外部向量資料庫或實際部署 MCP Server；已進行瀏覽器互動測試，使用者 Windows 本機驗收與公開網址仍待完成，詳見 [實驗紀錄](workflow/experiment-log-2026-11-20.md)。

## 資料夾內容

```text
MCP-LLM-Wiki/
├── README.md
├── AGENTS.md
├── index.md
├── log.md
├── sources.json
├── raw/               # S01～S05 官方文章的來源紀錄與重點筆記
├── wiki/              # 概念頁、比較、案例、詞彙、主題與來源對照
├── workflow/          # wiki→HTML 的 graph、檢核、測試範本
├── presentation/      # 12 頁互動式 HTML 簡報
└── scripts/           # Wiki 搜尋、靜態與瀏覽器測試
```

## 教學成果定位

已完成「什麼是 MCP？」12 頁教學 HTML 簡報及第一次瀏覽器互動檢查。已保留來源註記、測試證據與真實測試環境問題。**請勿把 `workflow/experiment-template.md` 的示範問題當成已經執行的實驗。**
