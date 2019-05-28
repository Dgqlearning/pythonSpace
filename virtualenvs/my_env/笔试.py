# coding: utf-8
print("段国庆")

#1.根据字典的key排序
dict={"name":"zs","age":18,"city":"深圳","tel":"1362626627"}
new_dict = {}
def sort_dict(key_name):
    new_dict[key_name] = dict[key_name]
    return key_name,new_dict[key_name]

key_sort = sorted(dict.items(),key=lambda x: str(x[1]),reverse=False)

a = sorted(dict.keys())
key_map = map(sort_dict,a)
for i in key_map:
    print(i)
print(new_dict)


# 25、统计字符串每个单词出现的次数"kjalfj;ldsjafl;hdsllfdhg;lahfbl;hl;ahlf;h"
# 利用collections库的Counter方法
from collections import Counter
a = "kjalfj;ldsjafl;hdsllfdhg;lahfbl;hl;ahlf;h"
res = Counter(a)
print(res)
print(res["j"])
print(type(res))
for k,v in res.items():
    print(k,v)

res = Counter(a)
print(res)

a.center
print(a)
print(a.count)

# 26、字符串a = "not 404 found 张三 99 深圳"，每个词中间是空格，
# 用正则过滤掉英文和数字，最终输出"张三  深圳"
import re
a = "not 404 fwwound 张三 99 深圳"
c = re.findall('[^\da-z]',a)
c = ''.join(c).strip()
c = re.sub(' +',' ',c)
print(''.join(c).strip())

# 继承
#父类中没有的方法和属性，在子类中出现叫做派生方法，派生属性
#子类对象调用时，优先使用子类的方法和属性，没有的时候调用父类的，都没有则报错
#如果还想使用父类的，单独调用父类的：
    #1.父类名.方法名(self)
    #2.super().方法名()
class Animal(object):
    
    def __init__(self, *args, **kwargs):
        print("执行Animal.init方法")
        self.func()
    
    def eat(self):
        print("%s eating"%self.name)

    def drink(self):
        print("%s drinking"%self.name)
    
    def func(self):
        print("Animal.func")

class Dog(Animal):
    
    def __init__(self, *args, **kwargs):
        print('执行Dog.init方法')

    def guard(self):
        print("guarding")
    
    def func(self):
        print("Dog.func")

dog = Dog()

#字典
dicty = {
    "name":"Dave",
    "age":18,
    "phone":10918
}

print(dicty.items())
print(dicty.keys())
print(dicty.values())
print(type(dicty.keys()))
print(type(dicty.values()))


tuple1 = (1,1,3,[1,2,3])
print(tuple1)

list1 = ['a','b','c']
print("j".join(list))
list1.sort(reverse=True)
list1.sort(reverse=False)
print(list1)

list1 = ['a','b','c']
sorted(list1,reverse=True,key=lambda x:'b'>x)


a = 'ajax'
b = a.capitalize()

print(a,end=',')
print(b)
print(id(a))
print(id(b))

import random

a = random.uniform(3,10)
print(a)

strs = 'duanguoqing'
print(strs[::-1])#gniqougnaud 反转

with open("test.txt",mode='a') as tf:
    # write = tf.write()
    # write('a')
    tf.write('ggg')
    tf.write('hhh')
    tf.writelines('aaabbbccc')

#实现树结构的类，树的节点有三个私有属性  左指针 右指针 自身的值
class Node():

    def __init__(self,data=None):
        self._data = data
        self._left = None
        self._right = None

    def set_data(self,data):
        self._data = data

    def get_data(self):
        return self._data

    def set_left(self,node):
        self._left = node

    def get_left(self):
        return self._left

    def set_right(self,node):
        self._right = node

    def get_right(self):
        return self._right

if __name__ == '__main__':
    #实例化根节点
    root_node = Node('a')
    # root_node.set_data('a')
    #实例化左子节点
    left_node = Node('b')
    left2_node = Node('d')
    right2_node = Node('e')
    left_node.set_left(left2_node)
    left_node.set_right(right2_node)
    #实例化右子节点
    right_node = Node('c')
    left2_node = Node('f')
    right2_node = Node('g')
    right_node.set_left(left2_node)
    right_node.set_right(right2_node)
    #给根节点的左指针赋值，使其指向左子节点
    root_node.set_left(left_node)
    #给根节点的右指针赋值，使其指向右子节点
    root_node.set_right(right_node)

print(root_node.get_data())
print(root_node.get_left().get_data(),root_node.get_right().get_data())
print(root_node.get_left().get_left().get_data(),root_node.get_left().get_right().get_data(),root_node.get_right().get_left().get_data(),root_node.get_right().get_right().get_data())



#实现树结构的类，树的节点有三个私有属性  左指针 右指针 自己的值
class Node():

    def __init__(self,data =None,left=None,right = None):
        self._data = data
        self._left = left
        self._right = right


#先序遍历  遍历过程 根左右
def pro_order(tree):
    if tree == None:
        return False
    print(tree._data)
    pro_order(tree._left)
    pro_order(tree._right)

#后序遍历
def pos_order(tree):
    if tree == None:
        return False
    # print(tree.get_data())
    pos_order(tree._left)
    pos_order(tree._right)
    print(tree._data)

#中序遍历
def mid_order(tree):
    if tree == None:
        return False
    # print(tree.get_data())
    mid_order(tree._left)
    print(tree._data)
    mid_order(tree._right)


#层次遍历
def row_order(tree):
    # print(tree._data)
    queue = []
    queue.append(tree)
    while True:
        if queue==[]:
            break
        print(queue[0]._data)
        first_tree = queue[0]
        if first_tree._left != None:
            queue.append(first_tree._left)
        if first_tree._right != None:
            queue.append(first_tree._right)
        queue.remove(first_tree)

if __name__ == '__main__':

    tree = Node('A',Node('B',Node('D'),Node('E')),Node('C',Node('F'),Node('G')))
    pro_order(tree)
    mid_order(tree)
    pos_order(tree)


#
b = [1,2,(1,3,5),3]
b[2][0] = 7
print(b)


a = (1,2,[4,5,6],3)
a[2].append(7)
a[2].extend([50,60])
a[2] += [50,60]
print(a)

