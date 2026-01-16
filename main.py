import phonenumbers
from myphone import number
from phonenumbers import geocoder, carrier

# 1. Number ko parse karna
pepnumber = phonenumbers.parse(number)

# 2. Location nikalna
location = geocoder.description_for_number(pepnumber, "en")
print("Location: ", location)

# 3. Service Provider nikalna
service_pro = carrier.name_for_number(pepnumber, "en")
print("Service Provider: ", service_pro)