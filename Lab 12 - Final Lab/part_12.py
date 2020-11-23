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
SPRITE_SCALING_EXPLOSION = 1
SPRITE_SCALING_FLAG = 1

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
    def __init__(self, image, scale, speed):
        super().__init__(image, scale)
        self.speed = speed

    def update(self):
        self.center_x -= self.speed


class Heart(arcade.Sprite):
    def __init__(self, image, scale, speed):
        super().__init__(image, scale)
        self.speed = speed

    def update(self):
        self.center_x -= self.speed


def level_1(box_list, heart_list):
    for i in range(ROCK_COUNT_1):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX, 2.5)
        asteroid_sprite.center_x = random.randrange(SCREEN_WIDTH + 800) + 800
        asteroid_sprite.center_y = random.randrange(SCREEN_HEIGHT)
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1

    for i in range(HEART_COUNT_1):
        # image from dreamstime.com
        heart_sprite = Heart("heart.png", SPRITE_SCALING_HEART, 2.5)
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
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX, 2.5)
        asteroid_sprite.center_x = x
        asteroid_sprite.center_y = 500
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1

    for x in range(2325, 2650, 64):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX, 2.5)
        asteroid_sprite.center_x = x
        asteroid_sprite.center_y = 300
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1

    for x in range(2325, 2650, 64):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX, 2.5)
        asteroid_sprite.center_x = x
        asteroid_sprite.center_y = 500
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1

    for x in range(875, 1575, 64):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX, 2.5)
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
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX, 2.5)
        asteroid_sprite.center_x = coordinate[0] + 75
        asteroid_sprite.center_y = coordinate[1] - 50
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1


def level_3(box_list):
    for x in range(800, 1500, 64):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX, 2.5)
        asteroid_sprite.center_x = x
        asteroid_sprite.center_y = 550
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1

    for x in range(800, 1500, 64):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX, 2.5)
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
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX, 2.5)
        asteroid_sprite.center_x = coordinate[0]
        asteroid_sprite.center_y = coordinate[1]
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1


def level_4(box_list):
    for y in range(0, 200, 64):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX, 2.5)
        asteroid_sprite.center_x = 1400
        asteroid_sprite.center_y = y
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1

    for y in range(325, 800, 64):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX, 2.5)
        asteroid_sprite.center_x = 1400
        asteroid_sprite.center_y = y
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1

    for y in range(0, 600, 64):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX, 2.5)
        asteroid_sprite.center_x = 1700
        asteroid_sprite.center_y = y
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1

    for y in range(725, 800, 64):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX, 2.5)
        asteroid_sprite.center_x = 1700
        asteroid_sprite.center_y = y
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1

    for y in range(0, 75, 64):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX, 2.5)
        asteroid_sprite.center_x = 2000
        asteroid_sprite.center_y = y
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1

    for y in range(200, 800, 64):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX, 2.5)
        asteroid_sprite.center_x = 2000
        asteroid_sprite.center_y = y
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1

    for y in range(0, 250, 64):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX, 2.5)
        asteroid_sprite.center_x = 2300
        asteroid_sprite.center_y = y
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1

    for y in range(375, 800, 64):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX, 2.5)
        asteroid_sprite.center_x = 2300
        asteroid_sprite.center_y = y
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1

    for y in range(125, 800, 64):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX, 2.5)
        asteroid_sprite.center_x = 2600
        asteroid_sprite.center_y = y
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1

    for y in range(0, 675, 64):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX, 2.5)
        asteroid_sprite.center_x = 2900
        asteroid_sprite.center_y = y
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1

    for y in range(775, 800, 64):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX, 2.5)
        asteroid_sprite.center_x = 2900
        asteroid_sprite.center_y = y
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1

    for y in range(0, 350, 64):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX, 2.5)
        asteroid_sprite.center_x = 3200
        asteroid_sprite.center_y = y
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1

    for y in range(475, 800, 64):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX, 2.5)
        asteroid_sprite.center_x = 3200
        asteroid_sprite.center_y = y
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1

    for y in range(0, 100, 64):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX, 2.5)
        asteroid_sprite.center_x = 3500
        asteroid_sprite.center_y = y
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1

    for y in range(225, 600, 64):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX, 2.5)
        asteroid_sprite.center_x = 3500
        asteroid_sprite.center_y = y
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1

    for y in range(725, 800, 64):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX, 2.5)
        asteroid_sprite.center_x = 3500
        asteroid_sprite.center_y = y
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1

    for y in range(0, 750, 64):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX, 2.5)
        asteroid_sprite.center_x = 3800
        asteroid_sprite.center_y = y
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1

    for y in range(0, 125, 64):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX, 2.5)
        asteroid_sprite.center_x = 4100
        asteroid_sprite.center_y = y
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1

    for y in range(200, 800, 64):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX, 2.5)
        asteroid_sprite.center_x = 4100
        asteroid_sprite.center_y = y
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1

    for y in range(0, 575, 64):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX, 2.5)
        asteroid_sprite.center_x = 4400
        asteroid_sprite.center_y = y
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1

    for y in range(700, 800, 64):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX, 2.5)
        asteroid_sprite.center_x = 4400
        asteroid_sprite.center_y = y
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1

    for y in range(0, 400, 64):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX, 2.5)
        asteroid_sprite.center_x = 4700
        asteroid_sprite.center_y = y
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1

    for y in range(525, 800, 64):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX, 2.5)
        asteroid_sprite.center_x = 4700
        asteroid_sprite.center_y = y
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1


def level_5(box_list, heart_list):
    for i in range(ROCK_COUNT_1 + 40):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX, 2.5)
        asteroid_sprite.center_x = random.randrange(SCREEN_WIDTH + 800) + 800
        asteroid_sprite.center_y = random.randrange(SCREEN_HEIGHT)
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1

    for i in range(HEART_COUNT_1):
        # image from dreamstime.com
        heart_sprite = Heart("heart.png", SPRITE_SCALING_HEART, 2.5)
        heart_placed = False
        while not heart_placed:

            heart_sprite.center_x = random.randrange(SCREEN_WIDTH + 800) + 800
            heart_sprite.center_y = random.randrange(SCREEN_HEIGHT)
            bad_hit_list = arcade.check_for_collision_with_list(heart_sprite,
                                                                box_list)
            if len(bad_hit_list) == 0:
                heart_placed = True
        heart_list.append(heart_sprite)


def level_6(box_list, heart_list):
    for i in range(ROCK_COUNT_1):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX, 3.5)
        asteroid_sprite.center_x = random.randrange(SCREEN_WIDTH + 800) + 800
        asteroid_sprite.center_y = random.randrange(SCREEN_HEIGHT)
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1

    for i in range(HEART_COUNT_1):
        # image from dreamstime.com
        heart_sprite = Heart("heart.png", SPRITE_SCALING_HEART, 3.5)
        heart_placed = False
        while not heart_placed:

            heart_sprite.center_x = random.randrange(SCREEN_WIDTH) + 800
            heart_sprite.center_y = random.randrange(SCREEN_HEIGHT)
            bad_hit_list = arcade.check_for_collision_with_list(heart_sprite,
                                                                box_list)
            if len(bad_hit_list) == 0:
                heart_placed = True
        heart_list.append(heart_sprite)


def level_7(box_list):
    for x in range(875, 1575, 64):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX, 3.5)
        asteroid_sprite.center_x = x
        asteroid_sprite.center_y = 500
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1

    for x in range(2325, 2650, 64):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX, 3.5)
        asteroid_sprite.center_x = x
        asteroid_sprite.center_y = 300
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1

    for x in range(2325, 2650, 64):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX, 3.5)
        asteroid_sprite.center_x = x
        asteroid_sprite.center_y = 500
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1

    for x in range(875, 1575, 64):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX, 3.5)
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
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX, 3.5)
        asteroid_sprite.center_x = coordinate[0] + 75
        asteroid_sprite.center_y = coordinate[1] - 50
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1


def level_8(box_list):
    for x in range(800, 1500, 64):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX, 3.5)
        asteroid_sprite.center_x = x
        asteroid_sprite.center_y = 550
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1

    for x in range(800, 1500, 64):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX, 3.5)
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
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX, 3.5)
        asteroid_sprite.center_x = coordinate[0]
        asteroid_sprite.center_y = coordinate[1]
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1


def level_9(box_list):
    for y in range(0, 200, 64):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX, 3.5)
        asteroid_sprite.center_x = 1400
        asteroid_sprite.center_y = y
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1

    for y in range(325, 800, 64):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX, 3.5)
        asteroid_sprite.center_x = 1400
        asteroid_sprite.center_y = y
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1

    for y in range(0, 600, 64):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX, 3.5)
        asteroid_sprite.center_x = 1700
        asteroid_sprite.center_y = y
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1

    for y in range(725, 800, 64):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX, 3.5)
        asteroid_sprite.center_x = 1700
        asteroid_sprite.center_y = y
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1

    for y in range(0, 75, 64):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX, 3.5)
        asteroid_sprite.center_x = 2000
        asteroid_sprite.center_y = y
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1

    for y in range(200, 800, 64):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX, 3.5)
        asteroid_sprite.center_x = 2000
        asteroid_sprite.center_y = y
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1

    for y in range(0, 250, 64):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX, 3.5)
        asteroid_sprite.center_x = 2300
        asteroid_sprite.center_y = y
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1

    for y in range(375, 800, 64):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX, 3.5)
        asteroid_sprite.center_x = 2300
        asteroid_sprite.center_y = y
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1

    for y in range(125, 800, 64):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX, 3.5)
        asteroid_sprite.center_x = 2600
        asteroid_sprite.center_y = y
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1

    for y in range(0, 675, 64):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX, 3.5)
        asteroid_sprite.center_x = 2900
        asteroid_sprite.center_y = y
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1

    for y in range(775, 800, 64):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX, 3.5)
        asteroid_sprite.center_x = 2900
        asteroid_sprite.center_y = y
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1

    for y in range(0, 350, 64):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX, 3.5)
        asteroid_sprite.center_x = 3200
        asteroid_sprite.center_y = y
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1

    for y in range(475, 800, 64):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX, 3.5)
        asteroid_sprite.center_x = 3200
        asteroid_sprite.center_y = y
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1

    for y in range(0, 100, 64):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX, 3.5)
        asteroid_sprite.center_x = 3500
        asteroid_sprite.center_y = y
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1

    for y in range(225, 600, 64):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX, 3.5)
        asteroid_sprite.center_x = 3500
        asteroid_sprite.center_y = y
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1

    for y in range(725, 800, 64):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX, 3.5)
        asteroid_sprite.center_x = 3500
        asteroid_sprite.center_y = y
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1

    for y in range(0, 750, 64):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX, 3.5)
        asteroid_sprite.center_x = 3800
        asteroid_sprite.center_y = y
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1

    for y in range(0, 125, 64):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX, 3.5)
        asteroid_sprite.center_x = 4100
        asteroid_sprite.center_y = y
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1

    for y in range(200, 800, 64):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX, 3.5)
        asteroid_sprite.center_x = 4100
        asteroid_sprite.center_y = y
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1

    for y in range(0, 575, 64):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX, 3.5)
        asteroid_sprite.center_x = 4400
        asteroid_sprite.center_y = y
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1

    for y in range(700, 800, 64):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX, 3.5)
        asteroid_sprite.center_x = 4400
        asteroid_sprite.center_y = y
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1

    for y in range(0, 400, 64):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX, 3.5)
        asteroid_sprite.center_x = 4700
        asteroid_sprite.center_y = y
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1

    for y in range(525, 800, 64):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX, 3.5)
        asteroid_sprite.center_x = 4700
        asteroid_sprite.center_y = y
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1


def level_10(box_list, heart_list):
    for i in range(ROCK_COUNT_1 + 40):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX, 3.5)
        asteroid_sprite.center_x = random.randrange(SCREEN_WIDTH + 800) + 800
        asteroid_sprite.center_y = random.randrange(SCREEN_HEIGHT)
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1

    for i in range(HEART_COUNT_1):
        # image from dreamstime.com
        heart_sprite = Heart("heart.png", SPRITE_SCALING_HEART, 3.5)
        heart_placed = False
        while not heart_placed:

            heart_sprite.center_x = random.randrange(SCREEN_WIDTH + 800) + 800
            heart_sprite.center_y = random.randrange(SCREEN_HEIGHT)
            bad_hit_list = arcade.check_for_collision_with_list(heart_sprite,
                                                                box_list)
            if len(bad_hit_list) == 0:
                heart_placed = True
        heart_list.append(heart_sprite)


def level_11(box_list, heart_list):
    for i in range(ROCK_COUNT_1):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX, 5)
        asteroid_sprite.center_x = random.randrange(SCREEN_WIDTH + 800) + 800
        asteroid_sprite.center_y = random.randrange(SCREEN_HEIGHT)
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1

    for i in range(HEART_COUNT_1):
        # image from dreamstime.com
        heart_sprite = Heart("heart.png", SPRITE_SCALING_HEART, 5)
        heart_placed = False
        while not heart_placed:

            heart_sprite.center_x = random.randrange(SCREEN_WIDTH) + 800
            heart_sprite.center_y = random.randrange(SCREEN_HEIGHT)
            bad_hit_list = arcade.check_for_collision_with_list(heart_sprite,
                                                                box_list)
            if len(bad_hit_list) == 0:
                heart_placed = True
        heart_list.append(heart_sprite)


def level_12(box_list):
    for x in range(875, 1575, 64):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX, 5)
        asteroid_sprite.center_x = x
        asteroid_sprite.center_y = 500
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1

    for x in range(2325, 2650, 64):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX, 5)
        asteroid_sprite.center_x = x
        asteroid_sprite.center_y = 300
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1

    for x in range(2325, 2650, 64):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX, 5)
        asteroid_sprite.center_x = x
        asteroid_sprite.center_y = 500
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1

    for x in range(875, 1575, 64):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX, 5)
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
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX, 5)
        asteroid_sprite.center_x = coordinate[0] + 75
        asteroid_sprite.center_y = coordinate[1] - 50
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1


def level_13(box_list):
    for x in range(800, 1500, 64):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX, 5)
        asteroid_sprite.center_x = x
        asteroid_sprite.center_y = 550
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1

    for x in range(800, 1500, 64):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX, 5)
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
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX, 5)
        asteroid_sprite.center_x = coordinate[0]
        asteroid_sprite.center_y = coordinate[1]
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1


def level_14(box_list):
    for y in range(0, 200, 64):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX, 5)
        asteroid_sprite.center_x = 1400
        asteroid_sprite.center_y = y
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1

    for y in range(325, 800, 64):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX, 5)
        asteroid_sprite.center_x = 1400
        asteroid_sprite.center_y = y
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1

    for y in range(0, 600, 64):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX, 5)
        asteroid_sprite.center_x = 1700
        asteroid_sprite.center_y = y
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1

    for y in range(725, 800, 64):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX, 5)
        asteroid_sprite.center_x = 1700
        asteroid_sprite.center_y = y
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1

    for y in range(0, 75, 64):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX, 5)
        asteroid_sprite.center_x = 2000
        asteroid_sprite.center_y = y
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1

    for y in range(200, 800, 64):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX, 5)
        asteroid_sprite.center_x = 2000
        asteroid_sprite.center_y = y
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1

    for y in range(0, 250, 64):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX, 5)
        asteroid_sprite.center_x = 2300
        asteroid_sprite.center_y = y
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1

    for y in range(375, 800, 64):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX, 5)
        asteroid_sprite.center_x = 2300
        asteroid_sprite.center_y = y
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1

    for y in range(125, 800, 64):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX, 5)
        asteroid_sprite.center_x = 2600
        asteroid_sprite.center_y = y
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1

    for y in range(0, 675, 64):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX, 5)
        asteroid_sprite.center_x = 2900
        asteroid_sprite.center_y = y
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1

    for y in range(775, 800, 64):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX, 5)
        asteroid_sprite.center_x = 2900
        asteroid_sprite.center_y = y
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1

    for y in range(0, 350, 64):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX, 5)
        asteroid_sprite.center_x = 3200
        asteroid_sprite.center_y = y
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1

    for y in range(475, 800, 64):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX, 5)
        asteroid_sprite.center_x = 3200
        asteroid_sprite.center_y = y
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1

    for y in range(0, 100, 64):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX, 5)
        asteroid_sprite.center_x = 3500
        asteroid_sprite.center_y = y
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1

    for y in range(225, 600, 64):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX, 5)
        asteroid_sprite.center_x = 3500
        asteroid_sprite.center_y = y
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1

    for y in range(725, 800, 64):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX, 5)
        asteroid_sprite.center_x = 3500
        asteroid_sprite.center_y = y
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1

    for y in range(0, 750, 64):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX, 5)
        asteroid_sprite.center_x = 3800
        asteroid_sprite.center_y = y
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1

    for y in range(0, 125, 64):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX, 5)
        asteroid_sprite.center_x = 4100
        asteroid_sprite.center_y = y
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1

    for y in range(200, 800, 64):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX, 5)
        asteroid_sprite.center_x = 4100
        asteroid_sprite.center_y = y
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1

    for y in range(0, 575, 64):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX, 5)
        asteroid_sprite.center_x = 4400
        asteroid_sprite.center_y = y
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1

    for y in range(700, 800, 64):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX, 5)
        asteroid_sprite.center_x = 4400
        asteroid_sprite.center_y = y
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1

    for y in range(0, 400, 64):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX, 5)
        asteroid_sprite.center_x = 4700
        asteroid_sprite.center_y = y
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1

    for y in range(525, 800, 64):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX, 5)
        asteroid_sprite.center_x = 4700
        asteroid_sprite.center_y = y
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1


def level_15(box_list, heart_list):
    for i in range(ROCK_COUNT_1 + 40):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX, 5)
        asteroid_sprite.center_x = random.randrange(SCREEN_WIDTH + 800) + 800
        asteroid_sprite.center_y = random.randrange(SCREEN_HEIGHT)
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1

    for i in range(HEART_COUNT_1):
        # image from dreamstime.com
        heart_sprite = Heart("heart.png", SPRITE_SCALING_HEART, 5)
        heart_placed = False
        while not heart_placed:

            heart_sprite.center_x = random.randrange(SCREEN_WIDTH + 800) + 800
            heart_sprite.center_y = random.randrange(SCREEN_HEIGHT)
            bad_hit_list = arcade.check_for_collision_with_list(heart_sprite,
                                                                box_list)
            if len(bad_hit_list) == 0:
                heart_placed = True
        heart_list.append(heart_sprite)


def level_16(box_list, heart_list):
    for i in range(ROCK_COUNT_1):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX, 6.5)
        asteroid_sprite.center_x = random.randrange(SCREEN_WIDTH + 800) + 800
        asteroid_sprite.center_y = random.randrange(SCREEN_HEIGHT)
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1

    for i in range(HEART_COUNT_1):
        # image from dreamstime.com
        heart_sprite = Heart("heart.png", SPRITE_SCALING_HEART, 6.5)
        heart_placed = False
        while not heart_placed:

            heart_sprite.center_x = random.randrange(SCREEN_WIDTH) + 800
            heart_sprite.center_y = random.randrange(SCREEN_HEIGHT)
            bad_hit_list = arcade.check_for_collision_with_list(heart_sprite,
                                                                box_list)
            if len(bad_hit_list) == 0:
                heart_placed = True
        heart_list.append(heart_sprite)


def level_17(box_list):
    for x in range(875, 1575, 64):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX, 6.5)
        asteroid_sprite.center_x = x
        asteroid_sprite.center_y = 500
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1

    for x in range(2325, 2650, 64):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX, 6.5)
        asteroid_sprite.center_x = x
        asteroid_sprite.center_y = 300
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1

    for x in range(2325, 2650, 64):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX, 6.5)
        asteroid_sprite.center_x = x
        asteroid_sprite.center_y = 500
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1

    for x in range(875, 1575, 64):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX, 6.5)
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
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX, 6.5)
        asteroid_sprite.center_x = coordinate[0] + 75
        asteroid_sprite.center_y = coordinate[1] - 50
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1


def level_18(box_list):
    for x in range(800, 1500, 64):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX, 6.5)
        asteroid_sprite.center_x = x
        asteroid_sprite.center_y = 550
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1

    for x in range(800, 1500, 64):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX, 6.5)
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
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX, 6.5)
        asteroid_sprite.center_x = coordinate[0]
        asteroid_sprite.center_y = coordinate[1]
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1


def level_19(box_list):
    for y in range(0, 200, 64):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX, 6.5)
        asteroid_sprite.center_x = 1400
        asteroid_sprite.center_y = y
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1

    for y in range(325, 800, 64):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX, 6.5)
        asteroid_sprite.center_x = 1400
        asteroid_sprite.center_y = y
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1

    for y in range(0, 600, 64):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX, 6.5)
        asteroid_sprite.center_x = 1700
        asteroid_sprite.center_y = y
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1

    for y in range(725, 800, 64):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX, 6.5)
        asteroid_sprite.center_x = 1700
        asteroid_sprite.center_y = y
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1

    for y in range(0, 75, 64):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX, 6.5)
        asteroid_sprite.center_x = 2000
        asteroid_sprite.center_y = y
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1

    for y in range(200, 800, 64):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX, 6.5)
        asteroid_sprite.center_x = 2000
        asteroid_sprite.center_y = y
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1

    for y in range(0, 250, 64):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX, 6.5)
        asteroid_sprite.center_x = 2300
        asteroid_sprite.center_y = y
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1

    for y in range(375, 800, 64):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX, 6.5)
        asteroid_sprite.center_x = 2300
        asteroid_sprite.center_y = y
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1

    for y in range(125, 800, 64):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX, 6.5)
        asteroid_sprite.center_x = 2600
        asteroid_sprite.center_y = y
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1

    for y in range(0, 675, 64):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX, 6.5)
        asteroid_sprite.center_x = 2900
        asteroid_sprite.center_y = y
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1

    for y in range(775, 800, 64):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX, 6.5)
        asteroid_sprite.center_x = 2900
        asteroid_sprite.center_y = y
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1

    for y in range(0, 350, 64):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX, 6.5)
        asteroid_sprite.center_x = 3200
        asteroid_sprite.center_y = y
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1

    for y in range(475, 800, 64):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX, 6.5)
        asteroid_sprite.center_x = 3200
        asteroid_sprite.center_y = y
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1

    for y in range(0, 100, 64):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX, 6.5)
        asteroid_sprite.center_x = 3500
        asteroid_sprite.center_y = y
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1

    for y in range(225, 600, 64):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX, 6.5)
        asteroid_sprite.center_x = 3500
        asteroid_sprite.center_y = y
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1

    for y in range(725, 800, 64):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX, 6.5)
        asteroid_sprite.center_x = 3500
        asteroid_sprite.center_y = y
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1

    for y in range(0, 750, 64):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX, 6.5)
        asteroid_sprite.center_x = 3800
        asteroid_sprite.center_y = y
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1

    for y in range(0, 125, 64):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX, 6.5)
        asteroid_sprite.center_x = 4100
        asteroid_sprite.center_y = y
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1

    for y in range(200, 800, 64):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX, 6.5)
        asteroid_sprite.center_x = 4100
        asteroid_sprite.center_y = y
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1

    for y in range(0, 575, 64):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX, 6.5)
        asteroid_sprite.center_x = 4400
        asteroid_sprite.center_y = y
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1

    for y in range(700, 800, 64):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX, 6.5)
        asteroid_sprite.center_x = 4400
        asteroid_sprite.center_y = y
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1

    for y in range(0, 400, 64):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX, 6.5)
        asteroid_sprite.center_x = 4700
        asteroid_sprite.center_y = y
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1

    for y in range(525, 800, 64):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX, 6.5)
        asteroid_sprite.center_x = 4700
        asteroid_sprite.center_y = y
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1


def level_20(box_list, heart_list):
    for i in range(ROCK_COUNT_1 + 40):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX, 6.5)
        asteroid_sprite.center_x = random.randrange(SCREEN_WIDTH + 800) + 800
        asteroid_sprite.center_y = random.randrange(SCREEN_HEIGHT)
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1

    for i in range(HEART_COUNT_1):
        # image from dreamstime.com
        heart_sprite = Heart("heart.png", SPRITE_SCALING_HEART, 6.5)
        heart_placed = False
        while not heart_placed:

            heart_sprite.center_x = random.randrange(SCREEN_WIDTH + 800) + 800
            heart_sprite.center_y = random.randrange(SCREEN_HEIGHT)
            bad_hit_list = arcade.check_for_collision_with_list(heart_sprite,
                                                                box_list)
            if len(bad_hit_list) == 0:
                heart_placed = True
        heart_list.append(heart_sprite)


def level_21(box_list, heart_list):
    for i in range(ROCK_COUNT_1):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX, 7.5)
        asteroid_sprite.center_x = random.randrange(SCREEN_WIDTH + 800) + 800
        asteroid_sprite.center_y = random.randrange(SCREEN_HEIGHT)
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1

    for i in range(HEART_COUNT_1):
        # image from dreamstime.com
        heart_sprite = Heart("heart.png", SPRITE_SCALING_HEART, 7.5)
        heart_placed = False
        while not heart_placed:

            heart_sprite.center_x = random.randrange(SCREEN_WIDTH) + 800
            heart_sprite.center_y = random.randrange(SCREEN_HEIGHT)
            bad_hit_list = arcade.check_for_collision_with_list(heart_sprite,
                                                                box_list)
            if len(bad_hit_list) == 0:
                heart_placed = True
        heart_list.append(heart_sprite)


def level_22(box_list):
    for x in range(875, 1575, 64):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX, 7.5)
        asteroid_sprite.center_x = x
        asteroid_sprite.center_y = 500
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1

    for x in range(2325, 2650, 64):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX, 7.5)
        asteroid_sprite.center_x = x
        asteroid_sprite.center_y = 300
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1

    for x in range(2325, 2650, 64):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX, 7.5)
        asteroid_sprite.center_x = x
        asteroid_sprite.center_y = 500
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1

    for x in range(875, 1575, 64):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX, 7.5)
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
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX, 7.5)
        asteroid_sprite.center_x = coordinate[0] + 75
        asteroid_sprite.center_y = coordinate[1] - 50
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1


def level_23(box_list):
    for x in range(800, 1500, 64):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX, 7.5)
        asteroid_sprite.center_x = x
        asteroid_sprite.center_y = 550
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1

    for x in range(800, 1500, 64):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX, 7.5)
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
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX, 7.5)
        asteroid_sprite.center_x = coordinate[0]
        asteroid_sprite.center_y = coordinate[1]
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1


def level_24(box_list):
    for y in range(0, 200, 64):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX, 7.5)
        asteroid_sprite.center_x = 1400
        asteroid_sprite.center_y = y
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1

    for y in range(325, 800, 64):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX, 7.5)
        asteroid_sprite.center_x = 1400
        asteroid_sprite.center_y = y
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1

    for y in range(0, 600, 64):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX, 7.5)
        asteroid_sprite.center_x = 1700
        asteroid_sprite.center_y = y
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1

    for y in range(725, 800, 64):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX, 7.5)
        asteroid_sprite.center_x = 1700
        asteroid_sprite.center_y = y
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1

    for y in range(0, 75, 64):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX, 7.5)
        asteroid_sprite.center_x = 2000
        asteroid_sprite.center_y = y
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1

    for y in range(200, 800, 64):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX, 7.5)
        asteroid_sprite.center_x = 2000
        asteroid_sprite.center_y = y
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1

    for y in range(0, 250, 64):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX, 7.5)
        asteroid_sprite.center_x = 2300
        asteroid_sprite.center_y = y
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1

    for y in range(375, 800, 64):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX, 7.5)
        asteroid_sprite.center_x = 2300
        asteroid_sprite.center_y = y
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1

    for y in range(125, 800, 64):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX, 7.5)
        asteroid_sprite.center_x = 2600
        asteroid_sprite.center_y = y
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1

    for y in range(0, 675, 64):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX, 7.5)
        asteroid_sprite.center_x = 2900
        asteroid_sprite.center_y = y
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1

    for y in range(775, 800, 64):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX, 7.5)
        asteroid_sprite.center_x = 2900
        asteroid_sprite.center_y = y
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1

    for y in range(0, 350, 64):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX, 7.5)
        asteroid_sprite.center_x = 3200
        asteroid_sprite.center_y = y
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1

    for y in range(475, 800, 64):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX, 7.5)
        asteroid_sprite.center_x = 3200
        asteroid_sprite.center_y = y
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1

    for y in range(0, 100, 64):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX, 7.5)
        asteroid_sprite.center_x = 3500
        asteroid_sprite.center_y = y
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1

    for y in range(225, 600, 64):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX, 7.5)
        asteroid_sprite.center_x = 3500
        asteroid_sprite.center_y = y
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1

    for y in range(725, 800, 64):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX, 7.5)
        asteroid_sprite.center_x = 3500
        asteroid_sprite.center_y = y
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1

    for y in range(0, 750, 64):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX, 7.5)
        asteroid_sprite.center_x = 3800
        asteroid_sprite.center_y = y
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1

    for y in range(0, 125, 64):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX, 7.5)
        asteroid_sprite.center_x = 4100
        asteroid_sprite.center_y = y
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1

    for y in range(200, 800, 64):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX, 7.5)
        asteroid_sprite.center_x = 4100
        asteroid_sprite.center_y = y
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1

    for y in range(0, 575, 64):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX, 7.5)
        asteroid_sprite.center_x = 4400
        asteroid_sprite.center_y = y
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1

    for y in range(700, 800, 64):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX, 7.5)
        asteroid_sprite.center_x = 4400
        asteroid_sprite.center_y = y
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1

    for y in range(0, 400, 64):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX, 7.5)
        asteroid_sprite.center_x = 4700
        asteroid_sprite.center_y = y
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1

    for y in range(525, 800, 64):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX, 7.5)
        asteroid_sprite.center_x = 4700
        asteroid_sprite.center_y = y
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1


def level_25(box_list, heart_list):
    for i in range(ROCK_COUNT_1 + 40):
        # image from nicepng.com
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX, 7.5)
        asteroid_sprite.center_x = random.randrange(SCREEN_WIDTH + 800) + 800
        asteroid_sprite.center_y = random.randrange(SCREEN_HEIGHT)
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1

    for i in range(HEART_COUNT_1):
        # image from dreamstime.com
        heart_sprite = Heart("heart.png", SPRITE_SCALING_HEART, 7.5)
        heart_placed = False
        while not heart_placed:

            heart_sprite.center_x = random.randrange(SCREEN_WIDTH + 800) + 800
            heart_sprite.center_y = random.randrange(SCREEN_HEIGHT)
            bad_hit_list = arcade.check_for_collision_with_list(heart_sprite,
                                                                box_list)
            if len(bad_hit_list) == 0:
                heart_placed = True
        heart_list.append(heart_sprite)


def level_26(box_list):
    coordinate_list = [[3225, 3350]]
    for coordinate in coordinate_list:
        asteroid_sprite = Box("asteroid.png", SPRITE_SCALING_BOX, 1)
        asteroid_sprite.center_x = coordinate[0]
        asteroid_sprite.center_y = coordinate[1]
        box_list.append(asteroid_sprite)
        asteroid_sprite.points_available = 1


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

        #Both sounds from opengameart.org
        self.rock_sound = arcade.load_sound("explosion.ogg")
        self.heart_sound = arcade.load_sound("heart.ogg")


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
        self.box_list.draw()
        self.heart_list.draw()

        if self.lives == 0:
            self.done = True

        output = "Score: " + str(self.score)
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)

        output_1 = "Lives: " + str(self.lives)
        arcade.draw_text(output_1, 10, 40, arcade.color.WHITE, 14)


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

        for heart in good_hit_list:
            self.lives += 1
            heart.remove_from_sprite_lists()
            arcade.play_sound(self.heart_sound)

        for rock in bad_hit_list:
            self.lives -= 1
            rock.remove_from_sprite_lists()
            arcade.play_sound(self.rock_sound)

        if self.lives <= 0:
            view = GameOverLossView(self.score)
            view.setup()
            self.window.show_view(view)
            pygame.mixer.music.stop()
            pygame.mixer.quit()

        if self.score == 25:
            view_1 = GameOverWinView()
            view_1.setup()
            self.window.show_view(view_1)
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
                self.level = 5
                self.score = 4

            elif advance_level and self.level == 5:
                level_6(self.box_list, self.heart_list)
                self.level = 6
                self.score = 5

            elif advance_level and self.level == 6:
                level_7(self.box_list)
                self.level = 7
                self.score = 6

            elif advance_level and self.level == 7:
                level_8(self.box_list)
                self.level = 8
                self.score = 7

            elif advance_level and self.level == 8:
                level_9(self.box_list)
                self.level = 9
                self.score = 8

            elif advance_level and self.level == 9:
                level_10(self.box_list, self.heart_list)
                self.level = 10
                self.score = 9

            elif advance_level and self.level == 10:
                level_11(self.box_list, self.heart_list)
                self.level = 11
                self.score = 10

            elif advance_level and self.level == 11:
                level_12(self.box_list)
                self.level = 12
                self.score = 11

            elif advance_level and self.level == 12:
                level_13(self.box_list)
                self.level = 13
                self.score = 12

            elif advance_level and self.level == 13:
                level_14(self.box_list)
                self.level = 14
                self.score = 13

            elif advance_level and self.level == 14:
                level_15(self.box_list, self.heart_list)
                self.level = 15
                self.score = 14

            elif advance_level and self.level == 15:
                level_16(self.box_list, self.heart_list)
                self.level = 16
                self.score = 15

            elif advance_level and self.level == 16:
                level_17(self.box_list)
                self.level = 17
                self.score = 16

            elif advance_level and self.level == 17:
                level_18(self.box_list)
                self.level = 18
                self.score = 17

            elif advance_level and self.level == 18:
                level_19(self.box_list)
                self.level = 19
                self.score = 18

            elif advance_level and self.level == 19:
                level_20(self.box_list, self.heart_list)
                self.level = 20
                self.score = 19

            elif advance_level and self.level == 20:
                level_21(self.box_list, self.heart_list)
                self.level = 21
                self.score = 20

            elif advance_level and self.level == 21:
                level_22(self.box_list)
                self.level = 22
                self.score = 21

            elif advance_level and self.level == 22:
                level_23(self.box_list)
                self.level = 23
                self.score = 22

            elif advance_level and self.level == 23:
                level_24(self.box_list)
                self.level = 24
                self.score = 23

            elif advance_level and self.level == 24:
                level_25(self.box_list, self.heart_list)
                self.level = 25
                self.score = 24

            elif advance_level and self.level == 25:
                level_26(self.box_list)
                self.level = 26
                self.score = 25

            for rock in self.box_list:
                if rock.right < 0:
                    rock.remove_from_sprite_lists()


class GameOverLossView(arcade.View):
    """ View to show when game is over """

    def __init__(self, score):
        """ This is run once when we switch to this view """
        super().__init__()

        self.texture = arcade.load_texture("space_background.jpg")

        # Reset the viewport, necessary if we have a scrolling game and we need
        # to reset the viewport back to the start so we can see what we draw.
        arcade.set_viewport(0, SCREEN_WIDTH - 1, 0, SCREEN_HEIGHT - 1)
        self.explosion_list = None
        self.score = score


    def setup(self):
        self.explosion_list = arcade.SpriteList()

        #image from hiclipart.com
        self.explosion_sprite = arcade.Sprite("explosion.png", SPRITE_SCALING_EXPLOSION)
        self.explosion_sprite.center_x = 480
        self.explosion_sprite.center_y = 370
        self.explosion_list.append(self.explosion_sprite)


    def on_draw(self):
        """ Draw this view """
        arcade.start_render()

        self.texture.draw_sized(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2,
                                SCREEN_WIDTH, SCREEN_HEIGHT)
        arcade.draw_text("You Exploded!", SCREEN_WIDTH / 2, SCREEN_HEIGHT - 150,
                         arcade.color.WHITE, font_size=45, anchor_x="center")
        arcade.draw_text(f"You Only Made it Through {self.score} Waves", SCREEN_WIDTH / 2, SCREEN_HEIGHT - 250,
                         arcade.color.WHITE, font_size=30, anchor_x="center")
        arcade.draw_text("Click to Play Again", SCREEN_WIDTH / 2, SCREEN_HEIGHT - 650,
                         arcade.color.WHITE, font_size=20, anchor_x="center")
        self.explosion_list.draw()


    def on_mouse_press(self, _x, _y, _button, _modifiers):
        """ If the user presses the mouse button, re-start the game. """
        game_view = GameView()
        game_view.setup()
        self.window.show_view(game_view)


class GameOverWinView(arcade.View):
    """ View to show when game is over """

    def __init__(self):
        """ This is run once when we switch to this view """
        super().__init__()

        self.score = None
        self.texture = arcade.load_texture("space_background.jpg")

        # Reset the viewport, necessary if we have a scrolling game and we need
        # to reset the viewport back to the start so we can see what we draw.
        arcade.set_viewport(0, SCREEN_WIDTH - 1, 0, SCREEN_HEIGHT - 1)
        self.flag_list = None

    def setup(self):
        self.flag_list = arcade.SpriteList()

        #image from shutterstock.com
        self.flag_sprite = arcade.Sprite("flag.png", SPRITE_SCALING_FLAG)
        self.flag_sprite.center_x = 500
        self.flag_sprite.center_y = 295
        self.flag_list.append(self.flag_sprite)

    def on_draw(self):
        """ Draw this view """
        arcade.start_render()
        self.texture.draw_sized(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2,
                                SCREEN_WIDTH, SCREEN_HEIGHT)
        arcade.draw_text("Congratulations", SCREEN_WIDTH / 2, SCREEN_HEIGHT - 150,
                         arcade.color.WHITE, font_size=45, anchor_x="center")
        arcade.draw_text("You Made it Through the Asteroid Field", SCREEN_WIDTH / 2, SCREEN_HEIGHT - 250,
                         arcade.color.WHITE, font_size=30, anchor_x="center")
        arcade.draw_text("You Survived 25 Waves", SCREEN_WIDTH / 2, SCREEN_HEIGHT - 350,
                         arcade.color.WHITE, font_size=30, anchor_x="center")
        arcade.draw_text("Click to Play Again", SCREEN_WIDTH / 2, SCREEN_HEIGHT - 650,
                         arcade.color.WHITE, font_size=20, anchor_x="center")
        self.flag_list.draw()


    def on_mouse_press(self, _x, _y, _button, _modifiers):
        """ If the user presses the mouse button, re-start the game. """
        game_view = GameView()
        game_view.setup()
        self.window.show_view(game_view)


def main():
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    start_view = InstructionView()
    window.show_view(start_view)
    arcade.run()


if __name__ == "__main__":
    main()