import sys
import openpyxl as px

"""
引数で指定されたファイル（フルパス）に存在する、対象文字列を指定した色で塗るクラス。

excel_colored(fileName, color, target)
"""

# グローバル変数定義
file_name = ""
color = ""
target = ""

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
    global file_name
    global color
    global target
    file_name = args[0]
    color = args[1]
    target = args[2]
    return True

# 色付けを実行する
def colored():
    global file_name
    global color
    global target
    # Excekの読み込み
    wb = px.load_workbook(file_name)
    # シート名一覧を取得（カンマ区切りで取得できる）
    sheetnames = wb.get_sheet_names()
    print (sheetnames) 


# main処理
if __name__ == '__main__':
    parse_result = parser()
    if (parse_result):
        colored()