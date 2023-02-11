from pathlib import Path

from django.db import models
from .screening.rcs import cf_haitou_hiritsu


class SecCodeList(models.Model):
    """銘柄コ－ドリストモデル"""

    class Meta:
        db_table = 'seccode_list'

    # テ－ブルコラムに対応するテ－ブルを定義
    seccode = models.IntegerField(verbose_name='銘柄コード', primary_key=True)
    company_name = models.CharField(verbose_name='銘柄名', max_length=50)
    settlement_month = models.CharField(verbose_name='決済月', max_length=2)
    dividends_zenki = models.IntegerField(verbose_name='配当金（前期）')
    dividends_yosou = models.IntegerField(verbose_name='配当金（予想）')
    shares = models.IntegerField(verbose_name='発行済株式数')

    def __str__(self):
        return self.company_name


class ScreeningList(models.Model):
    """スクリーニングリストモデル"""

    class Meta:
        db_table = 'screening_lists'

    # テ－ブルコラムに対応するテ－ブルを定義
    seccode = models.IntegerField(verbose_name='銘柄コード', primary_key=True)
    company_name = models.CharField(verbose_name='銘柄名', max_length=50)
    industry = models.CharField(verbose_name='業種', max_length=50)
    priority_market = models.CharField(verbose_name='優先市場', max_length=50)
    settlement_month = models.CharField(verbose_name='決済月', max_length=2)
    accounting_standards = models.CharField(verbose_name='会計基準', max_length=50)
    market_capitalization = models.IntegerField(verbose_name='時価総額')
    ev_ebitda = models.FloatField(verbose_name='EV/EBITDA')
    dividends_zenki = models.IntegerField(verbose_name='配当金（前期）')
    dividends_yosou = models.IntegerField(verbose_name='配当金（予想）')
    dividend_yield = models.FloatField(verbose_name='配当利回り')
    own_capital_ratio = models.FloatField(verbose_name='自己資本比率')
    operating_cf = models.IntegerField(verbose_name='営業キャッシュフロー')
    shares = models.IntegerField(verbose_name='発行済株式数')

    def cf_div_ratio(cf_haitou_hiritsu):
        """
        | 私のやりたいこと
        | 1. \decode\screeningにあるscreening_20221224083954.csvが他のサイトからダウンロードしたcsv
        | 2. 同一パッケージにあるrcs.pyのcf_haitou_hiritsuを使用してこの段階で調査対象の銘柄を絞り込んだbase_listを作成
        | 3. \seccode\models.pyのscreening_listクラスにおいてbase_listを基にした
        | screening_listsというデータベースを作成したい
        | 4. その後の利用目的としては調査対象であるbase_listと既に調査した銘柄リストの
        | 差分を抽出し今回の調査対象である銘柄リストを作成したいのが意図です
        | akiyokoさんの「Django管理サイトのつくり方」の本にdjango-import-exportパッケージを使用した
        | 記載があったので一旦はそちらを参照して対応してみます
        | 以上です
        """

        base_path = Path(__file__).parent
        csv_file_path = base_path / 'screening' / 'screening_20221224083954.csv'
        base_list = cf_haitou_hiritsu(csv_file_path)
        return base_list
