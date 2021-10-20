import pygame
import random


def main():

    WIDTH = 600
    HEIGHT = 400

    WHITE = (255, 255, 255)

    loop = 0

    starting_point = (WIDTH // 2, HEIGHT // 2)
    positions = [starting_point]

    separation = int(input('Type the separation between dots(int):'))
    frequency = int(input('Select the frequency of lines(10-many, 100-few): '))

    # The inclination of the initial line
    inclination = random.randint(separation*(-1), separation)
    available_x = inclination
    available_y = separation-inclination

    pygame.init()

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Paint")
    screen.fill(WHITE)

    print(available_x, available_y)

    while True:

        loop += 1

        # To close the game when ESC is pressed
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    quit()

        # To maintain the trail of previous dots
        last_pos = positions[len(positions) - 1]

        if loop % frequency != 0:
            next_position = (last_pos[0]+available_x, last_pos[1]+available_y)
            if next_position[0] < 0 or next_position[0] > WIDTH:
                available_x = available_x*(-1)
            elif next_position[1] < 0 or next_position[1] > HEIGHT:
                available_y = available_y*(-1)
            positions.append(next_position)
        else:
            inclination = random.randint(separation * (-1), separation)
            available_x = inclination
            available_y = separation - inclination

        for actual_pos in positions:
            pygame.draw.circle(screen, (0, 0, 0), actual_pos, 1)

        pygame.display.update()


if __name__ == "__main__":
    main()
