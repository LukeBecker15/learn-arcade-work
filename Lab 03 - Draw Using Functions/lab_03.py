# Import the "arcade" Library
import arcade


def draw_grass():
    """Draw the Grass"""
    arcade.draw_lrtb_rectangle_filled(0, 999, 200, 0, arcade.csscolor.GREEN)

def draw_base_house():
    """Draw Base of House"""
    arcade.draw_lrtb_rectangle_filled(500, 900, 500, 150, arcade.csscolor.RED)
    arcade.draw_triangle_filled(700, 680, 480, 500, 920, 500, arcade.color.ALLOY_ORANGE)

def draw_door():
    """Draw the Door"""
    arcade.draw_arc_filled(700, 150, 90, 250, arcade.csscolor.BROWN, 0, 180)
    arcade.draw_circle_filled(720, 200, 8, arcade.csscolor.BLACK)

def draw_window(x, y):
    """Draw a Window"""

    # Circle Window
    arcade.draw_circle_filled(580 + x, 280 + y, 38, arcade.csscolor.WHITE)
    arcade.draw_circle_filled(580 + x, 280 + y, 32, arcade.csscolor.CORNFLOWER_BLUE)

    # Cross on Window
    arcade.draw_lrtb_rectangle_filled(577 + x, 583 + x, 315 + y, 245 + y, arcade.csscolor.WHITE)
    arcade.draw_lrtb_rectangle_filled(545 + x, 615 + x, 283 + y, 277 + y, arcade.csscolor.WHITE)

def draw_tree(x, y):
    """Draw a Tree"""
    # Tree Trunk
    arcade.draw_lrtb_rectangle_filled(100 + x, 120 + x, 250 + y, 180 + y, arcade.color.SIENNA)

    # Tree Leaves
    arcade.draw_ellipse_filled(110 + x, 315 + y, 60, 150, arcade.color.DARK_GREEN)

def draw_main_sun():
    """Draw Sun Core"""
    # Circle of Sun
    arcade.draw_circle_filled(170, 650, 100, arcade.color.YELLOW)

def draw_sun_rays():
    """Draw Rays of Sun"""
    # Rays of Sun
    arcade.draw_line(290, 660, 420, 640, arcade.color.YELLOW, 3)
    arcade.draw_line(190, 540, 245, 450, arcade.color.YELLOW, 3)
    arcade.draw_line(245, 570, 325, 490, arcade.color.YELLOW, 3)
    arcade.draw_line(280, 610, 390, 560, arcade.color.YELLOW, 3)

def main():
    arcade.open_window(1000, 800, "Drawing")
    arcade.set_background_color(arcade.color.CAPRI)
    arcade.start_render()

    draw_grass()
    draw_base_house()
    draw_door()
    draw_window(0, 0)
    draw_window(240, 0)
    draw_window(0, 140)
    draw_window(240, 140)
    draw_tree(0, 0)
    draw_tree(100, 0)
    draw_tree(200, 0)
    draw_main_sun()
    draw_sun_rays()

    arcade.finish_render()
    arcade.run()

main()

