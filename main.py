'''
This is the main entry point to the fx trade program
It calls functions to
1.get data
2.compute trade signal and pnl
3.visualize using plotly
'''
# task:
#take commandline argument for main
import argparse
import config
from data import pull_data
from trade import moving_average
from graph import visualize_pnl


def run(str_start_dt:str,str_end_dt:str):
    '''run the main
       note that pulling data is taking a long time
       since the endpoint is build using day by day
       would have been better to pull all data
       but just want to keep it the same as what's provided
       during the interview
       commented out pull data
       pulled data already stored as fx.csv
    '''
    #pull_data(start_dt,end_dt)
    moving_average()
    visualize_pnl()

def init_argparse() -> argparse.ArgumentParser:
    '''init arguments'''
    parser = argparse.ArgumentParser()
    parser.add_argument("-s","--start_dt", required=False, \
                 help="start_dt for pulling data.format:YYYY-MM-DD")
    parser.add_argument("-e","--end_dt", required=False, \
                 help="end_dt for pulling data.format:YYYY-MM-DD")
    return parser

if __name__ == '__main__':
    config.LOGGER.info("Start running")

    parser = init_argparse()
    args = parser.parse_args()

    #default dates
    start_dt = '2021-08-02'
    if args.start_dt:
        start_dt = args.start_dt
    end_dt = '2022-08-01'     
    if args.end_dt:
        end_dt = args.end_dt

    run(start_dt,end_dt)
    config.LOGGER.info("end running")
