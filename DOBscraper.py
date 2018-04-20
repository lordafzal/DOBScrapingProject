
import csv
import requests
import bs4
import time
import random
import pandas as pd
import os
def scrape(borough, block, lot, largeFile):
    url = "http://a836-acris.nyc.gov/DS/DocumentSearch/BBLResult"
    headers = {'User-Agent': 'Mozilla/5.0'}
    count = 0
    bname = 0
    if borough=='0':
        bname = 'STATEN ISLAND / RICHMOND'
    elif borough=='1':
        bname = 'QUEENS'
    elif borough=='2':
        bname = 'MANHATTAN / NEW YORK'
    elif borough=='3':
        bname = 'BROOKLYN / KINGS'
    elif borough=='4':
        bname = 'BRONX'
    data = {
        'hid_borough': borough,
        'hid_borough_name': bname,
        'hid_block': block,
        'hid_block_value': block,
        'hid_lot': lot,
        'hid_lot_value': lot,
        'hid_doctype_name': 'All Document Classes',
        'hid_max_rows': '150',
        'hid_page': '1',
        'hid_SearchType': 'BBL',
        'hid_ISIntranet': 'N'
    }
    t = open("testfile" + ".csv", 'w+')
    response = requests.post(url, headers=headers, data=data)
    soup = bs4.BeautifulSoup(response.text, "lxml")
    table = soup.find(attrs={"cellspacing": "1", "width": "100%"})
    for row in table.find_all('tr')[1:]:
        for col in row.find_all('td')[1:]:
            for f in col.find_all('font'):
                value = f.string
                try:
                    value = value.replace(',', '')
                    t.write(value.strip())
                    t.write(',')
                except Exception:
                    t.write('*,')
                    pass
                count += 1
            if count != 0 and count % 14 == 0:
                t.write('\n')
    t.close()
    if not os.path.exists(largeFile):
        fout = open(largeFile, 'a+')
        fout.write("Reel/Pg/File,CRFN, Lot, Partial, Doc Date, Recorded / Filed, Document Type, Pages, Party1, Party2, Party3 / Other, More Party 1/2 Names, Corrected / Remarks, Doc Amount\n")
        for line in open("testfile.csv"):
            fout.write(line)
    else:
        fout = open(largeFile, 'a')
        for line in open("testfile.csv"):
            fout.write(line)

scrape("3", "1300", "35", "testdata.csv")
scrape("3", "3254", "63", "testdata.csv")
