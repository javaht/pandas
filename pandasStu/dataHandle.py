import pandas as pd

# DataFrame.dropna(axis=0, how='any', thresh=None, subset=None, inplace=False)
# axis：默认为 0，表示逢空值剔除整行，如果设置参数 axis＝1 表示逢空值去掉整列。
# how：默认为 'any' 如果一行（或一列）里任何一个数据有出现 NA 就去掉整行，如果设置 how='all' 一行（或列）都是 NA 才去掉这整行。
# thresh：设置需要多少非空值的数据才可以保留下来的。
# subset：设置想要检查的列。如果是多个列，可以使用列名的 list 作为参数。
# inplace：如果设置 True，将计算得到的值直接覆盖之前的值并返回 None，修改的是源数据。

# df = pd.read_csv("C:\pythonProject\pandas\datas\property-data.csv")

#把 n/a 和 NA 当作空数据，na 不是空数据
# print (df['NUM_BEDROOMS'])
# print (df['NUM_BEDROOMS'].isnull())


#na_values 可以额外指定缺失值
# missing_values = ["n/a", "na", "--"]
# df = pd.read_csv('C:\pythonProject\pandas\datas\property-data.csv', na_values = missing_values)
# print (df['NUM_BEDROOMS'])
# print (df['NUM_BEDROOMS'].isnull())

#删除空行的数据
# new_df = df.dropna()
# # new_df = df.dropnainplace = True)    替代原表数据
# print(new_df.to_string())

#移除指定列有空值的行
# df.dropna(subset=['ST_NUM'], inplace = True)
# print(df.to_string())

# 使用fillna()方法来替换一些空字段
# df.fillna('哈哈哈哈哈', inplace = True)
# print(df.to_string())

#Pandas使用 mean()、median() 和 mode() 方法计算列的均值（所有值加起来的平均值）、中位数值（排序后排在中间的数）和众数（出现频率最高的数）。


# 格式化日期
# data = { "Date": ['2020/12/01', '2020/12/02' , '20201226'],  "duration": [50, 40, 45]}
# df = pd.DataFrame(data, index = ["day1", "day2", "day3"])
# df['Date'] = pd.to_datetime(df['Date'])
# print(df.to_string())

# 清洗错误数据

person = { "name": ['Google', 'Runoob' , 'Taobao'], "age": [50, 40, 12345]}
df = pd.DataFrame(person)

# df.loc[2, 'age'] = 30 # 修改数据
# print(df.to_string())

# 大于120的数据替换
# for x in df.index:
#   if df.loc[x, "age"] > 120:
#     df.loc[x, "age"] = 120
# print(df.to_string())

#大于120的数据删除
# for x in df.index:
#   if df.loc[x, "age"] > 120:
#     df.drop(x, inplace = True)
# print(df.to_string())


#删除重复数据
# persons = {"name": ['Google', 'Runoob', 'Runoob', 'Taobao'], "age": [50, 40, 40, 23] }
# df = pd.DataFrame(persons)
# df.drop_duplicates(inplace = True)
# print(df)