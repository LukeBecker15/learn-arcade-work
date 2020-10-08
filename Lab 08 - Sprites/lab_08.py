import random
import arcade
import math

SPRITE_SCALING = 0.5

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
COIN_COUNT = 50
ROCK_COUNT = 30



class Coin(arcade.Sprite):

    def __init__(self, filename, sprite_scaling):
        """ Constructor. """
        # Call the parent class (Sprite) constructor
        super().__init__(filename, sprite_scaling)

        # Current angle in radians
        self.circle_angle = 0

        # How far away from the center to orbit, in pixels
        self.circle_radius = 0

        # How fast to orbit, in radians per frame
        self.circle_speed = 0.008

        # Set the center of the point we will orbit around
        self.circle_center_x = 0
        self.circle_center_y = 0

   
    def update(self):

        """ Update the ball's position. """
        # Calculate a new x, y
        self.center_x = self.circle_radius * math.sin(self.circle_angle) \
                        + self.circle_center_x
        self.center_y = self.circle_radius * math.cos(self.circle_angle) \
                        + self.circle_center_y

        # Increase the angle in prep for the next round.
        self.circle_angle += self.circle_speed + .02


class Rock(arcade.Sprite):

    def __init__(self, filename, sprite_scaling):
        """ Constructor. """
        # Call the parent class (Sprite) constructor
        super().__init__(filename, sprite_scaling)

        # Current angle in radians


        # How far away from the center to orbit, in pixels


        # How fast to orbit, in radians per frame



        # Set the center of the point we will orbit around

    def reset(self):
        self.center_x = random.randrange(SCREEN_WIDTH)

    def update(self):

        """ Update the ball's position. """
        # Calculate a new x, y

        self.center_y -= 2
        if self.center_y < 0:
            self.bottom = SCREEN_HEIGHT
            self.reset()


class MyGame(arcade.Window):

    """ Main application class. """

    def __init__(self, width, height):

        super().__init__(width, height)

        # Sprite lists
        self.player_list = None
        self.coin_list = None
        self.rock_list = None

        # Set up the player
        self.score = 0
        self.player_sprite = None

        self.lives = 5
        self.rock_sprite = None

    def drawing(self):
        arcade.draw_text("You're Pretty Bad at This!", 200, 300, arcade.color.WHITE, 30)

    def draw(self):
        arcade.draw_text("Congrats on the Dub!", 225, 300, arcade.color.WHITE, 30)

    def start_new_game(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()
        self.rock_list = arcade.SpriteList()

        # Set up the player
        self.score = 0

        # Character image from http://clipart-library.com/
        self.player_sprite = arcade.Sprite("unnamed.png", SPRITE_SCALING / 4)

        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 70
        self.player_list.append(self.player_sprite)

        for i in range(COIN_COUNT):


            # Coin image from https://www.pinterest.com/
            coin = Coin("c8884d6baa63c7497d28a9fae4f87a03.png", SPRITE_SCALING /12)

            # Position the center of the circle the coin will orbit
            coin.circle_center_x = random.randrange(SCREEN_WIDTH)
            coin.circle_center_y = random.randrange(SCREEN_HEIGHT)

            # Random radius from 10 to 200
            coin.circle_radius = random.randrange(10, 200)

            # Random start angle from 0 to 2pi
            coin.circle_angle = random.random() * 2 * math.pi

            # Add the coin to the lists
            self.coin_list.append(coin)


        for i in range(ROCK_COUNT):


            # Coin image from https://www.pinterest.com/
            rock = Rock("images.png", SPRITE_SCALING / 3)

            # Position the center of the circle the coin will orbit
            rock.center_x = random.randrange(SCREEN_WIDTH)
            rock.center_y = random.randrange(SCREEN_HEIGHT)

            # Random radius from 10 to 200
            rock.circle_radius = random.randrange(10, 200)

            # Random start angle from 0 to 2pi
            rock.circle_angle = random.random() * 2 * math.pi

            # Add the coin to the lists
            self.rock_list.append(rock)

        # Don't show the mouse cursor
        self.set_mouse_visible(False)

        # Set the background color
        arcade.set_background_color(arcade.color.AMAZON)

    def on_draw(self):

        # This command has to happen before we start drawing
        arcade.start_render()

        # Draw all the sprites.
        self.coin_list.draw()
        self.player_list.draw()
        self.rock_list.draw()
        if self.lives == 0:
            self.done = True
            self.drawing()
        if self.score == 50:
            self.done = True
            self.draw()

        # Put the text on the screen.
        output = "Score: " + str(self.score)
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)

    def on_mouse_motion(self, x, y, dx, dy):

        if self.score < 50 and self.lives > 0:
            self.player_sprite.center_x = x
            self.player_sprite.center_y = y

    def update(self, delta_time):
        """ Movement and game logic """
        self.done = False
        # Call update on all sprites (The sprites don't do much in this
        # example though.)
        if self.score < 50 and self.lives > 0:
            self.coin_list.update()
            self.rock_list.update()



        # Generate a list of all sprites that collided with the player.
        good_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                        self.coin_list)
        bad_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                        self.rock_list)
        # Loop through each colliding sprite, remove it, and add to the score.
        for coin in good_hit_list:
            self.score += 1
            coin.remove_from_sprite_lists()

        for rock in bad_hit_list:
            self.lives -= 1
            rock.remove_from_sprite_lists()






def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    window.start_new_game()
    arcade.run()


if __name__ == "__main__":
    main()