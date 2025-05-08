# CRM (Customer Relationship Management)

# 📄 Mini CRM System for Insurance Renewals

A lightweight, automation-driven CRM tool built using **Python**, **Google Sheets**, and **Apps Script** to help insurance brokers **never miss a policy renewal again**.

---

## 🚀 Features

- **Extracts key data from insurance PDFs**  
  - Client Name  
  - Renewal Date  
  - Registration Number  

- **Syncs data to Google Sheets**  
  Central dashboard powered by Google Sheets for real-time data visibility.

- **Automated Email Reminders**  
  - Personalized renewal alerts sent via Gmail.
  - Triggered 30 days before policy expiry.
  - Example subject: `Insurance Expiry Alert`.

---

## 🔧 Tech Stack

- **Python**  
  - [`PyMuPDF`](https://pymupdf.readthedocs.io/en/latest/) (for PDF parsing)  
  - `re` (regex)  
  - [`gspread`](https://github.com/burnash/gspread) + `oauth2client` (Google Sheets API)  

- **Google Apps Script**  
  - Hourly function: `sendRenewalReminders()`  
  - Gmail integration for sending emails

---

## 🧠 How It Works

1. **PDF Data Extraction**
   - Uses `PyMuPDF` and `regex` to pull:
     - `Client Name`
     - `Renewal Date`
     - `Registration Number`

2. **Sync to Google Sheets**
   - Uploads extracted data using `gspread` + OAuth2 to a centralized spreadsheet.

3. **Automated Reminders**
   - Google Apps Script runs hourly.
   - Checks for policies expiring in exactly 30 days.
   - Sends customized emails with all relevant details.

---

## ✅ Benefits

- ❌ No more manual data entry  
- 🕐 No missed renewal deadlines  
- ⚙️ Scales easily to thousands of clients  
- 💡 Acts as a CRM-lite for small insurance businesses  

---
