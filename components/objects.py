import pygame
import random


class FlappyBird():
    """ The Flappy Bird character that the user controls.
    """
    def __init__(self,x,y):
        """Initializes the FlappyBird class. 

        Args:
            x (int): The x coordinate of the flappy bird.
            y (int): The y coordinate of the flappy bird.
        """
        self.jump_sound = pygame.mixer.Sound('./assets/sounds/jump.wav')
        self.x = x
        self.y = y
        self.images = []
        self.index = 0
        self.counter = 0
        self.images.append(pygame.transform.scale(pygame.image.load('./assets/images/birds/bird1.png'),(51,36)))
        self.images.append(pygame.transform.scale(pygame.image.load('./assets/images/birds/bird2.png'),(51,36)))
        self.images.append(pygame.transform.scale(pygame.image.load('./assets/images/birds/bird3.png'),(51,36)))
        self.image = self.images[self.index]
        self.jump_counter = 1
        self.isJumping = False
    

    def update(self):
        """ Calculates when to change the image of the flappy bird.
        """
        self.counter += 1
        flap_change = 5

        if self.counter > flap_change:
            self.counter = 0
            self.index += 1
            if(self.index == 3):
                self.index = 0

        self.image = self.images[self.index]


    def jump(self):
        """ Executes the jump motion of the flappy bird.
        """
        #This makes sure the jump sound plays once throught jump sequence
        if self.isJumping == True:

            if self.jump_counter == 2:
                pygame.mixer.Sound.play(self.jump_sound)

            if self.jump_counter < 6:
                self.y -= 30 * (1/(self.jump_counter))
                self.jump_counter += 1
            elif self.jump_counter < 11:
                self.y += 3 * (1/(self.jump_counter - 5))
                self.jump_counter += 1
            else:
                self.isJumping = False
                self.jump_counter = 1 
        else:
            self.y += 3

    def get_top(self):
        """ Gets the top y coordinate of the flappy bird.

        Returns:
            int: The top y coordinate of the flappy bird.
        """
        return self.y 

    def get_bottom(self):
        """ Gets the bottom y coordinate of the flappy bird.

        Returns:
            int: The bottom y coordinate of the flappy bird.
        """
        return self.y + 36
    
    def get_right(self):
        """ Gets the right x coordinate of the flappy bird.

        Returns:
            int: The right x coordinate of the flappy bird.
        """
        return (self.x + 51)
    
    def get_left(self):
        """ Gets the left x coordinate of the flappy bird.

        Returns:
            int: The left x coordinate of the flappy bird.
        """
        return self.x


class pipe():
    """ The pipe objects that represents the two pipes that the flappy bird must dodge.
    """
    def __init__(self, x, y):
        """Initializes the pipe object.

        Args:
            x (int): The x coordinate of the pipe.
            y (int): The y coordinate of the pipe.
        """
        self.x = x 
        self.y = y


    def get_pipes():
        """ Returns a list of 100 pipe objects.

        Returns:
            List: List of 100 pipe objects.
        """
        pipes = []
        for i in range(100):
            if len(pipes) < 1:
                pipes.append(pipe(400,random.randrange(50,300)))
            else:
                pipes.append(pipe(pipes[-1].x + 300 ,random.randrange(50,300)))
        return pipes
    
    def update(self):
        """ Increments the x coordinate of the pipes by -3
        """
        self.x -= 3


    def get_bottombar(self):
        """ Gets the y coordinate of the top of the bottom bar.

        Returns:
            int: The Y coordinate of the top of the bottom bar.
        """
        return self.y + 150
    

    def get_topbar(self):
        """ Gets the y coordinate of the bottom of the topbar.

        Returns:
            int: The y coordinate of the bottom of the topbar.
        """
        return self.y
    

    def get_leftbar(self):
        """Gets the left x coordinate of the pipes.

        Returns:
            int: The left x coordinate of the pipes.
        """
        return self.x
    

    def get_rightbar(self):
        """ Gets the right x coordinate of the pipes.

        Returns:
            int: The right x coordinate of the pipes.
        """
        return self.x + 80
    

class bottom():
    """ Bottom piece object that moves backwards along with the pipes.
    """
    def __init__(self,x):
        """ Initializes the bottom class.

        Args:
            x (int): The x coordinate of the bottom piece.
        """
        self.x = x

    def get_bottoms():
        """ Returns a list of bottom pieces.

        Returns:
            List: List of bottom pieces.
        """
        bottoms = []
        for i in range(10):
            bottoms.append(bottom(71* i))
        return bottoms
    
    def update(self):
        """ Increments the x coordinate of the bottom down by 3.
        """
        self.x -= 3

    def get_right(self):
        """ Gets the right x coordinate of the bottom.

        Returns:
            int: The right x coordinate of the bottom.
        """
        return self.x + 71
    

        

