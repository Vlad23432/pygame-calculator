import pygame
import button
pygame.init()
bounds = (360, 640)
# buttonrovno = button.button('#000000', '#696969', '=', 90, 90, bounds, bounds[0] - 360, bounds[1] - 90 )
screen = pygame.display.set_mode(bounds)

pygame.display.set_caption('Calculator')
clock = pygame.time.Clock()
buttons = ['0', ',', '=', '1', '2', '3', '+','4','5','6','-','7','8','9','x','AC','+/-','%','/']
buttonsObjects = []
i = 1
height = 90
width = 360
for btn in buttons:
    if i % 4 == 0:
        height += 90
        width = 360
    buttonsObjects.append(button.button('#000000', '#696969', btn, 180 if i == 1 else 90, 90, bounds, bounds[0] - width, bounds[1] - height))
    width -= 180 if i == 1 else 90
    i += 1
run = True
while run:
    clock.tick(60)
    isClicked = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    screen.fill('#ffffff')

    for btn in buttonsObjects:
        btn.draw(screen)

    pygame.display.flip()

pygame.quit()
