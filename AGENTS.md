# AGENTS.md

## Formatting Rules

- リポジトリ内のテキスト編集後は、必ず Prettier を実行すること。
- 基本コマンドは `npm run format` を使用すること。
- 変更ファイルだけを整形する場合は `npx prettier --write {path}` を使用してよい。
- 最終確認として `npm run lint:prettier` を実行し、整形崩れがないことを確認すること。
- push 前には、CI で実行される lint と同じ `npm run lint` を必ず通すこと。
- push 後には、CI の結果を watch して完了を確認すること。

## 基本方針

@docs/repository-philosophy.md

## コンテンツ構造

@docs/content-structure.md

## Markdown と文章ルール

@docs/markdown-writing-rules.md

## GitHub 運用

@docs/github-workflow.md

## 活動サマリ

@docs/summaries-workflow.md
