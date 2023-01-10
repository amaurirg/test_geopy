from geopy.geocoders import Nominatim


location = Nominatim(user_agent="GetLoc")
locname = location.reverse("70.60050201416, 29.691400527954")
print(locname.address)
