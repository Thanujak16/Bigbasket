import gspread
from oauth2client.service_account import ServiceAccountCredentials
import requests

# === CONFIG ===
GOOGLE_SHEET_NAME = 'Big Basket Tracker'
SHEET_TAB_NAME = 'Dump'
JSON_URL = 'https://raw.githubusercontent.com/yourusername/bigbasket-data/main/bigbasket_stores.json'

# === AUTHENTICATION ===
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
client = gspread.authorize(creds)

# === LOAD SHEET ===
sheet = client.open(Big Basket Tracker).worksheet(Dump)
sheet.clear()

# === FETCH JSON DATA FROM GITHUB ===
response = requests.get(JSON_URL)
data = response.json()

# === HEADER ROW ===
headers = list(data[0].keys())
sheet.append_row(headers)

# === DATA ROWS ===
for row in data:
    sheet.append_row([row.get(key, '') for key in headers])
