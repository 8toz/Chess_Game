# import the pygame module, so you can use it
import pygame


WIDTH = 800
HEIGHT = 800

# define a main function
def main():

    # initialize the pygame module
    pygame.init()
    # load and set the logo
    logo = pygame.image.load(".\static\logo.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("minimal program")

    # create a surface on screen that has the size of 240 x 180
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    control_color = -1
    for fila in range(8):
        control_color *= -1  #  control_color = control_color * -1
        for columna in range(8):
            if control_color == 1:
                casilla = pygame.Rect(
                    fila * (WIDTH // 8),
                    columna * (HEIGHT // 8),
                    WIDTH // 8,
                    HEIGHT // 8,
                )
                pygame.draw.rect(screen, (255, 255, 255), casilla)

                control_color *= -1
            elif control_color == -1:
                casilla = pygame.Rect(
                    fila * (WIDTH // 8),
                    columna * (HEIGHT // 8),
                    WIDTH // 8,
                    HEIGHT // 8,
                )
                pygame.draw.rect(screen, (0, 0, 0), casilla)
                control_color *= -1

    pygame.display.flip()

    # define a variable to control the main loop
    running = True

    # main loop
    while running:
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False


# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__ == "__main__":
    # call the main function
    main()