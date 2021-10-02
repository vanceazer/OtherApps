import requests
import pandas as pd
import numpy as np
import schedule
import threading
import time



# Define urls
BASE_URL = 'https://prod-etraffika.azurewebsites.net'
INVOICE_DUPLICATION_FIX = f'{BASE_URL}/api/reconciliationmanager/cbs/duplicate/invoice/fix'

invoice = 'C:/Users/sirmi/Desktop/Duplicate_Invoices.xlsx'
invoice_df = pd.read_excel(invoice)
# print(invoice_df['InvoiceId'])
invoice_needed = invoice_df['InvoiceId']


# command to call the invoice duplication fix endpoint
def invoice_duplication_fix(item):
    body = {
        "invoiceId": invoice_id
    }
    invoice_dup_fix = requests.post(INVOICE_DUPLICATION_FIX, json=body)
    print(invoice_dup_fix.status_code)
    print(invoice_dup_fix.json())
    if invoice_dup_fix.status_code == 200:
        print('Invoice duplicate fix successful')
    else:
        print('Invoice duplicate fix failed')


for items in invoice_needed.values:
    print('-------------------------------------------')
    print(items)
    # compare = invoice_df[invoice_df['InvoiceId'] == items]
    # invoice_id = int(compare['InvoiceId'].values)

    # print(invoice_id)
    invoice_id = int(items)
    invoice_duplication_fix(items)
    print('-------------------------------------------')
