import arcade
arcade.open_window(1000, 800, "Drawing")
arcade.set_background_color(arcade.color.CAPRI)
arcade.start_render()
# Draw Grass
arcade.draw_lrtb_rectangle_filled(0, 999, 200, 0, arcade.csscolor.GREEN)

# --- Draw the House ---

# Base of house
arcade.draw_lrtb_rectangle_filled(500, 900, 500, 150, arcade.csscolor.RED)

# Draw Door
arcade.draw_arc_filled(700, 150, 90, 250, arcade.csscolor.BROWN, 0, 180)
arcade.draw_circle_filled(720, 200, 8, arcade.csscolor.BLACK)

# Bottom Left Window
arcade.draw_circle_filled(580, 280, 38, arcade.csscolor.WHITE)
arcade.draw_circle_filled(580, 280, 32, arcade.csscolor.CORNFLOWER_BLUE)
arcade.draw_lrtb_rectangle_filled(577, 583, 315, 245, arcade.csscolor.WHITE)
arcade.draw_lrtb_rectangle_filled(545, 615, 283, 277, arcade.csscolor.WHITE)

# Bottom Right Window
arcade.draw_circle_filled(820, 280, 38, arcade.csscolor.WHITE)
arcade.draw_circle_filled(820, 280, 32, arcade.csscolor.CORNFLOWER_BLUE)
arcade.draw_lrtb_rectangle_filled(817, 823, 315, 245, arcade.csscolor.WHITE)
arcade.draw_lrtb_rectangle_filled(785, 855, 283, 277, arcade.csscolor.WHITE)

# Top Left Window
arcade.draw_circle_filled(580, 420, 38, arcade.csscolor.WHITE)
arcade.draw_circle_filled(580, 420, 32, arcade.csscolor.CORNFLOWER_BLUE)
arcade.draw_lrtb_rectangle_filled(577, 583, 455, 385, arcade.csscolor.WHITE)
arcade.draw_lrtb_rectangle_filled(545, 615, 423, 417, arcade.csscolor.WHITE)

# Top Right Window
arcade.draw_circle_filled(820, 420, 38, arcade.csscolor.WHITE)
arcade.draw_circle_filled(820, 420, 30, arcade.csscolor.CORNFLOWER_BLUE)
arcade.draw_lrtb_rectangle_filled(817, 823, 455, 385, arcade.csscolor.WHITE)
arcade.draw_lrtb_rectangle_filled(785, 855, 423, 417, arcade.csscolor.WHITE)

# Roof
arcade.draw_triangle_filled(700, 680, 480, 500, 920, 500, arcade.color.ALLOY_ORANGE)

# --- Draw Trees ---

# Right Tree
arcade.draw_lrtb_rectangle_filled(300, 320, 250, 180, arcade.color.SIENNA)
arcade.draw_arc_filled(310, 250, 60, 200, arcade.color.DARK_GREEN, 0, 180)

# Middle Tree
arcade.draw_lrtb_rectangle_filled(200, 220, 250, 180, arcade.color.SIENNA)
arcade.draw_ellipse_filled(210, 315, 60, 150, arcade.color.DARK_GREEN)

# Left Tree
arcade.draw_lrtb_rectangle_filled(100, 120, 250, 180, arcade.color.SIENNA)
arcade.draw_circle_filled(110, 290, 50, arcade.color.DARK_GREEN)

# --- Draw the Sun ---

# Core of Sun
arcade.draw_circle_filled(170, 650, 100, arcade.color.YELLOW)

# Top Middle Ray
arcade.draw_line(280, 610, 390, 560, arcade.color.YELLOW, 3)

# Bottom Middle Ray
arcade.draw_line(245, 570, 325, 490, arcade.color.YELLOW, 3)

# Very Bottom Ray
arcade.draw_line(190, 540, 245, 450, arcade.color.YELLOW, 3)

# Very Top Ray
arcade.draw_line(290, 660, 420, 640, arcade.color.YELLOW, 3)
arcade.finish_render()
arcade.run()
