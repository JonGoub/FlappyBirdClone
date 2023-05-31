import pygame
import time
from components.objects import pipe, bottom, FlappyBird

class GameplayScreen():
    """ The gameplay screen of the Flappy Bird game.
    """

    def __init__(self,screen):
        """ Initializes the gameplay screen.

        Args:
            screen (pygame.display): The screen the start screen elements will be displayed on.
        """
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.running = True
        self.score = 0

        #point variables
        self.first = False
        self.second = False

        #Loading images
        self.background = pygame.image.load('./assets/images/screens/background.png')
        self.background = pygame.transform.scale(self.background,(400,600))
        self.bottom_image = pygame.image.load('./assets/images/bottom/block.png')
        topbar = pygame.image.load('./assets/images/pipes/pipe_down.png')
        self.topbar = pygame.transform.scale(topbar,(80,600))
        bottombar = pygame.image.load('./assets/images/pipes/pipe_up.png')
        self.bottombar = pygame.transform.scale(bottombar,(80,600))

        #Gamefont
        self.font = pygame.font.Font('freesansbold.ttf', 32)

        #Audio
        self.hit_sound = pygame.mixer.Sound('./assets/sounds/hit.wav')
        self.point_sound = pygame.mixer.Sound('./assets/sounds/point.wav')

        #Creating bird
        self.bird = FlappyBird(40,100)

        #Creating game pipes
        self.pipes = pipe.get_pipes()

        #Creating moving bottom row
        self.bottoms = bottom.get_bottoms()

    def run(self):
        """ Runs the game loop for the gameplay screen.

        Returns:
            int: The final score the user earned.
        """
        while self.running:

            #Displays background
            self.screen.blit(self.background,(0, 0))
      
            ##Shuts down application if user exits out of window
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    exit()

                #Handling user input
                keys = pygame.key.get_pressed()
                if keys[pygame.K_SPACE] or keys[pygame.K_UP]:
                    self.bird.isJumping = True
                    self.bird.jump_counter = 1 

            #Gravity and jumping
            self.bird.jump()

            #Checking for collision with ground
            if self.bird.get_bottom() >= 510:
                pygame.mixer.Sound.play(self.hit_sound)
                time.sleep(1)
                self.running = False
                return self.score

            #Displaying pipes and checking if player earns a point 
            self.second = False
            for pipe in self.pipes:
                if (self.bird.get_left() >= pipe.get_leftbar() and self.bird.get_right() <= pipe.get_rightbar()) or (self.bird.get_right() >= pipe.get_leftbar() and self.bird.get_right() <= pipe.get_rightbar()) or (self.bird.get_left() < pipe.get_rightbar() and self.bird.get_right() > pipe.get_rightbar()):
                    self.first = True
                    self.second = True
                    #Checking if bird hit top pipe
                    if self.bird.get_top() <= pipe.get_topbar() :
                        pygame.mixer.Sound.play(self.hit_sound)
                        time.sleep(1)
                        self.running = False
                        return self.score
                    #Checking if bird hit bottom pipe
                    if self.bird.get_bottom() >= pipe.get_bottombar():
                        pygame.mixer.Sound.play(self.hit_sound)
                        time.sleep(1)
                        self.running = False
                        return self.score
                    
                #Updating and displaying pipes on screen
                pipe.update()
                self.screen.blit(self.topbar, (pipe.x,pipe.get_topbar()-600))
                self.screen.blit(self.bottombar, (pipe.x, pipe.get_bottombar()))

            #Checking if bird past pipes
            if self.first == True and self.second == False:
                pygame.mixer.Sound.play(self.point_sound)
                self.second = False
                self.first = False
                self.score += 1

            #Displaying all the bottoms
            for b in self.bottoms: 
                b.update()
                self.screen.blit(self.bottom_image,(b.x,510))

            #Looping bottoms that are off screen
            for b in self.bottoms:
                if b.get_right() < 0:
                    self.bottoms.remove(b)
                    newb = bottom(self.bottoms[-1].x + 71)
                    self.bottoms.append(newb)
                
            #Display birds
            self.screen.blit(self.bird.image,(40,self.bird.y))
            self.bird.update()

            #Displaying score
            self.display_score()

            #Check if user won
            self.wongame()
        
            # Flip the display
            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()

  
    def display_score(self):
        """ Displays live score on screen.
        """
        text = self.font.render(f'{self.score}', True, (255, 255, 255))
        self.screen.blit(text,(200,20))


    def wongame(self):
        """ Displays message indicating user won the game.
        """
        if self.score == 100:
            text = self.font.render("Congrats!", True, (255, 255, 255))
            text2 = self.font.render("you have no life!", True, (255, 255, 255))
            self.screen.blit(text,(120,50))
            self.screen.blit(text2,(80,82))
        

    def reset(self):
        """ Resets all round dependent values.
        """
        self.running = True
        self.score = 0
        self.first = False
        self.second = False
        self.pipes = pipe.get_pipes()
        self.bottoms = bottom.get_bottoms()
        self.bird = FlappyBird(40,100)







