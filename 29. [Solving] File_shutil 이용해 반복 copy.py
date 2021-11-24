import os
import shutil

# 이곳에 코드를 작성해주세요.
name_temp = "diary_jan_"
for i in range(1, 30 + 1):
    shutil.copy("diary.hwp", name_temp + str(i) + ".hwp")

# 채점 코드
for f in sorted(os.listdir()):
    print(f)
