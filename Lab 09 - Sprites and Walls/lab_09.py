"""
Use sprites to scroll around a large screen.

Simple program to show basic sprite usage.

Artwork from http://kenney.nl

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.sprite_move_scrolling
"""


import arcade
import os

SPRITE_SCALING = 0.5

SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Sprite Move Lab"

# How many pixels to keep as a minimum margin between the character
# and the edge of the screen.
VIEWPORT_MARGIN = 20

MOVEMENT_SPEED = 10


class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height, title):
        """
        Initializer
        """
        super().__init__(width, height, title)

        # Set the working directory (where we expect to find files) to the same
        # directory this .py file is in. You can leave this out of your own
        # code, but it is needed to easily run the examples using "python -m"
        # as mentioned at the top of this program.
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)



        self.score = 0

        # Sprite lists
        self.player_list = None

        # Set up the player
        self.player_sprite = None

        self.coin_list = None
        self.wall_list = None


        self.physics_engine = None

        # Used in scrolling
        self.view_bottom = 0
        self.view_left = 0


    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()

        # Set up the player

        # Sandwich image from vecteezy.com
        self.player_sprite = arcade.Sprite("images2.png", 0.2)
        self.player_sprite.center_x = 64
        self.player_sprite.center_y = 270
        self.player_list.append(self.player_sprite)


        self.coin = arcade.Sprite("images3.png", .15)
        self.coin.center_x = 1350
        self.coin.center_y = 900
        self.coin_list.append(self.coin)

        self.coin = arcade.Sprite("images3.png", .15)
        self.coin.center_x = 333
        self.coin.center_y = 300
        self.coin_list.append(self.coin)

        self.coin = arcade.Sprite("images3.png", .15)
        self.coin.center_x = 653
        self.coin.center_y = 480
        self.coin_list.append(self.coin)

        self.coin = arcade.Sprite("images3.png", .15)
        self.coin.center_x = 1043
        self.coin.center_y = 480
        self.coin_list.append(self.coin)

        self.coin = arcade.Sprite("images3.png", .15)
        self.coin.center_x = 1680
        self.coin.center_y = -100
        self.coin_list.append(self.coin)

        self.coin = arcade.Sprite("images3.png", .15)
        self.coin.center_x = 50
        self.coin.center_y = 1100
        self.coin_list.append(self.coin)

        self.coin = arcade.Sprite("images3.png", .15)
        self.coin.center_x = 50
        self.coin.center_y = -80
        self.coin_list.append(self.coin)

        self.coin = arcade.Sprite("images3.png", .15)
        self.coin.center_x = 1680
        self.coin.center_y = 1100
        self.coin_list.append(self.coin)

        # -- Set up several columns of walls

        # Blue box image from teacherspayteachers.com
        for x in range(150, 800, 64):
                wall = arcade.Sprite("images.png", .39)
                wall.center_x = x
                wall.center_y = 960
                self.wall_list.append(wall)

        for x in range(915, 1615, 64):
                wall = arcade.Sprite("images.png", .39)
                wall.center_x = x
                wall.center_y = 960
                self.wall_list.append(wall)

        for x in range(150, 1542, 64):
            wall = arcade.Sprite("images.png", .39)
            wall.center_x = x
            wall.center_y = 0
            self.wall_list.append(wall)


        for x in range(270, 1422, 64):
            wall = arcade.Sprite("images.png", .39)
            wall.center_x = x
            wall.center_y = 120
            self.wall_list.append(wall)

        for x in range(270, 1422, 64):
            wall = arcade.Sprite("images.png", .39)
            wall.center_x = x
            wall.center_y = 832
            self.wall_list.append(wall)

        for x in range(-64, 1792, 64):
            wall = arcade.Sprite("images.png", .39)
            wall.center_x = x
            wall.center_y = 1200
            self.wall_list.append(wall)

        for x in range(-64, 1792, 64):
            wall = arcade.Sprite("images.png", .39)
            wall.center_x = x
            wall.center_y = -192
            self.wall_list.append(wall)

        for x in range(398, 1294, 64):
            wall = arcade.Sprite("images.png", .39)
            wall.center_x = x
            wall.center_y = 248
            self.wall_list.append(wall)

        for x in range(398, 1294, 64):
            wall = arcade.Sprite("images.png", .39)
            wall.center_x = x
            wall.center_y = 704
            self.wall_list.append(wall)

        for x in range(522, 1166, 64):
            wall = arcade.Sprite("images.png", .39)
            wall.center_x = x
            wall.center_y = 576
            self.wall_list.append(wall)

        for x in range(522, 842, 64):
            wall = arcade.Sprite("images.png", .39)
            wall.center_x = x
            wall.center_y = 376
            self.wall_list.append(wall)

        for x in range(906, 1166, 64):
            wall = arcade.Sprite("images.png", .39)
            wall.center_x = x
            wall.center_y = 376
            self.wall_list.append(wall)

        for y in range(-192, 1200, 64):
            wall = arcade.Sprite("images.png", .39)
            wall.center_x = -64
            wall.center_y = y
            self.wall_list.append(wall)

        for y in range(-192, 1200, 64):
            wall = arcade.Sprite("images.png", .39)
            wall.center_x = 1792
            wall.center_y = y
            self.wall_list.append(wall)

        for y in range(0, 960, 64):
            wall = arcade.Sprite("images.png", .39)
            wall.center_x = 150
            wall.center_y = y
            self.wall_list.append(wall)

        for y in range(0, 960, 64):
            wall = arcade.Sprite("images.png", .39)
            wall.center_x = 1556
            wall.center_y = y
            self.wall_list.append(wall)

        for y in range(120, 500, 64):
            wall = arcade.Sprite("images.png", .39)
            wall.center_x = 1408
            wall.center_y = y
            self.wall_list.append(wall)

        for y in range(576, 852, 64):
            wall = arcade.Sprite("images.png", .39)
            wall.center_x = 1408
            wall.center_y = y
            self.wall_list.append(wall)

        for y in range(120, 832, 64):
            wall = arcade.Sprite("images.png", .39)
            wall.center_x = 270
            wall.center_y = y
            self.wall_list.append(wall)

        for y in range(251, 707, 64):
            wall = arcade.Sprite("images.png", .39)
            wall.center_x = 1294
            wall.center_y = y
            self.wall_list.append(wall)

        for y in range(251, 500, 64):
            wall = arcade.Sprite("images.png", .39)
            wall.center_x = 398
            wall.center_y = y
            self.wall_list.append(wall)

        for y in range(574, 710, 64):
            wall = arcade.Sprite("images.png", .39)
            wall.center_x = 398
            wall.center_y = y
            self.wall_list.append(wall)

        for y in range(381, 581, 64):
            wall = arcade.Sprite("images.png", .39)
            wall.center_x = 522
            wall.center_y = y
            self.wall_list.append(wall)

        for y in range(381, 581, 64):
            wall = arcade.Sprite("images.png", .39)
            wall.center_x = 906
            wall.center_y = y
            self.wall_list.append(wall)

        for y in range(381, 509, 64):
            wall = arcade.Sprite("images.png", .39)
            wall.center_x = 1161
            wall.center_y = y
            self.wall_list.append(wall)

        for y in range(381, 509, 64):
            wall = arcade.Sprite("images.png", .39)
            wall.center_x = 778
            wall.center_y = y
            self.wall_list.append(wall)

        # White box image from cleanpng.com
        wall = arcade.Sprite("images1.png", .35)
        wall.center_x = 1480
        wall.center_y = 600
        self.wall_list.append(wall)

        wall = arcade.Sprite("images1.png", .30)
        wall.center_x = 335
        wall.center_y = 400
        self.wall_list.append(wall)

        wall = arcade.Sprite("images1.png", .28)
        wall.center_x = 460
        wall.center_y = 400
        self.wall_list.append(wall)



        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)

        # Set the background color
        arcade.set_background_color(arcade.color.RED)

        # Set the viewport boundaries
        # These numbers set where we have 'scrolled' to.
        self.view_left = 0
        self.view_bottom = 0

    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        arcade.start_render()

        # Draw all the sprites.
        self.wall_list.draw()
        self.player_list.draw()
        self.coin_list.draw()



        self.output = "Score: " + str(self.score)
        arcade.draw_text(self.output, self.view_left, self.view_bottom, arcade.color.WHITE, 14)

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        if key == arcade.key.UP:
            self.player_sprite.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0

    def on_update(self, delta_time):
        """ Movement and game logic """

        # Call update on all sprites (The sprites don't do much in this
        # example though.)
        self.physics_engine.update()

        # --- Manage Scrolling ---

        # Keep track of if we changed the boundary. We don't want to call the
        # set_viewport command if we didn't change the view port.
        changed = False

        # Scroll left
        left_boundary = self.view_left + VIEWPORT_MARGIN
        if self.player_sprite.left < left_boundary:
            self.view_left -= left_boundary - self.player_sprite.left
            changed = True

        # Scroll right
        right_boundary = self.view_left + SCREEN_WIDTH - VIEWPORT_MARGIN
        if self.player_sprite.right > right_boundary:
            self.view_left += self.player_sprite.right - right_boundary
            changed = True

        # Scroll up
        top_boundary = self.view_bottom + SCREEN_HEIGHT - VIEWPORT_MARGIN
        if self.player_sprite.top > top_boundary:
            self.view_bottom += self.player_sprite.top - top_boundary
            changed = True

        # Scroll down
        bottom_boundary = self.view_bottom + VIEWPORT_MARGIN
        if self.player_sprite.bottom < bottom_boundary:
            self.view_bottom -= bottom_boundary - self.player_sprite.bottom
            changed = True

        # Make sure our boundaries are integer values. While the view port does
        # support floating point numbers, for this application we want every pixel
        # in the view port to map directly onto a pixel on the screen. We don't want
        # any rounding errors.
        self.view_left = int(self.view_left)
        self.view_bottom = int(self.view_bottom)

        # If we changed the boundary values, update the view port to match
        if changed:
            arcade.set_viewport(self.view_left,
                                SCREEN_WIDTH + self.view_left,
                                self.view_bottom,
                                SCREEN_HEIGHT + self.view_bottom)

        good_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                        self.coin_list)

        coin_sound = arcade.load_sound("powerUp11.ogg")

        for coin in good_hit_list:
            self.score += 1
            coin.remove_from_sprite_lists()
            arcade.play_sound(coin_sound)



def main():
    """ Main method """
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()