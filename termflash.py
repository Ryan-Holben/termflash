"""
termflash - Terminal Flash Utility

Author: Ryan Holben  
Date: 2025-02-18  
License: MIT  

Description:  
🚨 A simple utility to flash the terminal screen, useful for grabbing attention.  
Ideal for alerting when a long-running job is complete. 🚨  

Usage:  
    python termflash.py --rate 0.25 --duration 1  
"""

import argparse
import curses
from time import sleep

filler_char = "\u2588"  # █ (full block character)

def curses_main(stdscr, rate, duration, code):
    curses.start_color()
    color = curses.COLOR_GREEN if code == 0 else curses.COLOR_RED
    curses.init_pair(1, color, color)
    stdscr.clear()
    height, width = stdscr.getmaxyx()  # Get screen size
        
    def fill_scr(char):
        string = char * (width - 1)
        for row in range(height):
            stdscr.addstr(row, 0, string, curses.color_pair(1))
        stdscr.refresh()

    num_flashes = int(duration / (2 * rate))
    for _ in range(num_flashes):
        fill_scr(filler_char)
        sleep(rate)
        stdscr.clear()
        stdscr.refresh()
        sleep(rate)
        
    exit(code)

def main():
    parser = argparse.ArgumentParser(description="🚨 Make the terminal flash to grab your attention. 🚨")
    parser.add_argument("-r", "--rate", type=float, default=0.08, help="Time in seconds between flashes.")
    parser.add_argument("-f", "--duration", type=float, default=1.0, help="Total duration of flashing in seconds.")
    parser.add_argument("-c", "--code", "--color", type=int, default=0, help="Exit code to pass through.  0 gives green, other codes give red.")
    args = parser.parse_args()

    curses.wrapper(curses_main, args.rate, args.duration, args.code) 

if __name__ == "__main__":
    main()