from data import get_data
import pandas as pd
import logging


LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.INFO)
# create formatter
LOG_DATEFMT = '%Y-%m-%d %H:%M:%S'
LOG_FORMAT = ('\n[%(levelname)s/%(name)s:%(lineno)d] %(asctime)s ' +
              '(%(processName)s/%(threadName)s)\n> %(message)s')
FORMATTER = logging.Formatter(LOG_FORMAT, datefmt=LOG_DATEFMT)
FH = logging.FileHandler('trade.log')  # create file handler
FH.setLevel(logging.DEBUG)  # set handler level to debug
FH.setFormatter(FORMATTER)  # add formatter to fh
LOGGER.addHandler(FH)  # add file handler to logger

src_file_name = 'fx.csv'


def pullData(str_start_dt:str,str_end_dt:str):
    LOGGER.info("Getting data")
    start_dt = pd.to_datetime(str_start_dt,format='%Y-%m-%d')
    end_dt = pd.to_datetime(str_end_dt,format='%Y-%m-%d')

    res = []
    for date in pd.date_range(start_dt,end_dt):
        LOGGER.info("Getting data for " + str(date))
        data = get_data(date)       
        if data != []:
            for i in data:
                res.append(i)

    cols = ['Date','Currency','Close']
    df = pd.DataFrame(res,columns = cols)
    df['Date'] = pd.to_datetime(df['Date'],format='%Y-%m-%d 00:00:00')

    df_final = df.pivot(index='Date',columns='Currency',values='Close')
    df_final.to_csv(src_file_name)

def run(str_start_dt:str,str_end_dt:str):
    pullData(start_dt,end_dt)  

    df_main = pd.read_csv(src_file_name)
    print(df.head())

if __name__ == '__main__':
    LOGGER.info("Start running")

    start_dt = '2021-08-02'
    #start_dt = '2022-07-29'
    end_dt = '2022-08-01'
    run(start_dt,end_dt)

    LOGGER.info("end running")