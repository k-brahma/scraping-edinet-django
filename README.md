# sclayPing_Edinet_django
EdinetスクレイピングのDjangoアプリ
### SECRET_KEYをGitのバージョン管理の対象外に関する処理

- SECRET_KEYを管理対象外にしておりますのでクロ－ン後は以下の処理を行ってください

1. クロ－ンの実施
  git clone https://github.com/UtsuboHiroaki/sclayPing_Edinet_django.git

2. 仮想環境を作る

   ``` shell
   python -m venv venv
   ```

3. 仮想環境に入る

   ``` shell
   venv\Scripts\activate
   ```

4. Djangoをインストール

   ```shell
   pip install django

   ```
5. \config に移動


6. 移動先でターミナルを開く


7. 以下を実行する
  - python generate_secretkey_setting.py > local_settings.py


8. SECRET_KEYが生成されるのでコピ－


9. local_settings.pyにコピ－したSECRET_KEYを貼る
SECRET_KEY = ''
