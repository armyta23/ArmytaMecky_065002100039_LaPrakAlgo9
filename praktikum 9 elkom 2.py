# -*- coding: utf-8 -*-
"""
Created on Wed Dec 29 03:18:11 2021

@author: LENOVO
"""
print('tuple 1: ')
a=('1031','1032', '1033', '1034', '1035', '1036', '1037', '1038', '1039', '1040', '1050')
r = ", ".join(a[0:3])
m = ", ".join(a[4:7])
y= ", ".join(a[8:11])
print((r,m,y))
print('rata rata nilai dari masing masing tuple adalah: ')
print ([sum(map(float, filter(None, a[0:3])))/(len(a)-1),(sum(map(float, filter(None, a[4:7])))/(len(a)-1)),(sum(map(float, filter(None, a[8:11])))/(len(a)-1))])  
print('====== ARMYTA MECKY ======')
print('========= 065002100039 =========')