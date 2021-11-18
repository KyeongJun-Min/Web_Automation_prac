import os
import datetime

file = open("내가 좋아하는 노래.txt", encoding="UTF-8")
print(file.readline())
print(file.readline())

print(file.read())
print(file.seek(0))

print(file.readlines())
