import pygame
import random



pygame.init()
pygame.display.set_caption("Task 2")

screen = pygame.display.set_mode((800,400))
clock = pygame.time.Clock()
font = pygame.font.Font(r"C:\Users\Ерасыл\OneDrive\Desktop\task1\font\Pixeltype.ttf", 50)
DEFAULT_IMAGE_SIZE = (800, 400)
bg = pygame.image.load(r"C:\Users\Ерасыл\OneDrive\Desktop\task2\pics\bg2.webp").convert()
bg = pygame.transform.scale(bg , DEFAULT_IMAGE_SIZE )

musics = [
    r"C:\Users\Ерасыл\OneDrive\Desktop\task2\music\alone.mp3",
    r"C:\Users\Ерасыл\OneDrive\Desktop\task2\music\betsy.mp3",
    r"C:\Users\Ерасыл\OneDrive\Desktop\task2\music\gardens.mp3",
    r"C:\Users\Ерасыл\OneDrive\Desktop\task2\music\kugelsicher.mp3",
    r"C:\Users\Ерасыл\OneDrive\Desktop\task2\music\sigmaboy.mp3"
]
current_track = 0
pygame.mixer.music.load(musics[current_track])


def play_pause():
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.pause()
    else:
        pygame.mixer.music.unpause()
        pygame.mixer.music.play()

def next_tr():
    global current_track
    current_track = (current_track + 1) % len(musics)
   
    pygame.mixer.music.load(musics[current_track])
    pygame.mixer.music.play()

def prev_tr():
    global current_track
    current_track = (current_track - 1) % len(musics)
    pygame.mixer.music.load(musics[current_track])
    pygame.mixer.music.play()








play_but = pygame.image.load(r"C:\Users\Ерасыл\OneDrive\Desktop\task2\pics\play.png").convert_alpha()
play_but = pygame.transform.scale(play_but, (100,100))
play_rect = play_but.get_rect(center = (400,300))


stop_but = pygame.image.load(r"C:\Users\Ерасыл\OneDrive\Desktop\task2\pics\pause.png").convert_alpha()
stop_but = pygame.transform.scale(stop_but,(100,100))
stop_rect = stop_but.get_rect(center = (400, 300))



next_but = pygame.image.load(r"C:\Users\Ерасыл\OneDrive\Desktop\task2\pics\next.png").convert_alpha()
next_but = pygame.transform.scale(next_but, (100,100))
next_rect = next_but.get_rect(center = (530,300))



prev_but = pygame.image.load(r"C:\Users\Ерасыл\OneDrive\Desktop\task2\pics\previous.png").convert_alpha()
prev_but = pygame.transform.scale(prev_but, (100,100))
prev_rect = prev_but.get_rect(center = (250, 300))



done = False



while not done:

    screen.blit(bg, (0,0))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.KEYDOWN:
            flag = True
            if event.key == pygame.K_RIGHT :
                

                next_tr()
            if event.key == pygame.K_LEFT:
                prev_tr()
            if event.key == pygame.K_SPACE:
                play_pause()
            




    if pygame.mixer.music.get_busy():
        screen.blit(stop_but, stop_rect)  
    else:
        screen.blit(play_but, play_rect) 


   
    text = font.render((musics[current_track]), True, 'Black')
    screen.blit(text, (100, 100))
    screen.blit(next_but, next_rect)
    screen.blit(prev_but, prev_rect)

    
    
    
    




   
       
                
            

      
    

    



    pygame.display.update()
    clock.tick(0)

        





