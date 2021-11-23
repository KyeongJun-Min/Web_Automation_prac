reviews = ["computer_science.txt", "git.txt",
           "python_programming.txt", "web_publishing.txt"]

# 이곳에 코드를 작성해주세요.
with open("all_reviews.txt", "a", encoding="UTF-8") as file:
    for one in reviews:
        with open(one, "r", encoding="UTF-8") as review:
            content = review.read()
        file.write(content + "\n\n")

# 채점 코드
with open("all_reviews.txt") as review_txt:
    print(review_txt.read().strip())
