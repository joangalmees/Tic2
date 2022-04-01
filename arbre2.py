import arcade

def arbre (px,py): 
    arcade.draw_lrtb_rectangle_filled(px, 30+px, 120+py, py, arcade.csscolor.SIENNA)
    arcade.draw_circle_filled(15+px, 140+py, 60, arcade.csscolor.DARK_GREEN)

def arbre2 (px,py): 
    arcade.draw_lrtb_rectangle_filled(px, 30+px, 120+py, py, arcade.csscolor.SIENNA)
    arcade.draw_circle_filled(15+px, 140+py, 60, arcade.csscolor.DARK_GREEN)

def nuvol (px,py):
    arcade.draw_circle_filled(140, 500, 30, arcade.csscolor.ALICE_BLUE)
    arcade.draw_circle_filled(100, 500, 30, arcade.csscolor.ALICE_BLUE)
    arcade.draw_circle_filled(60, 500, 30, arcade.csscolor.ALICE_BLUE)

def nuvol2 (px,py):
    arcade.draw_circle_filled(540, 500, 30, arcade.csscolor.ALICE_BLUE)
    arcade.draw_circle_filled(500, 500, 30, arcade.csscolor.ALICE_BLUE)
    arcade.draw_circle_filled(460, 500, 30, arcade.csscolor.ALICE_BLUE)

def sol (px,py):
    arcade.draw_circle_filled(300, 550, 30, arcade.csscolor.YELLOW)

arcade.open_window(600, 600, "Drawing Example")

# Set the background color
arcade.set_background_color(arcade.csscolor.SKY_BLUE)

# Get ready to draw
arcade.start_render()

#Rectangles: 
arcade.draw_lrtb_rectangle_filled(0, 599, 300, 0, arcade.csscolor.OLIVE_DRAB)

arbre(100,200)
arbre2(400,200)
nuvol(100,400)
nuvol2(400,400)
sol(300,500)

# Finish drawing
arcade.finish_render()

# Keep the window up until someone closes it.
arcade.run()