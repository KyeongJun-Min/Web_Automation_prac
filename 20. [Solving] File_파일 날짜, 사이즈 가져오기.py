import os
import datetime

filename = "introduction.pptx"

# 이곳에 코드를 작성해주세요.
timestamp = os.path.getmtime(filename)
mtime = datetime.datetime.fromtimestamp(timestamp)

size = os.path.getsize(filename)

# 채점 코드
print("파일의 이름은 {}이고, {}에 수정되었습니다.".format(filename, mtime))
print("파일의 용량은 {}byte입니다.".format(size))
