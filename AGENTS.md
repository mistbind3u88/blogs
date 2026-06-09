# AGENTS.md

## Formatting Rules

- リポジトリ内のテキスト編集後は、必ず Prettier を実行すること。
- 基本コマンドは `npm run format` を使用すること。
- 変更ファイルだけを整形する場合は `npx prettier --write {path}` を使用してよい。
- 最終確認として `npm run lint:prettier` を実行し、整形崩れがないことを確認すること。
- push 前には、CI で実行される lint と同じ `npm run lint` を必ず通すこと。
- push 後には、CI の結果を watch して完了を確認すること。

## Default File Format

- ユーザーから明示的な指定がない限り、新規作成・更新するテキストファイルのフォーマットは統一すること。
- 文字コードは `UTF-8 (BOM なし)` を使用すること。
- Markdown は見出し・段落・空行の構造を保ち、文途中改行を避けること。

## Writing Article Agent Notes

- 執筆記事に関するエージェントの作業メモは、記事本文とは別ファイルに分離すること。
- メモファイル名は対象記事のファイル名に `.AGENTS.md` を付けた形式とすること。
- 例: `journey.2026.四国旅行計画帳.md` のメモは `journey.2026.四国旅行計画帳.AGENTS.md` とする。
- 記事本文ファイルには、公開先へ投稿する本文のみを置くこと。

## 基本方針

@docs/repository-philosophy.md

## コンテンツ構造

@docs/content-structure.md

## Markdown と文章ルール

@docs/markdown-writing-rules.md

## GitHub 運用

@docs/github-workflow.md
