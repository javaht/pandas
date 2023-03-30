import  pandas as pd

# 从 HTML 页面中读取数据
# url = 'https://www.runoob.com'
# dfs = pd.read_html(url)
# df = dfs[0] # 选择第一个数据框

df = pd.read_html("https://stock.qianzhan.com/hs/lirun_600166.sh.html")
# 显示前五行数据
# df.head()
# # 显示后五行数据
# df.tail()
# # 显示数据信息
# df.info()
# # 显示基本统计信息
# df.describe()
# # 显示数据的行数和列数
# df.shape

# nb = df[0]['2021年年报']   通过列名筛选

# nb  = df[0].loc[2, '2021年年报']  #行号和列名

# nb =  df[0].iloc[2, 4]  #行号和列号

# nb = df.filter(items=[column_name1, column_name2])  #选择指定的列

# nb =  df[0].filter(regex='2021年年报')


df =   df[0].filter(regex=' |2021年年报')
df.columns = ['name','number']

print(df[df['name'] == '销售费用(元)'])

# engine = sqlalchemy.create_engine("mysql+pymysql://root:123456@localhost:3306/zht?charset=utf8")
# df.to_sql(name='表名',con=engine,if_exists='replace',index=True)

print(df[df['name'] == '销售费用(元)'])


# # 读取 JSON 数据
# df = pd.read_json('data.json')
#
# # 删除缺失值
# df = df.dropna()
#
# # 用指定的值填充缺失值
# df = df.fillna({'age': 0, 'score': 0})
#
# # 重命名列名
# df = df.rename(columns={'name': '姓名', 'age': '年龄', 'gender': '性别', 'score': '成绩'})
#
# # 按成绩排序
# df = df.sort_values(by='成绩', ascending=False)
#
# # 按性别分组并计算平均年龄和成绩
# grouped = df.groupby('性别').agg({'年龄': 'mean', '成绩': 'mean'})
#
# # 选择成绩大于等于90的行，并只保留姓名和成绩两列
# df = df.loc[df['成绩'] >= 90, ['姓名', '成绩']]
#
# # 计算每列的基本统计信息
# stats = df.describe()
#
# # 计算每列的平均值
# mean = df.mean()
#
# # 计算每列的中位数
# median = df.median()
#
# # 计算每列的众数
# mode = df.mode()
#
# # 计算每列非缺失值的数量
# count = df.count()
