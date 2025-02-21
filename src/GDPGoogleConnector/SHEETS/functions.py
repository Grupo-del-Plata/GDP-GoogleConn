


class SheetsFunctions:
    """
    Google Sheets functions used in manager.
    """
    def __init__(self, manager):
        self.manager = manager

    def write_data_in_sheet(self, spreadsheet_id, sheet_name, data, start_row=1, start_col=1, data_format='json'):
        """
        Updates data in a Google Sheet through a Google Apps Script function.

        Args:
            spreadsheet_id (str): The ID of the Google Sheet.
            sheet_name (str): The name of the sheet to update.
            data (str | list): Data to be written, either a JSON string or a list structure.
            start_row (int): Starting row for the data update.
            start_col (int): Starting column for the data update.
            data_format (str): Format of the data provided ('json' or 'array').

        Returns:
            Any: Result of the data update script execution.
        """
        parameters = [spreadsheet_id, sheet_name, data, start_row, start_col, data_format]
        return self.manager._execute_script('writeData', parameters)

    def list_google_sheets(self):
        """
        Retrieves a list of all Google Sheets in the user's Google Drive.
        Returns:
            list: List of dictionaries containing 'id' and 'name' of each spreadsheet.
        """
        return self.manager._execute_script('listGoogleSheets', [])

    def get_sheet_names(self, spreadsheet_id):
        """
        Retrieves all sheet names from a specified Google Spreadsheet.
        Args:
            spreadsheet_id (str): The ID of the Google Spreadsheet.
        Returns:
            list: List of sheet names.
        """
        return self.manager._execute_script('getSheetNames', [spreadsheet_id])

    def read_sheet_data(self, spreadsheet_id, sheet_name, start_row=1, start_col=1, end_row=None, end_col=None):
        """
        Retrieves data from a specified range in a Google Spreadsheet.
        Args:
            spreadsheet_id (str): The ID of the Google Spreadsheet.
            sheet_name (str): The name of the sheet from which to read data.
            start_row (int): Starting row index for the data retrieval.
            start_col (int): Starting column index for the data retrieval.
            end_row (int): Ending row index for the data retrieval.
            end_col (int): Ending column index for the data retrieval.
        Returns:
            list: 2D list of data from the specified range.
        """
        parameters = [spreadsheet_id, sheet_name, start_row, start_col, end_row, end_col]
        return self.manager._execute_script('readData', parameters)
