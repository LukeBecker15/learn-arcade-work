import arcade
import random

ROCK_COUNT_1 = 50
HEART_COUNT_1 = 2


SPRITE_SCALING_PLAYER = .3
SPRITE_SCALING_BOX = .4
SPRITE_SCALING_HEART = .2
SPRITE_SCALING_BACKGROUND = 5
SPRITE_SCALING_SUN = 11


SCREEN_HEIGHT = 800
SCREEN_WIDTH = 1000


class Box(arcade.Sprite):
    def update(self):
        self.center_x -= 1

class Heart(arcade.Sprite):
    def update(self):
        self.center_x -= 1



class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Final Lab")

        self.background = None

        self.player_list = None
        self.box_list = None
        self.heart_list = None
        self.sun_list = None

        self.player_sprite = None
        self.lives = 3
        self.score = 0

        self.set_mouse_visible(False)

    def setup(self):


        # image from wallpapersafari.com
        self.background = arcade.load_texture("background.png")

        self.player_list = arcade.SpriteList()
        self.box_list = arcade.SpriteList()
        self.heart_list = arcade.SpriteList()
        self.sun_list = arcade.SpriteList()

        self.lives = 3
        self.score = 0


        # image from freepik.com
        self.player_sprite = arcade.Sprite("spaceman.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 300
        self.player_sprite.center_y = 400
        self.player_list.append(self.player_sprite)

        #image from webstockreview.net
        self.sun_sprite = arcade.Sprite("sun.png", SPRITE_SCALING_SUN)
        self.sun_sprite.center_x = -850
        self.sun_sprite.center_y = 450
        self.sun_list.append(self.sun_sprite)


        for i in range(ROCK_COUNT_1):
            # image from nicepng.com
            self.asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX)
            self.asteroid_sprite.center_x = random.randrange(SCREEN_WIDTH) + 800
            self.asteroid_sprite.center_y = random.randrange(SCREEN_HEIGHT)
            self.box_list.append(self.asteroid_sprite)

        for i in range(HEART_COUNT_1):
            # image from dreamstime.com
            self.heart_sprite = Heart("heart.png", SPRITE_SCALING_HEART)
            self.heart_sprite.center_x = random.randrange(SCREEN_WIDTH) + 800
            self.heart_sprite.center_y = random.randrange(SCREEN_HEIGHT)
            self.heart_list.append(self.heart_sprite)


    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, self.background)
        self.player_list.draw()
        self.sun_list.draw()
        self.box_list.draw()
        self.heart_list.draw()

        if self.lives == 0:
            self.done = True

    def on_mouse_motion(self, x, y, dx, dy):
        """ Handle Mouse Motion """

        # Move the center of the player sprite to match the mouse x, y
        if self.lives > 0:
            self.player_sprite.center_y = y

    def update(self, delta_time):


        self.done = False

        if self.lives > 0:
            self.box_list.update()
            self.heart_list.update()

        good_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                             self.heart_list)
        bad_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                            self.box_list)

        rock_sound = arcade.load_sound("explosion.ogg")
        heart_sound = arcade.load_sound("heart.ogg")

        for heart in good_hit_list:
            self.lives += 1
            heart.remove_from_sprite_lists()
            arcade.play_sound(heart_sound)

        for rock in bad_hit_list:
            self.lives -= 1
            rock.remove_from_sprite_lists()
            arcade.play_sound(rock_sound)


def main():
    window = MyGame()
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()