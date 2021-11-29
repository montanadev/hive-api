import subprocess as proc
from datetime import datetime

import qrcode
from reportlab.lib.units import inch
from reportlab.lib.utils import ImageReader, simpleSplit
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfgen import canvas


def print_qr_label(upc, description):
    timestamp = datetime.now().strftime("%m.%d.%Y %H:%M:%S%p")

    text = f"{upc}\n{description}\n{timestamp}"

    LABEL_SIZE = (1.125 * inch, 3.25 * inch)

    # create label
    c = canvas.Canvas("label.pdf", pagesize=LABEL_SIZE)

    # transform so that we can render as if it's landscape mode
    c.rotate(-90)
    c.translate(-LABEL_SIZE[1], 0)

    # draw qr code
    qr_size = LABEL_SIZE[0]
    qr = qrcode.make(upc)
    c.drawImage(ImageReader(qr._img), LABEL_SIZE[1] - qr_size, 0, qr_size, qr_size)

    # font
    c.setFont("Helvetica", 10)

    # font metrics
    def getTextHeight(fontName, fontSize):
        face = pdfmetrics.getFont(fontName).face
        ascent = (face.ascent * fontSize) / 1000.0
        descent = (face.descent * fontSize) / 1000.0

        height = ascent - descent  # <-- descent it's negative
        return height

    item_spacing = 4

    # margins
    leftMargin = 4
    c.translate(leftMargin, 0)

    # vertically centered text drawn from the current point in multiple lines so
    # that it fits in the given box size
    def wrappedTextBox(canvas, text, boxSize, fontName, fontSize):
        c.saveState()

        lineHeight = getTextHeight(fontName, fontSize)
        lines = simpleSplit(text, fontName, fontSize, textWidth)

        totalHeight = len(lines) * lineHeight

        if totalHeight > boxSize[1]:
            raise RuntimeError("ERROR: Text is too big")

        # center text vertically
        c.translate(0, (boxSize[1] - totalHeight) / 2 + totalHeight - lineHeight)

        # print each line
        for i in range(len(lines)):
            c.setFont("Helvetica", 10)
            if i == 0:
                c.setFont("Helvetica-Bold", 8)
            if i == len(lines) - 1:
                c.setFont("Helvetica", 6)

            c.drawString(0, -lineHeight * (i * 1.4), lines[i])

        c.restoreState()

    # TODO: top/bottom margin
    textWidth = LABEL_SIZE[1] - qr_size - leftMargin - item_spacing + 10
    wrappedTextBox(c, text, (textWidth, LABEL_SIZE[0]), "Helvetica", 10)

    # save label pdf file
    c.save()

    # print
    print("Printing label...")
    proc.check_call(["lp", "label.pdf"])
    print("Done")
