'''
Use ploty to visualize the resulting trade strategy data
'''
import pandas as pd
import plotly.express as px
from plotly.subplots import make_subplots
import config


def visualize_pnl():
    '''visualize the fx rates, signal, and the associated pnl'''
    df_main = pd.read_csv(config.STRAT_OUT_FILE,index_col='Date')

    #adjusting to fit the graph
    df_main['JPY'] = df_main['JPY'] / 100.0
    df_main['signal'] = df_main['signal'] * 1.5
    subfig = make_subplots(specs=[[{"secondary_y": True}]])

    #now compiling graphs
    fig = px.line(df_main, x=df_main.index, y=['AUD','CAD','JPY'])

    fig2 = px.line(df_main, x=df_main.index, y=['pnl'])
    fig2.update_traces(marker_color='maroon')
    fig2.update_traces(yaxis="y2")

    fig3 = px.bar(df_main, x=df_main.index, y=['signal'])
    fig3.update_traces(marker_color='grey')
    subfig.add_traces(fig.data + fig2.data + fig3.data)
    subfig.show()
    subfig.write_html(config.OUTPUT_DIR + 'result.html')

