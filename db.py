import psycopg2
import json

from credentials import creds

connection_string = 'dbname={0[DATABASE_NAME]} user={0[DATABASE_USER]} password={0[DATABASE_PASSWORD]} host={0[DATABASE_HOST]}'.format(creds())

conn =  psycopg2.connect(connection_string)
cursor = conn.cursor()

def test():
    print(creds())
    return str(creds())
    
def receivePost(request):
    body = request.get_json()
    body = json.dumps(body)
    
    insertString = '''INSERT INTO posts (requestbody) VALUES (\'{0}\');'''.format(body)
    print(insertString)
    
    cursor.execute(insertString)
    committed = conn.commit()
    return str(committed)