""" Lab 7 - User Control """

import arcade
# --- Constants ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
MOVEMENT_SPEED = 5
class Basket:

    def __init__(self, position_x, position_y, change_x, change_y, width, height, color,):
        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        self.width = width
        self.height = height
        self.color = color


    def draw(self):
        arcade.draw_rectangle_filled(self.position_x, self.position_y, self.width, self.height, self.color)



class Basketball:
    def __init__(self, position_x2, position_y2, change_x2, change_y2, radius, color):
        self.position_x2 = position_x2
        self.position_y2 = position_y2
        self.change_x2 = change_x2
        self.change_y2 = change_y2
        self.radius = radius
        self.color = color



    def drawing(self):
        arcade.draw_circle_filled(self.position_x2, self.position_y2, self.radius, self.color)

        super().__init__(self, text, start_x, start_y, color, font_size)
        self.text = text
        self.start_x = start_x
        self.start_y = start_y
        self.color = color
        self.font_size = font_size


    def drawing_2(self):
        arcade.draw_text(self.text, self.start_x, self.start_y, self.color, self.font_size)

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



        #  Call the parent class initializer


        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 7 - User Control")
        arcade.set_background_color(arcade.color.CAPRI)

        self.applause = arcade.load_sound("applause.wav")

        self.set_mouse_visible(False)

        self.backboard = Basket(50, 50, 0, 0, 200, 130, arcade.color.WHITE)
        self.rim = Basket(50, 50, 0, 0, 76, 12, arcade.color.GIANTS_ORANGE)
        self.bottom_line = Basket(50, 50, 0, 0, 80, 2, arcade.color.BLACK)
        self.right_line = Basket(50, 50, 0, 0, 2, 50, arcade.color.BLACK)
        self.left_line = Basket(50, 50, 0, 0, 2, 50, arcade.color.BLACK)
        self.top_line = Basket(50, 50, 0, 0, 80, 2, arcade.color.BLACK)

        self.ball = Basketball(50, 50, 0, 0, 20, arcade.color.ORANGE)
        self.text = Basketball("Spalding", 50, 60, arcade.color.BLACK, 24)

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

    def on_mouse_press(self):
        arcade.play_sound(self.applause)


def main():
    window = MyGame()
    arcade.run()


main()