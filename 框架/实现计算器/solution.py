from collections import deque
def str_trans_int():
    """
    #把字符串转换成正整数
    """
    string = '458'
    n = 0
    i = 0
    while(i<len(string)):
        c= string[i]
        print("c is ",ord(c))
        n = 10 * n + (ord(c)-ord('0'))
        print("n is ",n)
        i = i + 1
    return n

def calculate(string):
    """
    处理加减法
    """
    stack = deque()
    num = 0
    sign = '+'
    i = 0
    while(i<len(string)):
        c = string[i]
        if c.isdigit():
            num = 10 *num + (ord(c)-ord('0'))
        if (not c.isdigit() or i == len(string) - 1):
            if sign == '+':
                stack.append(num)
            if sign == '-':
                stack.append(-num)
            sign = c
            num = 0
        i = i + 1
    res = 0
    while(stack):
        res = res + stack.pop()
    return res

def calculate_02(string):
    """
    处理乘除法
    """
    stack = deque()
    num = 0
    sign = '+'
    i = 0
    while(i<len(string)):
        c = string[i]
        if c.isdigit():
            num = 10 *num + (ord(c)-ord('0'))
        if (not c.isdigit() or i == len(string) - 1):
            if sign == '+':
                stack.append(num)
            if sign == '-':
                stack.append(-num)
            if sign == '*':
                pre = stack.pop() #抛出栈顶数据项，无参数，返回被抛出的数据项，栈本身发生变化
                stack.append(pre * num)  #当前结果又存入刚弹出的栈顶元素的位置处
            if sign == '/':
                pre = stack.pop()
                stack.append(pre//num)
            sign = c
            num = 0
        i = i + 1
    res = 0
    while(stack):
        res = res + stack.pop()
    return res


def calculate_03(string):
    """
    处理括号
    """
    string = list(string)
    stack = deque()
    num = 0
    sign = '+'
    while(len(string) > 0 ):
        c = string.pop(0)
        print("string is ",string)
        if c.isdigit():
            num = 10 *num + (ord(c)-ord('0'))
        if c == '(':
            print("string c=='(' is ",string)
            num = calculate_03(string)
        if (not c.isdigit() and c != ' ' ) or len(string) == 0:
            if sign == '+':
                stack.append(num)
            if sign == '-':
                stack.append(-num)
            if sign == '*':
                # pre = stack.pop() #抛出栈顶数据项，无参数，返回被抛出的数据项，栈本身发生变化
                # stack.append(pre * num)  #当前结果又存入刚弹出的栈顶元素的位置处
                stack[-1] = stack[-1] * num
            if sign == '/':
                # pre = stack.pop()
                # stack.append(pre//num)
                stack[-1] = stack[-1] // num

            sign = c
            num = 0
        if c == ')':
            print("string c==')' is ",string)
            print("stack is ",stack)
            break

    # while(stack):
    #     res = res + stack.pop()
    return sum(stack)


"""
python中栈可以用以下三种方法实现：

１）list

２）collections.deque

３）queue.LifoQueue

使用列表实现栈

python的内置数据结构list可以用来实现栈，用append()向栈顶添加元素, pop() 可以以后进先出的顺序删除元素

但是列表本身有一些缺点，主要问题就是当列表不断扩大的时候会遇到速度瓶颈．列表是动态数组，因此往其中添加新元素而没有空间保存新的元素时，它会自动重新分配内存块，并将原来的内存中的值复制到新的内存块中．这就导致了一些append()操作会消耗更多的时间



参考：
https://www.jianshu.com/p/189ea3fc3084
经典参考：https://www.cnblogs.com/laozhanghahaha/p/12302836.html

python数据结构之栈:https://zhaochj.github.io/2016/05/14/2016-05-14-%E6%95%B0%E6%8D%AE%E7%BB%93%E6%9E%84-%E6%A0%88/

了解python的数据结构！！！！
"""

if __name__ == '__main__':
    # rst = str_trans_int()
    string = "(4+5)/8"
    # rst = calculate(string)
    # rst = calculate_02(string)
    rst = calculate_03(string)    #问题？？这个地方结果为14，stack为[9,5]有错误；
    print("rst is ",rst)