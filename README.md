# Assignment: APIs

In this assignment, you'll practice:

* Including and using modules and packages
* Using data from APIs
* Reading documentation for modules and APIs

## Deliverables and Submitting

The usual!

---

# Part 1: Geo Cody

Cody and his friends Heather and Matt are going on a road trip across the Western United States and Canada. They want to visit several landmarks, national parks, and big cities.

Here's their agenda:

```
Space Needle
Crater Lake
Golden Gate Bridge
Yosemite National Park
Las Vegas, Nevada
Grand Canyon National Park
Aspen, Colorado
Mount Rushmore
Yellowstone National Park
Sandpoint, Idaho
Banff National Park
Capilano Suspension Bridge
```

Your job is to put these destinations into a list of strings called `destinations`. Then, import the [geocoder](https://geocoder.readthedocs.io/providers/ArcGIS.html#geocoding) module, and use it to translate each of the landmarks into latitude-longitude coordinates.

Loop through the list, and print each location's latitude and longitude.

We will be using `arcgis` service to translate the places to coordinates, which is directly usable via the `geocoder` module. The `geocoder` module is a *wrapper* that wraps the functionality of the `arcgis` service (among others) so you don't have to do it manually.

Visit the [docs](https://geocoder.readthedocs.io) for more sample code.

## Sample Code: `geocoder`

```python
import geocoder
location = geocoder.arcgis('Redlands, CA')
print(location.latlng) # latlng is a list with a length of 2
```

**Hint:** This follows the pattern in the `geonames` example in the [docs](https://geocoder.readthedocs.io/results.html). The only difference is using the `arcgis` provider instead of the `geonames` provider.

## Sample Code: Decimal Places Display

If you'd like to truncate the display of floating point numbers, you can specify exactly how many digits you want after the period using `f`-strings:

```python
my_float = 1.23456789
print(f'{my_float}')     #--> 1.23456789
print(f'{my_float:.2f}') #--> 1.23 (2 decimal places)
print(f'{my_float:.4f}') #--> 1.2345 (4 decimal places)
```

## Starter Code

Some starter code is already in the file `part1.py`. Continue your implementation there.

## Expected Output

```
Space Needle is located at (47.6205, -122.3493)
Crater Lake is located at (42.8684, -122.1685)
Golden Gate Bridge is located at (37.8199, -122.4783)
Yosemite National Park is located at (37.8651, -119.5383)
Las Vegas, Nevada is located at (36.1699, -115.1398)
Grand Canyon National Park is located at (36.1070, -112.1130)
Aspen, Colorado is located at (39.1911, -106.8175)
Mount Rushmore is located at (43.8791, -103.4591)
Yellowstone National Park is located at (44.4280, -110.5885)
Sandpoint, Idaho is located at (48.2766, -116.5535)
Banff National Park is located at (51.4968, -115.9281)
Capilano Suspension Bridge is located at (49.3429, -123.1149)
```

---

# Part 2: Heather Weather

Cody is satisfied by geolocating his landmarks, but Heather wants to take it one step further and get the current weather at each location.

Help Heather with some code that calls an API to get current weather based on latitude-longitude coordinates. Use the [Dark Sky API](https://darksky.net/dev/register) for this.

**Note:** You will need to register for an account to get an API key, but it is free to use.

## The Dark Sky API

When you first log in to the Dark Sky API site, you will see your personal API key, as well as an example of how to use that key to make a call to the API with latitude and longitude coordinates. You can click on this sample call to see what it returns.

The data is in a format called `JSON`, which is basically a big object with a bunch of data.

You can see in your web browser what that object looks like. But, unless you have a [JSON prettify plug-in](https://chrome.google.com/webstore/detail/json-formatter/bcjindcccaagfpapjjmafapmmgkkhgoa?hl=en), it will probably look like a huge mess of data and curly braces. That's OK, because your Python program won't care about how the data looks!

The important part is that the data we are getting includes a field called `currently`, which includes subfields `summary` and `temperature`, which together give us a pretty good idea of how we should dress for the weather.

## Calling an API

Now, you'll have to call the Dark Sky API directly using the [requests module](http://docs.python-requests.org/en/master/api/#module-requests), instead of using a wrapper.

Remember to `import requests` at the top of your program.

## Starter Code

Some starter code is already in the file `part2.py`.

Continue your implementation in `part2.py`.

You will have to copy over some of the code you have written from `part1.py` into `part2.py`.

**Hint:** In the API results, you are accessing an object called `currently`, which has properties called `temperature` and `summary`. Therefore, you can access those fields like so: `result['currently']['summary']`.

### Expected Output

```
The Space Needle is located at (47.6199, -122.3487)
At The Space Needle right now, it's Partly Cloudy with a temperature of 65.63
Crater Lake is located at (42.9116, -122.1483)
At Crater Lake right now, it's Clear with a temperature of 63.52
The Golden Gate Bridge is located at (37.8183, -122.4784)
At The Golden Gate Bridge right now, it's Partly Cloudy with a temperature of 59.98
Yosemite National Park is located at (37.7490, -119.5885)
At Yosemite National Park right now, it's Clear with a temperature of 83.1
Las Vegas, Nevada is located at (36.1719, -115.1400)
At Las Vegas, Nevada right now, it's Clear with a temperature of 104.72
Grand Canyon National Park is located at (36.0573, -112.1096)
At Grand Canyon National Park right now, it's Clear with a temperature of 88.37
Aspen, Colorado is located at (39.1900, -106.8182)
At Aspen, Colorado right now, it's Clear with a temperature of 86.87
Mount Rushmore is located at (43.8803, -103.4588)
At Mount Rushmore right now, it's Partly Cloudy with a temperature of 77.62
Yellowstone National Park is located at (44.9775, -110.6983)
At Yellowstone National Park right now, it's Clear with a temperature of 72.09
Sandpoint, Idaho is located at (48.2730, -116.5478)
At Sandpoint, Idaho right now, it's Clear with a temperature of 68.81
Banff National Park is located at (51.1356, -115.4073)
At Banff National Park right now, it's Partly Cloudy with a temperature of 63.91
Capilano Suspension Bridge is located at (49.3432, -123.1133)
At Capilano Suspension Bridge right now, it's Mostly Cloudy with a temperature of 65.11
```

## Remove Your Key!

When you are done with Part 2, **remove your key from your source code file** before committing and pushing your code to Github!

---

# (STRETCH) Part 3: Format for Matt

**Note:** Part 3 is a stretch goal for those who just can't get enough. It's not difficult, so you should do it if you have the time to do so. Simply continue the implementation in `part2.py` if you choose to do the Bonus part!

Matt likes Heather's idea of getting the weather for each location they plan on visiting, but he thinks the data is unreadable.

Modify your code to:

1. Display a newline after each location (`\n`)
1. Display only one decimal place on the temperature (think about string formatting)
1. Display an F (for Fahrenheit)
1. Display a unicode degree (&deg;) character
   * You're gonna have to research a bit to figure out how to print out a Unicode character!
   * Here's some additional resources:
      * [List of Unicode Characters](https://en.wikipedia.org/wiki/List_of_Unicode_characters)
      * [Obscure Unicode Characters](http://jrgraphix.net/r/Unicode)
   * **Hint:** The degree (&deg;) character has a Unicode Code of 00B0

### Expected Output

```
The Space Needle is located at (47.6199, -122.3487)
At The Space Needle right now, it's Partly Cloudy with a temperature of 65.6°F

Crater Lake is located at (42.9116, -122.1483)
At Crater Lake right now, it's Clear with a temperature of 63.5°F

The Golden Gate Bridge is located at (37.8183, -122.4784)
At The Golden Gate Bridge right now, it's Partly Cloudy with a temperature of 60.0°F

Yosemite National Park is located at (37.7490, -119.5885)
At Yosemite National Park right now, it's Clear with a temperature of 83.1°F

Las Vegas, Nevada is located at (36.1719, -115.1400)
At Las Vegas, Nevada right now, it's Clear with a temperature of 104.7°F

Grand Canyon National Park is located at (36.0573, -112.1096)
At Grand Canyon National Park right now, it's Clear with a temperature of 88.3°F

Aspen, Colorado is located at (39.1900, -106.8182)
At Aspen, Colorado right now, it's Clear with a temperature of 86.9°F

Mount Rushmore is located at (43.8803, -103.4588)
At Mount Rushmore right now, it's Partly Cloudy with a temperature of 77.6°F

Yellowstone National Park is located at (44.9775, -110.6983)
At Yellowstone National Park right now, it's Clear with a temperature of 72.0°F

Sandpoint, Idaho is located at (48.2730, -116.5478)
At Sandpoint, Idaho right now, it's Clear with a temperature of 68.8°F

Banff National Park is located at (51.1356, -115.4073)
At Banff National Park right now, it's Partly Cloudy with a temperature of 63.9°F

Capilano Suspension Bridge is located at (49.3432, -123.1133)
At Capilano Suspension Bridge right now, it's Mostly Cloudy with a temperature of 65.1°F
```

---

# Done and Done!

Too bad we don't have time for an actual road trip...

![](https://media.giphy.com/media/PqwqtOLfG19Ti/giphy.gif)
