import pandas as pd
import quandl

# Google Stocks
df = quandl.get('WIKI/GOOGL')

df = df[
    [
        'Adj. Open', # Starting price for the day
        'Adj. High',
        'Adj. Low',
        'Adj. Close',
        'Adj. Volume'
    ]
]

# High minus low % volatility
df['HL_PCT'] = (df['Adj. High'] - df['Adj. Low']) / df['Adj. Low'] * 100.0

# daily % change
df['PCT_change'] = (df['Adj. Close'] - df['Adj. Open']) / df['Adj. Open'] * 100.0

df = df[['Adj. Close', 'HL_PCT', 'PCT_change', 'Adj. Volume']]

# Value we want in the future
forecast_col = 'Adj. Close'