import os
import json
import requests
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# --- Google Sheets Setup ---
SPREADSHEET_NAME = "Big Basket Tracker"
SHEET_NAME = "Dump"

# --- Authenticate with Google via GitHub Secret ---
google_creds = os.environ.get("GSHEET_SECRET")
creds_dict = json.loads(google_creds)

scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scope)

# Connect to Google Sheets
client = gspread.authorize(creds)
sheet = client.open(SPREADSHEET_NAME).worksheet(SHEET_NAME)

# --- API Call to Foodspark ---
url = "https://www.foodspark.io/api/big-basket/"
response = requests.get(url)
data = response.json()

# Clear existing sheet content (optional, if needed)
# sheet.clear()

# Append header row
headers = list(data[0].keys())
sheet.append_row(headers)

# Append each store's data
for store in data:
    sheet.append_row([store.get(key, "") for key in headers])

