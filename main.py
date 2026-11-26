#!/usr/bin/env python3
"""Name the Robot Band — writes one funny robot band name + hit song line."""
import os

ENTRY = 'The Unplugged \u2014 hit single "Battery Low (Acoustic)".'

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
