def solution(board, row):
    if row == len(board):  #注意这个地方的终止条件，应当是len(board)，而不是len(board)-1,因为算完之后，自动加1了进行回溯了；
        print("board is ", board)
        return True
    for col in range(len(board)):
        # 做选择
        if is_ok(board, col, row) == False:
            continue
        #
        board[row][col] = "Q"
        solution(board, row + 1)
        board[row][col] = 0


# def is_ok_err(board, col, row):
#     for i in range(len(board)):
#         if board[i][col] == "Q":
#             return False
#     try:  # 而且这个地方，会报index溢出，最好的解决办法就是提前结束循环，不让他溢出，因为知道它能取得的最大值。
#         if board[row][col - 1] == "Q" or board[row][col + 1] == "Q":  # 旧版本，这个地方对N皇后理解不到位
#             return False
#     except:
#         pass
#     return True


def is_ok(board, col, row):
    # 同列判断 --- 因为当前行是新判断行，不会有同行的问题
    for i in range(len(board)):
        if board[i][col] == "Q":
            return False
    # 左上角的判断，单独命名变量，防止被干扰
    r1 = row-1
    c1 = col-1
    while (r1 >= 0 and c1 >= 0):
        if board[r1][c1] == 'Q':
            return False
        r1 = r1 - 1
        c1 = c1 - 1

    # 右上角的判断，单独命名变量，防止被干扰
    r2 = row-1
    c2 = col+1
    while (r2 >= 0 and c2 <= len(board) - 1):
        if board[r2][c2] == 'Q':
            return False
        r2 = r2 - 1
        c2 = c2 + 1
    return True

"""
N皇后自我理解：
（1）同行同列不能出现Q
（2）主副对角线上不能出现Q
上面两个可作为第N行遍历的时候的选择判断。

"""

if __name__ == '__main__':
    # board = [[0, 0, 0, 0]] * 4 #这种初始化，一次赋值会同时针对一列赋值；
    board =[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    row = 0
    solution(board, row)
"""
答案是2种排列方式：
board is  [[0, 'Q', 0, 0], [0, 0, 0, 'Q'], ['Q', 0, 0, 0], [0, 0, 'Q', 0]]
board is  [[0, 0, 'Q', 0], ['Q', 0, 0, 0], [0, 0, 0, 'Q'], [0, 'Q', 0, 0]]

"""