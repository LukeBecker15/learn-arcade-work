"""
Array Backed Grid version 2

Show how to use a two-dimensional list/array to back the display of a
grid on-screen.
"""
import arcade

# Set how many rows and columns we will have
ROW_COUNT = 10
COLUMN_COUNT = 10

# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 20
HEIGHT = 20

# This sets the margin between each cell
# and on the edges of the screen.
MARGIN = 5

# Do the math to figure out our screen dimensions
SCREEN_WIDTH = (WIDTH + MARGIN) * COLUMN_COUNT + MARGIN
SCREEN_HEIGHT = (HEIGHT + MARGIN) * ROW_COUNT + MARGIN


class MyGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self, width, height):
        """
        Set up the application.
        """
        super().__init__(width, height)

        # Create a 2 dimensional array. A two dimensional
        # array is simply a list of lists.
        self.grid = []
        for row in range(ROW_COUNT):
            # Add an empty array that will hold each cell
            # in this row
            self.grid.append([])
            for column in range(COLUMN_COUNT):
                self.grid[row].append(0)  # Append a cell

        arcade.set_background_color(arcade.color.BLACK)

        """ Create a list to hold buffered shapes, and load the list """
        self.grid_shape_list = None
        self.create_shapes_from_grid()

    def create_shapes_from_grid(self):
        """ This creates a list of buffered shapes, and loads the
        rectangles into that list for faster display. """
        self.grid_shape_list = arcade.ShapeElementList()

        for row in range(ROW_COUNT):
            for column in range(COLUMN_COUNT):

                # Figure out what color to draw the box
                if self.grid[row][column] == 1:
                    color = arcade.color.GREEN
                else:
                    color = arcade.color.WHITE

                # Figure where to put the box
                x = (MARGIN + WIDTH) * column + MARGIN + WIDTH // 2
                y = (MARGIN + HEIGHT) * row + MARGIN + HEIGHT // 2

                # Create the box and add to the list
                rectangle = arcade.create_rectangle_filled(x, y, WIDTH, HEIGHT, color)
                self.grid_shape_list.append(rectangle)

    def on_draw(self):
        """ Render the screen. """

        # This command has to happen before we start drawing
        arcade.start_render()

        self.grid_shape_list.draw()

    def on_mouse_press(self, x, y, button, modifiers):
        """ Called when the user presses a mouse button. """

        # Change the x/y screen coordinates to grid coordinates
        column = x // (WIDTH + MARGIN)
        row = y // (HEIGHT + MARGIN)

        print(f"Click coordinates: ({x}, {y}). Grid coordinates: ({row}, {column})")

        # Make sure we are on-grid. It is possible to click in the upper right
        # corner in the margin and go to a grid location that doesn't exist
        if row < ROW_COUNT and column < COLUMN_COUNT:

            # Flip the location between 1 and 0.
            if self.grid[row][column] == 0:
                self.grid[row][column] = 1

            elif self.grid[row][column] == 1:
                self.grid[row][column] = 0

            if x > WIDTH + MARGIN:
                if self.grid[row][column - 1] == 0:
                    self.grid[row][column - 1] = 1
                elif self.grid[row][column - 1] == 1:
                    self.grid[row][column - 1] = 0

            if x < SCREEN_WIDTH - WIDTH:
                if self.grid[row][column + 1] == 0:
                    self.grid[row][column + 1] = 1
                elif self.grid[row][column + 1] == 1:
                    self.grid[row][column + 1] = 0

            if y > HEIGHT + MARGIN:
                if self.grid[row - 1][column] == 0:
                    self.grid[row - 1][column] = 1
                elif self.grid[row - 1][column] == 1:
                    self.grid[row - 1][column] = 0

            if y < SCREEN_HEIGHT - HEIGHT:
                if self.grid[row + 1][column] == 0:
                    self.grid[row + 1][column] = 1
                elif self.grid[row + 1][column] == 1:
                    self.grid[row + 1][column] = 0

        self.create_shapes_from_grid()


        total_cells = 0

        for row_cells in range(ROW_COUNT):
            for column_cells in range(COLUMN_COUNT):
                if self.grid[row_cells][column_cells] == 1:
                    total_cells += 1

        print("Total of", total_cells, "cells are selected.")




        for row_cells in range(ROW_COUNT):
            row_total = 0
            continuous_count = 0
            for column_cells in range(COLUMN_COUNT):
                if self.grid[row_cells][column_cells] == 1:
                    row_total += 1
                    continuous_count += 1
                else:
                    if continuous_count > 2:
                        print("There are", continuous_count, "continuous blocks selected on row", row_cells)
                    continuous_count = 0

            if continuous_count > 2:
                print("There are", continuous_count, "continuous blocks selected on row", row_cells)
            print("Row", row_cells, "has", row_total, "cells selected.")



        for column_cells in range(COLUMN_COUNT):
            column_total = 0
            for row_cells in range(ROW_COUNT):
                if self.grid[row_cells][column_cells] == 1:
                    column_total += 1

            print("Column", column_cells, "has", column_total, "cells selected.")




def main():

    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()


if __name__ == "__main__":
    main()