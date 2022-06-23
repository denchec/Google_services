from __future__ import print_function

from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build


def create_table(service, creds):
    spreadsheet = service.spreadsheets().create(body={
        'properties': {'title': 'Rare', 'locale': 'ru_RU'},
        'sheets': [{'properties': {'sheetType': 'GRID',
                                   'sheetId': 0,
                                   'title': 'list1',
                                   'gridProperties': {'rowCount': 8, 'columnCount': 5}}}]
    }).execute()

    create_access_for_new_table(spreadsheet['spreadsheetId'], creds)

    return spreadsheet


def create_access_for_new_table(spreadsheet_id, creds):
    drive_service = build('drive', 'v3', credentials=creds)
    share_res = drive_service.permissions().create(
        fileId=spreadsheet_id,
        body={'type': 'anyone', 'role': 'reader'},
        fields='id'
    ).execute()


def data_recording(service, spreadsheet_id):
    results = service.spreadsheets().values().batchUpdate(spreadsheetId=spreadsheet_id, body={
        "valueInputOption": "USER_ENTERED",
        "data": [
            {"range": "A1:B2",
             "majorDimension": "ROWS",
             "values": [["This is A1", "This is B1"], ["This is A2", "This is B2"]]},
            {"range": "D7:E8",
             "majorDimension": "COLUMNS",
             "values": [["This is D7", "This is D8"], ["This is E7", "This is E8"]]}
        ]
    }).execute()


def clear_data(service, spreadsheet_id):
    results = service.spreadsheets().values().batchClear(spreadsheetId=spreadsheet_id, body={
        "ranges": ["A1:B1", "E7:E8"]
    }).execute()


def update_data(service, spreadsheet_id):
    results = service.spreadsheets().values().batchUpdate(spreadsheetId=spreadsheet_id, body={
        "valueInputOption": "USER_ENTERED",
        "data": [
            {"range": "B2:B2",
             "values": [["Or maybe not"]]},
            {"range": "D7:D7",
             "values": [["Or maybe not"]]}
        ]
    }).execute()


def main():
    creds = Credentials.from_service_account_file('token.json')

    service = build('sheets', 'v4', credentials=creds)

    spreadsheet = create_table(service, creds)
    data_recording(service, spreadsheet['spreadsheetId'])
    clear_data(service, spreadsheet['spreadsheetId'])
    update_data(service, spreadsheet['spreadsheetId'])

    print(spreadsheet['spreadsheetUrl'])


if __name__ == '__main__':
    main()
