import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook

wb = Workbook(write_only=True)
ws = wb.create_sheet("SBS 데이터")
ws.append(['기간', '순위', '프로그램', '시청률'])

for year in range(2010, 2018 + 1):
    for month in range(1, 12 + 1):
        for weekidx in range(0, 5):

            response = requests.get("https://workey.codeit.kr/ratings/index?year={}&month={}&weekIndex={}".format(year, month, weekidx))
            soup = BeautifulSoup(response.text, 'html.parser')
            week = "{}년 {}월 {}주차".format(year, month, weekidx + 1)
            for tr_data in soup.select("tr")[1:]:
                if(tr_data.select_one("td.channel").get_text() == "SBS"):
                    rank = tr_data.select_one("td.rank").get_text()
                    program = tr_data.select_one("td.program").get_text()
                    rate = tr_data.select_one("td.percent").get_text()
                    ws.append([week, rank, program, rate])

wb.save("SBS_데이터.xlsx")

