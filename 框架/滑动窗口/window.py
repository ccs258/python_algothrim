"""
滑动窗口算法的代码框架:时间复杂度是 O(N)
"""
from collections import Counter

INT_MAX = 1000000


def solution(s, t):
    left = 0
    right = 0
    window = []
    while (right < len(s)):
        window.append(s[right])  # 增大窗口
        right = right + 1
        while (window):  # window needs shrink #减小窗口
            window.remove(s[left])
            left = left + 1


# 判断s中是否存在t的排列

def checkSolution(s: str, t):
    need = Counter(t)
    print("need is ", need)
    window = dict(map(lambda x: (x, 0), Counter(s).keys()))
    left = 0
    right = 0
    valid = 0
    start = 0
    max_len = INT_MAX
    while (right < len(s)):
        c = s[right]
        right = right + 1
        if (need.get(c)):
            window[c] = window[c] + 1
            if window[c] == need[c]:
                valid = valid + 1

        while (valid == len(need.keys())):
            if right - left < max_len:
                start = left
                max_len = right - left

            d = s[left]
            left = left + 1
            if (need.get(d)):
                if window[d] == need[d]:
                    valid = valid - 1
                window[d] = window[d] - 1  #注意这个地方是检测到了字母存在，但与实际需要不等，证明多了，需要减去1，证明当前窗口不是最优的（出现次数最少的）；
    if max_len == INT_MAX:
        return ""
    else:
        return s, start, max_len, s[start:start + max_len]


# 滑动窗口算法框架
def slideWindow(s, t):
    need = Counter(t)
    window = Counter(s)
    left = 0
    right = 0
    valid = 0
    while (right < len(s)):
        # c是将要移入窗口的字符
        c = s[right]
        right = right + 1
        # 进行窗口内数据的一系列更新
        ##...content...##
        # debug输出位置
        print("window:[%d,%d]" % (left, right))

        # 判断左侧窗口是否要收缩
        while (window):  # window needs shrink
            d = s[left]
            left = left + 1
            ##...content...##
"""
说明：
其中上述两处##...content...##都是表示更新窗口数据的地方，直接在里面填就可以了。
"""


if __name__ == '__main__':
    s = "EBANCF"
    t = "ABC"
    rst = checkSolution(s, t)
    print("rst is ", rst)
