import sys

def is_piece_threat(piece, dr, dc, dist):
    if piece == 'Q': return True
    if piece == 'R': return dr == 0 or dc == 0
    if piece == 'B': return dr != 0 and dc != 0
    if piece == 'P': return dr == 1 and dc != 0 and dist == 1
    return False

def check_direction(rows, start_r, start_c, dr, dc):
    r, c = start_r + dr, start_c + dc
    dist = 1
    height = len(rows)
    width = len(rows[0])

    while 0 <= r < height and 0 <= c < width:
        piece = rows[r][c]
        if piece != '.':
            if is_piece_threat(piece, dr, dc, dist):
                return True  
            else:
                return False 
        r += dr; c += dc; dist += 1
    return False 

def checkmate(board):
    try:
        # Case 1: ไม่มีข้อมูลส่งมาเลย หรือเป็น None
        if not board:
            print("Error: Input board is empty or None.")
            return

        # Parse Board
        rows = board.split('\n')
        if rows and rows[-1] == "":
            rows.pop()
        
        # Case 2: หลังจัดการ string แล้ว ไม่เหลือข้อมูลใน list
        if not rows:
            print("Error: Board contains no rows.")
            return

        height = len(rows)
        width = len(rows[0])

        # Case 3: เช็คว่า board เป็นสี่เหลี่ยมจัตุรัส (กว้าง != สูง)
        if height != width:
            print(f"Error: The board is not a square. (Height: {height}, Width: {width})")
            return

        # Case 4: เช็คความยาวของแต่ละบรรทัดว่าเท่ากันหรือเปล่า
        for i, row in enumerate(rows):
            if len(row) != width:
                print(f"Error: Row {i} length is inconsistent. (Expected {width}, got {len(row)})")
                return
            
        # 2. Find King 
        k_row, k_col = None, None
        for r, row in enumerate(rows):
            if 'K' in row: 
                k_row, k_col = r, row.index('K') 
                break
        
        # Case 5: หาตัว King ไม่เจอ
        if k_row is None:
            print("Error: King ('K') not found on the board.")
            return

        # 3. Checkmate Logic
        directions = [
            (-1, 0), (1, 0), (0, -1), (0, 1),
            (-1, -1), (-1, 1), (1, -1), (1, 1)
        ]

        for dr, dc in directions:
            if check_direction(rows, k_row, k_col, dr, dc):
                print("Success")
                return

        print("Fail")

    except Exception as e:
        # Case 6: Error อื่น ๆ
        print(f"Error: An unexpected error occurred: {e}")