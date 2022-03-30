from dataclasses import dataclass
from datetime import datetime

@dataclass 
class Location:
    latitude:float
    longitude:float

@dataclass
class SunData:
    sunrise:datetime
    sunset:datetime
  
@dataclass
class Observation:
    date:datetime
    location:Location
    sun:SunData

