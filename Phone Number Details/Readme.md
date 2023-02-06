# Phone Number Details Extraction

In this project we will take any number from user as input perameter and after that we will provide details of that given phone number.

### Required Modules

1. phonenumbers
2. carrier
3. geocoder
4. timezone

### Working
We import modules from phonenumbers module
1. phonenumber.parse(number) : for info about phone number.
2. timezone.time_zones_for_number(number_details) : (Continent/City)
3. carrier.name_for_number(number_details,"en") : Name of service provider.
4. geocoder.description_for_number(number_details,"en") : City of registration and State of registration.