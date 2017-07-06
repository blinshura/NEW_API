
import subprocess as sp
import os
#sp.call(r'C:/open_me.py')
#os.system(r'C:/open_me.py')
#os.system(r'C:/1.txt')
import sys

import subprocess

child = os.path.join(os.path.dirname(__file__), r'C:/open_me.py')
command = [sys.executable, child]
pipe = subprocess.Popen(command, stdin=subprocess.PIPE)
pipe.wait()