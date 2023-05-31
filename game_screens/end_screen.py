import pygame
import time
class EndScreen():
    """ The end screen of the Flappy Bird game.
    """
    def __init__(self,screen):
        """ Initializes the end screen.

        Args:
            screen (pygame.display): The screen the start screen elements will be displayed on.
        """
        self.score = 0
        self.running = True
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.highscore = 0
        self.background = pygame.image.load('./assets/images/screens/end_screen.png')
        self.background = pygame.transform.scale(self.background,(400,600))

    def run(self,score):
        """ Runs the game loop for the end screen.

        Args:
            score (int): The score the user earned during their gameplay.
        """
        while self.running:
            self.screen.blit(self.background,(0, 0))

            # Did the user click the window close button?
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    exit()
                    
            #Processing user input
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE] or keys[pygame.K_UP]:
                self.running = False
                time.sleep(.5)
                return 

            #Updating and displaying scores
            self.update_highscore(score)
            self.display_scores(score)

            # Flip the display
            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()


    def display_scores(self,score):
        """ Displays the score and highscore on the end screen.

        Args:
            score (int): The score the user earned during their gameplay.
        """
        #Font used for scores
        font = pygame.font.Font('freesansbold.ttf', 32)

        #Display current score
        score = font.render(f'{score}', True, (255, 255, 255))
        self.screen.blit(score,(300,255))

        #Display highscore
        highscore = font.render(f'{self.highscore}', True, (255, 255, 255))
        self.screen.blit(highscore,(300,320))

    #Retrieves saved highscore and overwrites if necissary
    def update_highscore(self,score):
        """ Overwrites saved highscore value if user got a score higher than their previous highscore.

        Args:
            score (int): The score the user earned during their gameplay.
        """
        f = open("./assets/highscore.py","r+")
        highscore = int(f.readline().strip("\n"))

        if score > highscore:
            f = open("./assets/highscore.py","w")
            self.highscore = score
            f.write(str(score))
        else:
            self.highscore = highscore


    def reset(self):
        """ Resets all round dependent values.
        """
        self.score = 0
        self.running = True

        
        
        














