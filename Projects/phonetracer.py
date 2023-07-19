import phonenumbers
from phonenumbers import timezone, geocoder, carrier
number = input("Enter your number with +91 : ")
x = str(number)
phone = phonenumbers.parse(x)
time = timezone.time_zones_for_number(x)
carr = carrier.name_for_number(phone, "en")
reg = geocoder.description_for_number(phone, "en")
print(phone)
print(time)
print(carr)
print(reg)