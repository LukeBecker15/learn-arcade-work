"""
Asteroid Attack
"""

import arcade
import random
import pygame


ROCK_COUNT_1 = 50
HEART_COUNT_1 = 2

SPRITE_SCALING_PLAYER = .3
SPRITE_SCALING_BOX = .4
SPRITE_SCALING_HEART = .2
SPRITE_SCALING_BACKGROUND = 5
SPRITE_SCALING_EXPLOSION = 3

SCREEN_HEIGHT = 800
SCREEN_WIDTH = 1000
SCREEN_TITLE = "Asteroid Attack"


class InstructionView(arcade.View):
    def on_show(self):
        """ This is run once when we switch to this view """
        self.background = arcade.load_texture("space_background.jpg")
        arcade.set_viewport(0, SCREEN_WIDTH - 1, 0, SCREEN_HEIGHT - 1)

    def on_draw(self):
        """ Draw this view """
        arcade.start_render()
        arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, SCREEN_WIDTH, SCREEN_HEIGHT, self.background)
        arcade.draw_text("Welcome to Asteroid Attack", SCREEN_WIDTH / 2, SCREEN_HEIGHT - 100,
                         arcade.color.WHITE, font_size=35, anchor_x="center")
        arcade.draw_text("Click to advance", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 125,
                         arcade.color.WHITE, font_size=15, anchor_x="center")
        arcade.draw_text("Use the cursor to move the spaceman up and down to avoid oncoming asteroids", SCREEN_WIDTH / 2, SCREEN_HEIGHT - 350,
                         arcade.color.WHITE, font_size=20, anchor_x="center")
        arcade.draw_text("Collect hearts to gain lives", SCREEN_WIDTH / 2, SCREEN_HEIGHT - 400,
                         arcade.color.WHITE, font_size=20, anchor_x="center")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        """ If the user presses the mouse button, start the game. """
        game_view = GameView()
        game_view.setup()
        self.window.show_view(game_view)


class Box(arcade.Sprite):
    def update(self):
        self.center_x -= 2.5


class Heart(arcade.Sprite):
    def update(self):
        self.center_x -= 2.5


def level_1(box_list, heart_list):
    for i in range(ROCK_COUNT_1):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX)
        asteroid_sprite.center_x = random.randrange(SCREEN_WIDTH + 800) + 800
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

def level_2(box_list):
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
                   [3025, 100], [3100, 150], [3175, 200], [3250, 250], [3325, 300], [3400, 350],
                   [1575, 450], [1650, 500], [1725, 550], [1800, 600], [1875, 600],
                   [1650, 400], [1725, 350], [1800, 300], [1875, 300],
                   [1950, 550], [2025, 500], [2100, 450],
                   [1950, 350], [2025, 400],
                   [2725, 450], [2800, 500], [2875, 550], [2950, 600], [3025, 600],
                   [2800, 400], [2875, 350], [2950, 300], [3025, 300],
                   [3100, 550], [3175, 500], [3250, 450],
                   [3100, 350], [3175, 400],
                   [1800, 700], [2975, 200]]

    for coordinate in coordinate_list:
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX)
        asteroid_sprite.center_x = coordinate[0] + 75
        asteroid_sprite.center_y = coordinate[1] - 50
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1


def level_3(box_list):
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


def level_4(box_list):
    for y in range(0, 200, 64):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX)
        asteroid_sprite.center_x = 1400
        asteroid_sprite.center_y = y
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1

    for y in range(325, 800, 64):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX)
        asteroid_sprite.center_x = 1400
        asteroid_sprite.center_y = y
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1

    for y in range(0, 600, 64):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX)
        asteroid_sprite.center_x = 1700
        asteroid_sprite.center_y = y
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1

    for y in range(725, 800, 64):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX)
        asteroid_sprite.center_x = 1700
        asteroid_sprite.center_y = y
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1

    for y in range(0, 75, 64):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX)
        asteroid_sprite.center_x = 2000
        asteroid_sprite.center_y = y
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1

    for y in range(200, 800, 64):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX)
        asteroid_sprite.center_x = 2000
        asteroid_sprite.center_y = y
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1

    for y in range(0, 250, 64):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX)
        asteroid_sprite.center_x = 2300
        asteroid_sprite.center_y = y
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1

    for y in range(375, 800, 64):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX)
        asteroid_sprite.center_x = 2300
        asteroid_sprite.center_y = y
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1

    for y in range(125, 800, 64):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX)
        asteroid_sprite.center_x = 2600
        asteroid_sprite.center_y = y
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1

    for y in range(0, 675, 64):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX)
        asteroid_sprite.center_x = 2900
        asteroid_sprite.center_y = y
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1

    for y in range(775, 800, 64):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX)
        asteroid_sprite.center_x = 2900
        asteroid_sprite.center_y = y
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1

    for y in range(0, 350, 64):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX)
        asteroid_sprite.center_x = 3200
        asteroid_sprite.center_y = y
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1

    for y in range(475, 800, 64):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX)
        asteroid_sprite.center_x = 3200
        asteroid_sprite.center_y = y
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1

    for y in range(0, 100, 64):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX)
        asteroid_sprite.center_x = 3500
        asteroid_sprite.center_y = y
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1

    for y in range(225, 600, 64):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX)
        asteroid_sprite.center_x = 3500
        asteroid_sprite.center_y = y
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1

    for y in range(725, 800, 64):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX)
        asteroid_sprite.center_x = 3500
        asteroid_sprite.center_y = y
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1

    for y in range(0, 750, 64):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX)
        asteroid_sprite.center_x = 3800
        asteroid_sprite.center_y = y
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1

    for y in range(0, 125, 64):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX)
        asteroid_sprite.center_x = 4100
        asteroid_sprite.center_y = y
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1

    for y in range(200, 800, 64):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX)
        asteroid_sprite.center_x = 4100
        asteroid_sprite.center_y = y
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1

    for y in range(0, 575, 64):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX)
        asteroid_sprite.center_x = 4400
        asteroid_sprite.center_y = y
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1

    for y in range(700, 800, 64):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX)
        asteroid_sprite.center_x = 4400
        asteroid_sprite.center_y = y
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1

    for y in range(0, 400, 64):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX)
        asteroid_sprite.center_x = 4700
        asteroid_sprite.center_y = y
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1

    for y in range(525, 800, 64):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX)
        asteroid_sprite.center_x = 4700
        asteroid_sprite.center_y = y
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1


def level_5(box_list, heart_list):
    for i in range(ROCK_COUNT_1 + 50):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX)
        asteroid_sprite.center_x = random.randrange(SCREEN_WIDTH + 800) + 800
        asteroid_sprite.center_y = random.randrange(SCREEN_HEIGHT)
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1

    for i in range(HEART_COUNT_1):
        # image from dreamstime.com
        heart_sprite = Heart("heart.png", SPRITE_SCALING_HEART)
        heart_placed = False
        while not heart_placed:

            heart_sprite.center_x = random.randrange(SCREEN_WIDTH + 800) + 800
            heart_sprite.center_y = random.randrange(SCREEN_HEIGHT)
            bad_hit_list = arcade.check_for_collision_with_list(heart_sprite,
                                                                box_list)
            if len(bad_hit_list) == 0:
                heart_placed = True
        heart_list.append(heart_sprite)


class GameOverLossView(arcade.View):
    """ View to show when game is over """

    def __init__(self):
        """ This is run once when we switch to this view """
        super().__init__()

        self.texture = arcade.load_texture("space_background.jpg")

        # Reset the viewport, necessary if we have a scrolling game and we need
        # to reset the viewport back to the start so we can see what we draw.
        arcade.set_viewport(0, SCREEN_WIDTH - 1, 0, SCREEN_HEIGHT - 1)
        self.explosion_list = None


    def setup(self):
        self.explosion_list = arcade.SpriteList()

        #image from hiclipart.com
        self.explosion_sprite = arcade.Sprite("explosion.png", SPRITE_SCALING_EXPLOSION)
        self.explosion_sprite.center_x = 300
        self.explosion_sprite.center_y = 300
        self.explosion_list.append(self.explosion_sprite)


    def on_draw(self):
        """ Draw this view """
        arcade.start_render()
        self.explosion_list.draw()
        self.texture.draw_sized(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2,
                                SCREEN_WIDTH, SCREEN_HEIGHT)


    def on_mouse_press(self, _x, _y, _button, _modifiers):
        """ If the user presses the mouse button, re-start the game. """
        game_view = GameView()
        game_view.setup()
        self.window.show_view(game_view)


class GameView(arcade.View):
    def __init__(self):
        super().__init__()

        self.background = None

        self.player_list = None
        self.box_list = None
        self.heart_list = None

        self.player_sprite = None
        self.lives = 3
        self.score = 0
        self.level = 0

        self.window.set_mouse_visible(False)
        self.physics_engine = None


    def setup(self):
        # image from wallpaperset.com
        self.background = arcade.load_texture("space_background.jpg")

        self.player_list = arcade.SpriteList()
        self.box_list = arcade.SpriteList()
        self.heart_list = arcade.SpriteList()

        self.level = 0
        self.lives = 3
        self.score = 0

        # image from freepik.com
        self.player_sprite = arcade.Sprite("spaceman.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 300
        self.player_sprite.center_y = 400
        self.player_list.append(self.player_sprite)

        pygame.mixer.init()
        pygame.init()

        # Background music from opengameart.org
        pygame.mixer.music.load("Background_music.ogg")
        pygame.mixer.music.play(loops=-1)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, SCREEN_WIDTH, SCREEN_HEIGHT, self.background)

        self.player_list.draw()
        #self.sun_list.draw()
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

        if self.lives == 0:
            view = GameOverLossView()
            view.setup()
            self.window.show_view(view)
            pygame.mixer.music.stop()
            pygame.mixer.quit()

        else:
            advance_level = True
            for asteroid in self.box_list:
                if asteroid.right > 0:
                    advance_level = False
                    break

            if advance_level and self.level == 0:
                level_1(self.box_list, self.heart_list)
                self.level = 1
                self.score = 0

            elif advance_level and self.level == 1:
                level_2(self.box_list)
                self.level = 2
                self.score = 1

            elif advance_level and self.level == 2:
                level_3(self.box_list)
                self.level = 3
                self.score = 2

            elif advance_level and self.level == 3:
                level_4(self.box_list)
                self.level = 4
                self.score = 3

            elif advance_level and self.level == 4:
                level_5(self.box_list, self.heart_list)
                self.score = 4


def main():
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    start_view = InstructionView()
    window.show_view(start_view)
    arcade.run()


if __name__ == "__main__":
    main()