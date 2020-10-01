""" Lab 7 - User Control """

import arcade
# --- Constants ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
MOVEMENT_SPEED = 5
def draw_hoop(x, y):
    arcade.draw_rectangle_filled(50, 50, 200, 130, arcade.color.WHITE)
    arcade.draw_rectangle_filled(50, 50, 76, 12, arcade.color.GIANTS_ORANGE)
    arcade.draw_rectangle_filled(50, 50, 80, 2, arcade.color.BLACK)
    arcade.draw_rectangle_filled(50, 50, 2, 50, arcade.color.BLACK)
    arcade.draw_rectangle_filled(50, 50, 2, 50, arcade.color.BLACK)
    arcade.draw_rectangle_filled(50, 50, 80, 2, arcade.color.BLACK)

def draw_ball(x, y):
    arcade.draw_circle_filled(50, 50, 20, arcade.color.ORANGE)
    arcade.draw_text("Spalding", 45, 55, arcade.color.BLACK, 24)

class Basket:

    def __init__(self, position_x, position_y, change_x, change_y):
        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        self.upper_bound = 0
        self.lower_bound = 0



    def draw(self):
        draw_hoop(self.position_x, self.position_y,)



class Basketball:
    def __init__(self, position_x2, position_y2, change_x2, change_y2, radius):
        self.position_x2 = position_x2
        self.position_y2 = position_y2
        self.change_x2 = change_x2
        self.change_y2 = change_y2
        self.radius = radius



    def drawing(self):
        draw_ball(self.position_x2, self.position_y2)

    def drawing_2(self):
        arcade.draw_text(self.position_x2, self.position_y2)

    def update(self):
        if self.position_x2 < self.radius:
            self.position_x2 = self.radius

        if self.position_x2 > SCREEN_WIDTH - self.radius:
            self.position_x2 = SCREEN_WIDTH - self.radius

        if self.position_y2 < self.radius:
            self.position_y2 = self.radius

        if self.position_y2 > SCREEN_HEIGHT - self.radius:
            self.position_y2 = SCREEN_HEIGHT - self.radius


class MyGame(arcade.Window):
    """ Our Custom Window Class"""
    def __init__(self):



        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 7 - User Control")
        arcade.set_background_color(arcade.color.CAPRI)

        self.set_mouse_visible(False)

        self.backboard = Basket(50, 50, 0, 0)
        self.rim = Basket(50, 50, 0, 0)
        self.bottom_line = Basket(50, 50, 0, 0)
        self.right_line = Basket(50, 50, 0, 0)
        self.left_line = Basket(50, 50, 0, 0)
        self.top_line = Basket(50, 50, 0, 0)

        self.ball = Basketball(50, 50, 0, 0, 20)
        self.text = Basketball("Spalding", 50, 60, 24, arcade.color.BLACK)

    def on_draw(self):
        arcade.start_render()
        self.backboard.draw()
        self.rim.draw()
        self.bottom_line.draw()
        self.right_line.draw()
        self.left_line.draw()
        self.top_line.draw()
        self.ball.drawing()

    def update(self, delta_time):
        self.ball.update()

        def on_key_press(self, key, modifiers):
            """ Called whenever the user presses a key. """
            if key == arcade.key.LEFT:
                self.ball.change_x2 = -MOVEMENT_SPEED
            elif key == arcade.key.RIGHT:
                self.ball.change_x2 = MOVEMENT_SPEED
            elif key == arcade.key.UP:
                self.ball.change_y2 = MOVEMENT_SPEED
            elif key == arcade.key.DOWN:
                self.ball.change_y2 = -MOVEMENT_SPEED

        def on_key_release(self, key, modifiers):
            """ Called whenever a user releases a key. """
            if key == arcade.key.LEFT or key == arcade.key.RIGHT:
                self.ball.change_x2 = 0
            elif key == arcade.key.UP or key == arcade.key.DOWN:
                self.ball.change_y2 = 0

        def draw_grass():
            arcade.draw_lrtb_rectangle_filled(0, 800, 100, 0, arcade.color.AO)

        draw_grass()
        self.backboard.draw()
        self.rim.draw()
        self.bottom_line.draw()
        self.right_line.draw()
        self.left_line.draw()
        self.top_line.draw()
        self.ball.drawing()


    def on_mouse_motion(self, x, y, dx, dy):
        self.backboard.position_x = x
        self.backboard.position_y = y
        self.rim.position_x = x
        self.rim.position_y = y - 25
        self.bottom_line.position_x = x
        self.bottom_line.position_y = y - 20
        self.right_line.position_x = x + 40
        self.right_line.position_y = y + 5
        self.left_line.position_x = x - 40
        self.left_line.position_y = y + 5
        self.top_line.position_x = x
        self.top_line.position_y = y + 30

def main():
    window = MyGame()
    arcade.run()


main()