import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import json
import get_path
from img_to_br import img_braille
global c
c=0
class QExampleLabel (QtWidgets.QLabel):
    f=""
    # rf = open("/Users/adityachandra/Environments/myocr/Gui/config.json")
    # config = json.load(rf)
    # rf.close()
    def __init__(self,f, parentQWidget = None):
        super(QExampleLabel, self).__init__(f,parentQWidget)
        self.initUI(f)

    def initUI (self,f):

        self.setPixmap(QPixmap(f).scaled(600,600,QtCore.Qt.IgnoreAspectRatio,QtCore.Qt.SmoothTransformation))

    def mousePressEvent (self, eventQMouseEvent):
        self.originQPoint = eventQMouseEvent.pos()
        self.currentQRubberBand = QtWidgets.QRubberBand(QtWidgets.QRubberBand.Rectangle, self)
        self.currentQRubberBand.setGeometry(QtCore.QRect(self.originQPoint, QtCore.QSize()))
        self.currentQRubberBand.show()

    def mouseMoveEvent (self, eventQMouseEvent):
        self.currentQRubberBand.setGeometry(QtCore.QRect(self.originQPoint, eventQMouseEvent.pos()).normalized())

    def mouseReleaseEvent (self, eventQMouseEvent):
        self.currentQRubberBand.hide()
        currentQRect = self.currentQRubberBand.geometry()
        self.currentQRubberBand.deleteLater()
        cropQPixmap = self.pixmap().copy(currentQRect)
        global c
        c=c+1
        stri=get_path.get_images()
        file_path = stri+"/output"+str(c)+".png"
        cropQPixmap.save(file_path)
        i_obj = img_braille(file_path)
        i_obj.convert_img()

if __name__ == '__main__':
    myQApplication = QApplication(sys.argv)
    myQExampleLabel = QExampleLabel('/Users/adityachandra/Environments/myocr/ncrt2.png')
    myQExampleLabel.show()
    sys.exit(myQApplication.exec_())
