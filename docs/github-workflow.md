# GitHub 運用

このリポジトリでは、記事執筆や運用改善を GitHub の Issue / PR 単位で扱う。目的は、書いたものだけでなく、何をしようとしていたか、どう区切って進めたかを追えるようにすることにある。

## 基本ルール

- 変更には原則として Issue を立てる。
- Issue と PR は 1:1 対応を基本とする。
- ひとつの更新単位を 1 Issue とみなし、Close 前に追記修正が必要なら同じ PR で続けてもよい。
- Issue は立てっぱなしにせず、期日を持つ Milestone に紐づけて管理する。

## タイトルと本文

Issue タイトルは `type(scope): subject` を基本とする。PR タイトルは `type(scope): #<issue番号> subject` を基本とし、対応する Issue 番号を明示する。

`subject` は日本語で具体的に書く。`type` や `scope` は整理のための型であり、本文の中心は何を扱う更新かがすぐ分かることに置く。

Issue 本文は、必要なら `背景`、`やりたいこと`、`完了条件` を短く置く。PR 本文は、必要以上に長くせず `概要`、`変更内容`、`確認方法` が読み取れる形を優先する。

## テンプレートの読み方

`.github/ISSUE_TEMPLATE.md` と `.github/PULL_REQUEST_TEMPLATE.md` は、そのまま使う前提でよい。ただし意図としては、Issue 側が `Why`、PR 側が `How` を受け持つ。

- Issue の `Subject` は、更新の目的や題材を表す。
- Issue の `Where` は、公開先や想定媒体を書く場所とみなす。
- PR の `Subject as How` は、Issue の目的をどう実現したかを短く説明する場所とみなす。

## ブランチ命名

- 記事執筆、改稿、更新は `feature/#{id}-{description}`
- 訂正は `fix/#{id}-{description}`

ここでいう「訂正」は、単なる追記や改稿ではなく、誤りを正すこと自体が主目的の変更を指す。

## コミットメッセージ

コミットメッセージは概ね Angular 系の Conventional Commits を参考にする。厳密な自動運用よりも、後で見たときに更新の種類と主題が分かることを優先する。

## 補足

PR 本文には `Closes #<issue番号>` または `Resolves #<issue番号>` を明示し、マージ時に Issue が閉じる状態を保つ。
