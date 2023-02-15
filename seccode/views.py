from django.views.generic import ListView
from .models import SecCodeList, ScreeningList
from pathlib import Path

from .screening.rcs import cf_haitou_hiritsu


# Create your views here.
class SecCodeListV(ListView):
    model = SecCodeList
    template_name = 'sec_code_list.html'


class ScreeningListV(ListView):
    model = ScreeningList
    context_object_name = 'screening_lists'
    template_name = 'screening_list.html'

    def cf_div_ratio():

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


    def table_create(base_list):
        for row in base_list:
            screening_lists = ScreeningList.objects.create(
                seccode=int(row['銘柄コード']),
                company_name=row['会社名'],
                industry=row['業種'],
                priority_market=row['優先市場'],
                settlement_month=row['決算月'],
                accounting_standards=row['会計基準'],
                market_capitalization=int(row['時価総額']),
                ev_ebitda=float(row['EV/EBITDA']),
                dividends_zenki=int(row['配当金(前期)']),
                dividends_yosou=int(row['配当金(会予)']),
                dividend_yield=float(row['配当利回り(会予)']),
                own_capital_ratio=float(row['自己資本比率']),
                operating_cf=int(row['営業CF']),
                shares_outstanding=int(row['発行済株式総数']),
            )
        return screening_lists



