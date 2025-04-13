from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(801, 541)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(180, 70, 431, 121))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label.setStyleSheet("background-color: rgb(128, 128, 128); color: rgb(0, 0, 0);")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(180, 210, 81, 16))
        self.label_2.setFont(QtGui.QFont("", 6))
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(180, 280, 131, 16))
        self.label_3.setFont(QtGui.QFont("", 6))
        self.label_3.setObjectName("label_3")

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(180, 350, 91, 16))
        self.label_4.setFont(QtGui.QFont("", 6))
        self.label_4.setObjectName("label_4")

        self.horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider.setGeometry(QtCore.QRect(280, 210, 331, 22))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setMinimum(20)
        self.horizontalSlider.setMaximum(60)
        self.horizontalSlider.setValue(40)
        self.horizontalSlider.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.horizontalSlider.setTickInterval(5)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.horizontalSlider.valueChanged.connect(self.change_font_size)

        self.horizontalSlider_2 = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_2.setGeometry(QtCore.QRect(330, 280, 281, 22))
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setMinimum(0)
        self.horizontalSlider_2.setMaximum(255)
        self.horizontalSlider_2.setValue(128)
        self.horizontalSlider_2.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.horizontalSlider_2.setTickInterval(20)
        self.horizontalSlider_2.setObjectName("horizontalSlider_2")
        self.horizontalSlider_2.valueChanged.connect(self.change_background_color)

        self.horizontalSlider_3 = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_3.setGeometry(QtCore.QRect(280, 350, 331, 22))
        self.horizontalSlider_3.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_3.setMinimum(0)
        self.horizontalSlider_3.setMaximum(255)
        self.horizontalSlider_3.setValue(0)
        self.horizontalSlider_3.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.horizontalSlider_3.setTickInterval(20)
        self.horizontalSlider_3.setObjectName("horizontalSlider_3")
        self.horizontalSlider_3.valueChanged.connect(self.change_font_color)

        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(160, 400, 461, 41))
        self.label_5.setFont(QtGui.QFont("", 6))
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 801, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def change_font_size(self, value):
        font = self.label.font()
        font.setPointSize(value)
        self.label.setFont(font)

    def change_background_color(self, value):
        current_font_color = self.horizontalSlider_3.value()
        self.label.setStyleSheet(
            f"background-color: rgb({value},{value},{value}); color: rgb({current_font_color},{current_font_color},{current_font_color});"
        )

    def change_font_color(self, value):
        current_bg_color = self.horizontalSlider_2.value()
        self.label.setStyleSheet(
            f"background-color: rgb({current_bg_color},{current_bg_color},{current_bg_color}); color: rgb({value},{value},{value});"
        )

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Font Size and Color Adjuster"))
        self.label.setText(_translate("MainWindow", "F1D022120"))
        self.label_2.setText(_translate("MainWindow", "Font Size"))
        self.label_3.setText(_translate("MainWindow", "Background Color"))
        self.label_4.setText(_translate("MainWindow", "Font Color"))
        self.label_5.setText(_translate("MainWindow", "Created By : Fernandao Kwangtama Tekayadi (F1D022120)"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
