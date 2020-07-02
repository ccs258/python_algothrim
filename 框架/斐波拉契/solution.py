import time


# 版本1：传统的方式，但是存在重复计算可以加一个容器存储结果
def feb(n):
    if n == 1 or n == 2:
        return 1
    else:
        return feb(n - 1) + feb(n - 2)


# 版本2：也利用了递归，不过引入了存储结果表，不用重复计算；
def feb_2(n):
    def helper(n, method):
        if method[n] != 0:
            return method[n]
        if n == 1 or n == 2:
            method[n] = 1
            return method[n]
        else:
            method[n] = helper(n - 1, method) + helper(n - 2, method)
            return method[n]

    method = [0] * (n + 1)
    method = helper(n, method)
    return method


#版本3：因为递归是自顶向下，现在采用自底向上的方式；
def feb_3(n):
    cur = 0
    rst = 0
    for i in range(1,n+1,1):
        if i == 1 or i == 2:
            pre = 0
            cur = 1
            rst = cur + pre
        else:
            pre = cur
            cur = rst
            rst = pre + cur
    return rst

if __name__ == '__main__':
    start = time.time()
    rst = feb(40)
    print("rst is ", rst)
    end = time.time()
    print("time cost is ", end - start)

    start = time.time()
    rst = feb_2(40)
    print("rst2 is ", rst)
    end = time.time()
    print("time cost is ", end - start)

    start = time.time()
    rst = feb_3(40)
    print("rst3 is ", rst)
    end = time.time()
    print("time cost is ", end - start)

    """
当输入n为40的时候：
版本1：自顶向下递归，没有中间结果缓存表
rst is  102334155
time cost is  26.054733991622925

版本2：自顶向下递归，有中间结果缓存表
rst2 is  102334155
time cost is  0.0009486675262451172

版本3：自底向上
rst3 is  102334155
time cost is  0.0


总结：可以看出，有中间结果缓存表，其速度会快上万倍；
自底向上相比自顶向下会快，上千倍；
    """