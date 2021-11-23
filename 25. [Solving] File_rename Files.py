import os
filenames = ['service_contract.hwp', 'account_book.pptx',
             'business_report.docx', 'accounting_report.pptx', 'christmas_report.pptx']

# 이곳에 코드를 작성하세요.
for name in filenames:
    os.rename(name, "codeit_"+name)

# 채점 코드
for f in sorted(os.listdir()):
    if f == 'main.py':
        continue
    print(f)
