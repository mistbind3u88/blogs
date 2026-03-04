---
name: stories-three-subjects-finish-workflow
description: Workflow for updating Issues and Pull Requests for completed 三題噺 stories in mistbind3u88/blogs, based on patterns from past merged PRs. Use after the story in stories/three_subjects/YYYY_MM_DD.md is complete and you want to align Issue/PR with the final work.
---

# stories-three-subjects-finish-workflow

このスキルは、`mistbind3u88/blogs` リポジトリの三題噺ストーリー（`stories/three_subjects/*.md`）について、

- 作品が書き上がった後に Issue と PR の内容を「完成した作品」に合わせて更新する

ためのワークフローをまとめたものです。
初期の Issue 作成〜ファーストコミット〜Draft PR 作成までは `stories-three-subjects-workflow` と `blogs-issue-pr-workflow` のルールに従い、その続きとして使います。

重要:

- Issue 更新時は `.github/ISSUE_TEMPLATE.md` の見出し（`Subject as Why` / `Where` / `What`）を維持する。
- PR 更新時は `.github/PULL_REQUEST_TEMPLATE.md` の見出し（`Subject as How` / `Details`）を維持する。
- 独自見出し（`概要` / `変更内容` / `確認方法` など）へ置き換えない。

---

## 前提

- 対象リポジトリは `mistbind3u88/blogs`。
- `stories/three_subjects/YYYY_MM_DD.md` の本文とメモが「一旦完成」と言える状態になっている。
- 対応する Issue と Draft PR が既に存在している。
  - Issue タイトル例: `feat(stories): 三題噺 '24/04/11`
  - PR タイトル例: `feat(stories): #172 三題噺 '24/04/11`
- Issue / PR の基本ルールは `blogs-issue-pr-workflow` に従う。

---

## Step 1: 作品情報を整理する

1. 対象ファイルから次の情報を拾う。
   - 作品タイトル（`# 見出し` 部分に載っているタイトル）
   - お題の 3 語（本文中の「お題」やリンクから分かる語句）
   - 作品のテーマ・狙い（あとがきやメモに書かれていれば要約する）
2. 作品を外部に公開済みであれば、その URL と掲載先（note / カクヨム / なろう / はてなブログ 等）も控える。

これらの情報を元に、Issue / PR の subject や本文を「完成版」に揃えていく。

---

## Step 2: Issue を完成した作品に合わせて更新する

1. **Issue タイトルを見直す**
   - 初期状態: `feat(stories): 三題噺 '24/04/11` のように日付ベースになっていることが多い。
   - 完成後も日付ベースのままでよければそのままでもよいが、必要に応じて作品タイトルを短く追加してもよい。
     - 例: `feat(stories): 三題噺 '24/04/11「雨女の酒肴」`
2. **Issue 本文を更新する**
   - `# Subject as Why`
     - 三題と狙いを 1〜3 行で更新する。
   - `# Where`
     - 公開先（note / カクヨム / なろう / はてなブログ）とURLを更新する。
   - `# What`
     - 完了済みの項目が分かるように箇条書きを更新する。
     - 例:

```markdown
# What

- 本文執筆が完了している ✅
- 掲載先 note に公開済み ✅
  - https://example.com/your-note-url
```

3. **Issue の状態を確認する**
   - PR 側でマージされる前であれば、Issue は Open のままにしておく。
   - PR マージ後も何か残タスクがある場合は、Issue でそれを明示しておく。

---

## Step 3: PR タイトルを作品に合わせて整える

1. `blogs-issue-pr-workflow` の PR タイトルルールに従い、三題噺の 3 語を含める:
   - 形式: `feat(stories): #<id> 三題噺「お題1」「お題2」「お題3」`
   - 例: `feat(stories): #172 三題噺「山崩れ」「料理人」「アルバム」`
2. 作品タイトルも載せたい場合は、区切り記号（`｜` など）を使って短く追加してもよい。
   - 例: `feat(stories): #172 三題噺「山崩れ」「料理人」「アルバム」｜雨女の酒肴`

PR タイトルだけで「どの Issue を解決している」「どんな三題の作品か」が分かる状態を目指す。

---

## Step 4: PR 本文を完成形に更新する

1. `# Subject as How` を更新する
   - 作品完成に向けて何をどう実施したかを 1〜3 行で要約する。
   - 例:

```markdown
# Subject as How

- 三題「山崩れ」「料理人」「アルバム」を使った短編三題噺です。
- 山村の料理人を軸に、過去の記憶と現在の選択が交差する話になっています。
```

2. `# Details` を具体化する
   - 三題噺ファイルと、その周辺のメモや補足に分けて書く。
   - 例:

```markdown
# Details

## 本文

- `stories/three_subjects/24_04_11.md` を完成版に更新

## お題と構成

- 使用したお題と構成メモを追記

## 公開情報

- 公開先URLを追記
```

3. 外部公開している場合は、`Details` 内に URL を 1 箇所以上載せる。

---

## Step 5: 状態を更新してクローズに備える

1. PR が Draft のままであれば、「Ready for review」に変更するタイミングを相談し、必要であればこのスキルの手順に従ってから切り替える。
2. GitHub 上で Issue と PR の紐付けがきちんと行われているか確認する。
   - タイトルの `#<id>` だけでなく、必要に応じて PR 本文に `Closes #<id>` を追加してもよい。
3. マージ後に Issue が自動クローズされているか確認し、足りない情報があれば Issue または PR に最終的なメモ（公開 URL など）を残す。

---

## チェックリスト

- [ ] 対象ファイル `stories/three_subjects/YYYY_MM_DD.md` の本文とメモが一通り完成している。
- [ ] 作品タイトルと三題（お題 3 語）が整理できている。
- [ ] Issue タイトルと本文が、完成した作品の状態に合うように更新されている。
- [ ] PR タイトルに `#<id>` と三題（必要なら作品タイトル）を含めている。
- [ ] Issue 本文の `Subject as Why` / `Where` / `What` が最終状態に合っている。
- [ ] PR 本文の `Subject as How` / `Details` が最終状態に合っている。
- [ ] 公開済みであれば、少なくともどこかに公開 URL を記載している。
- [ ] PR の状態（Draft / Ready for review）と Issue の状態（Open / Closed）が意図どおりになっている。
