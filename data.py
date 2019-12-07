import requests
import lxml.html as lh
import pandas as pd

months = ['januari', 'februari', 'mars', 'april', 'maj', 'juni', 'juli', 'augusti', 'september', 'oktober', 'november', 'december']
months_num = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']

def get_month_df(url):
    page = requests.get(url)
    doc = lh.fromstring(page.content)
    tr_elements = doc.xpath('//tr')

    col=[]
    df = []
    i=0
    for t in tr_elements[0]:
        i+=1
        cols = []
        for col in t.iterchildren():
            cols.append(col.text_content())
        df.append(cols)

    for j in range(1,len(tr_elements)):
        T = tr_elements[j]
        
        if len(T) != 4:
            continue
        
        i=0
        cols = []
        for t in T.iterchildren():
            data=t.text_content()
            data = str(data).replace(' ', '').replace('\t', '').replace('\n', '')
            cols.append(data)
            i+=1
        df.append(cols)

    df_2 = []
    for row in df:
        rec = []
        if len(row) == 4:
            rec.append(modify_date(row[0]))
            rec.append(row[1])
            rec.append(row[2])
            rec.append(row[3])
            df_2.append(rec)
    del df

    df = pd.DataFrame.from_records(df_2, columns=['date', 'sun_up', 'sun_down', 'day_length'])
    return df

def modify_date(date_str):
    date = date_str.split(',')[0].strip()
    for m in months:
        if date.find(m) != -1:
            date.find(m)
            date = date.replace(m, '-'+months_num[months.index(m)]+'-')
            break
    if len(date) != 10:
        date = '0' + date
    date_arr = date.split('-')
    date = date_arr[2] + '-' + date_arr[1] + '-' + date_arr[0]
    return date

def get_all_months_data(baseUrl):
    all_months_data = []
    for mon in months:
        url = baseUrl + mon
        print('Downloading: ',url)
        df = get_month_df(url)
        all_months_data.append(df)
    all_months_data = pd.concat(all_months_data, ignore_index=True)
    return all_months_data
