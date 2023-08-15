import json

import json
#Json 파일에 저장되어 있는 username, host, db 등 불러오기

config_file = r'C:\projects\myapi\config.json'  # Raw 문자열로 표시
config = json.loads(open(config_file).read())
DB = config["DB"]

print(DB)

print(DB['user'])

DATABASE = f"mysql+pymysql://{DB['user']}:{DB['password']}@{DB['host']}:{DB['port']}/{DB['database']}?charset=utf8"

print(DB['database'])
