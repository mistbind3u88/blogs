# about this repository

このリポジトリは個人でブログ執筆をする上での草案などを履歴管理する事を目的とする。READMEにはディレクトリ構成の意図や執筆環境として利用しているツールなどを言語化し再現可能にするための整理をしていくために利用していく予定。

基本的には私用でメイン機として利用しているWindows環境を前提として記載する。

## about Posting Sites

現在のところ下記のサービスを対象に記事を投稿している。

- [note](https://note.com/mistbind_artisan/all)
- [カクヨム](https://kakuyomu.jp/users/mistbind_artisan)
- [はてなブログ](https://mistbind3u88.hatenablog.com/)（縮退傾向）

## about Directories

本リポジトリのディレクトリ構成について記載する。

トップレベルには設定ファイルを配置し、下位ディレクトリをトピック毎に切る。

### [entertainments](https://github.com/mistbind3u88/blogs/tree/main/entertainments)

アバウトにエンタメ感想系。

取り敢えずは完結済みの漫画シリーズや映画の感想をメインに書いていく。物語構造や自分がおもしろいと思った事の整理としてまとめていく。

ウマ娘を始めて1度競馬の予想などもしてみた。

### [games](https://github.com/mistbind3u88/blogs/tree/main/games)

日頃プレイしたゲームのプレイに関する考察など。

映画・漫画の感想系との区別として、純粋に楽しんだ事のまとめという要素の他にゲームデザインに対する考察や攻略のアイデアという能動的な要素を含む。

### [stories](https://github.com/mistbind3u88/blogs/tree/main/stories)

三題噺など短編を書いた時に。

## about Editors

### Visual Studio Code

基本的に記事はmarkdown形式に落とすので、執筆時にエディターとして利用する。

以下、執筆時に利用してるプラグインについて記載する。

#### EditorConfig for Visual Studio Code

VS Codeの設定管理として。

#### Sort JSON objects

"setting.js"のソート用に。setting.jsのOnSaveでは上手く動かなかった？

#### markdownlint

markdown向けのlinter。

- 「MD024 - Multiple headings with the same content」をoff
- 「MD026 - Trailing punctuation in heading」をoff
  - ！や？も使えないので

#### テキスト校正くん

文章自体のの簡易的な校正のために利用する。

- ~~markdownのlintと競合するため、「設定 > Japanese-proofreading › Textlint: 全角文字と半角文字の間」をoffにする。~~
  - 競合部分をprettierで扱わない事にしたのでonに。
- 「Japanese-proofreading › Textlint: かっこ類と隣接する文字の間のスペースの有無」をoff
- 「Japanese-proofreading › Textlint: ダッシュ(-)」をoff
- 「Japanese-proofreading › Textlint: 丸かっこ（）」をoff
  - markdownのBold記法と組み合わせた時に大かっこの後に半角スペースを入れないといけない場面がある
- 「Japanese-proofreading › Textlint: 大かっこ［］」をoff
  - テキスト校正くんのバージョンアップで入った内容
  - windowsの入力周りで全角大かっこの入力が手間なので
- 「Japanese-proofreading › Textlint: 疑問符(？)」をoff
  - ？の後に全角スペースは普通に入れない
- 「Japanese-proofreading › Textlint: 算用数字と漢数字の使い分け」をoff
  - 残したいところではあったが、どうしても漢数字を使う方が自然に思える箇所で算用数字を要求される場面がある

#### Prettier Formatter for Visual Studio Code

markdownのformatterとしてprettierを利用する。

[Prettier に関して markdown のフォーマッタとしての問題](https://qiita.com/tats-u/items/bcbfe2bb4e71bf0a2b87)があったため拡張機能デフォルトのprettierではなくnodeモジュールをインストールしたものを利用する。

（noteに転記したところ全体として滅茶苦茶読み難かった。）

#### YAML Language Support by Red Hat

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

参考: [VS Code – ターミナルで UTF8 をデフォルトにする方法 (Windows)](https://pystyle.info/vscode-change-default-encoding-of-terminal-to-utf8/#outline__3)

## how to Write

書いてく時のルールについて記載する。

### git

#### issues

リポジトリに変更を加える際は必ずIssueを立てて目的別にPRする。

Issueの粒度は更新の単位として、1Issue-1PRで原則完結させる。IssueのClose前に修正を入れる場合はPRを可とする。

#### milestones

Issueは立てっぱなしを防止し期日管理をするため、必ず期日設定をしたMilestoneに紐づける。

たとえば、感想系の単発記事は月単位でリリース予定を設定したMilestoneに紐づける。一定期間継続的に更新を駆けていく記事や、複数記事をシリーズとしてリリースする、PRが複数になる事を前提した更新に際しては専用のMilestoneを用意し一連のIssueを紐づける。

#### branch

ブランチを切って作業する時にはリポジトリにissueを立ててそのidをブランチに含める。

- 記事執筆/改稿/更新時: `feature/#{id}-{description}`
- 記事訂正時: `fix/#{id}-{description}`
  - 訂正と改稿/更新の違いは内容の誤りを正す事が目的かどうか。

#### commit message

コミットメッセージのフォーマットはざっくり [Angular のメッセージフォーマット](https://gist.github.com/brianclements/841ea7bffdb01346392c#type) を参考にする。

これを簡便にするnode moduleが [commitizen](https://www.npmjs.com/package/commitizen) なのだけれど、GitBash環境でどうも上手く動いていないっぽい。macOS（開発機）で利用していた時は問題なかった `git cz` 入力後にターミナルが操作を受け付けなくなっており、要調査。

### markdown

#### 見出し

```markdown
# タイトル

## 大項目

### 小項目

#### 記事中では強調などで扱うケース

必要に応じて適宜箇条書きを用いる事
```

- H5以上は使わない。

  - 文字が小さくなりすぎそう。

- 段落は1行で書く。

  - アウトプット先のnoteはWYSIWYGなので読点で改行するとそのまま反映される。

#### Bold

```markdown
noteは**Bold**対応済み。
ただし、**括弧 (かっこ)** を使うときにVS Codeのプレビューが全角半角問わず前後に半角スペースを要求する事に留意。
```

#### 組み込み記法（マークアップ）

twitter等を扱うのにマークアップは使わない。

- noteはマークアップに対応していない。note側のエディターでtwitterのURLリンクを埋め込む。

### 特異記法

#### ルビ

```markdown
ルビの書き方の説明《せつめい》。
この書き方だとカクヨムは自動的に漢字までを構文解析して振ってくれる。

noteではルビを振る範囲を|必ず《かならず》指定する
カクヨムでもひらがなや複数単語にまで跨ったルビを振るにはこちらの記法にする必要がある。
```
