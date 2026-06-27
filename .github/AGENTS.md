# .github AGENTS.md

## Purpose

- `.github/` 配下のテンプレートや関連ファイルを扱うときの注意点をまとめる。
- GitHub運用全体の説明は `../docs/github-workflow.md` を参照し、このファイルでは `.github/` 配下の資源の扱い方に絞る。

## Common Rules

- `.github/` 配下のファイルは、GitHub上のIssue、Pull Request、workflow設定などに直接対応する資源として扱う。
- `.github/ISSUE_TEMPLATE.md` と `.github/PULL_REQUEST_TEMPLATE.md` を参照するときは、見出し構成とプレースホルダーを崩さない。

## Issue Template Notes

- `Subject as Why` には、そのIssueが必要な理由や背景を書く。
- `Where` には参照先をMarkdownリンクで並べる。
- `What` には実施項目や完了条件を書く。

## PR Template Notes

- `Subject as How` には「どう取り込んだか」「どう変更したか」を1段落で書く。
- `Details` は変更のまとまりごとに `## ...` を埋める。
- 関連Issueを閉じるときは、本文の末尾に `Closes #<number>` を置く。
