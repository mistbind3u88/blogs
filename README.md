# about this repository

このリポジトリは個人でブログ執筆をする上での草案などを履歴管理する事を目的とする。
README にはディレクトリ構成の意図や執筆環境として利用しているツールなどを言語化し再現可能にするための整理をしていくために利用していく予定。

基本的には私用でメイン機として利用している Windows 環境を前提として記載する。

## about Directories

本リポジトリのディレクトリ構成について記載する。

トップレベルには設定ファイルを配置し、下位ディレクトリをトピック毎に切る。

### 映画・漫画感想系

アバウトにエンタメ感想系。

取り敢えずは完結済みの漫画シリーズや映画の感想をメインに書いていく。物語構造や自分がおもしろいと思った事の整理としてまとめていく。

### ゲーム体験系

日頃プレイしたゲームのプレイに関する考察など。

映画・漫画の感想系との区別として、純粋に楽しんだ事のまとめという要素の他にゲームデザインに対する考察や攻略のアイデアという能動的な要素を含む。

## about Editors

### Visual Studio Code

基本的に記事は markdown 形式に落とすので、執筆時にエディターとして利用する。

#### plugins

執筆時に利用してるプラグインについて記載する。

- EditorConfig for Visual Studio Code

  - VS Code の設定管理として

- markdownlint

  - markdown 向けの linter。

- テキスト校正くん

  - 文章自体のの簡易的な校正のために利用する。
  - markdown の lint と競合するため、「設定 > Japanese-proofreading › Textlint: 全角文字と半角文字の間」を off にする。

- Prettier Formatter for Visual Studio Code

  - markdown の formatter として prettier を利用する。

- YAML Language Support by Red Hat
  - prettier の設定ファイルは yaml で書く。

### xmind

mindmap エディター。ネタ出し、アイデアノートとしてアドホックに文を羅列する段階で利用する。

## about node modules

執筆時に便利な道具として node module を利用する場合がある。node.js 自体のバージョン管理は nvm で行う。

### commitzen

~~git のコミットログを整理するための npm モジュール。~~
windows の VS Code ターミナル (GitBash) だと相性が悪くコミットを上手く作れないっぽい。

## about Terminal

### GitBash

Windows で git を扱う為に Git for Windows をインストール。ついでに GitBash が入るので基本的にはこれを使う。

#### 留意点

VS Code 上でターミナルを扱う時に初期設定では文字化けする。VS Code 側の設定で標準出力を utf-8 に変更する必要がある。

私の場合は windows 環境で対応するため intl.cpl から変更してしまった。

参考: [VSCode – ターミナルで UTF8 をデフォルトにする方法 (Windows)](https://pystyle.info/vscode-change-default-encoding-of-terminal-to-utf8/#outline__3)

## how to Write

書いてく時のルールについて記載する。

### markdown

#### 見出し

- H5 以上は使わない。
  - 文字が小さくなりすぎそう。
