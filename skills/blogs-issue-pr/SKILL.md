---
name: blogs-issue-pr-workflow
description: Guidelines for creating GitHub Issues, Pull Requests, and related branches in mistbind3u88/blogs. Use when proposing titles/bodies for Issues or PRs, or when naming branches for this repository.
---

# blogs-issue-pr-workflow

このスキルは、`mistbind3u88/blogs` リポジトリにおける Issue / PR / ブランチ作成の方針をまとめたものです。
会話の中で Issue / PR を作成・提案するとき、このスタイルに合わせて生成する。

## 全体方針

- Conventional Commits 風のフォーマットをベースにする。
- タイトルは「英語の型」＋「日本語で具体的に」のハイブリッド。
- Issue と PR は 1:1 対応を基本とし、PR タイトルに `#issue番号` を含めて紐付けを明示する。
- メンテ作業や設定調整も通常の Issue / PR で扱う（特別扱いしない）。

---

## Issue の作り方

### タイトル

- 形式: `type(scope): subject`
- `type` の例:
  - `feat` : 新しい記事・大きめの追加
  - `fix` : バグ修正・明確な不具合の修正
  - `chore` : 設定・メンテナンス・CI など
  - `refactor` : 振り返り記事や構成整理など
  - `docs` : ドキュメントのみの変更
- `scope` の例:
  - `stories`, `reading`, `entertainments`, `games`, `profile`, `essays`
  - リポジトリ全体のメンテや設定は `repo` を使う: `chore(repo): ...`
- `subject` は日本語で具体的に書く。
  - 三題噺系: `feat(stories): 三題噺 '24/04/11`
  - 読書系: `feat(reading): 「根」「命日」「水門」｜三題噺 2024.03`
  - メンテ系: `chore(repo): lint設定とCIおよびCODEOWNERSの整備`

### 本文

- 必要な場合のみ、簡潔な Markdown で補足を書く。
- 推奨構成（すべて必須ではない）:
  - `## 背景` : なぜこの Issue が必要か。
  - `## やりたいこと` : 箇条書きでやること。
  - `## 完了条件` : 何ができれば Close とみなすか。
- このリポジトリでは、短めの本文や本文なしの Issue も多い。
  → 詳細な説明が不要な場合はタイトルだけでも良いが、機械生成するときは上記 3 セクションを用意してから、不要なら省く。

---

## PR の作り方

### タイトル

- 形式: `type(scope): #<issue番号> subject`
- 例:
  - `feat(stories): #172 三題噺「山崩れ」「料理人」「アルバム」`
  - `refactor(stories): #150 「蛇」「夢」「窓」をなろう向けに改稿する`
  - メンテ系: `chore(repo): #XXX lint設定とCIおよびCODEOWNERSの整備`
- Issue と同じ `type(scope)` を使い、どの Issue を解決するかを `#番号` で明示する。

### 本文

- 必要以上に長くしないが、何を変えたかは箇条書きで分かるようにする。
- 推奨構成:
  - `## 概要` : 一文〜数行で変更の目的を説明。
  - `## 変更内容` : ファイルや観点ごとに箇条書き。
  - `## 確認方法` : レビュー前に実行してほしいコマンドや確認手順。
- 例（メンテ PR のイメージ）:

```markdown
## 概要

- Markdown 関連の lint / format 設定を整理し、CI からも実行できるようにします。

## 変更内容

- `package.json`
  - devDependencies に prettier / markdownlint-cli / textlint などを追加
  - `lint:prettier`, `lint:markdown`, `lint:text`, `lint`, `format`, `test` スクリプトを追加
- `.markdownlint.jsonc`
  - MD024/MD026/MD028 を無効化
- `.textlintrc.json`
  - `preset-japanese` を有効化
- `.github/workflows/lint.yml`
  - push / PR 時に `npm run lint` を実行
- `.github/CODEOWNERS`
  - `* @mistbind3u88` を追加

## 確認方法

- `npm install`
- `npm test` または `npm run lint`
- この PR の GitHub Actions (Lint) が green であること
```

---

## ブランチ命名

- README のルールを踏襲する:
  - 機能追加・記事執筆: `feature/#{id}-{description}`
  - 修正: `fix/#{id}-{description}`
- `{id}` は対応する Issue 番号。
- `{description}` は英語のスラッグ（kebab-case）で簡潔に。
  - 例: `feature/#172-three-subjects-story`
  - メンテ系: `chore/repo-maintenance-lint-ci` のようなスラッグのみも許容。

---

## このスキルを使うときのチェックリスト

- [ ] このリポジトリか？ → `mistbind3u88/blogs` であること。
- [ ] Issue タイトルは `type(scope): subject` 形式か？
- [ ] PR タイトルは `type(scope): #issue番号 subject` 形式か？
- [ ] ブランチ名は Issue 番号と簡潔なスラッグを含んでいるか？
- [ ] 本文は「概要 / 変更内容 / 確認方法」を過不足なく満たしているか？
- [ ] README.md の内容は、この Issue/PR の目的に関係しない限り、勝手に書き換えない。
- [ ] push 前に `npm test` など関連する lint / テストをローカルで通しておく。
- [ ] fixup コミットやフォーマットのみのコミットがあれば、`--fixup` / `--autosquash` や `--amend` で潰してから push する。
