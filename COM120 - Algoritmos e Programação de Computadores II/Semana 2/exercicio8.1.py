class Point:
    def setx(self, coordx):
        self.x = coordx
    def sety(self, coordy):
        self.y = coordy
    def get(self):
        return (self.x, self.y)
    def move(self, dx, dy):
        self.x += dx
        self.y += dy
#Exercicio 8.1 Acrescente o método getx() à classe Ponto; esse método não aceita entrada e retorna a coordenada x do objeto Ponto que chama o método.
    def getx(self):
        return (self.x)