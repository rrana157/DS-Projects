
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SplashScreen(object):
    def setupUi(self, SplashScreen):
        SplashScreen.setObjectName("SplashScreen")
        SplashScreen.resize(680, 400)
        self.centralwidget = QtWidgets.QWidget(SplashScreen)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.DropShadowFrame = QtWidgets.QFrame(self.centralwidget)
        self.DropShadowFrame.setStyleSheet("QFrame{\n"
"background-color:rgb(12,177,242);\n"
"color:rgb(12,177,242);\n"
"border-radius: 10px;\n"
"\n"
"}")
        self.DropShadowFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.DropShadowFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.DropShadowFrame.setObjectName("DropShadowFrame")
        self.label_title = QtWidgets.QLabel(self.DropShadowFrame)
        self.label_title.setGeometry(QtCore.QRect(0, 100, 651, 91))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(40)
        font.setBold(False)
        font.setWeight(50)
        self.label_title.setFont(font)
        self.label_title.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_title.setObjectName("label_title")
        self.label_description = QtWidgets.QLabel(self.DropShadowFrame)
        self.label_description.setGeometry(QtCore.QRect(10, 190, 651, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_description.setFont(font)
        self.label_description.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_description.setAlignment(QtCore.Qt.AlignCenter)
        self.label_description.setObjectName("label_description")
        self.progressBar = QtWidgets.QProgressBar(self.DropShadowFrame)
        self.progressBar.setGeometry(QtCore.QRect(50, 260, 551, 24))
        self.progressBar.setStyleSheet("QProgressBar{\n"
"background-color:rgb(217,217,217);\n"
"color:rgb(13,13,13);\n"
"border-style: none;\n"
"border-radius:10px;\n"
"text-align: center;\n"
"}\n"
"\n"
"QProgressBar::chunk{\n"
"border-radius:10px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.511364, x2:1, y2:0.523,\n"
" stop:0 rgba(12,177,242), stop:1 rgba(5,242,219));\n"
"}")
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.label_loading = QtWidgets.QLabel(self.DropShadowFrame)
        self.label_loading.setGeometry(QtCore.QRect(0, 290, 651, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_loading.setFont(font)
        self.label_loading.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_loading.setAlignment(QtCore.Qt.AlignCenter)
        self.label_loading.setObjectName("label_loading")
        self.label_credits = QtWidgets.QLabel(self.DropShadowFrame)
        self.label_credits.setGeometry(QtCore.QRect(0, 350, 651, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.label_credits.setFont(font)
        self.label_credits.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_credits.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_credits.setObjectName("label_credits")
        self.verticalLayout.addWidget(self.DropShadowFrame)
        SplashScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(SplashScreen)
        QtCore.QMetaObject.connectSlotsByName(SplashScreen)

    def retranslateUi(self, SplashScreen):
        _translate = QtCore.QCoreApplication.translate
        SplashScreen.setWindowTitle(_translate("SplashScreen", "MainWindow"))
        self.label_title.setText(_translate("SplashScreen", "<html><head/><body><p><span style=\" font-weight:600;\">Weather App</span></p></body></html>"))
        self.label_description.setText(_translate("SplashScreen", "<html><head/><body><p><span style=\" font-weight:600;\">This App will give you the weather update of the selected location.</span></p></body></html>"))
        self.label_loading.setText(_translate("SplashScreen", "<html><head/><body><p><span style=\" font-weight:600;\">loading...</span></p></body></html>"))
        self.label_credits.setText(_translate("SplashScreen", "<strong>Developed by:</strong> Ravender Singh Rana"))
