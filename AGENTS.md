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

## Summary Workflow

- 活動サマリの集計や再生成を行う場合は skills/summaries-periodic-workflow/SKILL.md を使うこと。
- 年次サマリの出力先は summaries/YYYY.md、半期サマリの出力先は summaries/half-year/YYYY-H1.md / YYYY-H2.md とすること。
- 本文は一般の読み手が分かる語彙で書き、Git や実装寄りの用語をそのまま見出しや説明に出さないこと。
