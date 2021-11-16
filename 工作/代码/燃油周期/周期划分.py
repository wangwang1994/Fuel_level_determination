import pandas as pd
import numpy as np

data = pd.read_excel(r'E:\工作备份\工作\排放模型\加油周期\8月17日-9月5日---清洗后数据.xlsx')


def moving_average(interval, window_size):
    window = np.ones(int(window_size)) / float(window_size)
    return np.convolve(interval, window, 'same')  # numpy的卷积函数


x = data['油箱液位'].index.to_list()
y = data['油箱液位'].to_list()
y_array = np.array(y)
y_new = moving_average(interval=y_array, window_size=2000)
y_pd = pd.DataFrame(y_array)
y_new_pd = pd.DataFrame(y_new)

y_new_series = pd.Series(y_new)
# is increasing
chafen=y_new_pd-y_new_pd.shift(20)
fuel_point=chafen[chafen[0]>0.3][0]
fuel_index=fuel_point.index.to_frame()
fuel_chafen=fuel_index-fuel_index.shift(1)
fuel_cycle=fuel_chafen[fuel_chafen[0]>43200][0].index.to_list()

dfs=np.split(data, fuel_cycle, axis=0)

for i in range(len(dfs)):
    dfs[i].to_excel(str(i)+'号周期数据.xlsx')




