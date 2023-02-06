import phonenumbers
from phonenumbers import carrier,geocoder,timezone

number = input("Enter the number in this format [+________]:")
number_details = phonenumbers.parse(number)
number_timezone = timezone.time_zones_for_number(number_details)
number_carrier = carrier.name_for_number(number_details,"en")
number_region = geocoder.description_for_number(number_details,"en")

print(f"Details : {number_details}")
print(f"Timezone : {number_timezone}")
print(f"Carrier : {number_carrier}")
print(f"Region : {number_region}")