'''
pulling fx data from endpoints
'''

import requests
import pandas as pd
import config

def get_data(date):
    '''requesting data by date from endpoint'''
    date_str = date.strftime('%Y-%m-%d 00:00:00')
    req_str = f'http://localhost:5000/get_rates?date={date_str}'
    r = requests.get(req_str)

    if r.status_code == 200:
        return r.json()
    return []

def pull_data(str_start_dt:str,str_end_dt:str):
    '''combining fx rate data from a range of dates'''
    config.LOGGER.info("Getting data")
    start_dt = pd.to_datetime(str_start_dt,format='%Y-%m-%d')
    end_dt = pd.to_datetime(str_end_dt,format='%Y-%m-%d')

    res = []
    for date in pd.date_range(start_dt,end_dt):
        config.LOGGER.info("Getting data for %s", str(date))
        data = get_data(date)
        if data != []:
            for i in data:
                res.append(i)

    cols = ['Date','Currency','Close']
    df = pd.DataFrame(res,columns = cols)
    df['Date'] = pd.to_datetime(df['Date'],format='%Y-%m-%d 00:00:00')

    df_final = df.pivot(index='Date',columns='Currency',values='Close')
    df_final.to_csv(config.SRC_FILE)
