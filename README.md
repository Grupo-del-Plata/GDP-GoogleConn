
# Google Apps Script Manager

The Google Apps Script Manager is a Python class designed to facilitate the authentication and execution of Google Apps Scripts. This class simplifies the process of executing custom Google Apps Script functions from a Python environment, managing authentication seamlessly using OAuth 2.0 credentials.

## Objective

The objective of this class is to provide a straightforward and reusable approach to interact with Google Apps Script APIs. It handles authentication, session management, and script execution, enabling users to focus on the logic of their applications rather than the intricacies of the API.

## Installation

To install run:

```
pip install git+ssh://git@github.com/Grupo-del-Plata/GDP-GoogleConnector.git
```


## Features

- **OAuth 2.0 Authentication**: Manages OAuth 2.0 credentials to authenticate the Google API.
- **Session Management**: Uses Python context managers to handle API sessions efficiently.
- **Script Execution**: Facilitates the execution of custom functions in Google Apps Script.

## Requirements

- Python 3.6+
- Google API Client Library for Python
- Google Auth Library for Python

## Usage

Once installed, the module can be imported into any project using:

```python
from GDPGoogleConnector import GoogleConnector
```

To instantiate it, use:

```python
connector = GoogleConnector(
	credentials_file='path/to/credentials',  # Default: credentials.json
	token_file='path/to/token',  # Default: token.json
	scopes=SERVICES_SCOPES,  # Services it will access. Default: projects, drive, forms, spreadsheets
	services=['script'],
	SCRIPT_ID=SCRIPTS_ID  # The Google project script ID obtained after deployment
)
```

If the default values are used and the `credentials.json` file is placed in the same folder as the project, only the `SCRIPT_ID` input will be required, and it can be instantiated as:

```python
connector = GoogleConnector(SCRIPT_ID='YOUR_SCRIPTS_ID')
```

Then you can interact with arbitrary scripts using the *_execute_script* function:


```python
connector._execute_script(
	function='function1',					# The name of the function to execute, as defined in the google script
	parameters=['parameter1', 2],			# A list of parameters to use as inputs, must be passed in the orders defined in the google script
	script_id=None							# OPTIONAL: A different script_id that the one passed when instantiating
)
```
