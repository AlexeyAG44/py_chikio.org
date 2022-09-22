from datetime import datetime
import csv


file_handler = open('C://data.bin', 'rb')
data_byte = file_handler.read(5)
data_bin_list = []

with open('C://data.bin', 'rb') as fh:
    for i in data_byte:
        num_pp = int.from_bytes(fh.read(4), byteorder='big')
        num_phone = fh.read(10).decode('utf-8')
        num_year = int.from_bytes(fh.read(2), byteorder='little')
        num_month = int.from_bytes(fh.read(1), byteorder='little')
        num_day = int.from_bytes(fh.read(1), byteorder='little')
        hour = int.from_bytes(fh.read(1), byteorder='little')
        min = int.from_bytes(fh.read(1), byteorder='little')
        sec = int.from_bytes(fh.read(1), byteorder='little')
        date_str = str(num_year).strip() + '-' + str(num_month).strip() + '-' + str(num_day).strip() + ' ' + \
                   str(hour).strip() + ':' + str(min).strip() + ':' + str(sec).strip()
        datetime = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")

        data_bin_list.append(
            {
                'Номер': num_pp,
                'Номер телефона': num_phone,
                'Время события': datetime
            }
        )

with open("data_bin.csv", "w", encoding="utf-8-sig", newline='') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow(['Номер', 'Номер телефона', 'Время события'])
    for item in data_bin_list:
        writer.writerow([item['Номер'], item['Номер телефона'], item['Время события']])











'''
from datetime import datetime
import csv

file_handler = open('C://data.bin', 'rb')
data_byte = file_handler.read(21)
data_bin_list = []
while data_byte:
    data_bin_list.append(data_byte)
    data_byte = file_handler.read(21)

#print(data_bin_list)
for i in data_bin_list:



    #num_pp = int.from_bytes(i., byteorder='big')






with open('C://data.bin', 'rb') as fh:
    for i in fh.read():

        num_pp = int.from_bytes(fh.read(4), byteorder='big')
        num_phone = fh.read(10).decode('utf-8')
        num_year = int.from_bytes(fh.read(2), byteorder='little')
        num_month = int.from_bytes(fh.read(1), byteorder='little')
        num_day = int.from_bytes(fh.read(1), byteorder='little')
        hour = int.from_bytes(fh.read(1), byteorder='little')
        min = int.from_bytes(fh.read(1), byteorder='little')
        sec = int.from_bytes(fh.read(1), byteorder='little')
        date_str = str(num_year).strip() + '-' + str(num_month).strip() + '-' + str(num_day).strip() + ' ' + \
                str(hour).strip() + ':' + str(min).strip() + ':' + str(sec).strip()
        #datetime = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
        #print(num_pp, num_phone, datetime)


'''
