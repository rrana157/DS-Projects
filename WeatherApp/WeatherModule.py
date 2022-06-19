import requests
from datetime import datetime
from LoggerModule import logger
from geopy.geocoders import Nominatim


class getWeather:
    def __init__(self, city='Delhi'):
        self.city = city

    def weather(self):
        """
        This function will take city as an argument and return the weather details as an return.
        """
        try:
            self.base_url = "https://api.openweathermap.org/data/2.5/weather?&q={}&appid={}"  # Weather URL

            self.file = open("key.txt", "r")                            # Fetching API KEY
            self.api_key = self.file.read()                             # Reading the API KEY AND STORING INTO VARIABLE
            self. result = requests.get(self.base_url.format(self.city,
                                                  self.api_key))       # Reading the API DATA AND STORING INTO VARIABLE

            if self.result:
                self.json = self.result.json()
                self.city = self.json['name']
                self.unix_timestamp_rise = self.json['sys']['sunrise']
                self.unix_timestamp_set = self.json['sys']['sunset']
                self.datetime_obj_rise = datetime.fromtimestamp(int(self.unix_timestamp_rise))
                self.datetime_obj_set = datetime.fromtimestamp(int(self.unix_timestamp_set))
                self.sunrise = self.datetime_obj_rise.strftime("%H:%M:%S")
                self.sunset = self.datetime_obj_set.strftime("%H:%M:%S")
                self.country = self.json['sys']['country']
                self.temp_kelvin = self.json['main']['temp']
                self.min_kelvin = self.json['main']['temp_min']
                self.max_kelvin = self.json['main']['temp_max']
                self.feels_like_kelvin = self.json['main']['feels_like']
                self.temp_celsius = round((self.temp_kelvin - 273.15))
                self.temp_min_kelvin = round((self.min_kelvin - 273.15))
                self.temp_max_kelvin = round((self.max_kelvin - 273.15))
                self.temp_feels_like_kelvin = round(self.feels_like_kelvin - 273.15)
                self.temp_fahrenheit = round((self.temp_kelvin-273.15) * 9 / 5 + 32,2)
                self.pressure = self.json['main']['pressure']
                self.humidity = self.json['main']['humidity']
                self.visibility = self.json['visibility']
                self.wind_speed = self.json['wind']['speed']
                self.weathers = self.json['weather'][0]['main']
                self.clouds = self.json['clouds']
                keys = []
                for i in self.clouds.keys():
                    keys.append(i)

                final = (self.country, self.city, self.sunrise, self.sunset, self.temp_celsius, self.temp_min_kelvin,
                         self.temp_max_kelvin,self.temp_feels_like_kelvin, self.temp_fahrenheit, self.pressure,
                         self.humidity, self.visibility, self.wind_speed, self.weathers,keys[0])
                return final
            else:
                return None

        except Exception as e:
            logger.error("Error has occurred.")                            # STORING THE ERROR AND EXCEPTION INTO LOG FILE.
            logger.exception("Exception occurred" + str(e))

    def airQuality(self):
        """
        This function will take city as an argument and return the air quality details as a return.
        """
        try:
            self.loc = Nominatim(user_agent='Getoc')
            self.getloc = self.loc.geocode(self.city)
            self.get_lat = self.getloc.latitude
            self.get_long = self.getloc.longitude
            self.base_url = "http://api.openweathermap.org/data/2.5/air_pollution?lat={}&lon={}&appid={}"# AIR QUALITY URL

            self.file = open("key.txt", "r")                            # Fetching API KEY
            self.api_key = self.file.read()                             # Reading the API KEY AND STORING INTO VARIABLE
            self.result = requests.get(self.base_url.format(self.get_lat,
                                                  self.get_long,
                                                  self.api_key))       # Reading the API DATA AND STORING INTO VARIABLE

            if self.result:
                self.data = self.result.json()
                self.AQI = self.data['list'][0]['main']['aqi']
                self.CO = self.data['list'][0]['components']['co']
                self.NO = self.data['list'][0]['components']['no']
                self.NO2 = self.data['list'][0]['components']['no2']
                self.O3 = self.data['list'][0]['components']['o3']
                self.SO2 = self.data['list'][0]['components']['so2']
                self.PM2_5 = self.data['list'][0]['components']['pm2_5']
                self.PM10 = self.data['list'][0]['components']['pm10']
                self.NH3 = self.data['list'][0]['components']['nh3']

                AQI_STATUS = []
                for i in range(6):
                    if i == self.AQI:
                        if i == 5:
                            AQI_STATUS.append(str("Very Poor"))
                        elif i == 4:
                            AQI_STATUS.append(str("Poor"))
                        elif i == 3:
                            AQI_STATUS.append(str("Moderate"))
                        elif i == 2:
                            AQI_STATUS.append(str("Fair"))
                        else:
                            AQI_STATUS.append(str("Good"))

                return (AQI_STATUS[0], str(self.CO), str(self.NO), str(self.NO2), str(self.O3), str(self.SO2),
                        str(self.PM2_5), str(self.PM10) + str(' µg/m³'), str(self.NH3) + str(' µg/m³'))
            else:
                return None
        except Exception as e:
            logger.error("Error has occurred.")                        # STORING THE ERROR AND EXCEPTION INTO LOG FILE.
            logger.exception("Exception occurred" + str(e))


"""Weather ('IN', 'Delhi', '05:23:12', '19:21:12', 31, 30, 31, 37, 87.73, 1004, 70, 1500, 2.57, 'Haze', 'all')"""

""" Air Quality [{'main': {'aqi': 4}, 'components': {'co': 560.76, 'no': 0.77, 'no2': 9.17, 'o3': 158.79, 'so2': 18.84, 
'pm2_5': 37.99, 'pm10': 47.18, 'nh3': 5}, 'dt': 1655629200}]"""

