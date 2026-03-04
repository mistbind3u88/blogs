---
name: stories-three-subjects-workflow
description: Workflow for creating GitHub Issues, first commits, pushing branches, and draft Pull Requests for 三題噺 stories in mistbind3u88/blogs. Use when you have a new stories/three_subjects/YYYY_MM_DD.md file and want to go from first commit to draft PR with minimal but consistent Issue/PR contents.
---

# stories-three-subjects-workflow

このスキルは `mistbind3u88/blogs` リポジトリの三題噺用ストーリー（`stories/three_subjects/*.md`）について、

- Issue を作る
- ファーストコミットを作って push する
- Draft PR を作る

ところまでを、`blogs-issue-pr-workflow` の方針に沿って「必要最低限の情報」で揃えるための手順をまとめたものです。

---

## 前提

- 対象リポジトリは `mistbind3u88/blogs`。
- `stories/three_subjects/YYYY_MM_DD.md` がテンプレートから複製され、ある程度本文・メモが書かれている。
- 現在のブランチはその三題噺用に切られている（初回コミットはまだ、またはこれから作り直す前提）。
- Issue / PR の一般的なルールは `blogs-issue-pr-workflow` に従う。

---

## Step 1: 三題噺 Issue を作成する

1. 対象ファイルのパスと日付を確認する
   - 例: `stories/three_subjects/24_04_11.md` → 日付は `'24/04/11`
2. Issue タイトルを作る（`blogs-issue-pr-workflow` 準拠）
   - 形式: `feat(stories): 三題噺 '<YY>/<MM>/<DD>`
   - 例: `feat(stories): 三題噺 '24/04/11`
3. Issue 本文は最小構成でよい。デフォルトでは次を提案し、不要ならユーザーと相談して削る:

```markdown
## 背景

- 三題噺スイッチ改訂版から出力したお題で短編を書く。

## やりたいこと

- `stories/three_subjects/24_04_11.md` に三題噺本文とメモをまとめる。
- 公開予定があれば、掲載先（note / カクヨム 等）を簡単に決めておく。

## 完了条件

- 三題噺本文が最後まで書けている。
- 必要に応じて README や他ファイルへのリンク・補足を追記している。
```

4. Issue を作成したら、その番号 `#<id>` を控える（以降のブランチ名・PR タイトルで利用）。

---

## Step 2: ブランチ名を整える

1. まだ Issue を作る前にブランチを切っている場合は、Issue 作成後にブランチ名を `blogs-issue-pr-workflow` のルールに合わせておく。
2. 推奨ブランチ名:
   - 基本形: `feature/#<id>-three-subjects-story`
   - 日付を入れたい場合の例: `feature/#<id>-three-subjects-24-04-11`
3. ブランチ名を変更する必要がある場合のコマンド例（ローカルのみ）:

```bash
git branch -m <old-branch-name> feature/#<id>-three-subjects-story
```

4. 以降の例では `feature/#<id>-three-subjects-story` を前提とする。

---

## Step 3: ファーストコミットを作って push する

1. 変更を確認する:

```bash
git status
```

2. 三題噺の本文ファイルをステージングする:

```bash
git add stories/three_subjects/24_04_11.md
```

- 付随するメモファイルなどがあれば同じコミットに含めてもよいが、設定ファイルや全体メンテは別コミットに分ける。

3. コミットメッセージは Issue タイトルと同じ型で揃える:

```bash
git commit -m "feat(stories): 三題噺 '24/04/11"
```

4. 必要に応じて `npm test` や `npm run lint` を実行してから push する。

5. 初回 push:

```bash
git push -u origin feature/#<id>-three-subjects-story
```

---

## Step 4: Draft PR を作成する

1. PR タイトルは `blogs-issue-pr-workflow` のルールに従い、Issue と紐付ける。

   - 形式: `feat(stories): #<id> subject`
   - 三題噺の場合の subject は、最初は日付ベースでよい:
     - 例: `feat(stories): #172 三題噺 '24/04/11`
   - お題 3 つが確定していれば、それを入れる:
     - 例: `feat(stories): #172 三題噺「山崩れ」「料理人」「アルバム」`

2. PR 本文は最小構成とし、テンプレートの「Subject as How」「Details」に対応するよう、次のような内容をベースにする:

```markdown
## 概要

- 三題噺 '24/04/11 の本文とメモを追加します。

## 変更内容

- `stories/three_subjects/24_04_11.md`
  - 三題噺本文
  - お題と構成メモ

## 確認方法

- 記事本文を通読し、構成・日本語表現に違和感がないかを確認してください。
```

3. PR は Draft 状態で作成し、本文が書き上がった段階で「Ready for review」に切り替える。

4. 公開先や公開予定日など、運用上必要な情報があれば PR 本文または Issue に追記する。

---

## チェックリスト

- [ ] 対象リポジトリが `mistbind3u88/blogs` である。
- [ ] 対象ファイルが `stories/three_subjects/YYYY_MM_DD.md` で、テンプレートから作成されている。
- [ ] Issue タイトルが `feat(stories): 三題噺 'YY/MM/DD` 形式になっている。
- [ ] ブランチ名が `feature/#<id>-three-subjects-...` の形式になっている。
- [ ] ファーストコミットには三題噺本文関連のファイルのみを含めている。
- [ ] PR タイトルが `feat(stories): #<id> ...` になっており、Draft で作成されている。
- [ ] 追加の設定変更やメンテ作業は、必要に応じて別 Issue / PR に分離している。
