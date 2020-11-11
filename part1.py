import geocoder

def main():
    # Declare destinations list here
    destinations = ['Space Needle', 'Crater Lake', 'Golden Gate Bridge', 'Yosemite National Park', 'Las Vegas, Nevada', 'Grand Canyon National Park', 'Aspen, Colorado', 'Mount Rushmore', 'Yellowstone National Park', 'Sandpoint, Idaho', 'Banff National Park', 'Capilano Suspension Bridge']
    
    # Loop through each destination
    for destination in destinations:
        location = geocoder.arcgis(destination)
        my_float = location.latlng
        print(f'{destination} is located at ({my_float[0]:.4f}, {my_float[1]:.4f})')
        #   Get the lat-long coordinates from `geocoder.arcgis`
        #   Print out the place name and the coordinates

main()
