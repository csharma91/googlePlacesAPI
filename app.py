from googleplaces import GooglePlaces, types, lang
import secrets

from requests import get
import requests
import random

import requests

from selenium import webdriver
url = 'https://techcrunch.com/'
driver = webdriver.Chrome()
driver.get(url)
cookies_list = driver.get_cookies()
print(driver.get_cookies())
cookies_dict = {}
for cookie in cookies_list:
    print(cookie)
    cookies_dict[cookie['name']] = cookie['value']



# r = requests.post(url, headers = headers)
# print(r.cookies)

# for cookie in r.cookies:
#     print(cookie.__dict__)
#     print(cookie.secure)

# response = get(url, headers=headers)
# response.raise_for_status()
# print(response.cookies)



def getPlacesData():
    #https://github.com/slimkrazy/python-google-places
    YOUR_API_KEY = secrets.apiKeys['api']

    google_places = GooglePlaces(YOUR_API_KEY)

    # You may prefer to use the text_search API, instead.
    query_result = google_places.nearby_search(lat_lng = {'lat':'51.0523034', "lng":'-114.0767356'}, keyword='dentist',
            radius=100) #, types=[types.TYPE_FOOD])


    if query_result.has_attributions:
        print(query_result.html_attributions)


    for place in query_result.places:
        # Returned places from a query are place summaries.
        print ('****************************')
        print( place.name)
        print( place.geo_location)
        print( place.place_id)

        # The following method has to make a further API call.
        place.get_details()
        # Referencing any of the attributes below, prior to making a call to
        # get_details() will raise a googleplaces.GooglePlacesAttributeError.
        print( place.details) # A dict matching the JSON response from Google.
        print( place.local_phone_number)
        print( place.international_phone_number)
        print( place.website)
        print( place.url)

