import pygame
import random

def main():
    white = (255, 255, 255)

    pygame.init()
    positions = [(0, 0)]
    colors = [(0, 0, 0)]
    pressed_keys = pygame.key.get_pressed()


    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    quit()
        screen = pygame.display.set_mode((600, 400))
        pygame.display.set_caption("Paint")
        screen.fill(white)

        mouse_pos = pygame.mouse.get_pos()
        if mouse_pos != positions[len(positions)-1]:
            random_color = (random.randint(1, 255), random.randint(1, 255), random.randint(1, 255))
            positions.append(mouse_pos)
            colors.append(random_color)
        for actual_pos in positions:
            pygame.draw.circle(screen, colors[positions.index(actual_pos)], actual_pos, 20)
        pygame.display.update()


if __name__ == "__main__":
    main()