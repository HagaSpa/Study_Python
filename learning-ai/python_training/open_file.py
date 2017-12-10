#coding: UTF-8
score_list = []

score_list_file = open("score")

for score in score_list_file:
    # 行末の文字を削除。ここでは改行コード
    score = score.rstrip().split(",")
    score_list.append([score[0], int(score[1])])

score_list_file.close()

print score_list