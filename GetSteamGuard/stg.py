import os, json
from steampy.guard import generate_one_time_code

def GetSharedSecret(login):
    dir_name = os.path.abspath("./maFiles")
    for item in os.listdir(dir_name):
        try:
            with open(f'{dir_name}/{item}', 'r') as f:
                info = json.load(f)
                if info['account_name'].lower() == login:
                    return info['shared_secret']
        except (FileNotFoundError, json.JSONDecodeError):
            pass
    return None
code = generate_one_time_code(GetSharedSecret(login=""))