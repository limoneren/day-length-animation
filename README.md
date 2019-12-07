# day-length-animation

A fun animation to show the day lengths of your location during a year, inspired by [this](https://www.reddit.com/r/dataisbeautiful/comments/e6fc7r/oc_i_got_inspired_by_the_sunrise_and_sunset_post/) reddit post

### Prerequisites

First install required packages.

```
pip install -r requirements.txt
```

### Running

Then go to https://www.sunrise-and-sunset.com/sv/sun/turkiet/istanbul/2019/ and choose the city you want the animation of. 
Pay attention to the country and city names as they are in Swedish. Preferrably, choose the country and city name by navigating in the website, not replace in the url.

Then run it with url argument

e.g
```
python main.py https://www.sunrise-and-sunset.com/sv/sun/turkiet/istanbul/2019/
```
or
```
python main.py https://www.sunrise-and-sunset.com/sv/sun/storbritannien/london/2019/
```

### Example

You can check [this](https://www.youtube.com/watch?v=6Xd47HlPS3k) example. It's for London. Because of the Daylight Saving Time(DST), London's video lags somewhere a little. However, it is pretty smooth for Istanbul as Turkey does not have DST.
