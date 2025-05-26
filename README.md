# Bigbasket

name: Update Big Basket Sheet Daily

on:
  schedule:
    - cron: "30 0 * * *"  # Runs at 6:00 AM IST (0:30 UTC)
  workflow_dispatch:

jobs:
  update-sheet:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: "3.10"

      - name: Install dependencies
        run: pip install gspread oauth2client requests

      - name: Create credentials.json
        run: |
          echo "${{ secrets.GOOGLE_CREDENTIALS }}" > credentials.json

      - name: Run script
        run: python update_bigbasket.py
