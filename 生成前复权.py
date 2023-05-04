pathDir='d:\\python\\解析通达信数据\\day\\sz'
targetDir='d:\\python\\解析通达信数据\\qfq\\sz'

import pandas as pd

# 读取数据
df = pd.read_csv('D:\\python\\解析通达信数据\\day\\sh\\sh600276.day.csv', dtype={'date': str})

# 将日期列转换为datetime类型
df['date'] = pd.to_datetime(df['date'], format='%Y%m%d')

# 按日期升序排列
df.sort_values('date', inplace=True)

# 添加复权因子列，默认为1
df['factor'] = 1

# 计算复权后的收盘价和开盘价
df['close_adj'] = df['close'] * df['factor'].cumprod()
df['open_adj'] = df['open'] * df['factor'].cumprod()
df['high_adj'] = df['high'] * df['factor'].cumprod()
df['low_adj'] = df['low'] * df['factor'].cumprod()
# 计算复权因子
for i in range(1, len(df)):
# 计算复权因子
    factor = df.loc[i-1, 'close'] / df.loc[i-1, 'close_adj']
    # 更新当前行复权因子
    df.loc[i, 'factor'] = factor
    # 更新当前行复权收盘价和开盘价
    df.loc[i, 'close_adj'] = df.loc[i, 'close'] * factor
    df.loc[i, 'open_adj'] = df.loc[i, 'open'] * factor

# 将复权后的收盘价、开盘价、最高价、最低价保存到文件
df[['date', 'open_adj', 'high_adj', 'low_adj', 'close_adj', 'amout', 'vol', 'str07']].to_csv(targetDir+'\\data_adj_4.csv', index=False)