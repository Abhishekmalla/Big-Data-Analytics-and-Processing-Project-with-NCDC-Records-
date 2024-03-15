

#!/usr/bin/env python

import sys

current_month = None
min_height = int(99999)
max_height = int(-99999)
for line in sys.stdin:
  month, height = line.strip().split('\t')
  if month != current_month:
    print("{}\t{}".format(current_month, max_height - min_height))
    current_month = month
    min_height = int(99999)
    max_height = int(-99999)
  height = int(height)
  if height < min_height:
    min_height = height
  if height > max_height:
    max_height = height
if current_month is not None:
    print("{}\t{}".format(current_month, max_height - min_height))