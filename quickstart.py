from __future__ import print_function

from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build

SAMPLE_SPREADSHEET_ID = '1ddIga3TRxsiRxwfWxXAQT7l7226pyNKvNPUt_VPk3gw'
SAMPLE_RANGE_NAME = 'Лист1!A1:E1'


def main():
    creds = Credentials.from_service_account_file('token.json')

    service = build('sheets', 'v4', credentials=creds)

    spreadsheet = service.spreadsheets().create(body={
        'properties': {'title': 'Первый тестовый документ', 'locale': 'ru_RU'},
        'sheets': [{'properties': {'sheetType': 'GRID',
                                   'sheetId': 0,
                                   'title': 'Лист номер один',
                                   'gridProperties': {'rowCount': 100, 'columnCount': 15}}}]
    }).execute()

    spreadsheet_id = spreadsheet['spreadsheetId']

    print('https://docs.google.com/spreadsheets/d/' + spreadsheet_id)

    if __name__ == '__main__':
        main()
