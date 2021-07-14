#!/usr/bin/env python3

import sys
import subprocess

filename = sys.argv[1]

with open(filename, "r") as f:
    for _line in f.readlines():
        line = _line.strip()
        updated_path = line.replace("jane", "jdoe")
        subprocess.run(["mv", line, updated_path])
