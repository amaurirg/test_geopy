from geopy.geocoders import Nominatim


loc = Nominatim(user_agent="GetLoc")
location = loc.geocode("Aeroporto Brigadeiro Camarão Vilhena")
print(location.address)
print("Latitude = ", location.latitude)
print("Longitude = ", location.longitude)
