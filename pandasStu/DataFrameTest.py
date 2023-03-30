import pandas as pd

# pandas.DataFrame( data, index, columns, dtype, copy)
#
# data：一组数据(ndarray、series, map, lists, dict 等类型)。
# index：索引值，或者可以称为行标签。
# columns：列标签，默认为 RangeIndex (0, 1, 2, …, n) 。
# dtype：数据类型。
# copy：拷贝数据，默认为 False

#使用列表创建
# data = [['Google',10],['Runoob',12],['Wiki',13]]
# df = pd.DataFrame(data,columns=['Site','Age'],dtype=float)
# print(df)

#使用ndarrays创建
# data = {'Site':['Google', 'Runoob', 'Wiki'], 'Age':[10, 12, 13]}
# df = pd.DataFrame(data)
# print (df)


#还可以使用字典（key/value），其中字典的 key 为列名:
# data = [{'a': 1, 'b': 2},{'a': 5, 'b': 10, 'c': 20}]
# df = pd.DataFrame(data)
# print (df)

#Pandas 可以使用 loc 属性返回指定行的数据，如果没有设置索引，第一行索引为 0，第二行索引为 1，以此类推：
#data = { "calories": [420, 380, 390],"duration": [50, 40, 45]}
#df = pd.DataFrame(data)
# 返回第1,2行
# print(df.loc[[0, 1]])

#我们可以指定索引值，如下实例
df = pd.DataFrame(data, index = ["day1", "day2", "day3"])
print(df)