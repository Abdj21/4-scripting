#!/usr/bin/env python3
import sys
import time
name = sys.argv[1]
current_time = time.strftime("%Y-%m-%d %H:%M:%S %Z")
print(f"Hello {name},\nright now the time is {current_time}")
