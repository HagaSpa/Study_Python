import sys
import openpyxl as px
from openpyxl.styles import Font

"""
引数で指定されたファイル（フルパス）に存在する、対象文字列を指定した色で塗るクラス。

excel_colored(fileName, color, target)
"""

class ExcelColored:
    
    # コンストラクタで引数を用いて定義
    def __init__(self, file_name, color, target):
        self.file_name = file_name
        self.color = color
        self.target = target
    
    # 色付けを実行する
    def colored(self):
        # Excelの読み込み
        wb = px.load_workbook(self.file_name)
        # Excelの全シートを回す
        for sheet in wb.sheetnames:
            ws = wb.get_sheet_by_name(sheet)
            # xはワークシートの全行
            x = ws.rows
            # 全行の中の一行
            for u in x:
                # 一行の中の一つのセルを取得
                for v in u:
                    if v.value is not None:
                        # セル内の文字列が該当文字列を含むなら
                        if (self.target in v.value):
                            # 引数で指定された色（16進）で塗る
                            # TODO:部分一致した文字列のみを色塗りたい・・・
                            v.font = Font(color=self.color)
        # ファイル保存
        wb.save(self.file_name)

# main処理
if __name__ == '__main__':
    args = sys.argv
    if (len(args) == 4):
        args.pop(0)
        color = ExcelColored(args[0], args[1], args[2])
        # 着色
        color.colored()
    else:
        print("以下形式で実行してください")
        print("$ excel_colored.py <file_name> <color> <target>")
        
