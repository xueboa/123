import pandas as pd
from pyquery import PyQuery as pq

with open('D:/zhuomian/编程试题/实时更新：新型冠状病毒肺炎疫情地图.html', encoding="UTF-8") as f:
    f = f.read()
    doc = pq(f)
    new_df = pd.DataFrame(columns=['地区','新增', '无症状', '累计', '风险地区'])
    n = 0
    for value in doc('.VirusTable_1-1-350_3m6Ybq').items():
        n += 1
        city = value('.VirusTable_1-1-350_2NQDw6').text()
        new = value('.VirusTable_1-1-350_3x1sDV VirusTable_1-1-350_2bK5NN').eq(0).text()
        now = value('.VirusTable_1-1-350_3x1sDV').eq(0).text()
        all = value('.VirusTable_1-1-350_EjGi8c').eq(0).text()
        suc = value('.VirusTable_1-1-350_EjGi8c').eq(1).text()
        new_df.loc[n, '地区'] = city
        new_df.loc[n, '新增'] = new
        new_df.loc[n, '无症状'] = now
        new_df.loc[n, '累计'] = all
        new_df.loc[n, '风险地区'] = suc
        print(city, new, now, all, suc)
    new_df.to_csv('./国内疫情.csv')