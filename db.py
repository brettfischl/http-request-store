import psycopg2
import json

from credentials import creds

connection_string = 'dbname={0[DATABASE_NAME]} user={0[DATABASE_USER]} password={0[DATABASE_PASSWORD]} host={0[DATABASE_HOST]} port=5432'.format(creds())

conn =  psycopg2.connect(connection_string)
cursor = conn.cursor()

def acceptPost(request):
    if (isinstance(request.data, (bytes, bytearray))):
        body = json.loads(request.data)
        body = json.dumps(body)
        print('if', body)
    else:
        body = request.get_json()
        body = json.dumps(body)

    remote_address = request.remote_addr

    requested_url = request.url

    insertString = '''INSERT INTO posts (request_body, remote_address, request_url)
    VALUES (%s, %s, %s);'''

    cursor.execute(insertString, (body, remote_address, requested_url))
    committed = conn.commit()
    return str(committed)
