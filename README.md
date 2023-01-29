# sclayPing_Edinet_django
EdinetスクレイピングのDjangoアプリ
### SECRET_KEYをGitのバージョン管理の対象外に関する処理

- SECRET_KEYを管理対象外にしておりますのでクロ－ン後は以下の処理を行ってください

1. クロ－ンの実施

2. \config に移動

3. 移動先でターミナルを開く

4. 以下を実行する
  - python generate_secretkey_setting.py > local_settings.py

5. SECRET_KEYが生成されるのでコピ－

6. local_settings.pyにコピ－したSECRET_KEYを貼る
SECRET_KEY = ''
