"""
termflash - Terminal Flash Utility

Author: Ryan Holben  
Date: 2025-02-18  
License: MIT  

Description:  
🚨 A simple utility to flash the terminal screen, useful for grabbing attention.  
Ideal for alerting when a long-running job is complete. 🚨  

Usage:  
    python termflash.py --flash_rate 0.25 --duration 1  
"""

import argparse
import curses
from time import sleep

filler_char = "\u2588"  # █ (full block character)

def main(stdscr, flash_rate, duration):
    curses.start_color()
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_RED)
    stdscr.clear()
    height, width = stdscr.getmaxyx()  # Get screen size

    def fill_scr(char):
        string = char * (width - 1)
        for row in range(height):
            stdscr.addstr(row, 0, string, curses.color_pair(1))
        stdscr.refresh()

    num_flashes = int(duration / (2 * flash_rate))
    for _ in range(num_flashes):
        fill_scr(filler_char)
        sleep(flash_rate)
        stdscr.clear()
        stdscr.refresh()
        sleep(flash_rate)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="🚨 Make the terminal flash to grab your attention. 🚨")
    parser.add_argument("--flash_rate", type=float, default=0.08, help="Time in seconds between flashes.")
    parser.add_argument("--duration", type=float, default=1.0, help="Total duration of flashing in seconds.")

    args = parser.parse_args()
    curses.wrapper(main, args.flash_rate, args.duration)