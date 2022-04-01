import arcade
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


def draw_grass():
    """ Draw the ground """
    arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT / 3, 0, arcade.color.AIR_SUPERIORITY_BLUE)

def arbre (px,py): 
    arcade.draw_lrtb_rectangle_filled(px, 30+px, 120+py, py, arcade.csscolor.SIENNA)
    arcade.draw_circle_filled(15+px, 140+py, 60, arcade.csscolor.WHITE)

def draw_snow_person(x, y):
    """ Draw a snow person """

    # Draw a point at x, y for reference
    arcade.draw_point(x, y, arcade.color.RED, 5)

    # Snow
    arcade.draw_circle_filled(x, 30 + y, 30, arcade.color.WHITE)
    arcade.draw_circle_filled(x, 70 + y, 25, arcade.color.WHITE)
    arcade.draw_circle_filled(x, 100 + y, 20, arcade.color.WHITE)

    # Eyes
    arcade.draw_circle_filled(x - 7.5, 105 + y, 2.5, arcade.color.BLACK)
    arcade.draw_circle_filled(x + 7.5, 105 + y, 2.5, arcade.color.BLACK)

    # Nose
    arcade.draw_circle_filled(x , 100 + y, 2.5, arcade.color.DARK_ORANGE)

def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing with Functions")
    arcade.set_background_color(arcade.color.DARK_BLUE)
    arcade.start_render()

    draw_grass()
    draw_snow_person(random.randrange(600),random.randrange(200))
    draw_snow_person(random.randrange(600),random.randrange(200))
    draw_snow_person(random.randrange(600),random.randrange(200))
    draw_snow_person(random.randrange(600),random.randrange(200))
    draw_snow_person(random.randrange(600),random.randrange(200))
    draw_snow_person(random.randrange(600),random.randrange(200))
    arbre(700,200)

    # Finish and run
    arcade.finish_render()
    arcade.run()


# Call the main function to get the program started.
main()