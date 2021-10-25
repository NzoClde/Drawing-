import math, turtle, random

turtle.radians()
turtle.speed = 120

class FonctionDrawing:

    def __init__(self, interval, iteration, color, coo):
        self.interval = interval  # Intervall sur laquel dessiner les fonction
        self.iteration = iteration # Points de construction 
        self.color = color  # Couleur du crayon
        self.coo = coo # Coordonné de depart 
        self.fonction = self.makeRandomeFonction()
        self.drawFonction()
    
    def pythagore(self, a, b):
        """Calcule l'hypotenuse"""
        return math.sqrt(pow(a, 2) + pow(b, 2))

    def getAngle(self, a, b):
        """"Retourne l'angle de la tangante de b/a en radian"""
        assert(a != 0)
        return math.atan(b/a)

    def drawAccroissement(self, a, b):
        """Permet de dessiner la droite"""
        turtle.pendown()
        turtle.left(self.getAngle(a, b)) # On tourne d'un angle donné
        turtle.forward(self.pythagore(a, b)) # On avance de la longeur voulu 
        turtle.left(-self.getAngle(a, b)) # On revient à l'angle de depart 
        turtle.penup()

    def makeRandomeFonction(self):
        return lambda x: math.sin(x) + pow(x,2) + random.random() - 0.8
    
    def drawFonction(self):
        """Permet de recuperer tout les points de construction de la fonction"""
        turtle.penup()
        turtle.goto(self.coo[0], self.coo[1]) # La tortue va à ses coordonné
        turtle.pencolor(self.color)
        debutInt = self.interval[0] 
        while debutInt < self.interval[1]: # Tant que l'on n'as pas dessiner toute la fonction 
            debutInt += self.iteration # On itere 
            self.drawAccroissement(1, (self.fonction(debutInt) - self.fonction(debutInt - self.iteration))/self.iteration)
            # On calcule le taux de variation 

#turtle.pensize(4)
#turtle.right(math.pi/2)

#FonctionDrawing([-1, 1], 0.04, "brown", (0, 50))
#FonctionDrawing([-1, 1], 0.04, "blue", (0, 50))
#FonctionDrawing([-1, 1], 0.04, "red", (0, 50))




