### 0.- EXTRACTING DATASET FROM KAGGLE

import requests

rurl = 'https://www.kaggle.com/pavansubhasht/ibm-hr-analytics-attrition-dataset/downloads/WA_Fn-UseC_-HR-Employee-Attrition.csv/1'
local_filename = "dataset.csv"
kaggle_info = {'UserName': "saulgoodstuff", 'Password': "15975356356824AL"}

## ACCESSING KAGGLE
request = requests.get(url)
request = requests.post(request.url, data = kaggle_info)

## SAVING DATA INTO A FILE
to_file = open(local_filename,'w')
for chunk in request.iter_content(chunk_size=512*1024):
    if chunk:
        to_file.write(chunk)
to_file.close()





