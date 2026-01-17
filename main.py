import phonenumbers
from myphone import number
from phonenumbers import geocoder, carrier
from opencage.geocoder import OpenCageGeocode

# 1. Phone number details nikalna
pepnumber = phonenumbers.parse(number)
location = geocoder.description_for_number(pepnumber, "en")
print("Location: ", location)

service_pro = carrier.name_for_number(pepnumber, "en")
print("Service Provider: ", service_pro)

# 2. OpenCage se Exact Map Location nikalna
# Yahan apni API Key quotes (" ") ke andar likhein
key = "APKI_OPENCAGE_API_KEY_YAHAN_DAALEIN" 

geocoder_osm = OpenCageGeocode(key)
query = str(location)
results = geocoder_osm.geocode(query)

# Result print karein
if results:
    lat = results[0]['geometry']['lat']
    lng = results[0]['geometry']['lng']
    print(f"Latitude: {lat}, Longitude: {lng}")
else:
    print("Location nahi mili")