import arcade
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


def draw_grass():
    """ Draw the ground """
    arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT / 3, 0, arcade.color.OLIVE_DRAB)

def arbre (px,py): 
    arcade.draw_lrtb_rectangle_filled(px, 30+px, 120+py, py, arcade.csscolor.SIENNA)
    arcade.draw_circle_filled(15+px, 140+py, 60, arcade.csscolor.GREEN)

def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing with Functions")
    arcade.set_background_color(arcade.color.BLUE)
    arcade.start_render()

    draw_grass()
    arbre(random.randrange(600),random.randrange(200))
    arbre(random.randrange(600),random.randrange(200))
    arbre(random.randrange(600),random.randrange(200))
    arbre(random.randrange(600),random.randrange(200))
    arbre(random.randrange(600),random.randrange(200))
    arbre(random.randrange(600),random.randrange(200))

    # Finish and run
    arcade.finish_render()
    arcade.run()


# Call the main function to get the program started.
main()