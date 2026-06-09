# `docs/` 配下のドキュメント方針

このディレクトリには、設定ファイルを見るだけでは意図や判断基準が伝わらない、リポジトリ固有の運用知を書く。

## 基本方針

- 設定ファイルやテンプレート自体が一次情報になるものは、重複して書かない。
- ここに書くのは「なぜそうしているか」「どう判断するか」「どこまでをこのリポジトリの慣例とみなすか」。
- 個別トピックに強く依存する内容は、今は切り出さない。
  - 例: 三題噺固有の進め方、創作レビュー固有の構成
- README の説明をそのまま再掲するのではなく、エージェントや執筆者が判断に使う形に整理する。

## 現在の対象

- `repository-philosophy.md`
  - リポジトリ全体の目的、残すもの、エージェントが守る姿勢をまとめる。
- `content-structure.md`
  - トップレベルディレクトリの意味と、配置判断の基準をまとめる。
- `markdown-writing-rules.md`
  - Markdown の書き方、媒体差、本文とメモの切り分け方をまとめる。
- `github-workflow.md`
  - Issue / PR / Milestone / ブランチ / コミットの運用をまとめる。
- `summaries-workflow.md`
  - 活動サマリの対象、集計前提、本文方針、時点表記をまとめる。

## このディレクトリで扱わないもの

- `.editorconfig`、`.gitattributes`、`.prettierrc.yaml` だけで十分に表現できる整形仕様
- `.markdownlint.jsonc`、`.textlintrc.json`、`.vscode/settings.json` の設定値一覧
- `.github/workflows/*.yml` の実行内容そのもの
- 作品ジャンル固有の書き方や、特定ディレクトリ専用の詳細ワークフロー
