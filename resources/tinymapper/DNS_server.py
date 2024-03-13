import socket
host = 'z790.arthasjian.online'
ip = socket.getaddrinfo(host, None)


ip6 = ip[0][4][0]
ip4 = '127.0.0.1'

# Terraria 7777;Stardew 24642
port = 7777

tinymapperController = f"tinymapper.exe -l[{ip6}]:40800 -r{ip4}:{port} -t -u"

import os
os.system(tinymapperController)

