# 이곳에 코드를 작성해주세요.
import shutil

shutil.copy("log.txt", "error_log_jan.txt")
with open("log.txt", "r", encoding="UTF-8") as file:
    content = file.read()

with open("error_log_jan.txt", "w+", encoding="UTF-8") as file:
    file.write("january error log\n")
    file.write(content)

# 채점 코드
import os
print(os.path.getsize("error_log_jan.txt"))
