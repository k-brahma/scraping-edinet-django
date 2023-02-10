import csv


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
