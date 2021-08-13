# coding: UTF-8

QUESTION = [
    "King GnuのGt/Voは？",
    "King GnuのKey./Vo.は？",
    "King GnuのDr.は？",
    "King GnuのBa.は？"
]

R_ANS = ["常田大希","井口理","勢喜遊","新井和輝"]
R_ANS2 = ["ツネタダイキ","イグチサトル","セキユウ","アライカズキ"]
for i in range(3):
    print(QUESTION[i])
    ans = input()
    if ans == R_ANS[i] or ans == R_ANS2[i]:
        print("正解です")
    else:
        print("不正解です")
