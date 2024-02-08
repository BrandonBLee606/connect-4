import sys
from helper import play, win
from ai import chooseMove
import pygame

boardColor = '#BB86FC'
emptySpotColor = '#000000'
borderColor = '#834EC5'
playerOneColor = '#03DAC6'
playerTwoColor = '#CF6679'
white = '#FFFFFF' 
# light shade of the button 
color_light = (170,170,170) 
# dark shade of the button 
color_dark = (100,100,100) 


SQUARESIZE = 100
RADIUS =  int(SQUARESIZE/2-5)

# menu screen which will contain logic for gamemode
def menu():
    # initializing the constructor 
    pygame.init() 
    smallfont = pygame.font.SysFont('Corbel',35)
    # screen resolution 
    res = (720,720) 
    
    # opens up a window 
    screen = pygame.display.set_mode(res) 
    
    # stores the width of the 
    # screen into a variable 
    width = screen.get_width() 
    
    # stores the height of the 
    # screen into a variable 
    height = screen.get_height() 
    
    onePlayer = smallfont.render('One Players' , True , white) 
    twoPlayers = smallfont.render('Two Players' , True , white) 
    
    while True: 
        for ev in pygame.event.get(): 
            if ev.type == pygame.QUIT: 
                pygame.quit()   
            # picks gamemode
            if ev.type == pygame.MOUSEBUTTONDOWN: 
                if width/2-100 <= mouse[0] <= width/2+100 and height/2-150 <= mouse[1] <= height/2-90: 
                    pygame.quit()
                    return 0
                if width/2-100 <= mouse[0] <= width/2+100 and height/2-50 <= mouse[1] <= height/2+10: 
                    pygame.quit()
                    return 1
                    
        # fills the screen with a color 
        screen.fill((60,25,60)) 
        
        # stores the (x,y) coordinates into 
        # the variable as a tuple 
        mouse = pygame.mouse.get_pos() 
        
        # if mouse is hovered on a button it 
        # changes to lighter shade  
        if width/2-100 <= mouse[0] <= width/2+100 and height/2-150 <= mouse[1] <= height/2-90:
            pygame.draw.rect(screen, color_light, [width/2-100, height/2-150, 200, 60])
        else:
            pygame.draw.rect(screen, color_dark, [width/2-100, height/2-150, 200, 60])
        
        screen.blit(onePlayer, (width/2-85,height/2-135)) 

        if width/2-100 <= mouse[0] <= width/2+100 and height/2-50 <= mouse[1] <= height/2+10: 
            pygame.draw.rect(screen,color_light,[width/2-100,height/2-50,200,60]) 
            
        else: 
            pygame.draw.rect(screen,color_dark,[width/2-100,height/2-50,200,60]) 

        screen.blit(twoPlayers, (width/2-83,height/2-35)) 
    
        pygame.display.update() 

# screen which will set the board size
def defineBoard():
    # initializing the constructor 
    pygame.init() 
    
    # screen resolution 
    res = (720,720) 
    
    # opens up a window 
    screen = pygame.display.set_mode(res) 
    
    # stores the width of the 
    # screen into a variable 
    width = screen.get_width() 
    
    # stores the height of the 
    # screen into a variable 
    height = screen.get_height() 
    
    # configure text
    smallfont = pygame.font.SysFont('Corbel',35)
    mediumfont = pygame.font.SysFont('Corbel', 50) 
    heightText = mediumfont.render('Height', True, color_light) 
    widthText = mediumfont.render('Width', True, color_light)
    setHeight = 7
    setWidth = 6
    while True: 
        for ev in pygame.event.get():  
            if ev.type == pygame.QUIT: 
                pygame.quit()      
            # checks if a mouse is clicked 
            if ev.type == pygame.MOUSEBUTTONDOWN: 
                
                # saves the width and height for the gameboard that the user clicks
                if 170 <= mouse[1] <= 220:
                    setClick = int((mouse[0]-70)/100 +5)
                    if 5 <= setClick <= 10:
                        setHeight = setClick
                elif height/2+130 <= mouse[1] <= height/2+180:
                    setClick = int((mouse[0]-70)/100 +4)
                    if 4 <= setClick <= 9:
                        setWidth = setClick
                if width/2-110 <= mouse[0] <= width/2+90 and height-120 <= mouse[1] <= height-50:
                    return [setHeight, setWidth]
        # fills the screen with a color 
        screen.fill((60,25,60)) 

        mouse = pygame.mouse.get_pos() 
        
        # creates height objects
        screen.blit(heightText, (width/2-67, 40))
        for i in range(5, 11):
            if (setHeight == i or (70 +(i-5)*100) <= mouse[0] <= (100 +(i-5)*100)+80 and 170 <= mouse[1] <= 220):
                pygame.draw.rect(screen, color_light, [(70 +(i-5)*100), 170, 80, 50])
            else:
                pygame.draw.rect(screen, color_dark, [(70 +(i-5)*100), 170, 80 , 50])
            if i%2 == 1:
                screen.blit(smallfont.render(str(i) , True , white) , (100 + (i-5)*100, 170))
            else:
                screen.blit(smallfont.render(str(i) , True , white) , (100 + (i-5)*100, 177))
        
        # creates width objects
        screen.blit(widthText, (width/2-67, height/2))
        for i in range(4, 10):
            if (setWidth == i or (70 +(i-4)*100) <= mouse[0] <= (70 +(i-4)*100)+80 and height/2+130 <= mouse[1] <= height/2+180):
                pygame.draw.rect(screen, color_light, [(70 +(i-4)*100), height/2+130, 80, 50])
            else:
                pygame.draw.rect(screen, color_dark, [(70 +(i-4)*100), height/2+130, 80 , 50])
            if i%2 == 1:
                screen.blit(smallfont.render(str(i) , True , white) , (100 + (i-4)*100, height/2+130))
            else:
                screen.blit(smallfont.render(str(i) , True , white) , (100 + (i-4)*100, height/2+137))
    
        # creates begin object
        if (width/2-110 <= mouse[0] <= width/2+90 and height-120 <= mouse[1] <= height-50):
            pygame.draw.rect(screen, color_light, [width/2-110, height-120, 200 , 70])
        else:
            pygame.draw.rect(screen, color_dark, [width/2-110, height-120, 200 , 70])
        screen.blit(mediumfont.render("Begin" , True , white) , (width/2-70, height-110))

        pygame.display.update() 

# Initalizes the board
def UI(board, height, width):
    pygame.init()
    widthPixel = width * SQUARESIZE
    heightPixel = (height+1) * SQUARESIZE
    size = (widthPixel, heightPixel)
    screen = pygame.display.set_mode(size)
    draw_board(board, height, width, screen)
    return screen

# Updates the visuals for the board
def draw_board(board, height, width, screen):
    for r in range(height):
        for c in range(width):
            pygame.draw.rect(screen, boardColor, (c*SQUARESIZE, r*SQUARESIZE+SQUARESIZE, SQUARESIZE, SQUARESIZE))
            pygame.draw.circle(screen, borderColor, (c*SQUARESIZE+SQUARESIZE/2, r*SQUARESIZE + SQUARESIZE + SQUARESIZE/2), int(SQUARESIZE/2-5))
            if board[r][c] == 0:
                pygame.draw.circle(screen, emptySpotColor, (c*SQUARESIZE+SQUARESIZE/2, r*SQUARESIZE + SQUARESIZE + SQUARESIZE/2), int(SQUARESIZE/2-10))
            elif board[r][c] == 1:
                pygame.draw.circle(screen, playerOneColor, (c*SQUARESIZE+SQUARESIZE/2, r*SQUARESIZE + SQUARESIZE + SQUARESIZE/2), int(SQUARESIZE/2-10))
            elif board[r][c] == 2:
                pygame.draw.circle(screen, playerTwoColor, (c*SQUARESIZE+SQUARESIZE/2, r*SQUARESIZE + SQUARESIZE + SQUARESIZE/2), int(SQUARESIZE/2-10))
    pygame.display.update()

def main():
    mode = menu()
    [width, height] = defineBoard()
    game(mode, width, height)
        
# The game logic 
def game(mode, width, height):
    board = [[0 for _ in range(width)] for _ in range(height)]
    player = 2
    screen = UI(board, height, width)
    smallfont = pygame.font.SysFont('Corbel',35) 
    winner = 0
    # While the game is in progress
    while True:
        if player == 1 or mode == 1:
            move = -1
            # Awaiting player move
            while move == -1:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()
                    if player == 1:
                        color = playerOneColor
                    else:
                        color = playerTwoColor
                    # This will create the player piece above the corresponding position
                    if event.type == pygame.MOUSEMOTION:
                        # This will erase the previous piece by overwriting it with a blank space
                        pygame.draw.rect(screen, emptySpotColor, (0, 0, width*SQUARESIZE, SQUARESIZE))
                        # Indexes the mouse position to over each possible playing position
                        posx = round((event.pos[0]-50)/100.0) * SQUARESIZE + 50
                        # This will create the player piece
                        pygame.draw.circle(screen, color, (posx, int(SQUARESIZE/2)), RADIUS)
                    pygame.display.update()
                    # Sets the player move
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        move = round((event.pos[0]-50)/100.0)
        # AI's move            
        else:         
            move = chooseMove(board, height, width, 2)
        # In the case that the move cannot be played
        if move >= width or move < 0 or not play(board, int(move), player, height):
            continue
        else:
            # Change the turn
            player = (player % 2) + 1
            # Check for a win/draw
            winner = win(board, height, width)
            # Update the board
            draw_board(board, height, width, screen)
            # If there's a winner, move on
            if (winner[0] != -2):
                winner = winner[0]
                break
    # After the game is over
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            mouse = pygame.mouse.get_pos() 
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Clicking the 'Try Again' button to restart this game with the same settings
                if (screen.get_width()/2-100 <= mouse[0] <= screen.get_width()/2+50 and screen.get_height()/2-100 <= mouse[1] <= screen.get_height()/2-30):
                    return game(mode, width, height)
                # Clicking the 'Menu' button to go back to the Menu screen 
                if (screen.get_width()/2-100 <= mouse[0] <= screen.get_width()/2+50 and screen.get_height()/2-20 <= mouse[1] <= screen.get_height()/2+50):
                    return main()
            # Creates the 'Try Again' object
            if (screen.get_width()/2-100 <= mouse[0] <= screen.get_width()/2+50 and screen.get_height()/2-100 <= mouse[1] <= screen.get_height()/2-30):
                pygame.draw.rect(screen, boardColor, [screen.get_width()/2-75, screen.get_height()/2-100, 150, 70])
            else:
                pygame.draw.rect(screen, borderColor, [screen.get_width()/2-75, screen.get_height()/2-100, 150, 70])
            screen.blit(smallfont.render("Try Again" , True , white) , (screen.get_width()/2-65, screen.get_height()/2-85))

            # Creates the 'Menu' object
            if (screen.get_width()/2-100 <= mouse[0] <= screen.get_width()/2+50 and screen.get_height()/2-20 <= mouse[1] <= screen.get_height()/2+50):
                pygame.draw.rect(screen, boardColor, [screen.get_width()/2-75, screen.get_height()/2-20, 150, 70])
            else:
                pygame.draw.rect(screen, borderColor, [screen.get_width()/2-75, screen.get_height()/2-20, 150, 70])
            screen.blit(smallfont.render("Menu" , True , white) , (screen.get_width()/2-40, screen.get_height()/2-5))

            # Checks for winner and adjusts the text accordingly
            if winner == 1:
                    screen.blit(smallfont.render("Player 1 Wins" , True , boardColor), (screen.get_width()/2-100, 50))
            elif winner == -1:
                    screen.blit(smallfont.render("Player 2 Wins" , True , boardColor), (screen.get_width()/2-100, 50))
            else:
                screen.blit(smallfont.render("Cats Game" , True , playerOneColor), (screen.get_width()/2-100, 50))
        pygame.display.update()

main()
