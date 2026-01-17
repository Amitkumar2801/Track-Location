import phonenumbers
from myphone import number
from phonenumbers import geocoder, carrier

from opencage.geocoder import OpenCageGeocode # Line 4: Sahi spelling ke saath

# 1. Phone details
pepnumber = phonenumbers.parse(number)
location = geocoder.description_for_number(pepnumber, "en")
print("Location: ", location)

# 2. OpenCage Setup
key = "APNI_API_KEY_YAHAN_DALO" # Dashboard se copy karke yahan paste karein
coder = OpenCageGeocode(key)
query = str(location)
results = coder.geocode(query)

# Latitude aur Longitude nikalna
lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']
print(lat, lng)