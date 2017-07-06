import os
import subprocess
import sys


child = os.path.join(os.path.dirname(__file__), "./ips3_child.py")
word  = 'word'
file = ['./parent.py','./child.py']

pipes = []
print('parent start')
for i in range(0,100):
  command = [sys.executable, child]
  pipe = subprocess.Popen(command, stdin=subprocess.PIPE)
  pipes.append(pipe)
  # pipe.stdin.write(word.encode("utf8") + b"\n")
  # pipe.stdin.write(file[i].encode("utf8") + b"\n")
  pipe.stdin.close()

while pipes:
    pipe = pipes.pop()
    pipe.wait()