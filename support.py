import pygame

def draw_tile(tile_pos, tilesize, color):

    screen = pygame.display.get_surface()

    rect = pygame.Rect(tile_pos[0] * tilesize, tile_pos[1] * tilesize, tilesize, tilesize)
    pygame.draw.rect(screen, color, rect)

def draw_text(text, color, pos):

    screen = pygame.display.get_surface()

    font = pygame.font.SysFont('Arial', 20)

    text_img = font.render(f'{text}', True, color).convert_alpha()
    text_rect = text_img.get_rect(center=pos)
    screen.blit(text_img, text_rect)