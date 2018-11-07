#!/usr/bin/env python3
"""
timer.py
This "desktop countdown timer" runs in a terminal window
and rings an alarm when the indicated number of minutes
has elapsed. Time can be entered in one of two formats:
    1. Minutes, in decimal form: 3, or 2.5, or
       120 (= 2 hours), etc.
    2. Standard MM:SS format, or HH:MM:SS format
Playing the alarm bell requires the importing of the
pyaudio and wave modules, as well as the file
alarm_bell.wav, created by me from a live desk bell
and processed using Audacity.
"""
__author__ = 'Richard White'
__version__ = '2018-11-03'

import time
import os
import pyaudio  # to play alarm
import wave     # to play alarm


def play_bell():
    """Geez, playing audio in Python is kind of complicated!
    """
    # set things up to play a file
    chunk = 1024    # defines a stream chunk
    f = wave.open(r"./alarm_bell.wav","rb")
    p = pyaudio.PyAudio()
    stream = p.open(format = p.get_format_from_width(f.getsampwidth()), channels = f.getnchannels(), rate = f.getframerate(), output = True)
    data = f.readframes(chunk)
    # go through the file and play the file
    while data:
        stream.write(data)
        data = f.readframes(chunk)
    # close things up
    stream.stop_stream()
    stream.close()
    p.terminate()

def input_time():
    t_string = input("Countdown time (min, or xx:yy:zz): ")
    # process the input to find out which format it's in,
    # and convert input string to minutes
    if ":" in t_string:
        t_list = t_string.split(":")
        if len(t_list) == 2:
            t = float(t_list[0]) + \
                float(t_list[1])/60.0
        elif len(t_list) == 3:
            t = float(t_list[0]) * 60 + \
                float(t_list[1]) + \
                float(t_list[2]) / 60.0
        else:
            print("Error. Time format should be MM:SS or HH:MM:SS.")
            os.exit()
    else:
        t = eval(t_string)
    return t

def time_string(tf):
    secs_remaining = int(tf - time.time())
    hours = secs_remaining // 3600
    minutes = (secs_remaining - hours * 3600) // 60
    seconds = secs_remaining - hours * 3600 - minutes * 60
    return "{0:2s}:{1:2s}:{2:2s}".format(str(hours).zfill(2), str(minutes).zfill(2), str(seconds).zfill(2))

         
def run_loop(tf):
    while time.time() < tf - 1:
        os.system("clear")
        print(time_string(tf))
        time.sleep(1)
 
def main():
    t = input_time()
    tf = time.time() + t*60 + 1 # off-by-one error, start at given time
    run_loop(tf)
    os.system("clear")
    print("00:00:00")
    play_bell()

if __name__ == "__main__":
    main()
