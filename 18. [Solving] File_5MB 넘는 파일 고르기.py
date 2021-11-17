import os

filenames = ['service_contract.hwp', 'christmas_report.pptx',
             'business_report.docx', 'accounting_report.pptx', 'account_book.pptx']
over_5mb_filenames = []

# 이곳에 코드를 작성하세요.
for file in filenames:
    mb_size = os.path.getsize(file)/(1000*1000)
    if(mb_size > 5):
        over_5mb_filenames.append(file)

# 채점 코드
print("5MB가 넘는 파일 리스트:")
print(over_5mb_filenames)
