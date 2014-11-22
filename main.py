import pygame
import random


def drawPad(surface, length, breadth, x, y):

    if x > surface.get_width() - length:
        x = surface.get_width() - length

    if x < 0:
        x = 0
    
    pygame.draw.rect(surface, pygame.color.Color("cyan"), [x, y, length, breadth])

def showMenu(surface, width, height):
    
    ## LOAD FONT
    font = pygame.font.Font("assets/fonts/Tr2n.ttf", 50)

    ## CREATE TEXT
    title = font.render("PONG", 1, (0, 255, 255))
    singlePlayer = font.render("Single Player", 1, (0, 255, 255))
    multiPlayer = font.render("Multiplayer", 1, (0, 255, 255))
    quitText = font.render("Quit", 1, (0, 255, 255))

    diffLevels = ["Easy", "Medium", "Hard", "Insanity"]
    diffStatus = 1
    difficulty = font.render("Difficulty: "+diffLevels[diffStatus], 1, (0, 255, 255))
    
    ## MARGINS
    titleMargin = 50
    spMargin = 100
    mpMargin = 160
    dMargin = 220
    qMargin = 280
    
    ## BOOLEAN FLAGS FOR STUFF
    flag = True
    quit = False
    clicked = False
    
    ## TO CHECK WHICH OPTION IS BEING HOVERED ON
    textStatii = [False, False, False, False]
     
    while flag:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                flag = False
                quit = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                clicked = True

        ## SINGLE
                
        if (width/2 - singlePlayer.get_width()/2 <= pygame.mouse.get_pos()[0] <= width/2 + singlePlayer.get_width()/2) and (titleMargin + spMargin <= pygame.mouse.get_pos()[1] <= titleMargin + spMargin + singlePlayer.get_height()):
            textStatii[0] = True
            
            singlePlayer = font.render("Single Player", 1, (255, 255, 255))
            pygame.mouse.set_cursor(*pygame.cursors.diamond)

            if clicked:
                clicked = False
                flag = False
        else:
            textStatii[0] = False
            
            singlePlayer = font.render("Single Player", 1, (0, 255, 255))

            if True not in textStatii:
                pygame.mouse.set_cursor(*pygame.cursors.arrow)

        ## MULTI
                
        if (width/2 - multiPlayer.get_width()/2 <= pygame.mouse.get_pos()[0] <= width/2 + multiPlayer.get_width()/2) and (titleMargin + mpMargin <= pygame.mouse.get_pos()[1] <= titleMargin + mpMargin + multiPlayer.get_height()):
            textStatii[1] = True
            
            multiPlayer = font.render("Multiplayer", 1, (255, 255, 255))
            pygame.mouse.set_cursor(*pygame.cursors.diamond)

            if clicked:
                clicked = False
                flag = False
        else:
            textStatii[1] = False
            
            multiPlayer = font.render("Multiplayer", 1, (0, 255, 255))

            if True not in textStatii:
                pygame.mouse.set_cursor(*pygame.cursors.arrow)

        ## DIFFICULTY
                
        if (width/2 - difficulty.get_width()/2 <= pygame.mouse.get_pos()[0] <= width/2 + difficulty.get_width()/2) and (titleMargin + dMargin <= pygame.mouse.get_pos()[1] <= titleMargin + dMargin + difficulty.get_height()):
            textStatii[2] = True
            
            difficulty = font.render("Difficulty: "+diffLevels[diffStatus], 1, (255, 255, 255))
            pygame.mouse.set_cursor(*pygame.cursors.diamond)

            if clicked:
                clicked = False

                diffStatus = diffStatus + 1 - (len(diffLevels) * (diffStatus/(len(diffLevels) - 1)))
                
        else:
            textStatii[2] = False
            
            difficulty = font.render("Difficulty: "+diffLevels[diffStatus], 1, (0, 255, 255))

            if True not in textStatii:
                pygame.mouse.set_cursor(*pygame.cursors.arrow)

        ## QUIT
                
        if (width/2 - quitText.get_width()/2 <= pygame.mouse.get_pos()[0] <= width/2 + quitText.get_width()/2) and (titleMargin + qMargin <= pygame.mouse.get_pos()[1] <= titleMargin + qMargin + quitText.get_height()):
            textStatii[3] = True
            
            quitText = font.render("Quit", 1, (255, 255, 255))
            pygame.mouse.set_cursor(*pygame.cursors.diamond)

            if clicked:
                clicked = False
                flag = False
                quit = True
        else:
            textStatii[3] = False
            
            quitText = font.render("Quit", 1, (0, 255, 255))

            if True not in textStatii:
                pygame.mouse.set_cursor(*pygame.cursors.arrow)


        ## DRAW ALL TEXT

        surface.fill(pygame.Color("black"))
        
        surface.blit(title, (width/2 - title.get_width()/2, titleMargin))
        surface.blit(singlePlayer, (width/2 - singlePlayer.get_width()/2, titleMargin + spMargin))
        surface.blit(multiPlayer, (width/2 - multiPlayer.get_width()/2, titleMargin + mpMargin))
        surface.blit(difficulty, (width/2 - difficulty.get_width()/2, titleMargin + dMargin))
        surface.blit(quitText, (width/2 - quitText.get_width()/2, titleMargin + qMargin))

        if clicked:
            clicked = False
        
        pygame.display.update()

    if quit:
        return [False, diffStatus]
    else:
        return [True, diffStatus]

def run_game(surface, screen_width, screen_height, velocity):

    width = screen_width
    height = screen_height
    screen = surface

    ## HIT PAD STUFF
    length = 110
    breadth = 20
    
    marginX = length/2
    marginY = width - length/2

    ## USER HIT PAD

    userX = width/2 - length/2
    userY = 3*height/4 - breadth/2

    ## COMP HIT PAD

    compX = width/2 - length/2
    compY = height/4 - breadth/2

    ## BALL

    radius = 10

    initBallX = width/2 - radius
    initBallY = height/2 - radius

    ballX = initBallX
    ballY = initBallY
    
    velX = velocity
    velY = velocity

    bounceX = 1
    bounceY = 1

    ballMarginX = (radius, width - radius)
    ballMarginY = (radius, height - radius)
    
    ## MOUSE
    mX = 0
    mY = 0

    ## SCORES/SCORE TEXT
    ballOut = False

    userScore = 0
    compScore = 0
    
    scoreFont = pygame.font.Font("assets/fonts/lcd.ttf", 40)
    
    ## START/STOP SWITCH
    keepGoing = True
    menuStatus = False

    ## FPS
    fps = 30
    clock = pygame.time.Clock()
    
    while (keepGoing):

        clock.tick(fps)
        
        screen.fill(pygame.color.Color("black"))
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    keepGoing = False
                    menuStatus = True


        ## SCORE DISPLAY
        userScoreDisplay = scoreFont.render("P 1: "+str(userScore), 1, (0, 255, 255))
        compScoreDisplay = scoreFont.render("P2: "+str(compScore), 1, (0, 255, 255))
      
        surface.blit(userScoreDisplay, (20, height-90))
        surface.blit(compScoreDisplay, (20, height-40))
        
        ## PADS
                
        mX = pygame.mouse.get_pos()[0]
        
        if (mX > marginX and mX < marginY):
            userX = mX - length/2

        ## COMP/P2 - CALCULATE TRAJECTORY AND MOVE
        targetX = compY - ballY + ballX ## Using: y - y1 = m(x - x1) and
                                        ## formula for intersection of lines
        compX = targetX
        
        drawPad(screen, length, breadth, userX, userY)
        drawPad(screen, length, breadth, compX, compY)

        ## BALL

        if (ballY <= ballMarginY[0] or ballY >= ballMarginY[1]):
            ballOut = True

            if ballY <= ballMarginY[0]:
                userScore += 1
            else:
                compScore += 1

        if ballOut:
            ballX = initBallX
            ballY = initBallY

            bounceX = 1
            bounceY = 1

            ballOut = False

        else:
            if (userX <= ballX <= userX + length and userY - radius/2 <= ballY <= userY + breadth - radius/2):
                bounceY *= -1

            if (compX <= ballX <= compX + length and compY - radius/2 <= ballY <= compY + breadth - radius/2):
                bounceY *= -1
                
            if (ballX < ballMarginX[0] or ballX > ballMarginX[1]):
                bounceX *= -1
        
            ballX += velX * bounceX
            ballY += velY * bounceY
        
        pygame.draw.circle(screen, pygame.color.Color("cyan"), (ballX, ballY), radius)

        pygame.display.update()

    return menuStatus


def main():

    pygame.init()
    pygame.font.init()
  
    width = 640
    height = 480
    screen = pygame.display.set_mode((width,height))
    
    menuData = showMenu(screen, width, height)
    velocity = (menuData[1] + 1)**2 + 1
    
    displayMenu = False
    
    if menuData[0]:
        displayMenu = run_game(screen, width, height, velocity)

        if displayMenu:
            main()
    
    pygame.quit()

main()
