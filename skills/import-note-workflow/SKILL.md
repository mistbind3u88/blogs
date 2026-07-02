---
name: import-note-workflow
description: Import a published note article into a local Markdown file in mistbind3u88/blogs while preserving headings, images, links, and readable paragraph structure. Use when Codex needs to create or update a repository article file from an existing note post, including caption handling and note-specific cleanup such as removing publication-only hashtags.
---

# import-note-workflow

note に公開済みの記事を、このリポジトリの本文ファイルとして取り込む。

この skill は note 取り込み固有の判断に絞る。ローカル Markdown を作るまでを対象とし、整形、lint、commit、push、GitHub 文面更新のようなリポジトリ共通の開発手順はこの手順に含めない。

## 前提

- 対象リポジトリは `mistbind3u88/blogs`。
- 取り込み元の note 記事 URL または記事内容を参照できる状態にある。
- 置き先ディレクトリが未確定なら、同題材の既存記事を読んで配置先と粒度を合わせる。

## 入力として確認すること

- note 記事 URL
- 置き先の題材ディレクトリまたは候補
- 新規作成か既存ファイル更新か
- キャプションを本文側にも残すべき記事かどうか

置き先が曖昧な場合は、先に同題材の既存 Markdown を 2 つ以上読み、次を揃える。

- ディレクトリ
- ファイル名
- note URL の置き方
- 見出し深さ
- 画像と本文の並べ方

## 手順

### 1. 取り込み先を決める

1. 題材ベースで配置先を決める。媒体ベースでは決めない。
2. 同系統の既存記事があれば、その粒度に合わせて新規ファイル名または更新対象を決める。
3. 新規ファイルを作る場合も、タイトル、冒頭導入、見出し構成は近傍記事の流儀を優先する。

### 2. note 記事の構成を写す

1. 記事タイトルを `#` 見出しにする。
2. 段落は原則 1 段落 1 行で書き、文途中改行を持ち込まない。
3. 見出し階層、本文、箇条書き、引用、外部リンクを Markdown として自然に再構成する。
4. note 記事 URL は、同系統の既存記事が保持している場合だけ、その配置に合わせて本文中へ残す。

### 3. 画像とキャプションを取り込む

1. 画像がある場合は Markdown 画像記法で残す。
2. 画像の代替テキストには、画像キャプションまたは画像の意味が分かる短い文を使う。
3. 本文中でキャプションが説明文の役割を担っている場合は、画像の直後に本文段落としても同じ内容を残す。
4. キャプションが単なる補足で、本文として重ねる必要がない場合は、画像側だけに残してよい。

判断に迷う場合は、「画像を開かなくても流れが追えるか」を基準にする。

### 4. note 固有要素を掃除する

1. note 公開時だけに意味を持つハッシュタグは本文へ取り込まない。
2. 自動タグ付けのために本文中へ置かれていた `#...` は削除済みであることを確認する。
3. note 独自 UI に依存する要素は、そのまま転記せず Markdown で読める形に言い換える。

### 5. 必要な作業メモを分離する

1. 取り込み判断、未整理メモ、参照元確認メモが必要なら `<article>.AGENTS.md` に分離する。

### 6. 仕上げ確認をする

次を上から順に確認する。

- 見出し構造が崩れていない
- 段落が 1 段落 1 行になっている
- 画像 URL とリンク URL が壊れていない
- キャプションを本文側にも残すべき箇所が落ちていない
- note のハッシュタグを本文へ持ち込んでいない
