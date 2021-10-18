import pygame
import random


def main():

    WIDTH = 600
    HEIGHT = 400

    WHITE = (255, 255, 255)

    starting_point = (WIDTH // 2, HEIGHT // 2)
    positions = [starting_point]

    separation = int(input('Type the separation between dots(int):'))

    pygame.init()

    while True:

        # To close the game when ESC is pressed
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    quit()

        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Paint")
        screen.fill(WHITE)

        rand_x = random.randint(separation*-1, separation)
        rand_y = random.randint(separation*-1, separation)

        # To maintain the trail of previous dots
        last_pos = positions[len(positions) - 1]
        next_position = (last_pos[0]+rand_x, last_pos[1]+rand_y)
        positions.append(next_position)

        for actual_pos in positions:
            pygame.draw.circle(screen, (0, 0, 0), actual_pos, 1)

        pygame.display.update()


if __name__ == "__main__":
    main()
