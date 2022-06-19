
# Weather App

Weatherapp is a simple weather forecast app, which uses some APIs 
to fetch 5 day / 3 hour forecast data from the OpenWeatherMap 
and to fetch places,cities,counties,coords etc. from Algolia Places. The main goal of this app is to be a sample of how to build an high quality Android application that uses the Architecture components, Hilt etc. in Kotlin.


## Acknowledgements

 - [Get the inspiration](https://www.youtube.com/watch?v=Zh2eCvIdDdw)
 - [Awesome Python GUI](https://www.youtube.com/c/WandersonIsMe)
 

## App Screenshots

![Loading Page](https://github.com/rrana157/DS-Projects/blob/main/WeatherApp/Screenshots/LoadingPage.png?raw=true)

![Home Page](https://github.com/rrana157/DS-Projects/blob/main/WeatherApp/Screenshots/MainPage.png?raw=true)

![Result Page](https://github.com/rrana157/DS-Projects/blob/main/WeatherApp/Screenshots/ResultPage.png?raw=true)

## API Reference

#### Weather API

```http
  https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `city name` | `string` | **Required**. Your city name is required.
|`API KEY` | `string` | **Required**. Your unique API key (you can always find it on your account page under the "API key" tab).

#### Air Quality API

```http
  http://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={API key}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `lat, lon`      | `string` | **Required**. Geographical coordinates (latitude, longitude).
|`API KEY` | `string` | **Required**. Your unique API key (you can always find it on your account page under the "API key" tab).


#### Example for Weather API
https://api.openweathermap.org/data/2.5/weather?q=London&appid={API key}

{
     "coord": {
       "lon": -0.13,
       "lat": 51.51
     },
     "weather": [
       {
         "id": 300,
         "main": "Drizzle",
         "description": "light intensity drizzle",
         "icon": "09d"
       }
     ],
     "base": "stations",
     "main": {
       "temp": 280.32,
       "pressure": 1012,
       "humidity": 81,
       "temp_min": 279.15,
       "temp_max": 281.15
     },
     "visibility": 10000,
     "wind": {
       "speed": 4.1,
       "deg": 80
     },
     "clouds": {
       "all": 90
     },
     "dt": 1485789600,
     "sys": {
       "type": 1,
       "id": 5091,
       "message": 0.0103,
       "country": "GB",
       "sunrise": 1485762037,
       "sunset": 1485794875
     },
     "id": 2643743,
     "name": "London",
     "cod": 200
     }

#### Example for Air Quality API

http://api.openweathermap.org/data/2.5/air_pollution/forecast?lat=50&lon=50&appid={API key}

{
  "coord":[
    50,
    50
  ],
  "list":[
    {
      "dt":1605182400,
      "main":{
        "aqi":1
      },
      "components":{
        "co":201.94053649902344,
        "no":0.01877197064459324,
        "no2":0.7711350917816162,
        "o3":68.66455078125,
        "so2":0.6407499313354492,
        "pm2_5":0.5,
        "pm10":0.540438711643219,
        "nh3":0.12369127571582794
      }
    }
  ]
}
  

## Authors

- [Ravender Singh Rana](https://github.com/rrana157)


## 🚀 About Me
I'm a Report Developer. And A passionate aspiring Data Scientist.


# Hi, I'm Ravender Singh Rana! 👋


## 🔗 Links
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/ravender-singh-rana-ba947897/)
[![github](https://img.shields.io/badge/github-1DA1F2?style=for-the-badge&logo=github&logoColor=white)](https://github.com/rrana157)


## License

[MIT](https://choosealicense.com/licenses/mit/)

Copyright (c) 2022 Ravender Singh Rana

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

- The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
- The Software is Provided "AS IS" Without Warranty of Any Kind, Express or implied, including But Not Limited To The Warranties Of Merchantability, fitness For A Particular Purpose And Non Infringement. In No Event Shall The Authors Or Copyright Holders Be Liable For Any Claim Damages Or Other liability Whether In An Action Of Contract TORT Or Otherwise Arising From, out Of Or In Connection With The Software Or The Use Or Other Dealings In The software.
