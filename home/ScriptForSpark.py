import csv
import pandas as pd
from tabulate import tabulate
import numpy as np


CSV_READ = 'phones.csv'
CSV_WRITE = 'new_phones.csv'


with open(CSV_READ, "r", encoding="utf-8-sig", newline='') as file:
    reader = csv.DictReader(file, delimiter=';')
    new_list_phone = []
    num = 0
    for item in reader:
        title_list = item['title'].split()
        new_list_phone.append(
            {
                'smartphone_id': num,
                'smartphone_brand': title_list[0],
                'smartphone_model': " ".join(title_list[1:len(title_list)]),
                'price': item['price']
            }
        )
        num = num + 1
        print(item)


with open(CSV_WRITE, "w", encoding="utf-8-sig", newline='') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow(['smartphone_brand', 'smartphone_model', 'smartphone_price'])
    for item in new_list_phone:
        writer.writerow([item['smartphone_brand'], item['smartphone_model'], item['price']])


df = pd.read_csv(CSV_WRITE, index_col=False, decimal=',', delimiter=';')
df['smartphone_price'] = df['smartphone_price'].str.replace(r'\D+', '', regex=True).astype(int)
df = df.groupby(['smartphone_model', 'smartphone_brand'], as_index=False)[['smartphone_price']].mean()
df['smartphone_id'] = df.groupby(['smartphone_model'])['smartphone_model'].rank(ascending=True, method='first')
df = df.sort_values('smartphone_brand')
df["smartphone_id"] = np.arange(1, 1 + len(df))
df_new = df.reindex(columns=['smartphone_id', 'smartphone_brand', 'smartphone_model', 'smartphone_price'])




#print(tabulate(df, headers='keys', tablefmt='psql'))
#print(tabulate(df_new, headers='keys', tablefmt='psql'))
