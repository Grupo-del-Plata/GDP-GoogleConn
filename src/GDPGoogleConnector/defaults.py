#  The project scopes, i.e. services it will acess
SCOPES = ['https://www.googleapis.com/auth/script.projects', 'https://www.googleapis.com/auth/drive', 'https://www.googleapis.com/auth/forms', 'https://www.googleapis.com/auth/spreadsheets']

#  The services' versions map
VERSIONS = {
    'script': 'v1',
    'forms': 'v1',
    'drive': 'v3'
}

#  The file containing the access token. Must be json.
TOKEN_FILE = 'token.json'

#  The file the credentials will be stored in. Must be of json format.
CREDENTIALS_FILE = 'credentials.json'
