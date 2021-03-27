# 手順
1. リポジトリのクローン
git clone git@github.com:user/

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

5. python core.py

6. 必ず終了！

# エラーが起きたとき
  ## ベータ版が入っていると不具合が起きる！！ uninstallする！
    * googleapis-common-protosを取り除いてからapicore を入れる！↓
    * python -m pip install google-cloud-core==1.5.0

  ## portが埋まっているとき
    1. apt install lsof
    2. lsof -i :5000
    3. kill -9 901

# メモ書き
python3 -m pip install google-cloud-speech
sudo pip install --upgrade google-cloud-speech
sudo pip install --upgrade google-cloud

# pyaudio
sudo apt-get install portaudio19-dev python-all-dev
sudo pip3 install pyaudio

# 環境周り
## パッケージマネージャーの更新
sudo apt update
sudo apt upgrade

## pipのインストール
sudo apt install python-pip
pip install --upgrade pip

## (venv)
pip install virtualenv
python -m virtualenv venv

## venvのインストール
sudo apt install python3-venv

## venvの作成とアクティブ化
python3 -m venv my_venv
. my_venv/bin/activate


# 以下 管理用
## requirements.txtの取り扱い
pip list
pip freeze
pip freeze > requirements.txt

## 最初にreadmeを作った時
git fetch
git merge origin/master

こうするとlocalにReadme.mdがmergeされる。あとは以下のコマンドでpushを再度チャレンジ。
git push -u origin master

## Git
1. git init（初回のみ）
2. git add .
3. git commit -m "base"
4. git branch -M master
5. git remote add origin git@github.com:suzuki-hikaru/
6. git remote set-url origin git@github.com:suzuki-hikaru/ （変更したいとき）
7. git push -u origin master