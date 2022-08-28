import os
from dotenv import load_dotenv
load_dotenv('./env')

def generate_db_url():
    local_db_url = None
    remote_db_url = None

    # Constructing the local database url
    local_db_username = str(os.getenv('POSTGRES_USER', ''))
    local_db_password = str(os.getenv('POSTGRES_PASSWORD',''))
    local_db_host = str(os.getenv('POSTGRES_HOST',''))
    local_db_port = str(os.getenv('POSTGRES_PORT', ''))
    local_db_db_name = str(os.getenv('POSTGRES_DB', ''))
    local_db_url = 'postgresql://' + local_db_username + ':'+ local_db_password + '@' + local_db_host+ ':' + local_db_port + '/' + local_db_db_name

    if local_db_url == 'postgresql://:@:/':
        print('Local DB setup not possible. Check env vars.')
    
    remote_db_url = str(os.getenv('DATABASE_URL',''))

    if not remote_db_url:
        print('Remote DB setup not possible. Check env var for remote DATABASE_URL')
    
    db_url = remote_db_url if remote_db_url else local_db_url

    print('DB URL => ', db_url)

    return db_url


db_url = generate_db_url()