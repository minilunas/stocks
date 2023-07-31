import pandas as pd
import matplotlib.pyplot as plt

# Read in daily stock data
try:
    df = pd.read_csv('D:\python\解析通达信day日线数据\day\sh600196.day.csv')
except Exception as e:
    print(f"Error reading data: {e}")
    exit()

# Convert date column to datetime format
df['date'] = pd.to_datetime(df['date'])

# Set date column as index
df.set_index('date', inplace=True)

# Plot daily stock data
try:
    
    plt.plot(df['close'])
    plt.title('Daily Stock Chart')
    plt.xlabel('Date')
    plt.ylabel('Closing Price')
    plt.show()
except Exception as e:
    print(f"Error displaying plot: {e}")