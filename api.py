import pyowm

owm = pyowm.OWM("c5ee9c50723ce0c97892e4fd6ef2caef")
observation = owm.weather_at_place("Cape Coast, Ghana")
observation2 = owm.weather_at_place("Koforidua, Ghana")
w = observation.get_weather()
w2 = observation2.get_weather()

print(w2.get_wind()['deg'])
print(w.get_humidity())
print(w.get_temperature()['temp'])