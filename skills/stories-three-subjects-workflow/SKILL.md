---
name: stories-three-subjects-workflow
description: Workflow for creating GitHub Issues, first commits, pushing branches, and draft Pull Requests for 三題噺 stories in mistbind3u88/blogs. Use when you have a new stories/three_subjects/YYYY_MM_DD.md file and want to go from first commit to draft PR with minimal but consistent Issue/PR contents.
---

# stories-three-subjects-workflow

このスキルは `mistbind3u88/blogs` リポジトリの三題噺用ストーリー（`stories/three_subjects/*.md`）について、

- Issue を作る
- ファーストコミットを作って push する
- Draft PR を作る

ところまでを、`blogs-issue-pr-workflow` の方針に沿って揃えるための手順をまとめたものです。

重要:

- Issue 作成時は `.github/ISSUE_TEMPLATE.md` の見出し（`Subject as Why` / `Where` / `What`）をそのまま使う。
- PR 作成時は `.github/PULL_REQUEST_TEMPLATE.md` の見出し（`Subject as How` / `Details`）をそのまま使う。
- 本スキル内の文章例より、テンプレートの見出し・項目を優先する。

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
3. Issue 本文は `.github/ISSUE_TEMPLATE.md` をベースに作る。見出し名は変更しない:

```markdown
# Subject as Why

- 三題噺スイッチ改訂版から出力したお題で短編を書く。

# Where

- note（予定）

# What

## 本文執筆

- `stories/three_subjects/24_04_11.md` に本文を書く

## お題整理

- コトバンク参照とメモを更新する

## 仕上げ

- 公開前の最終見直しを行う
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

2. PR 本文は `.github/PULL_REQUEST_TEMPLATE.md` に合わせる。見出し名は変更しない:

```markdown
# Subject as How

- 三題噺 '24/04/11 の本文とメモを追加します。

# Details

## 本文

- `stories/three_subjects/24_04_11.md` に本文を追加

## お題とメモ

- お題情報と構成メモを更新

## 確認

- 通読して構成・日本語表現を確認
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
- [ ] Issue 本文が `Subject as Why` / `Where` / `What` を使っている。
- [ ] PR 本文が `Subject as How` / `Details` を使っている。
- [ ] 追加の設定変更やメンテ作業は、必要に応じて別 Issue / PR に分離している。
