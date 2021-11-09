import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook

# HTML 코드 받아오기
response = requests.get("https://workey.codeit.kr/orangebottle/index")

# BeautifulSoup 사용해서 HTML 코드 정리
soup = BeautifulSoup(response.text, 'html.parser')

branch_infos = []
idx = 0

# 모든 지점에 대한 태그 가져오기
wb = Workbook(write_only=True)
ws = wb.create_sheet("오렌지 보틀 지점 정보")
ws.append(['지점 이름', '주소', '전화번호'])

branch_tags = soup.select('div.branch')

for branch_tag in branch_tags:
    # 각 태그에서 지점 이름, 전화번호 가져오기
    branch_name = branch_tag.select_one('p.city').get_text()
    address = branch_tag.select_one('p.address').get_text()
    phone_number = branch_tag.select_one('span.phoneNum').get_text()
    branch_infos.append([branch_name, address, phone_number])

    ws.append(branch_infos[idx])
    idx += 1

# 출력 코드
print(branch_infos)
wb.save("오렌지_보틀.xlsx")
