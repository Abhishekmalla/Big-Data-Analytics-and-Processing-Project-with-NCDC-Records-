
#!/usr/bin/env python

import re
import sys

for line in sys.stdin:
  val = line.strip()
  (month, height, q) = (val[19:21], val[70:75], val[75:76])
  if (height != "99999" and re.match("[01459]", q)):
    print "%s\t%s" % (month, height)