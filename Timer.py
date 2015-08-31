#!/usr/bin/env python

from datetime import datetime
import time

class Timer:
  
  def converter(self, UserMin, UserHour): # Hour + Min To Seconds
    # Hour To Seconds
    hour_to_seconds = UserHour * 60
    hour_to_seconds = hour_to_seconds * 60
    
    # Minute To Seconds
    min_to_seconds = UserMin * 60
    
    return hour_to_seconds + min_to_seconds

