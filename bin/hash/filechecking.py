import hashlib
import time
FILE_PATH = '../conf/DNS_setting.json'

def calculate_md5(file_path):
    hash_md5 = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def monitor_file_changes(file_path=FILE_PATH, interval=3):
    initial_md5 = calculate_md5(file_path)
    print(f"Initial MD5: {initial_md5}")
    while True:
        time.sleep(interval)
        current_md5 = calculate_md5(file_path)
        if current_md5 != initial_md5:
            print("DNS_setting.json file has changed!" + "New md5 is: " + current_md5)
            initial_md5 = current_md5
            break

        else:
            # print("No change detected.")
            pass
            # print("break point")


# monitor_file_changes(FILE_PATH, 3)  # 每 3秒检查一次文件是否变化
