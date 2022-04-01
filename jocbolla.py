import arcade

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

def colissio(a, b):
    #de les posicions i el radi
    #retorna si hi ha posició
    a.radius
    b.radius
    if (a.position_x == b.position_x):
        print("x=x")
        return True
    else:
        return False
class Arbre:
    def __init__(self, px, py):
        self.px = px
        self.py = py
        self.color = arcade.csscolor.GREEN
    def draw(self):
        px = self.px
        py = self.py
        
        arcade.draw_lrtb_rectangle_filled(px, 30+px, 120+py, py, arcade.csscolor.SIENNA)
        arcade.draw_circle_filled(15+px, 140+py, 60, self.color)
    
    def canvia(self):
        self.color = arcade.csscolor.RED

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


class MyGame(arcade.Window):

    def __init__(self, width, height, title):

        # Call the parent class's init function
        super().__init__(width, height, title)

        # Set the background color
        arcade.set_background_color(arcade.color.ASH_GREY)

                # Attributes to store where our ball is
        self.ball = Ball(50, 50, 3, 3, 20, arcade.color.YELLOW)
        self.ball2 = Ball(50, 50, 6, 6, 20, arcade.color.RED)
        self.arbre = Arbre(300, 0)

    def on_draw(self):
        """ Called whenever we need to draw the window. """
        arcade.start_render()
        self.ball.draw()
        self.ball2.draw()
        self.arbre.draw()

    def update(self, delta_time):
        """ Called to update our objects. Happens approximately 60 times per second."""
        self.ball.update()
        self.ball2.update()
        colissio(self.ball,self.ball2)

def main():
    window = MyGame(640, 480, "Drawing Example")

    arcade.run()


main()