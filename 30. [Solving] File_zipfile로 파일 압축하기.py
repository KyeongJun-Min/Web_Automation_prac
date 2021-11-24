import zipfile
import os

filenames = ['service_contract.hwp', 'christmas_report.pptx',
             'business_report.docx', 'accounting_report.pptx', 'account_book.pptx']

# 이곳에 코드를 작성해주세요.
with zipfile.ZipFile("all_files.zip", "w", compression=zipfile.ZIP_DEFLATED) as zip:
    for file in filenames:
        zip.write(file)

print(os.path.getsize("all_files.zip"))
