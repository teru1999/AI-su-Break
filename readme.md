# AI-su-Break

## 概要
### ユースケース
* リモートワークやオンライン教育状況下でのコミュニケーション支援。

### 予定機能
* 機械学習による表情分析
* 会話テキスト解析（google speech to text API）とword2vecを用いた話題提供
* 頻出話題とTwitterトレンド語の関係性を用いた話題の効果的な選定
* skywayやwebsocketを用いたビデオ通話・チャット
* リアルタイムでの盛り上がり度の描画（d3, epoch）
* 会話時間の計測

## 手順
1. リポジトリのクローン
git clone git@github.com:user/AI-su-Break.git

2. 認証用のJSONファイルのアップロード

3. pip install requirements.txt
    * 今は不要なものがたくさんあるからだめ

4. 環境変数の登録
    * Linux&Mac
        * export GOOGLE_APPLICATION_CREDENTIALS="key.json"
    * powershell
        * $env:GOOGLE_APPLICATION_CREDENTIALS="key.json"
    * command pronpt
        * set GOOGLE_APPLICATION_CREDENTIALS=key.json

5. python app.py

6. 必ず終了！

## エラーが起きたとき
  ### ベータ版が入っていると不具合が起きる！！ uninstallする！
    googleapis-common-protosを取り除いてからapicore を入れる！↓
    python -m pip install google-cloud-core==1.5.0

  ### portが埋まっているとき
    apt install lsof
    lsof -i :5000
    kill -9 901

## メモ書き
* python3 -m pip install google-cloud-speech
* sudo pip install --upgrade google-cloud-speech
* sudo pip install --upgrade google-cloud

## pyaudio
* sudo apt-get install portaudio19-dev python-all-dev
* sudo pip3 install pyaudio

## コーパスの入手と展開
1. mkdir dataset
2. cd dataset
3. wget https://www.rondhuit.com/download/ldcc-20140209.tar.gz
4. tar zxvf ldcc-20140209.tar.gz
