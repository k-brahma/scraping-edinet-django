# scraping-edinet-django

EdinetスクレイピングのDjangoアプリ

### SECRET_KEYをGitのバージョン管理の対象外に関する処理

- SECRET_KEYを管理対象外にしておりますのでクロ－ン後は以下の処理を行ってください

1. クロ－ンの実施
   git clone https://github.com/UtsuboHiroaki/scraping-edinet-django.git

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

5. プロジェクト直下でターミナルを開く


6. 以下のコマンドを実行

   ``` shell
   python manage.py shell
   ```

7. 対話モードで以下のコードを実行

   ```python
   from django.core.management.utils import get_random_secret_key
   
   get_random_secret_key()
   ```

8. 出力された文字列をコピ－


9. /config に移動しsettings_local_sample.pyの名称をsettings_local.pyに変更

10. settings_local.pyにコピ－したSECRET_KEYを貼る
    SECRET_KEY = ''
