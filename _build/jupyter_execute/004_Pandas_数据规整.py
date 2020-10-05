#!/usr/bin/env python
# coding: utf-8

# % # Pandas 数据规整

# In[1]:


from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all" 


# In[2]:


import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels as sm


# ## 数据导入与导出
# 
# ```python
# pd.read_csv('examples/ex1.csv')
# pd.read_table('examples/ex1.csv', sep=',')
# 
# data.to_csv('examples/out.csv')
# 
# 
# xlsx = pd.ExcelFile('examples/ex1.xlsx')
# pd.read_excel(xlsx, 'Sheet1')
# ```
# 
# 

# ## 数据规整

# ### 行筛选
# 
# #### 条件筛选
# 
# ```
# df.query(expr, inplace=False, **kwargs)
# ```
# 
# #### 行去重
# 
# ```
# df.drop_duplicates()
# ```
# 
# #### 预览头部
# 
# ```
# df.head(n)
# ```
# 
# #### 预览尾部
# 
# ```
# df.tail(n)
# ```
# 
# #### 按比例采样
# 
# ```
# df.sample(frac=0.5)
# ```
# 
# #### 按数量采样
# 
# ```
# df.sample(n=10)
# ```
# 
# #### 按值取top
# 
# ```
# df.nlargest(n, 'value')
# df.nsmallest(n, 'value')
# ```
# 

# In[3]:


df = pd.DataFrame({'A': range(1, 6),
                   'B': range(10, 0, -2),
                   'C C': range(10, 5, -1)})
df
df.query('A > B')
# 等价于
df[df.A > df.B]
df.query('B == `C C`')  # 列名中有空格时，要用背引号包围
# 等价于
df[df.B == df['C C']]


# ### 行排序
# 
# 用sort_values方法，在排序时，任何缺失值默认都会被放到末尾

# In[4]:


frame = pd.DataFrame({'b': [4, 7, -3, 2], 'a': [0, 1, 0, 1]})
frame
frame.sort_values(by=['b','a'],ascending = [True,False])


# ### 列筛选
# 
# #### 根据列标签筛选
# 
# ```
# df.loc[:,'x2':'x4']
# ```
# 
# #### 根据列位置筛选
# 
# ```
# df.iloc[:,[1,2,5]]
# ```
# 
# #### 根据列标签特征筛选
# 
# ```
# df.filter(regex='regex')
# ```
# 
# #### 丢弃列
# 
# ```
# df.drop(columns=['Length','Height'])
# ```
# 
# #### 列重命名
# 
# ```
# df.rename(columns = {'y':'year'})
# ```

# ### 增加新列
# 
# ```
# df.assign(Area=lambda df: df.Length*df.Height)
# ```
# 

# In[5]:


df = pd.DataFrame({'temp_c': [17.0, 25.0]},
                   index=['Portland', 'Berkeley'])
df.assign(temp_f=lambda x: x.temp_c * 9 / 5 + 32)
df.assign(temp_f=df['temp_c'] * 9 / 5 + 32)
df.assign(temp_f=lambda x: x['temp_c'] * 9 / 5 + 32,
          temp_k=lambda x: (x['temp_f'] +  459.67) * 5 / 9)  # 引用了刚创建的列
# df.assign(temp_f=df['temp_c'] * 9 / 5 + 32,
#           temp_k=(df['temp_f'] +  459.67) * 5 / 9)  # 无法引用刚创建的列


# ### 层次化索引
# 
# 可以通过unstack方法将这段数据重新安排到一个DataFrame中，unstack的逆运算是stack

# In[6]:


data = pd.Series(np.random.randn(9),
                 index=[['a', 'a', 'a', 'b', 'b', 'c', 'c', 'd', 'd'],
                        [1, 2, 3, 1, 3, 1, 2, 2, 3]])
data
data.unstack()
data.unstack().stack()


# In[7]:


frame = pd.DataFrame(np.arange(12).reshape((4, 3)),
                      index=[['a', 'a', 'b', 'b'], [1, 2, 1, 2]],
                      columns=[['Ohio', 'Ohio', 'Colorado'],
                               ['Green', 'Red', 'Green']])
frame
frame.index.names = ['key1', 'key2']
frame.columns.names = ['state', 'color']
frame


# 有时，你需要重新调整某条轴上各级别的顺序，或根据指定级别上的值对数据进行排序。swaplevel接受两个级别编号或名称，并返回一个互换了级别的新对象

# In[8]:


frame.swaplevel('key1', 'key2')
frame.sort_index(level=1)


# 根据级别进行汇总
# 

# In[9]:


frame.sum(level='key2')


# 人们经常想要将DataFrame的一个或多个列当做行索引来用，或者可能希望将行索引变成DataFrame的列

# In[10]:


frame = pd.DataFrame({'a': range(7), 'b': range(7, 0, -1),
                       'c': ['one', 'one', 'one', 'two', 'two',
                             'two', 'two'],
                       'd': [0, 1, 2, 0, 1, 2, 3]})
frame
frame2 = frame.set_index(['c', 'd'])
frame2

# 默认情况下，那些列会从DataFrame中移除，但也可以将其保留下来
frame.set_index(['c', 'd'], drop=False)
# reset_index的功能跟set_index刚好相反，层次化索引的级别会被转移到列里面
frame2.reset_index()


# ### 数据合并（按值）
# 
# pandas.merge 可根据一个或多个键将不同DataFrame中的行连接起来。SQL或其他关系型数据库的用户对此应该会比较熟悉，因为它实现的就是数据库的join操作。
# 
# pandas.merge函数，都可以作为DataFrame对象的merge方法。
# 
# 默认情况下，merge做的是“内连接”；结果中的键是交集。其他方式还有"left"、"right"以及"outer"。外连接求取的是键的并集，组合了左连接和右连接的效果。
# 
# 如果没有指定，merge就会将重叠列的列名当做键。不过，最好明确指定一下。如果两个对象的列名不同，也可以分别进行指定。
# 
# 多对多连接产生的是行的笛卡尔积。要根据多个键进行合并，传入一个由列名组成的列表即可。
# 
# 如果有重叠的列非指定的列，则列名后会加`_x`、`_y`作为后缀，也可以自己指定后缀，用suffixes参数。

# In[11]:


df1 = pd.DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'a', 'b'],
                    'data1': range(7)})
df2 = pd.DataFrame({'key': ['a', 'b', 'd'],
                    'data2': range(3)})
df1
df2

pd.merge(df1, df2)
pd.merge(df1, df2, on='key')

df3 = pd.DataFrame({'lkey': ['b', 'b', 'a', 'c', 'a', 'a', 'b'],
                    'data1': range(7)})
df4 = pd.DataFrame({'rkey': ['a', 'b', 'd'],
                    'data2': range(3)})
pd.merge(df3, df4, left_on='lkey', right_on='rkey')

pd.merge(df1, df2, how='outer')

left = pd.DataFrame({'key1': ['foo', 'foo', 'bar'],
                     'key2': ['one', 'two', 'one'],
                     'lval': [1, 2, 3]})
right = pd.DataFrame({'key1': ['foo', 'foo', 'bar', 'bar'],
                      'key2': ['one', 'one', 'one', 'two'],
                      'rval': [4, 5, 6, 7]})
pd.merge(left, right, on=['key1', 'key2'], how='outer')

df3.merge(df4, left_on='lkey', right_on='rkey')


# ### 数据拼接（按索引）
# 
# concat只能作为函数，不能作为方法
# 
# - 用 concat 函数，默认为纵向拼接，各列对齐（不同列取并集），各行堆叠，未重叠部分填充NaN。
# - axis=1 表示横向拼接，各行对齐（不同行取并集），各列堆叠，未重叠部分填充NaN。
# - join='inner'表示不同列或行时取交集而非并集。
# - 假设你想要在连接轴上创建一个层次化索引。使用keys参数即可达到这个目的。

# In[12]:


df1 = pd.DataFrame(np.arange(6).reshape(3, 2), index=['a', 'b', 'c'],
                   columns=['one', 'two'])
df2 = pd.DataFrame(5 + np.arange(9).reshape(3, 3), index=['a', 'c','d'],
                   columns=['one','three', 'four'])
df1
df2
pd.concat([df1, df2])
pd.concat([df1, df2],axis=1)
pd.concat([df1, df2],join='inner')
pd.concat([df1, df2],axis=1,join='inner')
pd.concat([df1, df2], keys=['level1', 'level2'])
# df1.concat(df2)  # concat只能作为函数，不能作为方法

df3 = pd.DataFrame(np.arange(6).reshape(3, 2),
                   columns=['one', 'two'])
df4 = pd.DataFrame(4 + np.arange(6).reshape(3, 2),
                   columns=['one', 'two'])
df3
df4
pd.concat([df3, df4])  # 保留原索引，保留重复数据
pd.concat([df3, df4],ignore_index=True)  # 产生新索引，保留重复数据，相当于union all


# ### 宽转长
# 
# 可以是函数，也可以是方法。
# 
# ```
# pd.melt(DataFrame, id_vars=None, value_vars=None, var_name=None, value_name='value', col_level=None) -> DataFrame
# ```
# 

# In[13]:


df = pd.DataFrame({'group': ['foo', 'bar', 'baz'],
                    'A': [1, 2, 3],
                    'B': [4, 5, 6],
                    'C': [7, 8, 9]})
df
melted = pd.melt(df, ['group'])
melted
df.melt(id_vars=['group'],value_vars=['A','B','C'], 
        var_name='key',value_name='value')


# ### 长转宽
# 
# 
# 
# ```
# df.pivot(index=None, columns=None, values=None) -> 'DataFrame'
# ```
# 
# index未指定时，用已存在的index，values未指定时，剩下所有列作为value。

# In[14]:


reshaped = melted.pivot(index='group',columns='variable', values='value')
reshaped
reshaped.reset_index()  # 将索引变成普通列


# ### 哑变量
# 
# 

# In[15]:


df = pd.DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'b'],
                    'data1': range(6)})
df
pd.get_dummies(df['key'])


# ### 数据汇总
# 
# GroupBy的size方法给出分组大小.
# 你可以向groupby传入as_index=False以分组列自动作为行索引。

# In[16]:


df = pd.DataFrame({'key1' : ['a', 'a', 'b', 'b', 'a'],
                   'key2' : ['one', 'two', 'one', 'two', 'one'],
                   'data1' : np.random.randn(5),
                   'data2' : np.random.randn(5)})
df
grouped = df['data1'].groupby(df['key1'])
grouped.mean()
df.groupby(['key1', 'key2']).size()

(df['data1'].
    groupby([df['key1'], df['key2']]).
    mean())  
# 多分组，类似于R 管道操作 %>% 的写法，由于点的左右都不能断行，要在外面加括号
# 下面两种未加括号的写法都会报错

# df['data1']
# .groupby([df['key1'], df['key2']])
# .mean()  # 多分组

# df['data1'].
# groupby([df['key1'], df['key2']]).
# mean()  # 多分组

(df.
    groupby([df['key1'], df['key2']]).
    mean()) 
# 实质是在每一列，每个分组内都采取mean函数，并且将groupby的列作为index
(df.
    groupby([df['key1'], df['key2']]).
    mean().
    reset_index()) 

(df.
    groupby([df['key1'], df['key2']], as_index=False).
    mean()) 


# 实际上，分组键可以是任何长度适当的数组

# In[17]:


states = np.array(['Ohio', 'California', 'California', 'Ohio', 'Ohio'])
years = np.array([2005, 2005, 2006, 2005, 2006])
df['data1'].groupby([states, years]).mean()


# 通常，分组信息就位于相同的要处理DataFrame中。这里，你还可以将列名（可以是字符串、数字或其他Python对象）用作分组键。这意味着不用再外面写原数据框名，加方括号。

# In[18]:


df.groupby('key1').mean()
df.groupby(['key1', 'key2']).mean()


# 你可能已经注意到了，第一个例子在执行df.groupby('key1').mean()时，结果中没有key2列。这是因为df['key2']不是数值数据（俗称“麻烦列”），所以被从结果中排除了。默认情况下，所有数值列都会被聚合，虽然有时可能会被过滤为一个子集，稍后就会碰到。

# 如果用一个（单个字符串）或一组（字符串数组）列名对其进行索引，就能实现选取部分列进行聚合的目的。
# 
# ```python
# df.groupby('key1')['data1']
# df.groupby('key1')[['data2']]
# ```
# 是以下代码的语法糖
# ```python
# df['data1'].groupby(df['key1'])
# df[['data2']].groupby(df['key1'])
# ```

# #### 通过函数进行分组
# 
# 将函数跟数组、列表、字典、Series混合使用也不是问题，因为任何东西在内部都会被转换为数组

# In[19]:


people = pd.DataFrame(np.random.randn(5, 5),
                       columns=['a', 'b', 'c', 'd', 'e'],
                       index=['Joe', 'Steve', 'Wes', 'Jim', 'Travis'])
people
people.groupby(len).sum()


# #### 聚合函数
# 
# 常用聚合函数如下表。如果要使用你自己的聚合函数，只需将其传入aggregate或agg方法即可。自定义聚合函数要比表10-1中那些经过优化的函数慢得多。这是因为在构造中间分组数据块时存在非常大的开销（函数调用、数据重排等）。
# 
# ![](groupby聚合函数.png)

# In[20]:


df
grouped = df.groupby('key1')
grouped['data1'].quantile(0.9)
grouped.describe()

def peak_to_peak(arr):
    return arr.max() - arr.min()
grouped.agg(peak_to_peak)
grouped.agg(['mean','std',peak_to_peak])


# #### 离散化和面元划分
# 
# 跟“区间”的数学符号一样，圆括号表示开端，而方括号则表示闭端（包括）。哪边是闭端可以通过right=False进行修改

# In[21]:


ages = [17,20, 22, 25, 27, 21, 23, 37, 31, 61, 45, 41, 32,101]
bins = [18, 25, 35, 60, 100]
group_names = ['Youth', 'YoungAdult', 'MiddleAged', 'Senior']
pd.cut(ages, bins)
pd.cut(ages, bins,labels=group_names)
pd.cut(ages, [18, 26, 36, 61, 100], right=False)


# 如果向cut传入的是面元的数量而不是确切的面元边界，则它会根据数据的最小值和最大值计算等长面元。

# In[22]:


data = np.random.rand(20)
pd.cut(data, 4, precision=2)  # 选项precision=2，限定小数只有两位。


# qcut是一个非常类似于cut的函数，它可以根据样本分位数对数据进行面元划分。根据数据的分布情况，cut可能无法使各个面元中含有相同数量的数据点。而qcut由于使用的是样本分位数，因此可以得到大小基本相等的面元.与cut类似，你也可以传递自定义的分位数（0到1之间的数值，包含端点）.

# In[23]:


data = np.random.randn(1000)
cats = pd.qcut(data, 4)
cats
pd.value_counts(cats)
pd.qcut(data, [0, 0.1, 0.5, 0.9, 1.])


# In[24]:


frame = pd.DataFrame({'data1': np.random.randn(1000),
                     'data2': np.random.randn(1000)})
quartiles = pd.cut(frame.data1, 4)

def get_stats(group):
    return {'min': group.min(), 'max': group.max(),
            'count': group.count(), 'mean': group.mean()}
grouped = frame.data2.groupby(quartiles)
grouped.apply(get_stats).unstack()

grouping = pd.qcut(frame.data1, 10, labels=False)
grouped = frame.data2.groupby(grouping)
grouped.apply(get_stats).unstack()


# ### 透视表：同时实现长转宽与行列聚合
# 
# DataFrame有一个pivot_table方法，此外还有一个顶级的pandas.pivot_table函数。除能为groupby提供便利之外，pivot_table还可以添加分项小计，也叫做margins。

# In[25]:


melted
melted.pivot(index='group',columns='variable', values='value')
# 与上面功能相同
melted.pivot_table(index='group',columns='variable', values='value')
# 增加聚合项，默认为平均值
melted.pivot_table(index='group',columns='variable', values='value',margins=True)
# 增加聚合项，合计
melted.pivot_table(index='group',columns='variable', values='value',margins=True,aggfunc=sum)


# 
# 

# In[ ]:




