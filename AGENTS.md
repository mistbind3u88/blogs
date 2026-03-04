# AGENTS.md

## Formatting Rules

- リポジトリ内のテキスト編集後は、必ず Prettier を実行すること。
- 基本コマンドは `npm run format` を使用すること。
- 変更ファイルだけを整形する場合は `npx prettier --write <path>` を使用してよい。
- 最終確認として `npm run lint:prettier` を実行し、整形崩れがないことを確認すること。

## Default File Format

- ユーザーから明示的な指定がない限り、新規作成・更新するテキストファイルのフォーマットは統一すること。
- 文字コードは `UTF-8 (BOM なし)` を使用すること。
- Markdown は見出し・段落・空行の構造を保ち、文途中改行を避けること。
