import sys
import cv2
import numpy as np
import matplotlib.pyplot as plt
from PyQt5 import QtWidgets, uic, QtGui
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt

qtcreator_file = "design.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtcreator_file)

class DesignWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(DesignWindow, self).__init__()
        self.setupUi(self)

        self.Browse.clicked.connect(self.get_image)
        self.DisplayRedChan.clicked.connect(self.showRedChannel)
        self.DisplayGreenChan.clicked.connect(self.showGreenChannel)
        self.DisplayBlueChan.clicked.connect(self.showBlueChannel)
        self.DisplayColorHist.clicked.connect(self.show_HistColor)
        self.Valider.clicked.connect(self.show_UpdatedImgGray)
        self.DisplayGrayHist.clicked.connect(self.show_HistGray)

        self.img = None
        self.imgUpdated = None

    def makeFigure(self):
        pass

    def showDimensions(self):
        if self.img is not None:
            h, w, c = self.img.shape
            self.Dimensions.setText(f"{h}*{w}")

    def convert_cv_qt(self, cv_image):
        if len(cv_image.shape) == 3:
            h, w, ch = cv_image.shape
            bytes_per_line = ch * w
            cv_image_Qt_format = QtGui.QImage(cv_image.data, w, h, bytes_per_line, QtGui.QImage.Format_BGR888)
        else:
            h, w = cv_image.shape
            bytes_per_line = w
            cv_image_Qt_format = QtGui.QImage(cv_image.data, w, h, bytes_per_line, QtGui.QImage.Format_Grayscale8)
        return QPixmap.fromImage(cv_image_Qt_format)

    def display_scaled_image(self, cv_image, label):
        """Helper function to convert cv2 image and scale it to fit the QLabel"""
        qt_img = self.convert_cv_qt(cv_image)
        scaled_img = qt_img.scaled(label.width(), label.height(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        label.setPixmap(scaled_img)

    def get_image(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Open Image", "", "Images (*.png *.jpg *.jpeg)")
        if file_path:
            self.img = cv2.imread(file_path)
            self.display_scaled_image(self.img, self.OriginalImg)
            self.showDimensions()

    def showRedChannel(self):
        if self.img is not None:
            red_img = self.img.copy()
            red_img[:, :, 0] = 0
            red_img[:, :, 1] = 0
            self.display_scaled_image(red_img, self.RedChannel)

    def showGreenChannel(self):
        if self.img is not None:
            green_img = self.img.copy()
            green_img[:, :, 0] = 0
            green_img[:, :, 2] = 0
            self.display_scaled_image(green_img, self.GreenChannel)

    def showBlueChannel(self):
        if self.img is not None:
            blue_img = self.img.copy()
            blue_img[:, :, 1] = 0
            blue_img[:, :, 2] = 0
            self.display_scaled_image(blue_img, self.BlueChannel)

    def show_HistColor(self):
        if self.img is not None:
            plt.figure()
            colors = ('b', 'g', 'r')
            for i, col in enumerate(colors):
                hist = cv2.calcHist([self.img], [i], None, [256], [0, 256])
                plt.plot(hist, color=col)
            plt.savefig("Color_Histogram.png")
            plt.close()
            pixmap = QPixmap("Color_Histogram.png")
            scaled_pixmap = pixmap.scaled(self.ColorHist.width(), self.ColorHist.height(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.ColorHist.setPixmap(scaled_pixmap)

    def getContrast(self):
        # Reads the contrast from your UI input box (e.g. 1.2)
        try:
            return float(self.Contrast.text())
        except (ValueError, AttributeError):
            return 1.2

    def getBrightness(self):
        # Reads the brightness from your UI input box (e.g. 10)
        try:
            return int(self.Brightness.text())
        except (ValueError, AttributeError):
            return 10

    def show_UpdatedImgGray(self):
        if self.img is not None:
            alpha = self.getContrast()
            beta = self.getBrightness()
            self.Contrast.setText(str(round(alpha, 2)))
            self.Brillance.setText(str(round(beta, 2)))
            img_gray = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
            self.imgUpdated = cv2.convertScaleAbs(img_gray, alpha=alpha, beta=beta)
            self.display_scaled_image(self.imgUpdated, self.GrayImg)

    def calc_HistGray(self):
        if self.imgUpdated is not None:
            return cv2.calcHist([self.imgUpdated], [0], None, [256], [0, 256])
        return None

    def show_HistGray(self):
        hist = self.calc_HistGray()
        if hist is not None:
            plt.figure()
            plt.plot(hist, color='black')
            plt.savefig("Gray_Histogram.png")
            plt.close()
            pixmap = QPixmap("Gray_Histogram.png")
            scaled_pixmap = pixmap.scaled(self.GrayHist.width(), self.GrayHist.height(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.GrayHist.setPixmap(scaled_pixmap)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = DesignWindow()
    window.show()
    sys.exit(app.exec_())