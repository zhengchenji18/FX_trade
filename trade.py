'''
contains trade strategy, computing from input df
'''

import pandas as pd
import config


def moving_average():
    '''
    simply strategy
    when all currency spot > mv, buy end of today and sell 5 days later based on CAD
    trade singal is for usdcad
    trade pnl using $1mm invested
    '''
    df_main = pd.read_csv(config.SRC_FILE,index_col='Date')
    cols = list(df_main.columns)

    for col in cols:
        df_main[col + '_mv20'] = df_main[col].rolling(window=20).mean()
        df_main[col + '_signal'] = 0
        df_main.loc[df_main[col] > df_main[col + '_mv20'],col + '_signal'] = 1

    df_main['signal'] = 1
    for col in cols:
        df_main['signal'] = df_main['signal'] * df_main[col + '_signal']

    df_main['pnl'] = df_main['signal'] * df_main['CAD'].pct_change(periods=-5)
    df_main['pnl'] = df_main['pnl'] * 1000000.0
    df_main['pnl'] = df_main['pnl'].cumsum()


    cols.append('pnl')
    cols.append('signal')
    df_main = df_main[cols]

    df_main.to_csv(config.STRAT_OUT_FILE)
