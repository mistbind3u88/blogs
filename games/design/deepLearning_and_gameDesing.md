# 昨今のDeepLearning事情とゲームデザインについて思う所

## DL系プロダクト/サービスの発展は目覚ましく興味深い記事もよくあがっている

### 文章の多言語翻訳で活躍するGoogle翻訳・DeepLはもはや生活の友

[Google翻訳について](https://translate.google.com/about/)

[DeepLを選ぶ理由](https://www.deepl.com/ja/why-deepl-pro)

### 解析系が主流だった画像処理が遂にクリエイティブの領域に到達した

文字列を解釈して十分クオリティの高い画像を出力できるプロダクトとして[Midjourney](https://www.midjourney.com/home/)、[StableDiffusion](https://github.com/CompVis/stable-diffusion)が世間を賑わせた。

[魔術として理解するお絵描きAI講座](https://note.com/fladdict/n/n0f0be20e3e23)

日本産では、ユーザーが自分のイラストを入力する事で絵柄が類似したサンプルを出力できる特化型の[mimic](https://illustmimic.com/)が登場している。

最近では自分もStableDiffusionを利用してまさにnoteのサムネイルを作ってみている。

![2D fighting game battle screen in oil painting style. Unreal Engine, 4k.](https://user-images.githubusercontent.com/18084560/192193811-33eac4ab-697c-4ef8-ab86-902e847e8b6c.png)

### DLが最初に力を発揮した囲碁/将棋界隈ではさらなる発展に向けてより良質な学習環境の提供がサービス化されている

[ディープラーニングは今までの将棋AIとどう違う？HEROZエンジニアが開発した将棋AIが電竜戦で初優勝した理由](https://logmi.jp/tech/articles/324157)

## 先日リリースされた記事はゲームデザインに対する影響を考えさせるものだった

[AI技術者に訊くストV。自作のメナト使い分析ツールの話や、ウメハラを再現したAIを作成した話、AIが決めるストV最強キャラの話など。｜カミヅキ記録帳](https://www.camduki.com/entry/menatai)

### DL系の技術を活用して2D対戦格闘ゲームを攻略する人が出てきた

CFN（CAPCOM Fighters Network）という様々なプレイヤーの対戦データが開始から決着までの両プレイヤーの入力まで閲覧可能なシステムを利用して取得した動画データを解析し、ある程度のランク帯（プレイヤーの練度指標）別に勝敗に繋がる行動を確率的に判断して決定可能なDL系ツールを作成したらしい。

### 既に勝率を高める格闘ゲームの指導をDLによって実践できるところに来ていそうだ

**クソバイス問題はAIが解決する**という強烈な見出しの話が中でも興味深い

> カミヅキ　MASがすごいのは分かるんですけれども、これが実際のプレイにどう活きるんですか？
>
> きみ　たとえばカミヅキさんから頂いたアドバイスが本当かどうかというのをデータを使って検証するんですよ。
>
> カミヅキ　え、そんなことが分かるんですか。
>
> きみ　カミヅキさんは、メナトの負けパターンをブログでまとめてましたけど（参考）、アレが結構的を得てるんですよ。たとえば強スフィアを出したせいで水晶が返ってこなくて負けるパターンがゴールドやシルバーの人は38%あるんですよ。10回やったら4回ぐらいは勝てる試合を落としてるんです。

これはつまり、囲碁/将棋なら特定の盤面に対するある指し手による勝率を算出するのと同じ様に、対戦中の特定行動による勝敗への影響を統計的に弾き出せているという事である。

自分はシトネさん（[@sitone_sitone](https://twitter.com/sitone_sitone)）からのリツイートでこの記事を拝読したのだけれど、以前からたまに[ぴよ将棋](https://www.studiok-i.net/ps/)でというプロダクトでコンピューター相手に対戦をし、手の好悪をしてもらって練習するというプロセスを経験していたので2D対戦格闘ゲームでもそれが十分可能な領域に来ている様に思えた。

<https://twitter.com/sitone_sitone/status/1573989639307681793>

<https://twitter.com/645reform/status/1573998676393197569>

<https://twitter.com/645reform/status/1574000011737993216>

### DL系の技術を利用すれば各種パラメータを理想的な勝率に対して最適化できる

以前から考えていた事だけれど、その他にもDLを活用したゲーム製作の省力化は色々ありそうだ。

数値問題の最適化などはその最たるものの一つだ。これに関してはむしろDLが得意とする分野の1つに思える。

<https://twitter.com/645reform/status/1574228345365336069>

キャラクターやそれに紐づくスキルなどのパラメータ/効果量/発動率/発動可能タイミングみたいな要素を数値化してNNに食わせて得られる。例えばその出力としての予測勝率に対してシミュレーションで1000戦とか回した結果を比較しバックプレッシャーをかければ、学習フェーズを回す事ができる。

<https://twitter.com/645reform/status/1574228347823222784>

<https://twitter.com/645reform/status/1574229818979545088>

他には格闘ゲームならコンボや返し難い連携の発見を自動化できる。

<https://twitter.com/645reform/status/1574234636913643520>

マリオを攻略するDL系の試みを考えればこれは大分前から現実的に思える。

[スーパーマリオを人工知能で攻略　米エンジニア、秒速クリアに挑戦](https://withnews.jp/article/f0150711000qq000000000000000W0230901qq000012241A)

[MarI/O - Machine Learning for Video Games](https://www.youtube.com/watch?v=qv6UVOQ0F44)

### 取れる行動の変化量が確率的に狭いゲームの最適化はDLが向いていそうだ

[MTGのチューリング完全性【要約版】｜note](https://note.com/kind_aster978/n/nfd883d0c5411)

## DL系では自動化しきれないの問題

### プレイ体験に対する最適化は人の感性でしか成否を出せない

<https://twitter.com/645reform/status/1574228349802942464>

### そもそもパラメータの調整では解決できない問題はある

デザインの悪さからくる有利不利など。

## 昔みた囲碁/将棋のブレイクスルーに比べて転換点が訪れるのが早くなっている

### 最初にDLが世間一般に注目されるきっかけとなったAlphaGoの時代と比べると、登場から人間を超すまでのスピードが圧倒的に早い。

[ＡＩ作品が絵画コンテストで優勝、アーティストから不満噴出｜CNN](https://www.cnn.co.jp/tech/35192929.html)

![image](https://user-images.githubusercontent.com/18084560/192196945-31ced046-5a1e-49ec-ba63-3dc1f3321e9e.png)

- [電王戦で将棋ソフトに負けた棋士「完敗でした」｜日経ビジネス](https://business.nikkei.com/atcl/interview/15/279177/022600042/)
- [進化を遂げた囲碁AI「AlphaGo」の勝利に、人工知能の未来を見た：『WIRED』US版リポート](https://wired.jp/2017/05/24/revamped-alphago-wins-first-game-chinese-go-grandmaster/)

### 他にもMidjournty的に適用できそうな領域がいろいろありそうだ

パラメータのバランスを変えた大量のサンプルを生成して、それをベースに人が調整をかけるやり方。

[「FINAL FANTASY VII REMAKE」メイキング｜ポリゴノート](https://polygonote.com/2020_1223_17695/)を引用に。

- ライティングの調整とか
  - 光度
  - 反射率

![ライティングを変えたクラウド](https://polygonote.com/cms/wp-content/uploads/2022/01/18_.jpg)

- エフェクトの発生量とか

![火花が散るエフェクト](https://polygonote.com/cms/wp-content/uploads/2022/01/ss01.jpg)

- 流体シミュレーションの適用度とか

![カクテルを掲げるクラウド](https://polygonote.com/cms/wp-content/uploads/2022/01/14a_-1.jpg)

### ゲーム制作においてもDL系で「楽をする」のが当たり前になる時はすぐそこじゃないだろうか。
