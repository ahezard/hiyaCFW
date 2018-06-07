import io
import os
import subprocess
from struct import *
from collections import namedtuple
from collections import OrderedDict
from pprint import pprint
import os, sys
import binascii

try:
	print("Extracting Console ID...")

	footer = io.open('nand.bin', 'rb')
	footer.read(0xF000020)
	data = footer.read(8)
    
	print(data)

	if os.path.isfile("console_id.txt"):
		print("Old console_id.txt found, removing")
		os.remove("console_id.txt")
	
	footerConsoleId = namedtuple('consoleid',"id1 "
    "id2 ")     
	footerConsoleIdFormat="<II"
	
	consoleid=footerConsoleId._make(unpack_from(footerConsoleIdFormat, data))
    
	pprint(consoleid)

	with open('console_id.txt', 'a') as consoleidf:
		consoleidf.write("0"+hex(consoleid.id2)[2:])
		consoleidf.write(hex(consoleid.id1)[2:])
	footer.close()

except Exception as e:
	print("ERROR: {0}".format(e))
else:
	print("Success")
input("Press Enter to continue...")