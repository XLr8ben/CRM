import fitz  # PyMuPDF for PDF processing
import re
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Step 1: Extract text from PDF
pdf_path = r"C:\Users\ADMIN\Desktop\New folder\insurancedata.pdf"  # Change this to your PDF file
doc = fitz.open(pdf_path)

data_to_push = []

for page in doc:
    text = page.get_text("text")

    # Extract Renewal Date using Regex
    date_pattern = r"\b(\d{2}-[A-Za-z]{3}-\d{4})\b"
    matches = re.findall(date_pattern, text)
    
    # Extract Registration No using Regex
    reg_pattern = r"Registration No\s*:\s*([A-Z0-9]+)"
    reg_match = re.search(reg_pattern, text)

    if matches and reg_match:
        renewal_date = matches[0]  # First found renewal date
        reg_no = reg_match.group(1)  # Extract registration number

        # Store data
        data_to_push.append([renewal_date, reg_no])

# Step 2: Push to Google Sheets
# Google Sheets API setup
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)  # Add your credentials.json file
client = gspread.authorize(creds)

# Open Google Sheet (replace with your actual sheet ID)
sheet_id = "1SrPNVWmvDdutR9k8hKbU3em6qiO6BG7wJxUfqCRbgr8"
spreadsheet = client.open_by_key(sheet_id)  # Get Spreadsheet
sheet = spreadsheet.get_worksheet(0)  # Get first worksheet

# Add headers if the sheet is empty
if not sheet.get_all_values():
    sheet.append_row(["Renewal Date", "Registration No"])

# Append extracted data
sheet.append_rows(data_to_push)

print("Data successfully pushed to Google Sheets!")
