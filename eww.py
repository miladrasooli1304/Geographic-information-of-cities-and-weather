import requests
import time
import sqlite3



def sql_connect():
    con = sqlite3.connect('weather.db')
    cur = con.cursor()
    return con,cur


def create_table(con,cur):
    cur.execute("CREATE TABLE IF NOT EXISTS weather(city_name TEXT,temp REAL,humidity REAL,country TEXT,time TEXT)")
    con.commit()



def insert_data(con,cur,data):
    cur.execute("INSERT INTO weather VALUES(?,?,?,?,?)",tuple([v for k,v in data.items()]))
    con.commit()

def proccess_data(data):
    return {'city name':data['name'],'temp':data['main']['temp'],'humidity':data['main']['humidity'],'country':data['sys']['country'],'time':time.ctime(int(data["dt"]))}







def get_weather_data(city='Tabriz' ,kye_code='dc2c011fcfce8e9dce9e786edddb990a'):
    URL = "https://api.openweathermap.org/data/2.5/weather"

    PARAMS = {'q':city,'appid':kye_code}
    r = requests.get(url = URL, params = PARAMS)
    return proccess_data(r.json())

n = input("enter the name of the city : ")
data ={'coord': {'lon': 51.4215, 'lat': 35.6944}, 'weather': [{'id': 701, 'main': 'Mist', 'description': 'mist', 'icon': '50n'}], 'base': 'stations', 'main': {'temp': 279.84, 'feels_like': 278.43, 'temp_min': 277.74, 'temp_max': 280.14, 'pressure': 1012, 'humidity': 81}, 'visibility': 5000, 'wind': {'speed': 2.06, 'deg': 90}, 'clouds': {'all': 100}, 'dt': 1646679292, 'sys': {'type': 2, 'id': 47737, 'country': 'IR', 'sunrise': 1646621813, 'sunset': 1646663654}, 'timezone': 12600, 'id': 112931, 'name': 'Tehran', 'cod': 200}

con,cur = sql_connect()
create_table(con,cur)
while True: 
    print(get_weather_data(n))
    time.sleep(5)
    print("\n",'\n')
