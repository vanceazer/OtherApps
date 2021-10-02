import requests
import pandas as pd
import numpy as np
import schedule
import threading
import time



# Define urls
BASE_URL = 'https://prod-etraffika.azurewebsites.net'
OFFENCE_UPDATE_URL = f'{BASE_URL}/api/offense/update'

offence_data = 'C:/Users/sirmi/Desktop/offencesNew.xlsx'
offence_df = pd.read_excel(offence_data)
offence_ids = offence_df['id']


def listToString(s):
    # initialize an empty string
    str1 = ""

    # traverse in the string
    for ele in s:
        str1 = ele

        # return string
    return str1

# command to call the offence update endpoint
def offence_update(item):
    body = {
        "id": offence_id,
        "name": name,
        "code": code,
        "description": description,
        "additional": additional,
        "fineAmount": fineAmount,
        "finePoint": finePoint,
        "offenseCategoryId": offenseCategoryId,
        "organisationId": organisationId,
        "revenueGroupId": revenueGroupId,
        "revenueHeadId": revenueHead,
        "isActive": True
    }
    offence = requests.post(OFFENCE_UPDATE_URL, json=body)
    print(offence.status_code)
    # print(offence.json())
    if offence.status_code == 200:
        print('Offence Update successful')
    else:
        print('Offence Update failed')


for items in offence_ids.values:
    print('-------------------------------------------')
    print(items)
    compare = offence_df[offence_df['id'] == items]
    offence_id = int(compare['id'].values)
    print(offence_id)
    name = listToString(compare['name'])
    print(name)
    code = listToString(compare['code'])
    print(code)
    description = listToString(compare['description'])
    # print(description)
    additional = listToString(compare['additional'])
    # print(additional)
    fineAmount = int(compare['fineAmount'].values)
    # print(fineAmount)
    finePoint = int(compare['finePoint'].values)
    # print(finePoint)
    offenseCategoryId = int(compare['offenseCategoryId'].values)
    # print(offenseCategoryId)
    organisationId = int(compare['organisationId'].values)
    # print(organisationId)
    revenueGroupId = int(compare['revenueGroupId'].values)
    # print(revenueGroupId)
    revenueHead = int(compare['revenueHead'].values)
    # print(revenueHead)

    offence_update(items)

    print('-------------------------------------------')
