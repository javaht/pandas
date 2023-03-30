import pandas as pd

#根据索引值读取数据
#a = [1, 2, 3]
# myvar = pd.Series(a)
# print(myvar[1])

#指定索引值
# a = ["Google", "Runoob", "Wiki"]
# myvar = pd.Series(a, index = ["x", "y", "z"])
# print(myvar["y"])


#我们也可以使用 key/value 对象，类似字典来创建 Series
sites = {1: "Google", 2: "Runoob", 3: "Wiki"}
myvar = myvar = pd.Series(sites, index = [1, 2], name="Series-TEST" )
print(myvar)