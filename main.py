#!/usr/bin/env python

#TODO
# Add Option to pop up at a given time
# In The future add a gui config option window
  # Give option to start from that gui config
# Create a better graphic for the message in the Base class
# Add a sound on pop up
# Clean up code
# Add ability to run in background


from Base import Base
from Timer import Timer
import time
import argparse

class Main:
  
  
  def main():
    # Get User Argument Input
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--hour', type=int, required=True, dest='hour',
			help='hour for the timer')
    parser.add_argument('-m', '--minute', type=int, required=True, dest='minute',
			help='min for the timer')
    args = parser.parse_args()
    
    # Convert Hour and Minute to Seconds
    TimeStuff = Timer()
    TimeToWait = TimeStuff.converter(args.minute, args.hour)
    
    # Run The Base of the Main Reminder Window
    Reminder = Base()
    time.sleep(TimeToWait)
    Reminder.main()
    

# Run The Base of the Main Reminder Window
  if __name__ == "__main__":
    main()