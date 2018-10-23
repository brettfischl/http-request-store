import os
db_url = os.environ.get('DATABASE_URL', None)
credentials = {}

def creds():    
    if db_url:
        credentials['DATABASE_HOST'] = os.environ.get('DATABASE_HOST', None)
        credentials['DATABASE_USER'] = os.environ.get('DATABASE_USER', None)
        credentials['DATABASE_PASSWORD'] = os.environ.get('DATABASE_PASSWORD', None)
        credentials['DATABASE_NAME'] = os.environ.get('DATABASE_NAME', None)

    else:
        credentials['DATABSE_URL'] = 'postgres://kuikpnusgzlgik:10ad97657b90e0238847c2d7586984cdf8e07e7105b71667027c3e08f66b2eb8@ec2-184-73-169-151.compute-1.amazonaws.com:5432/d9sc4gblm6vnsk'
        
        credentials['DATABASE_HOST'] = 'ec2-184-73-169-151.compute-1.amazonaws.com'
        credentials['DATABASE_USER'] = 'kuikpnusgzlgik'
        credentials['DATABASE_PASSWORD'] = '10ad97657b90e0238847c2d7586984cdf8e07e7105b71667027c3e08f66b2eb8'
        credentials['DATABASE_NAME'] = 'd9sc4gblm6vnsk'
        
    
    return credentials