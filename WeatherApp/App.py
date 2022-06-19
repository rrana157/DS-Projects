import sys, platform
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from HomePage import Ui_SplashScreen ## ==> Home Page Window
from WeatherPage import Ui_MainWindow ## ==> Main Page Window
from PyQt5.QtGui import QColor
from WeatherModule import getWeather
from LoggerModule import logger

## ==> Global
counter = 0

# Application Screen
class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.search_pushButton.clicked.connect(self.GetUInput)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

    def GetUInput(self):
        """
        This Function will get the location as an input from user and fetched the weather information based on that.
        """
        try:
            u_input = self.ui.search_lineEdit.text()
            self.weather_data = getWeather(u_input)
            self.weather_result = self.weather_data.weather()
            self.air_result = self.weather_data.airQuality()
            self.ui.search_lineEdit.setText("")
            self.ui.Location_text_label.setText(str((self.weather_result[1])))
            self.ui.country_text_label.setText(str((self.weather_result[0])))
            self.ui.sunrise_text_label.setText((str(self.weather_result[2]) + ' am'))
            self.ui.sunset_text_label.setText((str(self.weather_result[3]) + ' pm'))
            self.ui.temp_text_label.setText((str(self.weather_result[4]) + '°'))
            self.ui.l_temp_text_label.setText('L: ' + (str(self.weather_result[5]) + '°'))
            self.ui.h_temp_text_label.setText('H: ' + (str(self.weather_result[6]) + '°'))
            self.ui.temp_feellike_text_label.setText('Feel like: ' + (str(self.weather_result[7]) + '°'))
            self.ui.pressure_text_label.setText((str(self.weather_result[9]) + ' hPa'))
            self.ui.humidity_text_label.setText((str(self.weather_result[10]) + '%'))
            self.ui.visibility_text_label.setText((str(self.weather_result[11]/1000) + ' Km'))
            self.ui.wind_text_label.setText((str(self.weather_result[12]) + ' kph'))

            # Air Quality label

            self.ui.AQI_text_label.setText(self.air_result[0])
            self.ui.CO_text_label.setText('CO ' + str(self.air_result[1]))
            self.ui.NO_text_label.setText('NO ' + str(self.air_result[2]))
            self.ui.NO2_text_label.setText('NO2 ' + str(self.air_result[3]))
            self.ui.O3_text_label.setText('O3 ' + str(self.air_result[4]))
            self.ui.SO2_text_label.setText('SO2 ' + str(self.air_result[5]))
            self.ui.PM25_text_label.setText('PM25 ' + str(self.air_result[6]))

            return self.weather_result
        except Exception as e:
            logger.error("Error has occurred.")  # STORING THE ERROR AND EXCEPTION INTO LOG FILE.
            logger.exception("Exception occurred" + str(e))

# Home Screen
class SplashScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)

        ## Removing the title bar
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        ## Drop shadow effect
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.ui.DropShadowFrame.setGraphicsEffect(self.shadow)

        ## Qtimer ==> Start
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        ## Timer in milliseconds
        self.timer.start(50)

        # Change the Description
        self.ui.label_description.setText("<strong>Welcome</strong> To My Application")
        QtCore.QTimer.singleShot(1500,lambda: self.ui.label_description.setText("<strong>Loading</strong> DATABASE"))
        QtCore.QTimer.singleShot(3000,lambda: self.ui.label_description.setText("<strong>Loading</strong> USER INTERFACE"))

        ## Show ==> Main Windows
        self.show()

    ## ==> App Functions

    def progress(self):
        """
        This function run the progress bar till the counter is less than or equal to 100 Milliseconds.
        """
        global counter
        # set value to progress bar
        self.ui.progressBar.setValue(counter)
        # close splash screen and open the main window
        if counter > 100:
            # Stop Timer
            self.timer.stop()
            self.main = MainWindow()
            self.main.show()
            # Close Home Screen
            self.close()

        # Increase the counter
        counter += 1


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SplashScreen()
    sys.exit(app.exec_())
