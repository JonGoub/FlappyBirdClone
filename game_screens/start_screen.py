import pygame
from components.objects import FlappyBird


class StartScreen():
    """ The start screen of the Flappy Bird game.
    """
    def __init__(self,screen):
        """ Initializes the start screen.

        Args:
            screen (pygame.display): The screen the start screen elements will be displayed on.
        """
        self.screen = screen
        self.running = True
        self.clock = pygame.time.Clock()
        self.background = pygame.image.load('./assets/images/screens/start_screen.png')
        self.background = pygame.transform.scale(self.background,(400,600))
        self.bird = FlappyBird(20,80)

    def run(self):
        """ Runs the game loop for the start screen.
        """

        while self.running:
        
            #Shuts down application if user exits out of window
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    exit()
                    
            #Gets and processes user input
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE] or keys[pygame.K_UP]:
                self.running = False
                return 
            
            #Displays images on screen
            self.screen.blit(self.background,(0, 0))
            self.screen.blit(self.bird.image,(40,100))
            self.bird.update()
                
            #Updates display and handles framerate
            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()


    def reset(self):
        """ Resets all round dependent values.
        """
        self.running = True
