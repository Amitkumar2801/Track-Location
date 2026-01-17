import phonenumbers
import opencage


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

from phonenumbers import carrier
service_pro = phonenumbers.parse(number)
print(carrier.name_for_number(service_pro, "en"))

from opencage.geocoder import opencage opencagegeocode

