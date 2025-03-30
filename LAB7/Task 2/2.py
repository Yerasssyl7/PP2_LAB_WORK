import pygame
import datetime
import time


def blitRotateCenter(surf, image, topleft, angle):

    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center = image.get_rect(topleft = topleft).center)

    surf.blit(rotated_image, new_rect)








pygame.init()
pygame.display.set_caption("Snake")



screen = pygame.display.set_mode((800,400))
clock = pygame.time.Clock()
font = pygame.font.Font (r"C:\Users\Ерасыл\OneDrive\Desktop\task1\font\Pixeltype.ttf", 100)
done = False

mickey = pygame.image.load(r"C:\Users\Ерасыл\OneDrive\Desktop\task1\pics\main1.png").convert()
mickey_rect = mickey.get_rect(topleft = (0 , 0))

right_hand = pygame.image.load(r"C:\Users\Ерасыл\OneDrive\Desktop\task1\pics\right-hand.png")
right_rect = right_hand.get_rect(center = (400,400))

left_hand = pygame.image.load(r"C:\Users\Ерасыл\OneDrive\Desktop\task1\pics\left-hand.png")
left_rect = left_hand.get_rect(center = (400,400))





DEFAULT_IMAGE_SIZE = (800, 400)
mickey = pygame.transform.scale(mickey, DEFAULT_IMAGE_SIZE)
right_hand = pygame.transform.scale(right_hand, (200,200))
left_hand = pygame.transform.scale(left_hand, (200,200))



while not done:
    
    time_of_clock = datetime.datetime.now().strftime(r"%M:%S")
    tt = datetime.datetime.now()
    min  = tt.minute
    sec = tt.second
    ang_min = -(6 * min + (sec / 10)) 
    ang_sec = -(6 * sec) - 90


    text = font.render(time_of_clock, True, 'Green')
    text_rect = text.get_rect(topleft = (100, 200)) 
  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

   




    print(F"{min} {sec}")


    screen.blit(mickey, mickey_rect)
    blitRotateCenter(screen, right_hand, (270,100), ang_min)
    blitRotateCenter(screen, left_hand, (270,100), ang_sec)
   

    screen.blit(text, text_rect)


    pygame.display.flip()
    pygame.display.update()
    clock.tick(60)






