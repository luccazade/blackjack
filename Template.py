#! /usr/bin/env python3
# this is the shebang line

import logging

# Set up the debug console
logging.basicConfig(filename='logFile.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
# Disable the debugging
logging.disable(logging.CRITICAL)
# Begin the program
logging.debug('Start of program')