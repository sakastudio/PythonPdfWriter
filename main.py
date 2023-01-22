from pdfrw import PdfReader
from pdfrw.buildxobj import pagexobj
from pdfrw.toreportlab import makerl
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import portrait, landscape, A3, A4, A5, A6, B3, B4, B5, B6
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, portrait
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont


def set_monshin_pdf():
    # フォントファイルを指定して、フォントを登録
    fontname = "IPA Gothic"
    pdfmetrics.registerFont(TTFont(fontname, './ipaexg.ttf'))

    monshin_template = './monshin_template.pdf'
    output_path = './monshin_output.pdf'

    # 元のPDFを読み込み
    pages = PdfReader(monshin_template, decompress=False).pages

    # キャンバスのセット
    cc = canvas.Canvas(output_path, pagesize=portrait(A4))

    # ページ取得
    pp = pagexobj(pages[0])
    cc.doForm(makerl(cc, pp))


    # 文字サイズで書き出し
    cc.setFont(fontname, 15)  # フォントとサイズを指定
    cc.drawString(60, 755, '京都')  # x, y, 文字列を指定

    # 丸を描画する
    cc.circle(195, 755, 7, 1, 0)



    cc.showPage()
    cc.save()


set_monshin_pdf()
