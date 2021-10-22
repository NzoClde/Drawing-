import math, turtle

turtle.radians()

class FonctionDrawing:

    def __init__(self, fonction, interval, iteration, color, coo):
        self.fonction = fonction # Fonction a dessiner 
        self.interval = interval  # Intervall sur laquel dessiner la fonction
        self.iteration = iteration # Points de construction 
        self.color = color  # Couleur du crayon
        self.coo = coo # Coordonné de depart 
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

# exemple = FonctionDrawing(math.exp, [0, 3], 0.01, "blue", (0, 0))
