# -*- coding: utf-8 -*-
# @Time : 2020/6/13 9:59
# @Author : ccs
"""
题目描述给定一长字符串a和一短字符串b。请问，如何最快地判断出短字符串b中的所有字符是否都在长字符串a中？请编写函数 bool String Contain（ string&a, string&b）
实现此功能。
为简单起见，假设输入的字符串只包含大写英文字母。下面举几个例子。
如果字符串a是"ABCD"，字符串b是"BAD"，答案是true，因为字符串b中的字母都在字符串a中，或者说b是a的真子集。
如果字符串a是"ABCD"，字符串b是"BCE"，答案是 false，因为字符串b中的字母E不在字符串a中。
如果字符串a是"ABCD"，字符串b是"AA"，答案是true，因为字符串b中的字母A包含在字符串a中。


解法四：位运算法如果面试官继续追问，到底有没有更好的办法呢？或许你绞尽脑汁能想到计数排序。但除了计数排序还有别的办法吗？
事实上，可以先把长字符串a中的所有字符都放入一个散列表（ hash table）中，然后轮询短字符串b，看b中的每个字符是否都在散列表里，如果都在，说明长字符串a包含短字符串b；否则，说明不包含。
再进一步，可以用位运算（26位整数表示）为长字符串a计算出一个“签名”，再逐一将短字符串b中的字符放到a中进行查找。


这个跟蛮力查找的区别就是：蛮力查找是a,b的每个元素直接遍历查找（时间复杂度为n），比较是否相等；
而hash查找是，构造好hash表后，利用key（hash值）进行查找，时间复杂度为1；
"""
def string_contain(string_a,string_b):
    string_a_dict = map(lambda x:(ord(x), x),set(string_a))
    string_a_dict = { i[0]:i[1] for i in list(string_a_dict)}
    print(string_a_dict)
    string_b_dict = map(lambda x: (ord(x),x), set(string_b))
    string_b_dict = { i[0]:i[1] for i in list(string_b_dict)}
    print(string_b_dict)
    for key,value in string_b_dict.items():
        if not string_a_dict.get(key,None):  #时间复杂度优化体现在这里；复杂度为1；
            return False
        else:
            continue
    return True
if __name__ == '__main__':
    string_a = "ABCD"
    string_b = "BCE"
    rst = string_contain(string_a, string_b)
    print(rst)

    string_a = "ABCD"
    string_b = "BAD"
    rst = string_contain(string_a, string_b)
    print(rst)

    string_a = "ABCD"
    string_b = "AA"
    rst = string_contain(string_a, string_b)
    print(rst)

