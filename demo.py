# Title: demo.py
# Revision: 0.7
# Python version: 3.x
# Author: Chalmer Lowe
# Usage: %run demo.py <filename.py>
#        * where <filename.py> is the name of the demo file you wish to run
# Description: Launches a demo file enabling interactive demonstrations of python within IPython.

import sys
from IPython.lib.demo import ClearIPDemo as demo

d = demo(sys.argv[1])

d()
