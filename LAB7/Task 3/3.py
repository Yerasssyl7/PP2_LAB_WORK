import pygame

pygame.init()

screen = pygame.display.set_mode((800,400))
white = (255, 255, 255)
red = (255, 0, 0)

pygame.display.set_caption("Task-3")
clock = pygame.time.Clock()
font = pygame.font.Font(r"C:\Users\Ерасыл\OneDrive\Desktop\task1\font\Pixeltype.ttf", 50)



x = 400
y = 200





done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
      

        
    key = pygame.key.get_pressed()
            
    if key[pygame.K_UP] and y >= 40:
        y -= 20
    if key[pygame.K_DOWN] and y <= 360:
        y += 20
    if key[pygame.K_RIGHT] and x <= 760:
        x += 20
    if key[pygame.K_LEFT] and x >= 40:
        x -= 20

    screen.fill(white)
    circle = pygame.draw.circle(screen, red,  [x, y], 25, 0)
    

    
    
    clock.tick(60)
    pygame.display.flip()


