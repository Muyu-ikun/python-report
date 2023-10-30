def is_valid_row(row):
    # 检查一行是否包含数字1到9且没有重复
    return sorted(row) == list(range(1, 10))

def validate_sudoku(board):
    # 检查每一行
    for row in board:
        if not is_valid_row(row):
            return False

    # 检查每一列
    for col in zip(*board):
        if not is_valid_row(col):
            return False

    # 检查每个九宫格
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            square = [board[x][y] for x in range(i, i+3) for y in range(j, j+3)]
            if not is_valid_row(square):
                return False

    return True

# 示例
sudoku_board = [  [5,3,4,6,7,8,9,1,2],
				  [6,7,2,1,9,5,3,4,8],
				  [1,9,8,3,4,2,5,6,7],
				  [8,5,9,7,6,1,4,2,3],
				  [4,2,6,8,5,3,7,9,1],
				  [7,1,3,9,2,4,8,5,6],
				  [9,6,1,5,3,7,2,8,4],
				  [2,8,7,4,1,9,6,3,5],
				  [3,4,5,2,8,6,1,7,9]]

result = validate_sudoku(sudoku_board)
print(result)  # 输出 True，因为这是一个有效的数独解决方案
