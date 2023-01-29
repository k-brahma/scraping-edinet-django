import csv
from pathlib import Path


def cf_haitou_hiritsu(csv_file_path):
    base_list = []
    with csv_file_path.open(mode='r', encoding='shift_jis') as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(row)
            cf = row['営業CF'].replace(",", "")
            eq = row['発行済株式総数'].replace(",", "")
            cf_haitou_hiritsu = float(eq) * float(row['配当金(前期)']) / int(cf) / 1000000
            if not cf_haitou_hiritsu > 0.4:
                # row.clear()
                base_list.append(row)
    return base_list

# base_path = Path(__file__).parent
# csv_file_path = base_path / 'screening_20221224083954.csv'
# cf_haitou_hiritsu(csv_file_path)

# by_write_path = base_path / 'screening' / 'csv_cashflow_new.csv'


# with by_write_path.open(mode='w', encoding='utf-8', newline='') as f:
#     fieldnames = ['銘柄コード', '会社名', '決算月', '配当金(前期)', '配当金(会予)', '発行済株式総数']
#     writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction='ignore')
#     writer.writeheader()
#     for row in base_list:
#         writer.writerow(row)
