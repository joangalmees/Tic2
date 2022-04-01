import arcade

# Open up a window.
# From the "arcade" library, use a function called "open_window"
# Set the window title to "Drawing Example"
# Set the dimensions (width and height)
arcade.open_window(600, 600, "Drawing Example")

# Set the background color
arcade.set_background_color(arcade.csscolor.SKY_BLUE)

# Get ready to draw
arcade.start_render()

#Rectangles: 
arcade.draw_lrtb_rectangle_filled(0, 599, 300, 0, arcade.csscolor.GREEN)
arcade.draw_rectangle_filled(300, 320, 40, 200, arcade.csscolor.SIENNA)
#Cercles: 
arcade.draw_circle_filled(300, 370, 60, arcade.csscolor.DARK_GREEN)
arcade.draw_circle_filled(140, 500, 30, arcade.csscolor.ALICE_BLUE)
arcade.draw_circle_filled(100, 500, 30, arcade.csscolor.ALICE_BLUE)
arcade.draw_circle_filled(60, 500, 30, arcade.csscolor.ALICE_BLUE)
arcade.draw_circle_filled(540, 500, 30, arcade.csscolor.ALICE_BLUE)
arcade.draw_circle_filled(500, 500, 30, arcade.csscolor.ALICE_BLUE)
arcade.draw_circle_filled(460, 500, 30, arcade.csscolor.ALICE_BLUE)
arcade.draw_circle_filled(300, 550, 30, arcade.csscolor.YELLOW)
arcade.draw_circle_filled(300, 330, 10, arcade.csscolor.RED)
arcade.draw_circle_filled(330, 350, 10, arcade.csscolor.RED)
arcade.draw_circle_filled(270, 350, 10, arcade.csscolor.RED)
arcade.draw_circle_filled(320, 390, 10, arcade.csscolor.RED)
arcade.draw_circle_filled(280, 390, 10, arcade.csscolor.RED)

# Finish drawing
arcade.finish_render()

# Keep the window up until someone closes it.
arcade.run()
