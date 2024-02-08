from helper import play, remove, win

# AI's logic for minmaxing
def chooseMove(board, height, width, player):
    moves = [i for i in range(width)]
    depth = 5
    # Create dummy move which will be overwritten later
    bestMove = -1
    bestPoint = [float('inf'), depth]
    # Check all possible moves within the depth
    for i in moves:
        # Play the move to update the board
        if play(board, i, player, height):
            # Check the worst case scenario given that the other player will play optimally
            currPoint = points(board, height, width, 1, depth, float('-inf'), bestPoint[0])
            # Remove this move
            remove(board, i, height)
            # If this move will put us in a position better than what we have saved in bestMove/bestPoint, then update it
            # If this move results in the same position value but quicker, then update it
            if bestMove == -1:
                bestPoint = currPoint
                bestMove = i
            elif currPoint[0] == float('inf'):
                if currPoint[1] < bestPoint[1] and currPoint[0] == currPoint[1]:
                    bestPoint = currPoint
                    bestMove = i
            elif (currPoint[0] == bestPoint[0] and currPoint[0] > bestPoint[1]) or (currPoint[0] < bestPoint[0]):
                bestPoint = currPoint
                bestMove = i
    return bestMove

# AI's logic for creating a point value for a given board state
def points(board, height, width, player, depth, alpha, beta):
    won = win(board, height, width)
    # Player 1 wins
    if won[0] == 1:
        return [float('inf'), depth]
    # Player 2 wins
    elif won[0] == -1:
        return [float('-inf'), depth]
    # Cat's Game
    elif won[0] == 0:
        return [0, depth]
    # If we reach the maximum depth, then create a value given this board state
    if depth == 0:
        # won[1] is the total number of pieces that are within 4 from EACH piece given that there are no opponent pieces inbetween
        # won[2] is the total number of potential wins
        return [won[1] + won[2]*0.25, depth]
   
   # All possible moves
    moves = [i for i in range(width)]
    # Set dummy values
    if player == 1:
        maxPoint = [float('-inf'), depth]
    else:
        maxPoint = [float('inf'), depth]
    for i in moves:
        if player == 1:
            # If the move is valid
            if play(board, i, player, height):
                currPoint = points(board, height, width, 2, depth-1, maxPoint[0], beta)
                remove(board, i, height)
                if currPoint[0] >= beta:
                    return currPoint
                # We want to maximize our points
                if (currPoint[0] == maxPoint[0] and (currPoint[1] > maxPoint[1] or (currPoint[0] == float('-inf') and currPoint[1] < maxPoint[1]))) or (currPoint[0] > maxPoint[0]):
                    maxPoint = currPoint
        if player == 2:
            # If the move is valid
            if play(board, i, player, height):
                currPoint = points(board, height, width, 1, depth-1, alpha, maxPoint[0])
                remove(board, i, height)
                if currPoint[0] <= alpha:
                    return currPoint
                # We want to minimize our points
                if (currPoint[0] == maxPoint[0] and (currPoint[1] > maxPoint[1] or (currPoint[0] == float('inf') and currPoint[1] < maxPoint[1]))) or (currPoint[0] < maxPoint[0]):
                    maxPoint = currPoint     
    return maxPoint