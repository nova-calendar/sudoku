

'''
make a NxN grid (list(s) within list)
'''
def make_board(n):
    board = []
    row = [0] * n

    for i in range(1,n+1):
        board.append(row)

    return board


def printer(board):
    for row in board:
        print(row)

if __name__ == "__main__":

    test3 = make_board(3)

    printer(test3)
        
