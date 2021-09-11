# FotMob-py

An unofficial FotMob API wrapper for python

## Example usage

``` py
from FotMob import FotMob

fm = FotMob()
r_league = fm.getLeague()
print(r_league.json())
```