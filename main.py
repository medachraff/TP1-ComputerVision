import QtWidgets
from PyQt5 import QtWidgets, uic, QtGui
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QPixmap
import cv2
import sys

# Définition du fichier UI et chargement automatique des classes
qtcreator_file = "design.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtcreator_file)


class DesignWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(DesignWindow, self).__init__()
        self.setupUi(self)


img = cv2.imread("lena.jpg")
img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
b, g, r = cv2.split(img)
img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)

import matplotlib.pyplot as plt

hist_gray = cv2.calcHist([img_gray], [0], None, [256], [0, 256])
plt.plot(hist_gray)
plt.title("Histogramme Gris")
plt.show()

colors = ('b', 'g', 'r')
for i, col in enumerate(colors):
    hist = cv2.calcHist([img], [i], None, [256], [0, 256])
    plt.plot(hist, color=col)
plt.title("Histogramme par Canaux")


def makeFiqure():
    return


def showDimensions():
    return


def convert_cv_qt(self, cv_image):
    h, w, ch = cv_image.shape
    bytes_per_line = ch * w
    # Conversion vers QImage au format BGR888
    cv_image_Qt_format = QtGui.QImage(cv_image.data, w, h, bytes_per_line, QtGui.QImage.Format_BGR888)
    return QPixmap.fromImage(cv_image_Qt_format)


def showRedChannel():


def showGreenChannel():
    def showBlueChannel():


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = DesignWindow()
    window.show()
    sys.exit(app.exec_())
from PyQt5 import QtWidgets,uic,QtGui
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QPixmap
import cv2
import sys

qtcreator_file = "design.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtcreator_file)

class DesignWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(DesignWindow, self).__init__()
        self.setupUi(self)

if __name__=="main":
    app = QtWidgets.QApplication(sys.argv)
    window = DesignWindow()
    window.show()
    sys.exit(app.exec_())