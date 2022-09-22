import pyowm

print('Введите город в формате: "Name, Country", пример: "London,GB"')
owm = pyowm.OWM('97d41801b2dbcbdcb3830771abab2e98')
inputDialog = input()
try:
    yar = owm.weather_manager().weather_at_place(inputDialog)
    # не так, если ключ ["temp"] не существует, то упадет в ошибку
    # yarWeather = yar.weather.temperature('celsius')["temp"]
    # а тут. если нет, то будет тупо 0
    yarWeather = yar.weather.temperature('celsius').get("temp", 0)
    result = f"City: {inputDialog}  Weather: {yarWeather}"
except:
    result = "Вы ввели неправильный формат города!"
print(result)


