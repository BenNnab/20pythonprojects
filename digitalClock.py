import sys
from PyQt5.QtWidgets import QApplication, QLCDNumber, QWidget, QVBoxLayout
from PyQt5.QtCore import QTimer, QTime, Qt

class DigitalClock(QWidget):
    def __init__(self):
        super().__init__()

        # Set up the clock display
        self.lcd = QLCDNumber(self)
        self.lcd.setDigitCount(11)  # Increase digit count to accommodate AM/PM
        self.lcd.setSegmentStyle(QLCDNumber.Flat)
        self.lcd.setStyleSheet("background-color: black; color: green;")
        self.lcd.setFixedSize(400, 100)

        # Set up the layout
        layout = QVBoxLayout()
        layout.addWidget(self.lcd)
        self.setLayout(layout)

        # Set up the timer to update the time every second
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)

        # Show the initial time
        self.showTime()

        # Configure the window
        self.setWindowTitle('Digital Clock')
        self.setGeometry(100, 100, 400, 100)
        self.show()

    def showTime(self):
        current_time = QTime.currentTime()
        if current_time.hour() > 12:
            formatted_time = current_time.toString('hh:mm:ss') + ' PM'
        elif current_time.hour() == 12:
            formatted_time = current_time.toString('hh:mm:ss') + ' PM'
        else:
            formatted_time = current_time.toString('hh:mm:ss') + ' AM'
        self.lcd.display(formatted_time)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    clock = DigitalClock()
    sys.exit(app.exec_())
