from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

from .defaults import SCOPES, VERSIONS, CREDENTIALS_FILE, TOKEN_FILE

from .SHEETS.functions import SheetsFunctions


class GoogleConnector:
    """
    Handles authentication and execution of Google Apps Script services.

    Attributes:
        credentials_file (str): Path to the OAuth 2.0 client credentials JSON file.
        token_file (str): Path to the stored OAuth tokens file.
        scopes (list): OAuth 2.0 scopes required by the application.
        services_list (list): List of Google services to be initialized.
        SCRIPT_ID (str, optional): Default Google Apps Script project ID.
        creds (Credentials): OAuth credentials.
        services (dict): Google services API client instances.
    """

    def __init__(
        self,
        credentials_file=CREDENTIALS_FILE,
        token_file=TOKEN_FILE,
        scopes=SCOPES,
        services=['script'],
        SCRIPT_ID=None
    ):
        """
        Initializes the GoogleConnector with the necessary configurations.

        Args:
            credentials_file (str): Path to the OAuth 2.0 Client Credentials JSON file.
            token_file (str): Path to the file storing the user's access and refresh tokens.
            scopes (list): List of OAuth 2.0 scopes required by the application.
            services (list): List of Google services to be used.
            SCRIPT_ID (str, optional): Google Apps Script project ID.
        """
        self.credentials_file = credentials_file
        self.token_file = token_file
        self.scopes = scopes
        self.services_list = services
        self.SCRIPT_ID = SCRIPT_ID
        self.services = {}

        self.authenticate()

        self.SHEETS = SheetsFunctions(self)  # Creates reference to sheets functions to access it's methods'



    def __enter__(self):
        """
        Context management entry method. Authenticates the user and creates the service object.

        Returns:
            GoogleAppsScriptManager: The instance of itself.
        """
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Context management exit method. Handles cleanup if necessary.

        Args:
            exc_type: Exception type.
            exc_val: Exception value.
            exc_tb: Traceback.
        """
        if exc_type:
            print(f'Error on exit: {exc_type}, {exc_val}')

    def authenticate(self):
        """
        Authenticates the user by loading stored tokens or by generating new ones through the OAuth flow.
        Saves the credentials if new tokens are generated.
        """
        try:
            self.creds = Credentials.from_authorized_user_file(self.token_file, self.scopes)
        except Exception as e:
            print(f"Failed to load credentials from file: {e}")
            self.creds = None

        if not self.creds or not self.creds.valid:
            if self.creds and self.creds.expired and self.creds.refresh_token:
                try:
                    self.creds.refresh(Request())
                except Exception as e:
                    print(f"Failed to refresh access token: {e}")
                    self.creds = None

            if not self.creds:
                flow = InstalledAppFlow.from_client_secrets_file(self.credentials_file, self.scopes)
                self.creds = flow.run_local_server(port=0)

                # Save the credentials for the next run
                with open(self.token_file, 'w') as token:
                    token.write(self.creds.to_json())

        self.services = {
            serv: build(serv, VERSIONS.get(serv), credentials=self.creds) for serv in self.services_list
        }

    def _execute_script(self, function: str='inputReceiver', parameters=[], script_id=None):
        """
        Executes a function in the Google Apps Script.

        Args:
            script_id (str): The id of the Script Project to be executed.
            function (str): The name of the function to execute in the Apps Script.
            parameters (list): A list of parameters to pass to the Apps Script function.

        Returns:
            The result of the script execution or None if an error occurred.
        """
        script_id = script_id if script_id else self.SCRIPT_ID
        request = {
            "function": function,
            "parameters": parameters,
        }
        try:
            response = self.services['script'].scripts().run(body=request, scriptId=script_id).execute()
            if 'error' in response:
                print(f"Script error: {response['error']['details'][0]['errorMessage']}")
                return None
            return response # .get('response', {}).get('result', None)
        except Exception as e:
            print(f"Failed to execute script function '{function}': {e}")
            return None
