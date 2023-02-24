import pygame
import time
import random


def main():
    draw()
    

def draw():
    pygame.init()
    white = [255, 255, 255]
    
    size = [900, 600]
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("Ghost game")

    done = False
    score = 0

    while done == False:
        screen.fill(white)

        rand_door = random.randint(1,3)
        door_surf = pygame.image.load('doors'+str(rand_door)+'.jpg')
        door_rect = door_surf.get_rect(bottomright=(900, 500))
        screen.blit(door_surf, door_rect)

        draw_text(screen, 'Which door do you open? Opened doors: ' + str(score))

        pygame.display.update()
        ghost_door = random.randint(1, 3)

        buttons = set()

        buttons.add(pygame.K_1)
        buttons.add(pygame.K_2)
        buttons.add(pygame.K_3)


        ev = False

        while ev == False:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    ev = True
                    done = True
                    
                elif event.type == pygame.KEYDOWN:
                    if event.key in buttons:
                        ev = True
                        
                    if event.key == pygame.K_1 and ghost_door == 1 or \
                       event.key == pygame.K_2 and ghost_door == 2 or \
                       event.key == pygame.K_3 and ghost_door == 3:
                        screen.fill(white)
                        draw_text(screen, '† GHOST. Game Over †')
                        ghost_surf = pygame.image.load('ghost1.jpg')
                        ghost_rect = ghost_surf.get_rect(bottomright=(900, 600))
                        screen.blit(ghost_surf, ghost_rect)
                        pygame.display.update()
                        done = True
                        time.sleep(3)
                else:
                    score += 1
                    
def draw_text(screen, text):
    font = pygame.font.Font(None, 30)
    black = [0, 0, 0]
    text = font.render(text, True, black)
    screen.blit(text, [30, 50])

        
        
if __name__ == '__main__':
    main()
    



