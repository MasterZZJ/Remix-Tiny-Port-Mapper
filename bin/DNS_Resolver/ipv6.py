import socket
import json
import time

# Find the public IP
def search_ip():
    # Load the setting file
    setting_file = open("../conf/settings.json", "r")
    setting = json.load(setting_file)
    setting_file.close()

    server, client = setting["server"], setting["client"]

    # Domain Name Resolution
    if server["needDNS"]:
        server_host = server["address"]
        if server["isIPv6"]:
            server_ip = f"[{socket.getaddrinfo(server_host, None)[0][4][0]}]"
        else:
            server_ip = socket.getaddrinfo(server_host, None)[1][4][0]
    else:
        server_ip = server["address"]

    if client["needDNS"]:
        client_host = client["address"]
        if client["isIPv6"]:
            client_ip = f"[{socket.getaddrinfo(client_host, None)[0][4][0]}]"
        else:
            client_ip = socket.getaddrinfo(client_host, None)[1][4][0]
    else:
        client_ip = client["address"]

    # "[","]"is adding



    server["address"] = server_ip
    client["address"] = client_ip



    overDNS = {
        "server": server,
        "client": client
    }

    DNS_setting_file = open("../conf/DNS_setting.json", "w+")
    json.dump(overDNS, DNS_setting_file)
    DNS_setting_file.close()


# while True:
#     search_ip()
#     time.sleep(3)