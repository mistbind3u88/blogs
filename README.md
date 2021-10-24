# about this repository

このリポジトリは個人でブログ執筆をする上での草案などを履歴管理する事を目的とする。READMEにはディレクトリ構成の意図や執筆環境として利用しているツールなどを言語化し再現可能にするための整理をしていくために利用していく予定。

基本的には私用でメイン機として利用しているWindows環境を前提として記載する。

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

基本的に記事はmarkdown形式に落とすので、執筆時にエディターとして利用する。

#### plugins

執筆時に利用してるプラグインについて記載する。

- EditorConfig for Visual Studio Code

  - VS Codeの設定管理として

- markdownlint

  - markdown向けのlinter。

- テキスト校正くん

  - 文章自体のの簡易的な校正のために利用する。
  - ~~markdownのlintと競合するため、「設定 > Japanese-proofreading › Textlint: 全角文字と半角文字の間」をoffにする。~~
    - 競合部分をprettierで扱わない事にしたのでonに。

- Prettier Formatter for Visual Studio Code

  - markdownのformatterとしてprettierを利用する。
  - [Prettier に関して markdown のフォーマッタとしての問題](https://qiita.com/tats-u/items/bcbfe2bb4e71bf0a2b87)があったため拡張機能デフォルトのprettierではなくnodeモジュールをインストールしたものを利用する。
    - noteに転記したところ全体として滅茶苦茶読み難かった。

- YAML Language Support by Red Hat
  - prettierの設定ファイルはyamlで書く。

### xmind

mindmapエディター。ネタ出し、アイデアノートとしてアドホックに文を羅列する段階で利用する。

## about node modules

執筆時に便利な道具としてnode moduleを利用する場合がある。node.js自体のバージョン管理はnvmで行う。

### prettier

[Prettier に関する markdown のフォーマッタとしての問題](https://qiita.com/tats-u/items/bcbfe2bb4e71bf0a2b87)を回避するため開発環境にインストールして利用する。

### commitzen

~~gitのコミットログを整理するためのnpmモジュール。~~
windowsのVS Codeターミナル (GitBash) だと相性が悪くコミットを上手く作れないっぽい。

## about Terminal

### GitBash

Windowsでgitを扱う為にGit for Windowsをインストール。ついでにGitBashが入るので基本的にはこれを使う。

#### 留意点

VS Code上でターミナルを扱う時に初期設定では文字化けする。VS Code側の設定で標準出力をutf-8に変更する必要がある。

私の場合はwindows環境で対応するためintl.cplから変更してしまった。

参考: [VSCode – ターミナルで UTF8 をデフォルトにする方法 (Windows)](https://pystyle.info/vscode-change-default-encoding-of-terminal-to-utf8/#outline__3)

## how to Write

書いてく時のルールについて記載する。

### git

#### commit message

コミットメッセージのフォーマットはざっくり [Angular のメッセージフォーマット](https://gist.github.com/brianclements/841ea7bffdb01346392c#type) を参考にする。

これを簡便にするnode moduleが [commitizen](https://www.npmjs.com/package/commitizen) なのだけれど、GitBash環境でどうも上手く動いていないっぽい。macOS（開発機）で利用していた時は問題なかった `git cz` 入力後にターミナルが操作を受け付けなくなっており、要調査。

### markdown

#### 見出し

- H5以上は使わない。

  - 文字が小さくなりすぎそう。
