import json
import ibm_db as db2

def read_database_info()->str:
    with open('database_credentials.json') as json_file:
        data = json.load(json_file)

def test_answers():
    read_database_info()

# connection = db2.connect(
#     'DATABASE=<database name>;'
#     'HOSTNAME=<database ip>;'  # 127.0.0.1 or localhost works if it's local
#     'PORT=<database port>;'
#     'PROTOCOL=TCPIP;'
#     'UID=<database username>;'
#     'PWD=<username password>;', '', ''
#     )

