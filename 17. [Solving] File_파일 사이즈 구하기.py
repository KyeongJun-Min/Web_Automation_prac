import os

def byte_to_mb(byte):
    return byte / (1000 * 1000)

# 이곳에 코드를 작성해주세요.
file_size = os.path.getsize("codeit_workshop.pptx")

# 아래의 출력 포맷을 사용하면 됩니다.
print("용량: {}MB".format(byte_to_mb(file_size)))
