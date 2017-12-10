#coding: UTF-8
a = [2012, 2013, 2014] #list（要素の追加・変更可）
b = (2012, 2013, 2014) #tuple（要素の追加・変更不可）
print a
print b

print a[1]
print b[1]

a[1] = 2016
print a

# b[1] = 2016
# print b

a.append(2015)
print a