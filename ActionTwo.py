# -*- coding: utf-8 -*-
#字符串和编码
print(ord('A'))
print(ord('B'))
print(ord('C'))
print(chr(88))
print(chr(66))

#格式化
#占位符：% %d %s %d %f
print('%s,你好,hopeless,for %d  %f '% ('Mu_Xing', 29, 172.00))
#format()
print('Mu_Xing,2022年月收入{0},身高达到{3:.2f}, 去一次{1},一直寻找的{2}'.format('18K以上', '都是枫树的地方露营', '伊甸园', 173.00))

s1 = 72
s2 = 85
print('成绩提升了:%.1f%%' % ((s2/s1-1)*100))