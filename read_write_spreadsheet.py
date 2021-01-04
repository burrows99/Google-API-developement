#pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
from googleapiclient.discovery import build
from google.oauth2 import service_account
import webbrowser

SERVICE_ACCOUNT_FILE = 'keys.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
creds= None
creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES) #creates credentials

SAMPLE_SPREADSHEET_ID = '1XG-sQDgXxVO-b_qXW50cvJnzm2m9eYkHZUAlvMdsBRs' #sheet id

service = build('sheets', 'v4', credentials=creds)
sheet = service.spreadsheets()

#Read
result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,range='sheet1!A1:E15').execute()
values = result.get('values', [])
print(values)

#Write
entries=list()
for i in range(5):
        x=input('Enter string to be entered in the row: ')
        x=list(x)
        entries.append(x)
request=sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID,range='sheet2!A1',valueInputOption='USER_ENTERED',body={'values':entries}).execute()

#opening the spreadsheet
webbrowser.open('https://docs.google.com/spreadsheets/d/1XG-sQDgXxVO-b_qXW50cvJnzm2m9eYkHZUAlvMdsBRs/edit#gid=796952289')
