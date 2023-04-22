import pygame

pygame.init()


def draw_text(screen, text, size, x, y, color):
    font_name = pygame.font.match_font('arial')
    font = pygame.font.Font(font_name, size)
    text_image = font.render(text, True, color)
    text_rect = text_image.get_rect()
    text_rect.center = (x, y)
    screen.blit(text_image, text_rect)


bounds = (360, 640)
screen = pygame.display.set_mode(bounds)

pygame.display.set_caption('Calculator')
clock = pygame.time.Clock()

run = True
while run:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    screen.fill('#FFFFFF')

    mousePos = pygame.mouse.get_pos()

    color = '#000000'
    if 360 > mousePos[0] > 360 - 90 and 640 > mousePos[1] > 640 - 90:
        color = '#353535'
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
    else:
        pygame.mouse.set_cursor()
    pygame.draw.rect(screen, color, (360 - 90, 640 - 90, 90, 90))
    draw_text(screen, '=', 45, 360 - 45, 640 - 45, '#FFFFFF')

    pygame.draw.rect(screen, '#009515', (360 - 180, 640 - 90, 90, 90))

    pygame.display.flip()

pygame.quit()
