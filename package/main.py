# animal package -> 폴더의 이름이 package의 이름
#dog, cat Module
#dog, cat modules can say "hi"
# package가 package임을 말하기 위해선 __init__.py가 필요
"""
from animal import dog #animal 패키지에서 dog라는 모듈을 갖고와줘
from animal import cat #animal 패키지에서 cat라는 모듈을 갖고와줘

#from animal import * #animal에서 갖고 있는 모든 모듈을 다 불러옴

d = dog.Dog()
c = cat.Cat()
#d = Dog()
#c = Cat()
d.hi()
c.hi()
"""
from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="wonie")
location = geolocator.geocode("seoul, south Korea")
print(location.address)
print((location.longitude, location.latitude))
