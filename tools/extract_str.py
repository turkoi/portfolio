#!/usr/bin/env python3

import sys
import re

def extract_strings(filepath, min_length=4):
    try:
        with open(filepath, "rb") as f:
            data = f.read()
    except FileNotFoundError:
        print(f"[!] File not found: {filepath}")
        return

    # ASCII strings
    ascii_strings = re.findall(rb"[ -~]{%d,}" % min_length, data)

    # Unicode strings (UTF-16LE)
    unicode_strings = re.findall(rb"(?:[\x20-\x7E]\x00){%d,}" % min_length, data)

    print("\n=== ASCII Strings ===")
    for s in ascii_strings:
        print(s.decode(errors="ignore"))

    print("\n=== Unicode Strings ===")
    for s in unicode_strings:
        print(s.decode("utf-16le", errors="ignore"))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 strings_extractor.py <filename>")
        sys.exit(1)

    extract_strings(sys.argv[1])
