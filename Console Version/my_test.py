import time
import socket,getpass
from JDAutoBuyTool import sendError
# import JDAutoBuyTool as jd

print('time.asctime() = {}'.format(time.asctime()))

print('time.time() = {}'.format(time.time()))
print('time.time() = {}'.format(time.time()))
print('username = {}, hostname = {}'.format(getpass.getuser(),socket.gethostname()))

