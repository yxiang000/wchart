
## python基础面试中，列表排序往往是一个热门话题，今天就和大家聊聊python的排序知识点

### 首先呢python list内置sort()方法就可以用来排序，用法也相当简单
### 其次python内置的全局sortd()方法也可以对迭代的序列排序生成新的序列
- list内置sort()方法无返回值，直接在原有列表上进行操作
- sortd()方法有返回值生成新的序列

### 下面我们用例子说明


```python
#对列表list_a分别利用sort和sortd进行排序
list_a = [12,4,78,-3,-45,33,66,1,-8]
#sort排序
print('原有列表为：',list_a)
print('list.sort()在list基础上修改，无返回值')
list_a.sort()
print('list.sort()排序后的结果为：',list_a)
```

    原有列表为： [12, 4, 78, -3, -45, 33, 66, 1, -8]
    list.sort()在list基础上修改，无返回值
    list.sort()排序后的结果为： [-45, -8, -3, 1, 4, 12, 33, 66, 78]
    

### list.sort()默认升序排列，若想要降序排序只需添加反转参数reverse=True即可：


```python
list_a.sort(reverse=True)
print('升序排序结果为:',list_a)
```

    升序排序结果为: [78, 66, 33, 12, 4, 1, -3, -8, -45]
    


```python
list_a = [12,4,78,-3,-45,33,66,1,-8]
res = sorted(list_a)
print('sortd()排序有返回值，得到的排序结果为：',res)
```

    sortd()排序有返回值，得到的排序结果为： [-45, -8, -3, 1, 4, 12, 33, 66, 78]
    

## sortd()默认也是升序排序，若想降序排序也只需要添加reverse=True参数即可
### sortd（）常用参数有三个，reverse=True为其中一个，还有一个参数为list_a这个iterable可迭代对象，还有一个为key函数，也就是自定义的一个函数，可以对排序进行简单的操作，下面举例说明


```python
#对列表list_a使用lambada函数排序
list_a = [12,4,78,-3,-45,33,66,1,-8]
res_1 = sorted(list_a)
res_2 = sorted(list_a,reverse=True)
res_3 = sorted(list_a,key=lambda x:x)
print('默认排序为:',res_1)
print('升序为：',res_2)
print('lambada函数排序为:',res_3)
```

    默认排序为: [-45, -8, -3, 1, 4, 12, 33, 66, 78]
    升序为： [78, 66, 33, 12, 4, 1, -3, -8, -45]
    lambada函数排序为: [-45, -8, -3, 1, 4, 12, 33, 66, 78]
    

#### 使用lambada函数对listlist_1排序，要求输出结果正数从小到大排序，负数从大到小排序


```python
list_a = [12,4,78,-3,-45,33,66,1,-8]
res = sorted(list_a,key=lambda x:(x<0,abs(x)))
print('排序结果为：',res)
```

    排序结果为： [1, 4, 12, 33, 66, 78, -3, -8, -45]
    

### 列表嵌套字典排序，分别根据年龄和姓名排序


```python

list_b = [
    {"name":"as","age":"12"},
    {"name":"cd","age":"34"},
    {"name":"dn","age":"45"},
    {"name":"dbv","age":"88"}
]
age = sorted(list_b,key=lambda x:x["age"],reverse=True)
print('年龄从大小排序结果为：',age)
name = sorted(list_b,key=lambda x:x["name"])
print('姓名从小到大排序为：',name)
```

    年龄从大小排序结果为： [{'name': 'dbv', 'age': '88'}, {'name': 'dn', 'age': '45'}, {'name': 'cd', 'age': '34'}, {'name': 'as', 'age': '12'}]
    姓名从小到大排序为： [{'name': 'as', 'age': '12'}, {'name': 'cd', 'age': '34'}, {'name': 'dbv', 'age': '88'}, {'name': 'dn', 'age': '45'}]
    

### 列表嵌套元组，分别按字母和数字排序


```python
list_c = [
    ('aa',12),("sd",23),("fgr",26),("jy",8)
]
res_word = sorted(list_c,key=lambda x:x[0])
res_num = sorted(list_c,key=lambda x:x[1],reverse=True)
print('字母排序结果为:',res_word)
print('数字排序结果为：',res_num)
```

    字母排序结果为: [('aa', 12), ('fgr', 26), ('jy', 8), ('sd', 23)]
    数字排序结果为： [('fgr', 26), ('sd', 23), ('aa', 12), ('jy', 8)]
    

### 列表嵌套列表排序，年龄数字相同怎么办？


```python
list_d = [
    ['qw',18],['sa',10],['fgd',18],['nh',45],['yu',23]
]
res = sorted(list_d,key=lambda x:(x[1],x[0]))
print('当年龄相同时添加另一个参数按照字母名称排序，结果为：',res)
```

    当年龄相同时添加另一个参数按照字母名称排序，结果为： [['sa', 10], ['fgd', 18], ['qw', 18], ['yu', 23], ['nh', 45]]
    

### 根据键对字典排序(方法一，zip函数)


```python
dict_1 = {"name":"yx","sex":"man","city":"cd"}
#将字典转列表嵌套元组
foo = zip(dict_1.keys(),dict_1.values())  #得到可迭代对象
foo = [i for i in foo]
print('字典转成列表嵌套元组:',foo)
res = sorted(foo,key=lambda x:x[0])  #字典嵌套元组排序
print('根据键排序结果为：',res)
#排序完成后构建新的字典
new_dic = {i[0]:i[1] for i in res}
print('排序后新的字典为：',new_dic)
```

    字典转成列表嵌套元组: [('name', 'yx'), ('sex', 'man'), ('city', 'cd')]
    根据键排序结果为： [('city', 'cd'), ('name', 'yx'), ('sex', 'man')]
    排序后新的字典为： {'city': 'cd', 'name': 'yx', 'sex': 'man'}
    

### 根据键对字典排序(方法儿，使用字典items方法)


```python
dict_1 = {"name":"yx","sex":"man","city":"cd"}
#字典转成列表嵌套元组
print(dict_1.items())
res = sorted(dict_1.items(),key=lambda x:x[0])
print('排序结果为：',res)
#构建新的字典
new_dic = {i[0]:i[1] for i in res}
print('排序后新的字典为：',new_dic)
```

    dict_items([('name', 'yx'), ('sex', 'man'), ('city', 'cd')])
    排序结果为： [('city', 'cd'), ('name', 'yx'), ('sex', 'man')]
    排序后新的字典为： {'city': 'cd', 'name': 'yx', 'sex': 'man'}
    

## 补充内容

- 除了上述操作外，列表排序还可以借助operator模块的itemgetter函数辅助列表排序
- operator模块提供的itemgetter函数用于获取对象的哪些维的数据，参数为一些序号
- operator.itemgetter函数获取的不是值，而是定义了一个函数，通过该函数作用到对象上才能获取值。


```python
#导包
from operator import itemgetter

list_e = [1,2,3,4,5]
func_1 = itemgetter(1)   #定义函数func_1,获取对象的第一个域的值
print(func_1(list_e))
```

    2
    


```python
list_e = [1,2,3,4,5]
func_2 = itemgetter(1,0)   #定义函数func_2,获取对象的第一个域和第0个域值
print(func_2(list_e))
```

    (2, 1)
    


```python
#按年龄为主要关键字，名字为次要关键字倒序排序：
students = [[3,'Jack',12],[2,'Rose',13],[1,'Tom',10],[5,'Sam',12],[4,'Joy',8]]

res = sorted(students,key=itemgetter(2,1),reverse=True)
print(res)
```

    [[2, 'Rose', 13], [5, 'Sam', 12], [3, 'Jack', 12], [1, 'Tom', 10], [4, 'Joy', 8]]
    


```python

```


```python

```


```python

```


```python

```
