import sys
import openpyxl as px

"""
引数で指定されたファイルに存在する、対象文字列を指定した色で塗るクラス。

excel_colored(fileName, color, target)
"""

# 引数をパースする
def parser():
    args = sys.argv
    # 引数の数が誤っている
    if (len(args) != 4):
        print ("正しい数の引数を指定してください")
        return False
    # 引数として自動的に付与される、ファイル名自身を削除
    args.pop(0)
    # 引数を変数へ代入
    file_name = args[0]
    color = args[1]
    target = args[2]
    return True

# main処理
if __name__ == '__main__':
    parse_result = parser()
    if (parse_result):
        print ("ok")