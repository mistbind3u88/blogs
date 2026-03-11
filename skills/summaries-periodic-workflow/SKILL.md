---
name: summaries-periodic-workflow
description: Create monthly, half-year, or yearly summaries in mistbind3u88/blogs by collecting GitHub Issue/PR data as JSON for a single period, then writing a substantial Japanese narrative summary from Issue bodies, PR bodies, and PR file patches.
---

# summaries-periodic-workflow

Issue / PR から活動サマリを作る。
この skill の原則は次の 2 点。

- 集計はスクリプトで JSON 化する
- 文章はエージェントが書く

## 対応期間

- `monthly`: `YYYY-MM`
- `half-year`: `YYYY-H1` / `YYYY-H2`
- `yearly`: `YYYY`

## 手順

### 1. 集計 JSON を作る

実行コマンド:

- 単一期間: `python skills/summaries-periodic-workflow/scripts/generate_summary.py --period-type half-year --label 2026-H1 --out tmp/2026-H1.json`
- 差分情報を省く場合のみ: `python skills/summaries-periodic-workflow/scripts/generate_summary.py --period-type half-year --label 2026-H1 --skip-pr-diff --out tmp/2026-H1-no-diff.json`

`generate_summary.py` が返す主な項目:

- 完了件数（Issue: `closedAt`, PR: `mergedAt`）
- 前期差分
- カテゴリ別件数
- 期間内作成で未完了の Open Issue / PR
- サンプル Issue / PR（`title`, `body`, `url`）
- PR の変更情報（デフォルト）
  - `periods[].pr_diff.fetch_policy`
  - `periods[].pr_diff.prs_total`
  - `periods[].pr_diff.prs_incomplete`
  - `periods[].pr_diff.entries[]`
  - `files[]`（`filename`, `status`, `additions`, `deletions`, `changes`, `patch`）

### 2. JSON を根拠に本文を書く

`なにやってたの？` は、最低でも次を読んでから書く。

- `samples.issues[].title`
- `samples.issues[].body`
- `samples.prs[].title`
- `samples.prs[].body`
- `pr_diff.entries[].files[].patch`

ここを薄くしないための必須ルール:

- 2 段落以上で書く
- 合計 4 文以上で書く
- 1 段落目では「何の題材に取り組んでいたか」を書く
- 2 段落目では「その題材で何をしていたか」を書く
- 可能なら 3 段落目で「書くだけでなく、運用・改稿・振り返り・整備までやっていたか」を書く
- 少なくとも 2 つ以上の具体例を Issue / PR の内容から入れる
- 少なくとも 1 つは変更内容から見える具体を入れる
- むずかしい言い回しを避ける
- 一般の読み手目線で分かる語彙を使うこと
- ただし、情報量は削りすぎない

言い換えルール:

- `patch` とは書かず、「変更内容」「修正内容」「差分」などに言い換える
- `Issue` / `PR` をそのまま並べるだけでなく、「検討メモ」「公開した記事」「更新した内容」など読者向けの言い方へ寄せる
- `essay` は「エッセイ」と書く
- `reading` `stories` などのカテゴリ名は、そのまま出す必要がなければ「読書メモ」「創作」など自然な日本語に直す
- ファイルパスは原則そのまま出さず、何を書いたファイルかを説明して書く

`なにやってたの？` に入れる観点:

- 主な題材
  - 例: ゲーム記録、三題噺、読書メモ、旅行記、キャリア整理
- 具体的にやっていたこと
  - 例: 結果の記録、振り返り、改稿、テンプレート整理、運用ルール追加
- 変更内容から分かる作業の実体
  - 例: 特定ディレクトリに変更集中、レビュー群を複数ファイルで更新、README / AGENTS / SKILL を同時に更新
- 半期の手触り
  - 例: 同じテーマを継続していた、多題材を並行していた、書くより整備寄りだった

書いてはいけないもの:

- 件数だけを言い換えた文章
- 「いろいろやっていた」「整えていた」だけで終わる文
- 具体的な題材名や作業内容が出てこない要約
- Git の内部用語を読者向け説明なしでそのまま出す文

### 3. 他の見出しを書く

見出しは次の順で出す。

1. `## なにやってたの？`
2. `## どれくらいやった？`
3. `## 前と比べると？`
4. `## 何ジャンルが多かった？`
5. `## 積み残しある？`
6. `## 代表トピックはこれ`
7. `## いつ時点のサマリ？`

補助ルール:

- `どれくらいやった？` では件数に加えて `additions / deletions` も書く
- `何ジャンルが多かった？` ではカテゴリ件数だけでなく、どの領域の変更が多かったかも自然な日本語で書く
- `積み残しある？` では Open Issue / PR と `incomplete` を書く
- 当年サマリでは Open Milestone も出す

### 4. Markdown を保存する

出力先:

- `monthly`: `summaries/monthly/YYYY/YYYY-MM.md`
- `half-year`: `summaries/half-year/YYYY-H1.md` / `YYYY-H2.md`
- `yearly`: `summaries/YYYY.md`

### 5. 整形確認

- `npm run format`
- `npm run lint:prettier`

## 必須ルール

- 本文・見出しは日本語
- 集計軸は毎回明記する
  - Issue = `closedAt`
  - PR = `mergedAt`
- `created` ベースと混在させない
- 日付は具体的に書く
  - 例: `2026-03-12 JST 時点`
- デフォルトで変更情報を使う
- `incomplete` 判定は本文に必ず反映する

## scripts

- `scripts/generate_summary.py`
  - GitHub から単一期間の集計 JSON を生成する
  - デフォルトで PR ごとの files 情報（patch / additions / deletions）を含める
  - `--skip-pr-diff` で差分取得を省ける
  - Markdown は生成しない
