import sys
import requests
from PyQt5.QtWidgets import QApplication, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget

class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.city_label = QLabel('Enter City:', self)
        self.city_input = QLineEdit(self)
        self.result_label = QLabel('', self)
        self.check_button = QPushButton('Check Weather', self)
        self.check_button.clicked.connect(self.show_weather)

        layout = QVBoxLayout()
        layout.addWidget(self.city_label)
        layout.addWidget(self.city_input)
        layout.addWidget(self.check_button)
        layout.addWidget(self.result_label)
        
        self.setLayout(layout)
        
        self.setWindowTitle('Weather App')
        self.setGeometry(100, 100, 300, 200)
        self.show()

    def show_weather(self):
        city = self.city_input.text()
        api_key = 'a612970492c12da59df651119d8c89bd'  # Replace with your OpenWeatherMap API key
        base_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
        
        try:
            response = requests.get(base_url)
            data = response.json()

            if data['cod'] == 200:
                weather_description = data['weather'][0]['description']
                temperature = data['main']['temp']
                self.result_label.setText(f'Weather: {weather_description}\nTemperature: {temperature}°C')
            else:
                self.result_label.setText('City not found.')
        except Exception as e:
            self.result_label.setText('Error fetching data.')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    sys.exit(app.exec_())
