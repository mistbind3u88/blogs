# AGENTS.md

## 必須チェック

- リポジトリ内のテキスト編集後は、必ず Prettier を実行すること。
- 基本コマンドは `npm run format` を使用すること。
- 変更ファイルだけを整形する場合は `npx prettier --write {path}` を使用してよい。
- 最終確認として `npm run lint:prettier` を実行し、整形崩れがないことを確認すること。
- push 前には、CI で実行される lint と同じ `npm run lint` を必ず通すこと。
- push 後には、CI の結果を watch して完了を確認すること。

## 新規・更新ファイルの既定形式

- ユーザーから明示的な指定がない限り、新規作成・更新するテキストファイルのフォーマットは統一すること。
- 文字コードは `UTF-8 (BOM なし)` を使用すること。
- Markdown は見出し・段落・空行の構造を保ち、文途中改行を避けること。

## 記事本文と作業メモの分離

- 執筆記事に関するエージェントの作業メモは、記事本文とは別ファイルに分離すること。
- メモファイル名は対象記事のファイル名に `.AGENTS.md` を付けた形式とすること。
- 例: `journey.2026.四国旅行計画帳.md` のメモは `journey.2026.四国旅行計画帳.AGENTS.md` とする。
- 記事本文ファイルには、公開先へ投稿する本文のみを置くこと。

## AGENTS.md の階層運用

- 下位 `AGENTS.md` は、上位 `AGENTS.md` のルールと参照先 docs が継承されることを前提にする。
- 上位で参照済みの docs を、下位 `AGENTS.md` で繰り返し参照しない。
- 下位 `AGENTS.md` は、その階層固有の追加ルールがある場合だけ置く。
- 上位ルールの適用を説明するだけのプレースホルダ `AGENTS.md` は作らない。

## リポジトリの価値判断

@docs/repository-philosophy.md

## 配置判断

@docs/content-structure.md

## Markdown と文章

@docs/markdown-writing-rules.md

## GitHub 運用

@docs/github-workflow.md
