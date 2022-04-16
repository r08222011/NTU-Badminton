import os
import getpass

def get_info():
    dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    with open(os.path.join(dir, "default.txt"), 'r', encoding="utf-8") as f:
        lines = f.readlines()
        info = {}
        for i in range(len(lines)):
            if ":" in lines[i]:
                key, value = lines[i].split(":")
                value = value.replace("\\n", "").strip()
                if "password" in key:
                    value = value if value != "" else getpass.getpass(f"{key} : ")
                else:
                    value = value if value != "" else input(f"{key} : ")
                key = key[key.index("[")+1:key.index("]")]
                info[key] = value
    return info