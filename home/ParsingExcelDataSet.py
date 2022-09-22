# Посчитать:
# 1. Сумму продаж по каждому магазину.
# 2. Cамый продаваемый товар по:
# - количеству
# - сумме продаж
# - по каждому магазину
# - помесячно
import pandas as pd


if __name__ == "__main__":
    df = pd.read_csv('C:\supermarket_sales.csv')
    '''
    # 1. Сумма продаж по каждому магазину.
    print(df.groupby(['Branch'])['Total'].sum().reset_index().drop_duplicates('Total', keep='first'))
    print()
    # 2. Cамый продаваемый товар по:
    # - количеству
    print(df.groupby(['Product line'])['Quantity'].agg(['count']).sort_values('count').reset_index().drop_duplicates(
        'Product line', keep='first').tail(1))
    print()
    # - сумме продаж
    print(df.groupby(['Product line'])['Total'].sum().reset_index().drop_duplicates('Total', keep='first').sort_values(
        'Total').tail(1))
    print()
    '''
    # - по каждому магазину
    print(df.groupby(['Branch', 'Product line'])['Total'].sum().reset_index().drop_duplicates('Total', keep='first').sort_values(['Branch', 'Total']))






