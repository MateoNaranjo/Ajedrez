import pygame


class Tablero:
    def __init__(self):
        self.ancho=800
        self.alto=800
        self.pantalla=pygame.display.set_mode((self.ancho, self.alto))
        pygame.display.set_caption("Tablero de Ajedrez")
        self.tamano_casilla=self.ancho // 8

    def draw_tablero(self):
        for fila in range (8):
            for columna in range(8):
                if (fila+columna)%2==0:
                    color=(255,255,255)
                else:
                    color=(0,0,0)
                pygame.draw.rect(self.pantalla, color, (columna*self.tamano_casilla, fila*self.tamano_casilla, self.tamano_casilla, self.tamano_casilla))

    def execute(self):
        ejecutar=True
        while ejecutar:
            for evento in pygame.event.get():
                if evento.type ==pygame.QUIT:
                    ejecutar=False

            pygame.display.flip()
        
        pygame.quit()


if __name__=="__main__":
    mi_tablero=Tablero()
    mi_tablero.draw_tablero()
    mi_tablero.execute()