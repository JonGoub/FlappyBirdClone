'''
This is a Flappy Birds clone.

Author: Jonathan Goubeaux
Email: jongfcps@gmail.com
'''

import pygame
from game_screens.gameplay_screen import GameplayScreen
from game_screens.end_screen import EndScreen
from game_screens.start_screen import StartScreen

#Setting up the game
pygame.init()
screen = pygame.display.set_mode((400, 600))
running = True

#Initializing the three different game screens
start_screen = StartScreen(screen)
gameplay_screen = GameplayScreen(screen)
end_screen = EndScreen(screen)

#Entry point into the game
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
           
    #Running the screens(The gameplay_screen object returns the score which is then displayed in the end screen)
    start_screen.run()
    score = gameplay_screen.run() 
    end_screen.run(score)
    
    #Resetting the screens for the new round
    start_screen.reset()
    gameplay_screen.reset()
    end_screen.reset()

#Exits the game window once the loop is done running
pygame.quit()