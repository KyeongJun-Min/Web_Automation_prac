import os
import datetime

filenames = ['service_contract.hwp', 'christmas_report.pptx', 'business_report.docx', 'accounting_report.pptx', 'account_book.pptx']

dictionary = dict()
array = []
for filename in filenames:
    mtime = datetime.datetime.fromtimestamp(os.path.getmtime(filename))
    size = os.path.getsize(filename)
    dictionary = {'filename': filename, 'mtime': str(mtime), 'size': size}
    array.append(dictionary)

# 이곳에 코드를 작성해주세요.

# 문제에 있는 출력 포맷을 참고해서 출력해주세요.
for i in range(0, len(array)):
    print(array[i])
