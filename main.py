import requests
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Google Sheet setup
SPREADSHEET_NAME = "Big Basket Tracker"
SHEET_NAME = "Dump"

# Authenticate with Google
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
client = gspread.authorize(creds)
sheet = client.open(SPREADSHEET_NAME).worksheet(SHEET_NAME)

# API call to foodspark
url = "https://www.foodspark.io/api/big-basket/"
response = requests.get(url)
data = response.json()

# Header row
headers = list(data[0].keys())
sheet.append_row(headers)

# Append each row
for store in data:
    sheet.append_row([store.get(key, "") for key in headers])
