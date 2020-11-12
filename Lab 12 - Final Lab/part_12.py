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
        self.center_x -= 3

class Heart(arcade.Sprite):
    def update(self):
        self.center_x -= 1.5

def level_1(box_list, heart_list):
    for i in range(ROCK_COUNT_1):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX)
        asteroid_sprite.center_x = random.randrange(SCREEN_WIDTH + 600) + 800
        asteroid_sprite.center_y = random.randrange(SCREEN_HEIGHT)
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1

    for i in range(HEART_COUNT_1):
        # image from dreamstime.com
        heart_sprite = Heart("heart.png", SPRITE_SCALING_HEART)
        heart_placed = False
        while not heart_placed:

            heart_sprite.center_x = random.randrange(SCREEN_WIDTH) + 800
            heart_sprite.center_y = random.randrange(SCREEN_HEIGHT)
            bad_hit_list = arcade.check_for_collision_with_list(heart_sprite,
                                                                box_list)
            if len(bad_hit_list) == 0:
                heart_placed = True
        heart_list.append(heart_sprite)

def level_2(box_list, heart_list):
    for x in range(800, 1500, 64):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX)
        asteroid_sprite.center_x = x
        asteroid_sprite.center_y = 550
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1

    for x in range(800, 1500, 64):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX)
        asteroid_sprite.center_x = x
        asteroid_sprite.center_y = 350
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1

    coordinate_list = [[1500, 600],
                   [1575, 650], [1650, 700], [1725, 750], [1800, 800],
                   [1500, 400], [1575, 450], [1650, 500], [1725, 550], [1800, 600],
                   [1875, 800], [1950, 750], [2025, 700], [2100, 650], [2175, 600], [2250, 550],
                   [2325, 500], [2400, 450], [2475, 400], [2550, 350], [2625, 300], [2700, 250],
                   [1875, 600], [1950, 550], [2025, 500], [2100, 450], [2175, 400], [2250, 350],
                   [2325, 300], [2400, 250], [2475, 200], [2550, 150], [2625, 100], [2700, 50],
                   [2775, 250], [2850, 300], [2925, 350], [3000, 400], [3075, 450], [3150, 500], [3225, 550],
                   [2775, 50], [2850, 100], [2925, 150], [3000, 200], [3075, 250], [3150, 300], [3225, 350]]
    for coordinate in coordinate_list:
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX)
        asteroid_sprite.center_x = coordinate[0]
        asteroid_sprite.center_y = coordinate[1]
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1




def level_3(box_list, heart_list):
    for x in range(875, 1575, 64):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX)
        asteroid_sprite.center_x = x
        asteroid_sprite.center_y = 500
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1

    for x in range(2325, 2650, 64):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX)
        asteroid_sprite.center_x = x
        asteroid_sprite.center_y = 300
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1

    for x in range(2325, 2650, 64):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX)
        asteroid_sprite.center_x = x
        asteroid_sprite.center_y = 500
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1

    for x in range(875, 1575, 64):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX)
        asteroid_sprite.center_x = x
        asteroid_sprite.center_y = 300
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1

    coordinate_list = [[1500, 600],
                   [1575, 650], [1650, 700], [1725, 750], [1800, 800],
                   [1500, 300], [1575, 250], [1650, 200], [1725, 150], [1800, 100],
                   [1875, 800], [1950, 750], [2025, 700], [2100, 650], [2175, 600], [2250, 550],
                   [1875, 100], [1950, 150], [2025, 200], [2100, 250], [2175, 300], [2250, 350],
                   [2650, 600], [2725, 650], [2800, 700], [2875, 750], [2950, 800],
                   [2650, 300], [2725, 250], [2800, 200], [2875, 150], [2950, 100],
                   [3025, 800], [3100, 750], [3175, 700], [3250, 650], [3325, 600], [3400, 550],
                   [3025, 100], [3100, 150], [3175, 200], [3250, 250], [3325, 300], [3400, 350]
                    ]

    for coordinate in coordinate_list:
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX)
        asteroid_sprite.center_x = coordinate[0] + 75
        asteroid_sprite.center_y = coordinate[1] - 50
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1

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

        self.physics_engine = None

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



        level_3(self.box_list, self.heart_list)




    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, self.background)
        self.player_list.draw()
        self.sun_list.draw()
        self.box_list.draw()
        self.heart_list.draw()


        if self.lives == 0:
            self.done = True

        output = "Score: " + str(self.score)
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)


    def on_mouse_motion(self, x, y, dx, dy):
        """ Handle Mouse Motion """

        # Move the center of the player sprite to match the mouse x, y
        if self.lives > 0:
            self.player_sprite.center_y = y

    def on_mouse_press(self, x, y, button, modifiers):
        background_music = arcade.load_sound("Background_music.ogg")
        arcade.play_sound(background_music)


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
        #for asteroid in box_list:

            #if asteroid.center_x < -1200 and asteroid_sprite.points_available == 1:
                #self.score += 1
                #self.asteroid_sprite.points_available = 0


def main():
    window = MyGame()
    window.setup()
    arcade.run()
    #background_music = arcade.load_sound("Background_music.ogg")
    #arcade.play_sound(background_music)

if __name__ == "__main__":
    main()