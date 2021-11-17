import os
import datetime

birthtimestamp = os.path.getctime("코스타그램.xlsx")
birthtime = datetime.datetime.fromtimestamp(birthtimestamp)
print("만든 날짜 : {}".format(birthtime))

mtimestamp = os.path.getmtime("코스타그램.xlsx")
mtime = datetime.datetime.fromtimestamp(mtimestamp)
print("만든 날짜 : {}".format(mtime))

accesstimestamp = os.path.getatime("코스타그램.xlsx")
accesstime = datetime.datetime.fromtimestamp(accesstimestamp)
print("만든 날짜 : {}".format(accesstime))
