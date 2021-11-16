import pandas as pd
import numpy as np

data = pd.read_excel('/Users/xuchangmao/Desktop/工作/排放模型/燃油周期/周期验证/7月29日-8月15原始数据.xlsx')


def moving_average(interval, window_size):
    window = np.ones(int(window_size)) / float(window_size)
    return np.convolve(interval, window, 'same')  # numpy的卷积函数


x = data['油箱液位'].index.to_list()
y_fuel = data['油箱液位'].to_list()  # 初始的油箱液位数据，list格式
y_fuel_array = np.array(y_fuel)  # 滤波处理之前需要转换为array
y_new_fuel = moving_average(interval=y_fuel_array, window_size=2000)  # 初始的油箱液位数据进行滤波处理
y_fuel_pd = pd.DataFrame(y_fuel_array)  # 原始的油箱液位，转换为dataframe
y_new_fuel_pd = pd.DataFrame(y_new_fuel)  # 处理后的油箱液位，转换为dataframe


fuel_diff = y_new_fuel_pd - y_new_fuel_pd.shift(20)  # 处理后的数据进行差分处理，20秒差分
fuel_point = fuel_diff[fuel_diff[0] > 0.3][0]  # 变化量大于30%的点定位为加油点
fuel_index = fuel_point.index.to_frame()  # 找到加油点的index，也就是时间
fuel_index_diff = fuel_index - fuel_index.shift(1)  # 加油点index的差分，用来寻找端点index
# 如果差分大于半天的秒数，那么就认为发生了加油行为，
fuel_cycle = fuel_index_diff[fuel_index_diff[0] > 43200][0].index.to_list()  # 用这个list来保留周期的信息，list中就是周期端点

dfs = np.split(data, fuel_cycle, axis=0)

for i in range(len(dfs)):
    dfs[i].to_excel(str(i) + '号周期数据.xlsx')

y_urea = data['反应剂余量'].to_list()  # 初始的尿素液位数据，list格式
y_urea_array = np.array(y_urea)  # 滤波处理之前需要转换为array
y_new_urea = moving_average(interval=y_urea_array, window_size=2000)  # 初始的尿素液位数据进行滤波处理
y_urea_pd = pd.DataFrame(y_urea_array)  # 原始的尿素液位，转换为dataframe
y_new_urea_pd = pd.DataFrame(y_new_urea)  # 处理后的尿素液位，转换为dataframe


urea_diff = y_new_urea_pd - y_new_urea_pd.shift(600)  # 处理后的数据进行差分处理，20秒差分
urea_point = urea_diff[urea_diff[0] > 15][0]  # 变化量大于30%的点定位为加油点
urea_index = urea_point.index.to_frame()  # 找到加油点的index，也就是时间
urea_index_diff = urea_index - urea_index.shift(1)  # 加油点index的差分，用来寻找端点index
# 如果差分大于半天的秒数，那么就认为发生了加油行为，
urea_cycle = urea_index_diff[urea_index_diff[0] > 13200][0].index.to_list()  # 用这个list来保留周期的信息，list中就是周期端点
