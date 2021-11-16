import pandas as pd
data=pd.read_excel('/Users/xuchangmao/Desktop/工作/排放模型/平台数据/LFNA4LJB3LTB12607测试数据---清洗后数据片段库/市区片段库/市区片段数据.xlsx')
start = '2021-07-29'
end = '2021-08-14'
dates = pd.date_range(start, end, freq='4D')
dates.strftime("%Y-%m-%d").tolist()
