# fotmoby

An unofficial FotMob API wrapper for python

## Installation

``` bash
pip install fotmoby
```

## Example usage

``` py
from FotMoby import FotMoby as fm

r_league = fm.getLeague()
print(r_league.json())
```