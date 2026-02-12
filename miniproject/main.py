from checkmate import checkmate

def main():
    board1 = """\
R...
.K..
..P.
....\
"""
    checkmate(board1) 

    board2 = """\
....
.K\
"""
    checkmate(board2) 

if __name__ == "__main__":
    main()