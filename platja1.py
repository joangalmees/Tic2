import arcade
import math

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

def fondo ():
    arcade.draw_lrtb_rectangle_filled(0, 599, 350, 200, arcade.csscolor.DODGER_BLUE)
    arcade.draw_lrtb_rectangle_filled(0, 599, 200, 0, arcade.csscolor.DARK_KHAKI)

def arbre (px,py): 
    arcade.draw_lrtb_rectangle_filled(px, 30+px, 120+py, py, arcade.csscolor.SIENNA)
    arcade.draw_circle_filled(15+px, 140+py, 60, arcade.csscolor.DARK_GREEN)

def illa (px,py):
    arcade.draw_ellipse_filled(0+px, 50+py, 200, 50, arcade.csscolor.SADDLE_BROWN)
    arcade.draw_ellipse_filled(0+px, 0+py, 50, 20, arcade.csscolor.SADDLE_BROWN)

def lluna (px,py):
    arcade.draw_circle_filled(0+px, 0+py, 30, arcade.csscolor.WHITE)

def lluna2 (px,py):
    arcade.draw_circle_filled(0+px, 0+py, 30, arcade.csscolor.MIDNIGHT_BLUE)

def tovallola (px,py):
    arcade.draw_lrtb_rectangle_filled(0+px, 50+px, 15+py, 0+py, arcade.csscolor.SPRING_GREEN)
    arcade.draw_lrtb_rectangle_filled(0+px, 50+px, 30+py, 15+py, arcade.csscolor.WHITE)
    arcade.draw_lrtb_rectangle_filled(0+px, 50+px, 45+py, 30+py, arcade.csscolor.SPRING_GREEN)
    arcade.draw_lrtb_rectangle_filled(0+px, 50+px, 60+py, 45+py, arcade.csscolor.WHITE)
    arcade.draw_lrtb_rectangle_filled(0+px, 50+px, 75+py, 60+py, arcade.csscolor.SPRING_GREEN)

def faro (px,py):
    arcade.draw_lrtb_rectangle_filled(0+px, 60+px, 20+py, 0+py, arcade.csscolor.RED)
    arcade.draw_lrtb_rectangle_filled(0+px, 60+px, 40+py, 20+py, arcade.csscolor.WHITE)
    arcade.draw_lrtb_rectangle_filled(0+px, 60+px, 60+py, 40+py, arcade.csscolor.RED)
    arcade.draw_lrtb_rectangle_filled(0+px, 60+px, 80+py, 60+py, arcade.csscolor.WHITE)
    arcade.draw_lrtb_rectangle_filled(0+px, 60+px, 100+py, 80+py, arcade.csscolor.RED)
    arcade.draw_lrtb_rectangle_filled(10+px, 50+px, 110+py, 100+py, arcade.csscolor.WHITE)
    arcade.draw_lrtb_rectangle_filled(0+px, 60+px, 150+py, 110+py, arcade.csscolor.RED)
    arcade.draw_lrtb_rectangle_filled(10+px, 30+px, 140+py, 120+py, arcade.csscolor.YELLOW)

class Ball:
    """ This class manages a ball bouncing on the screen. """

    def __init__(self, position_x, position_y, change_x, change_y, radius, color):
        """ Constructor. """

        # Take the parameters of the init function above, and create instance variables out of them.
        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        self.radius = radius
        self.color = color

    def draw(self):
        """ Draw the balls with the instance variables we have. """
        arcade.draw_circle_filled(self.position_x, self.position_y, self.radius, self.color)

    def update(self):
        """ Code to control the ball's movement. """

        # Move the ball
        self.position_y += self.change_y
        self.position_x += self.change_x

        # See if the ball hit the edge of the screen. If so, change direction
        if self.position_x < self.radius:
            self.change_x *= -1

        if self.position_x > SCREEN_WIDTH - self.radius:
            self.change_x *= -1

        if self.position_y < self.radius:
            self.change_y *= -1

        if self.position_y > SCREEN_HEIGHT - self.radius:
            self.change_y *= -1

def colisio(a,b):
    distancia = math.sqrt(math.pow((a.position_x - b.position_x),2) + math.pow((a.position_y - b.position_y),2))
    print(distancia)
    if distancia <= (a.radius):
        return True
    else:
        return False

class Gel (Ball):
    def update(self):
        """ Code to control the ball's movement. """

        # Move the ball
        self.position_y += self.change_y
        self.position_x += self.change_x

        # See if the ball hit the edge of the screen. If so, change direction
        if self.position_x < self.radius:
            self.change_x *= -1

        if self.position_x > SCREEN_WIDTH - self.radius:
            self.change_x *= -1
        
        
        
        if self.position_y < 0:
            self.position_y = SCREEN_HEIGHT

class Meteorit (Ball):
    def update(self):
        """ Code to control the ball's movement. """

        # Move the ball
        self.position_y += self.change_y
        self.position_x += self.change_x

        # See if the ball hit the edge of the screen. If so, change direction
        if self.position_x < self.radius:
            self.change_x *= -1

        if self.position_x > SCREEN_WIDTH - self.radius:
            self.change_x *= -1
        
        
        
        if self.position_y < 0:
            self.position_y = SCREEN_HEIGHT      

class MyGame(arcade.Window):

    def __init__(self, width, height, title):

        # Call the parent class's init function
        super().__init__(width, height, title)

        # Set the background color
        arcade.set_background_color(arcade.color.MIDNIGHT_BLUE)
   

                # Attributes to store where our ball is
        self.ball = Gel(20, 50, 0, -4, 3, arcade.color.CHARTREUSE)
        self.ball2 = Gel(40, 50, 0, -5, 3, arcade.color.CHARTREUSE)
        self.ball3 = Gel(60, 50, 0, -4.5, 3, arcade.color.CHARTREUSE)
        self.ball4 = Gel(80, 50, 0, -4.6, 3, arcade.color.CHARTREUSE)
        self.ball5 = Gel(100, 50, 0, -5.5, 3, arcade.color.CHARTREUSE)
        self.ball6 = Gel(120, 50, 0, -6, 3, arcade.color.CHARTREUSE)
        self.ball7 = Gel(140, 50, 0, -5.3,3, arcade.color.CHARTREUSE)
        self.ball8 = Gel(160, 50, 0, -7, 3, arcade.color.CHARTREUSE)
        self.ball9 = Gel(180, 50, 0, -5.2, 3, arcade.color.CHARTREUSE)
        self.ball10 = Gel(200, 50, 0, -4.2, 3, arcade.color.CHARTREUSE)
        self.ball11 = Gel(220, 50, 0, -2.6, 3, arcade.color.CHARTREUSE)
        self.ball12 = Gel(240, 50, 0, -6, 3, arcade.color.CHARTREUSE)
        self.ball13 = Gel(260, 50, 0, -5, 3, arcade.color.CHARTREUSE)
        self.ball14 = Gel(280, 50, 0, -4, 3, arcade.color.CHARTREUSE)
        self.ball15 = Gel(300, 50, 0, -5.2, 3, arcade.color.CHARTREUSE)
        self.ball16 = Gel(320, 50, 0, -6.2, 3, arcade.color.CHARTREUSE)
        self.ball17 = Gel(340, 50, 0, -4.5, 3, arcade.color.CHARTREUSE)
        self.ball18 = Gel(360, 50, 0, -3, 3, arcade.color.CHARTREUSE)
        self.ball19 = Gel(380, 50, 0, -7, 3, arcade.color.CHARTREUSE)
        self.ball20 = Gel(400, 50, 0, -3.8, 3, arcade.color.CHARTREUSE)
        self.ball21 = Gel(420, 50, 0, -4.1, 3, arcade.color.CHARTREUSE)
        self.ball22 = Gel(440, 50, 0, -5, 3, arcade.color.CHARTREUSE)
        self.ball23 = Gel(460, 50, 0, -5.7, 3, arcade.color.CHARTREUSE)
        self.ball24 = Gel(480, 50, 0, -2, 3, arcade.color.CHARTREUSE)
        self.ball25 = Gel(500, 50, 0, -7, 3, arcade.color.CHARTREUSE)
        self.ball26 = Gel(520, 50, 0, -3, 3, arcade.color.CHARTREUSE)
        self.ball27 = Gel(540, 50, 0, -6, 3, arcade.color.CHARTREUSE)
        self.ball28 = Gel(560, 50, 0, -4.7, 3, arcade.color.CHARTREUSE)
        self.ball29 = Gel(580, 50, 0, -5.4, 3, arcade.color.CHARTREUSE)

    def on_draw(self):
        """ Called whenever we need to draw the window. """
        arcade.start_render()
        fondo()
        arbre(100,200)
        illa(550,250)
        lluna(300,550)
        lluna2(275,550)
        tovallola(100,50)
        tovallola(250,50)
        tovallola(400,50)
        faro(500,300)
        self.ball.draw()
        self.ball2.draw()
        self.ball3.draw()
        self.ball4.draw()
        self.ball5.draw()
        self.ball6.draw()
        self.ball7.draw()
        self.ball8.draw()
        self.ball9.draw()
        self.ball10.draw()
        self.ball11.draw()
        self.ball12.draw()
        self.ball13.draw()
        self.ball14.draw()
        self.ball15.draw()
        self.ball16.draw()
        self.ball17.draw()
        self.ball18.draw()
        self.ball19.draw()
        self.ball20.draw()        
        self.ball21.draw()        
        self.ball22.draw()        
        self.ball23.draw()        
        self.ball24.draw()        
        self.ball25.draw()        
        self.ball26.draw()        
        self.ball27.draw()        
        self.ball28.draw()        
        self.ball29.draw()        

    def update(self, delta_time):
        """ Called to update our objects. Happens approximately 60 times per second."""
        colisio(self.ball,self.ball2)
        self.ball.update()
        self.ball2.update()
        self.ball3.update()
        self.ball4.update()
        self.ball5.update()
        self.ball6.update()
        self.ball7.update()
        self.ball8.update()
        self.ball9.update()
        self.ball10.update()
        self.ball11.update()
        self.ball12.update()
        self.ball13.update()
        self.ball14.update()
        self.ball15.update()
        self.ball16.update()
        self.ball17.update()
        self.ball18.update()
        self.ball19.update()
        self.ball20.update()
        self.ball21.update()
        self.ball22.update()
        self.ball23.update()
        self.ball24.update()
        self.ball25.update()
        self.ball26.update()
        self.ball27.update()
        self.ball28.update()
        self.ball29.update()

def main():
    window = MyGame(600, 600, "Drawing Example")

    arcade.run()


main()