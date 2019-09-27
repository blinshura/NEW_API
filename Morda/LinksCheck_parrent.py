import os
import subprocess
import sys

from datetime import datetime

start_time = datetime.now()

child = os.path.join(os.path.dirname(__file__), "./LinksCheck.py")
word  = 'word'
file = ['./parent.py','./child.py']

pipes = []
print('parent start')
for i in range(0,50):
  command = [sys.executable, child]
  pipe = subprocess.Popen(command, stdin=subprocess.PIPE)
  pipes.append(pipe)
  # pipe.stdin.write(word.encode("utf8") + b"\n")
  # pipe.stdin.write(file[i].encode("utf8") + b"\n")
  pipe.stdin.close()

while pipes:
    pipe = pipes.pop()
    pipe.wait()

end_time = datetime.now()
total_time = end_time - start_time
print('total_time ' + str(total_time))

