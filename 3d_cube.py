import pygame
import sys
import math
import numpy as np

pygame.init()
display = pygame.display
surface = display.set_mode((1000, 1000))
display.set_caption("3D Cube")

WHITE = (255, 255, 255)

points = (
    (100, 100, 100),
    (-100, 100, 100),
    (100, -100, 100),
    (100, 100, -100),
    (-100, 100, -100),
    (100, -100, -100),
    (-100, -100, -100),
    (-100, -100, 100),
)

rotation_points = np.array([[0], [0], [0]])

def rotate_lines(arr):
    pygame.draw.line(surface, WHITE, arr[0], arr[1], 1)
    pygame.draw.line(surface, WHITE, arr[0], arr[2], 1)
    pygame.draw.line(surface, WHITE, arr[0], arr[3], 1)
    pygame.draw.line(surface, WHITE, arr[1], arr[4], 1)
    pygame.draw.line(surface, WHITE, arr[1], arr[7], 1)
    pygame.draw.line(surface, WHITE, arr[2], arr[5], 1)
    pygame.draw.line(surface, WHITE, arr[2], arr[7], 1)
    pygame.draw.line(surface, WHITE, arr[3], arr[4], 1)
    pygame.draw.line(surface, WHITE, arr[4], arr[6], 1)
    pygame.draw.line(surface, WHITE, arr[5], arr[3], 1)
    pygame.draw.line(surface, WHITE, arr[5], arr[6], 1)
    pygame.draw.line(surface, WHITE, arr[6], arr[7], 1)
    pygame.display.update()


def Rx(theta):
    return np.matrix(
        [
            [1, 0, 0],
            [0, math.cos(theta), -math.sin(theta)],
            [0, math.sin(theta), math.cos(theta)],
        ]
    )


def Ry(theta):
    return np.matrix(
        [
            [math.cos(theta), 0, math.sin(theta)],
            [0, 1, 0],
            [-math.sin(theta), 0, math.cos(theta)],
        ]
    )


def Rz(theta):
    return np.matrix(
        [
            [math.cos(theta), -math.sin(theta), 0],
            [math.sin(theta), math.cos(theta), 0],
            [0, 0, 1],
        ]
    )


def main():
    run = True

    theta = math.pi

    clock = pygame.time.Clock()

    while run:
        clock.tick(60)

        keys = pygame.key.get_pressed()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False

        if keys[pygame.K_q]:
            run = False

        surface.fill((0, 0, 0))

        temp_points = []

        rotation = Rz(theta) * Ry(theta) * Rx(theta)

        for i in points:

            rotation_points = np.array([i])

            r = np.dot(rotation_points, rotation, out=None)

            arr = (np.asarray(r)).flatten()

            x, y, _ = arr

            temp_points.append((x + 500, y + 500))

        rotate_lines(temp_points)

        temp_points = []

        theta += 0.01

        display.flip()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
