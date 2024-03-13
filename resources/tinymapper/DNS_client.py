import signal
import socket
import time

host = 'wyh.arthasjian.online'
ip = socket.getaddrinfo(host, None)


ip6 = ip[0][4][0]
ip4 = '127.0.0.1'

# Terraria 7777;Stardew 24642


tinymapperController = f"tinymapper.exe -l{ip4}:40800 -r[{ip6}]:40800 -t -u"
print(tinymapperController)
# import os
# import subprocess
#
# # os.system(tinymapperController)
#
# process = subprocess.Popen(tinymapperController, shell=True)
# print(1111)
# time.sleep(3)
#
# process.terminate()
# process.wait()


