import geocoder
import requests

# Replace XXXXXXXXXXXXXXXXXX with your actual key, which
# will look like a bunch of letters and numbers!
API_KEY = 'XXXXXXXXXXXXXXXXXX'
# When you are done with the homework, remove your actual key
# and replace it back with XXXXXXXXXXXXXXXXXX before you commit
# and push to Github.

API_BASE_URL = f'https://api.darksky.net/forecast/{API_KEY}/'

def main():
    destinations = ['Space Needle', 'Crater Lake', 'Golden Gate Bridge', 'Yosemite National Park', 'Las Vegas, Nevada', 'Grand Canyon National Park', 'Aspen, Colorado', 'Mount Rushmore', 'Yellowstone National Park', 'Sandpoint, Idaho', 'Banff National Park', 'Capilano Suspension Bridge']
    degree_sign= u'\N{DEGREE SIGN}'
    # Loop through each destination
    for destination in destinations:
        ###########
        # COPY & PASTE RELEVANT CODE FROM PART 1 HERE
        ###########
        location = geocoder.arcgis(destination)
        my_float = location.latlng
        # You'll need to construct the full API url with the latitude and longitude,
        # with something like this:
        # full_api_url = API_BASE_URL + latitude + ',' + longitude
        full_api_url = API_BASE_URL + str(my_float[0])+','+str(my_float[1])
        result = requests.request('GET', full_api_url).json()

        # From the result, print out the summary and current temperature
        
        print(f'{destination} \n is located at ({my_float[0]:.4f}, {my_float[1]:.4f})')
        print(f"At the {destination} \n  right now, it's {result['currently']['summary']} with a temprature of {result['currently']['temperature']:.1f}{degree_sign}F")


main()
