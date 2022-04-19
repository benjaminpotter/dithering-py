import sys
import pygame

class DitheredImage(pygame.Surface):

    def __init__(self, filepath):
        super().__init__( (1280, 720) ) # full screen size
        loaded = pygame.image.load(filepath)
        size = loaded.get_rect().size
        self.blit(loaded, size)

def main():
    pygame.init()
    
    screen = pygame.display.set_mode( (1280, 720) )
    
    image = DitheredImage("assets/img1.bmp")
    image_rect = image.get_rect()
    image_pos = (image_rect.x, image_rect.y)
    #image = pygame.transform.scale(image, (10, 10))

    while True:
        for evt in pygame.event.get():
            if evt.type == pygame.QUIT: sys.exit()
            # other events here
            if evt.type == pygame.KEYDOWN:
                if   evt.key == pygame.K_w:
                    # move up
                    pass
                elif evt.key == pygame.K_s:
                    # move down
                    pass
                elif evt.key == pygame.K_a:
                    # move left
                    pass
                elif evt.key == pygame.K_d:
                    # move right
                    pass

        screen.fill( (0, 0, 0) )
        screen.blit(image, image_pos)
        pygame.display.flip()

if __name__ == "__main__":
    main()
