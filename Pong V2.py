import pygame
import time
import random

#Functions
pygame.init()
#Defining Player 1
def player1(y1):
    pygame.draw.rect(window,white, [50,y1,5,50])

#Defining Player 2
def player2(y2):
    pygame.draw.rect(window,white, [750,y2,5,50])

#Defining the ball
def ball(ballx,bally):
    pygame.draw.rect(window,white,[ballx+ballx_change,bally+bally_change-16,8,8])

#Defining where and with what font to display the score
def score_display():
    display_p1_score=my_font.render(score_values[p1_score],1,white)
    window.blit(display_p1_score,[250,50])
    display_p2_score=my_font.render(score_values[p2_score],1,white)
    window.blit(display_p2_score,[515,50])

#Counting score when ball hits either left or right boundary
def score_count():
    global p1_score
    global p2_score
    if ballx+ballx_change<=0:
        p2_score+=1
    if ballx+ballx_change>=(display_width-8):
        p1_score+=1

#Function that decides where the ball will start
def starting_ball():
    global ballx_change
    global bally_change
    global ballx
    global bally
    #Choosing random point on y-axis but staying in the center of the x-axis
    bally=random.randrange(0,display_height-8)
    ballx=400

    #Reseting velocity variables
    ballx_change=0
    bally_change=0

    #Reseting ball
    ball(ballx,bally)
    #If the ball spawns below the ceneter of the screen set direction as 4
    if bally>=300:
        bally_change+=ball_speed2
        direction=4
    #If the ball spawns above the center of the screen set direction as 3
    if bally<=300:
        bally_change+=ball_speed1
        direction=3
    #First ball always moves towards player 1 so ball_speed2 is chosen
    ballx_change+=ball_speed2
    #return False and the direction of initial travel
    return False,direction

#This is the core funtion that determines direction of travel based on input
#from other parts of the code
#This whole function is based on diagonal linear movement on a cartisian plane
def in_game(start_direction):
    global ballx_change
    global bally_change

    #If start direction is 3, ball moves in a direction of QuadrantIII on a
    #cartisian plane
    if start_direction==3:
        bally_change+=ball_speed1
        ballx_change+=ball_speed2
    #If start direction is 4, ball moves in a direction of QuadrantII on a
    #cartisian plane
    elif start_direction==4:
        bally_change+=ball_speed2
        ballx_change+=ball_speed2
    #If start direction is 5, ball moves in a direction of QuadrantIIII on a
    #cartisian plane
    elif start_direction==5:
        bally_change+=ball_speed1
        ballx_change+=ball_speed1
    #If start direction is 6, ball moves in a direction of QuadrantI on a
    #cartisian plane
    elif start_direction==6:
        bally_change+=ball_speed2
        ballx_change+=ball_speed1
    
#End screen function
def end_screen(p1_score,p2_score):

    #Screen loop
    end_screen=True
    #initialising colours
    colour1=white
    colour2=white
    while end_screen==True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
        
        window.fill(black)
        #If player 1 gets a score of 3 display that they won
        if p1_score==3:
            winner=my_font.render("Player 1 WINS!!!",1,white)
            window.blit(winner,[230,100])
        #Otherwise player 2 must have won so display that they won
        elif p2_score==3:
            winner=my_font.render("Player 2 WINS!!!",1,white)
            window.blit(winner,[250,100])
        else:
            winner=my_font.render("No one won",1,white)
            window.blit(winner,[280,100])

        #Display text for buttons
        restart=my_font.render("Restart",1,white)
        window.blit(restart,[175,300])
        quit_game=my_font.render("Quit",1,white)
        window.blit(quit_game,[500,300])

        #Checking mouse positions and clicks
        mouse_spot=pygame.mouse.get_pos()
        mouse_click=pygame.mouse.get_pressed()

        #If mouse is hovering over button change colour  
        if 200+100>=mouse_spot[0]>=200 and 400+50>=mouse_spot[1]>=400:
            colour1=green
            #If mouse is clicked on that button return the true value
            if mouse_click[0]==1:
                return True
        #If mouse is hovering over button change the colour
        elif 500+100>=mouse_spot[0]>=500 and 400+50>=mouse_spot[1]>=400:
            colour2=red
            #if mouse is clicked on that button return the false value
            if mouse_click[0]==1:
                return False
        #If mouse is not on buttons make them a neutral white colour
        else:
            colour1=white
            colour2=white
        #Draw the buttons
        pygame.draw.rect(window,colour1, [200,400,100,50])
        pygame.draw.rect(window,colour2, [500,400,100,50])
        #refresh screen
        pygame.display.update()
        clock.tick(60)

#title screen function (title screen function is down here to avoid an error...
#...I run into when it is declared at the top with the rest of the functions)
def title_screen():
    global ball_speed1
    global ball_speed2
    title=True
    #neutral button colours
    colour1=white
    colour2=white
    colour3=white
    while title==True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()

        #Filling screen with black and rendering all the text to the screen
        window.fill(black)
        title_name=my_font.render("2-Player Pong",1,white)
        easy=my_font.render("Easy",1,white)
        window.blit(easy,[125,300])
        medium=my_font.render("Medium",1,white)
        window.blit(medium,[325,300])
        hard=my_font.render("Hard",1,white)
        window.blit(hard,[575,300])
        window.blit(title_name,[265,100])

        #calling in a fucntion to check mouse positions and clicks
        mouse_spot=pygame.mouse.get_pos()
        mouse_click=pygame.mouse.get_pressed()

        #if mouse is over easy button change the colour
        if 125+100>=mouse_spot[0]>=125 and 400+50>=mouse_spot[1]>=400:
            colour1=green
            #if player clicks easy button set ballspeed to 2 and start game
            if mouse_click[0]==1:
                ball_speed1=2
                ball_speed2=-2
                break
        #if mouse is over medium button change the colour
        elif 350+100>=mouse_spot[0]>=350 and 400+50>=mouse_spot[1]>=400:
            colour2=yellow
            #if player clicks medium button set ballspeed to 3 and start game
            if mouse_click[0]==1:
                ball_speed1=3
                ball_speed2=-3
                break
        #if mouse is over hard button change the colour
        elif 575+100>=mouse_spot[0]>=575 and 400+50>=mouse_spot[1]>=400:
            colour3=red
            #if player clicks hard button set ballspeed to 4 and start game
            if mouse_click[0]==1:
                ball_speed1=4
                ball_speed2=-4
                break
        #if no button is pressed leave them as a neutral white colour
        else:
            colour1=white
            colour2=white
            colour3=white
        #draw the buttons to the sceeen
        pygame.draw.rect(window,colour1, [125,400,100,50])
        pygame.draw.rect(window,colour2, [350,400,100,50])
        pygame.draw.rect(window,colour3, [575,400,100,50])

        #refreshing screen at 60 fps
        pygame.display.update()
        clock.tick(60)

#Global Variables
#Just some variable declarations
#Window Dimensions
display_width=800
display_height=600

#Initialising colours
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
black=(0,0,0)
white=(255,255,255)
yellow=(255,255,0)

#Initialising Font
my_font=pygame.font.SysFont("OCR A Extended",60)

#Setting up window, window name and framerate
window=pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Pong")
clock=pygame.time.Clock()

#ball position at starting point
bally=random.randrange(0,display_height-8)
ballx=400

#Determines speed and changes the direction of movement for the ball
ball_speed1=0
ball_speed2=0

#Ballspeedx checks if the ball is moving positively or negatively along the x-axis
ballspeedx=False

#Changes in ball X and Y based on where it bounces off of
ballx_change=0
bally_change=0

#Restart variable
next_ball=True

#Initialising start_direction
start_direction=0

#List of possible scores and P1,P2 scores at any given moment
score_values=["0","1","2","3"]

#If player doesnt click the exit button then run will always be true
run=True

#Lists for possible bounce directions if the ball hits p1 or p2
list_p1_bounce=[5,6]
list_p2_bounce=[3,4]

#Restart Variable
end_game=True

#Restart Loop
while end_game==True:   
    #run the title screen once just before main game loop
    title_screen()
    #Reset the variables related to score and player positions
    p1_score=0
    p2_score=0
    y1=250
    y2=250
    y1_change=0
    y2_change=0
    run=True
    #Game Loop
    #If p1 and p2 are less than 3 and they havent pressed the exit button run the game
    while p1_score!=3 and p2_score!=3 and run==True:
        
        #Collecting all inputs from the players
        for event in pygame.event.get():
            #If exit button is pressed run becomes false and game ends
            if event.type==pygame.QUIT:
                run=False

            #If P1 or P2 uses their respective move keys move their player up or down
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_UP:
                    y2_change=-3
                elif event.key==pygame.K_DOWN:
                    y2_change=3
                elif event.key==pygame.K_w:
                    y1_change=-3
                elif event.key==pygame.K_s:
                    y1_change=3
        #Add the movement changes that the players did to their characters
        y1+=y1_change
        y2+=y2_change

        #Adding boundaries to the characters, doesnt allow movement passed window 
        if y1<=0 or y1>=550:
            y1_change=0
        if y2<=0 or y2>=550:
            y2_change=0

        #Drawing all functions to the window
        window.fill(black)
        player1(y1)
        player2(y2)
        score_count()
        score_display()
        
        #Running the next_ball function only once until ball is scored or game is exited
        if next_ball==True or run==False:
            next_ball,start_direction=starting_ball()

        #Keeps Printing ball
        ball(ballx,bally)

        #All different bounce possbilities based on which of the 4 cielings the ball
        #hits and in which direction the ball is travelling when it hits that cieling
        if bally_change+bally<=8 and ballx_change+ballx<=400 and ballspeedx==False: 
            start_direction=3
        if bally_change+bally>=600 and ballx_change+ballx<=400 and ballspeedx==False:
            start_direction=4
        if bally_change+bally<=8 and ballx_change+ballx>=400 and ballspeedx==False:
            start_direction=3
        if bally_change+bally>=600 and ballx_change+ballx>=400 and ballspeedx==False:
            start_direction=4
        if bally_change+bally<=8 and ballx_change+ballx<=400 and ballspeedx==True: 
            start_direction=5
        if bally_change+bally>=600 and ballx_change+ballx<=400 and ballspeedx==True:
            start_direction=6
        if bally_change+bally<=8 and ballx_change+ballx>=400 and ballspeedx==True:
            start_direction=5
        if bally_change+bally>=600 and ballx_change+ballx>=400 and ballspeedx==True:
            start_direction=6

        #If the ball hits Player 1 what happens?
        if ballx+ballx_change<=58:
            if bally+bally_change>=y1+y1_change and bally+bally_change<=(y1+y1_change)+50:
                if ballx+ballx_change>=50:
                    #Bounces randomly up or down
                    start_direction=random.choice(list_p1_bounce)
                    #Ball speed for the x-axis remains positive until it hits p2
                    ballspeedx=True
                
        #If the ball hits Player 2 what happens?
        if ballx+ballx_change>=742:
            if bally+bally_change>=(y2+y2_change) and bally+bally_change<=(y2+y2_change)+50:
                if ballx+ballx_change<=755:
                    #Bounces randomly up or down
                    start_direction=random.choice(list_p2_bounce)
                    #Ball speed for the x-axis remains negative until it hits p1
                    ballspeedx=False
             
        #Run the direction function to see where the ball should go
        in_game(start_direction)

        #Test cases to see if values do what they are supposed to
        '''
        print(bally_change,start_direction)
        print(ballx_change+ballx)
        print(start_direction)
        print(bally_change+bally)
        print(bally)
        print(clock)
        '''

        #If the ball hits either one of the goals restart the game
        if ballx+ballx_change<=0 or ballx+ballx_change>=792:
            next_ball=True

        #Update the window with new fills
        pygame.display.update()
        #Run at 60 fps
        clock.tick(60)

    #Only displays winner text if someone actually won, if player pressed quit...
    #...game just ends 
    if p1_score==3 or p2_score==3 or run==False:
        #If in the end game screen player chose restart the end_game variable...
        #...will remain true and restart the game but if the player...
        #...chose quit it will return false and proceed to exit the main game loop
        end_game=end_screen(p1_score,p2_score)

#Quits the game
pygame.quit()
quit()
