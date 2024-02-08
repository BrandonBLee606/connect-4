# Plays a piece and returns True if valid otherwise False
def play(board, pos, player, height):
    for i in range(height):
        # If the position is empty, then we can play the piece
        if (board[int(height) - 1 - i][pos] == 0):
            board[height - 1 - i][pos] = player
            return True
    # The position is full with pieces
    return False

# Checks for a win and calculates the value of the board
def win(board, height, width):
    # Number of empty positions within 4 without any enemy pieces inbetween
    potential = 0
    # Number of friendly pieces within 4 without any enemy pieces inbetween
    pieces = 0
    # Checks for Cat's Game
    count = 0
    for i in range(height):
        # Keeps track of previous piece
        previous = 0
        for j in range(width):
            curr = 0
            won = False
            if board[i][j] == 1:
                curr = 1
            elif board[i][j] == 2:
                curr = 2
            if curr == 1 or curr == 2:
                # Current piece is included in the 4 in a row
                count+=1
                # In the case that the previous is the same as the current, we already checked for a win, so no need to check for a horizontal win
                if previous != 1:
                    horizontalCheck = checkHorizontalWin(board, j, i, width, curr)
                    pieces, potential, won = pieces+horizontalCheck[0], potential+horizontalCheck[1], won or horizontalCheck[2]
                # Checks for a cross win
                xCheck = checkXWin(board, j, i, width, height, curr)
                # Checks for a vertical win
                verticalCheck = checkVerticalWin(board, j, i, height, curr)
                pieces, potential, won = pieces+xCheck[0]+verticalCheck[0], potential+xCheck[1]+verticalCheck[1], won or xCheck[2] or verticalCheck[2]
                # If there is a winner, there is no need to proceed any further
                if won:
                    if curr == 1:
                        return [1, pieces, potential]
                    else:
                        return [-1, pieces, potential]
    # If the pieces filled up all of the board, then it's a Cat's Game
    if count == height*width:
        return [0, pieces, potential]
    # Otherwise return the board's value
    return [-2, pieces, potential]         

# Checks for a cross win and calculates the points 
def checkXWin(board, posX, posY, width, height, player):
    # Keeps track of player pieces in a row
    count = 1
    # Keeps track of y
    hr = posY+1
    # Keeps track of x
    wr = posX+1
    # If the number of pieces are in a row
    straight = True
    # Keeps track of potential wins
    potential = 0
    # Keeps track of white spaces without any enemy pieces inbetween
    whiteSpace = 0
    # Keeps track of friendly pieces without any enemy pieces inbetween
    pieces = 1

    # Checks top right
    while hr < height and wr < width:
        if board[hr][wr] == player:
            if straight:
                count+=1
            pieces+=1
        elif board[hr][wr] == 0:
            whiteSpace +=1
            # Potential win
            if whiteSpace+count >= 4:
                potential +=1
            straight = False
        else:
            break
        hr +=1
        wr +=1
    
    
    hl = posY-1
    wl = posX-1
    # Checks bottom left
    while hl >= 0 and wl >= 0:
        if board[hl][wl] == player:
            if straight:
                count +=1
            pieces +=1
        elif board[hl][wl] == 0:
            whiteSpace +=1
            # Potential win
            if whiteSpace+count >= 4:
                potential +=1
            straight = False
        else:
            break
        hl -=1
        wl -=1
    if count >= 4:
        return [pieces, potential, True]

    # Backward X Win
    count = 1
    hr = posY+1
    wl = posX-1
    straight = True
    hl = posY-1
    wr = posX+1
    # Checks top left
    while hr < height and wl >= 0:
        if board[hr][wl] == player:
            if straight:
                count +=1
            pieces +=1
        elif board[hr][wl] == 0:
            whiteSpace +=1
            # Potential win
            if whiteSpace+count >= 4:
                potential +=1
            straight = False
        else:
            break
        hr +=1
        wl -=1

    straight = True
    # Checks bottom right
    while hl >= 0 and wr < width:
        if board[hl][wr] == player:
            if straight: 
                count +=1
            pieces +=1
        elif board[hl][wr] == 0:
            whiteSpace +=1
            # Potential win
            if whiteSpace+count >= 4:
                potential +=1
            straight = False
        else:
            break
        hl -=1
        wr +=1
    # Possible win
    if count >= 4:
        return [pieces, potential, True]
    # No win
    return [pieces, potential, False]
# Checks for a vertical win and calculates the points
def checkVerticalWin(board, posX, posY, height, player):
    # Keeps track of pieces in a row
    count = 1
    # Keeps track of above position
    top = posY+1
    # Keeps track of below position
    bottom = posY-1
    # Potential wins
    potential = 0
    # In a row
    straight = True
    whiteSpace = 0
    pieces = 1
    # Checks for down win
    while bottom >= 0:
        if board[bottom][posX] == player:
            if straight:
                count+=1
            pieces+=1
        elif board[bottom][posX] == 0:
            whiteSpace+=1
            if whiteSpace+count >= 4:
                potential +=1
            straight = False
        else:
            break
        bottom-=1
    straight = True
    # Checks for above win
    while top < height:
        if board[top][posX] == player:
            if straight:
                count +=1
            pieces +=1
        elif board[top][posX] == 0:
            whiteSpace +=1
            if whiteSpace+count >= 4:
                potential +=1
            straight = False
        else:
            break
        top +=1
    if count >= 4:
        return [pieces, potential, True]
    return [pieces, potential, False]
# Checks for a horizontal win and calculates the points
def checkHorizontalWin(board, posX, posY, width, player):
    # Number of friendly pieces in a row
    count = 1
    # Position of left
    left = posX-1
    # Position of right
    right = posX+1
    straight = True
    whiteSpace = 0
    # Potential wins
    potential = 0
    pieces = 1
    # Checks left
    while left >= 0:
        if board[posY][left] == player:
            if straight:
                count+= 1
            pieces+=1
        elif board[posY][left] == 0:
            whiteSpace+=1
            if whiteSpace+count >= 4:
                potential+=1
            straight = False
        else:
            break
        left -=1
    straight = True

    # Checks right
    while right < width:
        if (board[posY][right] == player):
            if straight:
                count +=1
            pieces +=1
        elif board[posY][right] == 0:
            whiteSpace +=1
            if whiteSpace+count >= 4:
                potential +=1
            straight = False  
        else:
            break
        right+=1
    if count >= 4:
        return [pieces, potential, True]
    return [pieces, potential, False]


# Removes a piece from the board. True if it's possible, False if it's not
def remove(board, pos, height):
    for i in range(height):
        if (board[i][pos] != 0):
            board[i][pos] = 0
            return True
    return False
