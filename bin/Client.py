from DNS_Resolver import ipv6
from hash import filechecking as fc
import json
import subprocess
import threading
import time

def main():


    tunnel_port = 40800
    # Load DNS setting file
    print("Load DNS setting file")
    setting_file = open("../conf/DNS_setting.json", "r")
    setting = json.load(setting_file)
    setting_file.close()
    server = setting["server"]
    client = setting["client"]

    tinymapperController = f"..\\resources\\tinymapper\\tinymapper.exe -l{client['address']}:{client['port']} -r{server['address']}:{tunnel_port} -t -u"
    print(tinymapperController)
    process = subprocess.Popen(tinymapperController, shell=True)


    fc.monitor_file_changes()


    process.terminate()
    process.wait()
    main()




if __name__ == '__main__':
    DNS_Handler = threading.Thread(target=ipv6.search_ip)
    DNS_Handler.start()
    time.sleep(2)
    main()