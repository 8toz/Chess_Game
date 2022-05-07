import pygame
import settings


def pinta_casillas(screen):
    control_color = -1
    for fila in range(8):
        control_color *= -1  #  control_color = control_color * -1
        for columna in range(8):
            if control_color == 1:
                casilla = pygame.Rect(
                    fila * (settings.WIDTH // 8),
                    columna * (settings.HEIGHT // 8),
                    settings.WIDTH // 8,
                    settings.HEIGHT // 8,
                )
                pygame.draw.rect(screen, (settings.BLACK_SQUARE_COLOR), casilla)

                control_color *= -1
            elif control_color == -1:
                casilla = pygame.Rect(
                    fila * (settings.WIDTH // 8),
                    columna * (settings.HEIGHT // 8),
                    settings.WIDTH // 8,
                    settings.HEIGHT // 8,
                )
                pygame.draw.rect(screen, (settings.WHITE_SQUARE_COLOR), casilla)
                control_color *= -1


def crea_pieza(screen, color, tipo, posicion):
    pieza = pygame.image.load("./static/Piezas/" + tipo + "_" + color + ".png")
    pieza = pygame.transform.scale(pieza, (settings.WIDTH // 8, settings.HEIGHT // 8))
    screen.blit(pieza, posicion)


def coloca_piezas(screen):
    colores = ["negro", "blanco"]
    piezas = ["rey", "reina", "alfil", "caballo", "torre", "peon"]
    for color in colores:
        for tipo in piezas:
            if color == "blanco":
                if tipo == "rey":
                    crea_pieza(screen, color, tipo, (400, 700))
                elif tipo == "reina":
                    crea_pieza(screen, color, tipo, (300, 700))
                elif tipo == "alfil":
                    crea_pieza(screen, color, tipo, (500, 700))
                    crea_pieza(screen, color, tipo, (200, 700))
                elif tipo == "caballo":
                    crea_pieza(screen, color, tipo, (600, 700))
                    crea_pieza(screen, color, tipo, (100, 700))
                elif tipo == "torre":
                    crea_pieza(screen, color, tipo, (700, 700))
                    crea_pieza(screen, color, tipo, (0, 700))
                elif tipo == "peon":
                    for peon in range(8):
                        crea_pieza(
                            screen, color, tipo, (peon * (settings.WIDTH // 8), 600)
                        )

            else:
                if tipo == "rey":
                    crea_pieza(screen, color, tipo, (400, 0))
                elif tipo == "reina":
                    crea_pieza(screen, color, tipo, (300, 0))
                elif tipo == "alfil":
                    crea_pieza(screen, color, tipo, (500, 0))
                    crea_pieza(screen, color, tipo, (200, 0))
                elif tipo == "caballo":
                    crea_pieza(screen, color, tipo, (600, 0))
                    crea_pieza(screen, color, tipo, (100, 0))
                elif tipo == "torre":
                    crea_pieza(screen, color, tipo, (700, 0))
                    crea_pieza(screen, color, tipo, (0, 0))
                elif tipo == "peon":
                    for peon in range(8):
                        crea_pieza(
                            screen, color, tipo, (peon * (settings.WIDTH // 8), 100)
                        )

    return None