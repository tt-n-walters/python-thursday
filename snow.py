import curses
from random import randint


class Screen:
    def __init__(self):
        self.screen = curses.initscr()
        curses.noecho()             # Stop user input being written in the terminal
        curses.curs_set(0)          # Hide the cursor
        self.screen.timeout(100)    # Set the time until __getch__ is cancelled automatically
        self.rows, self.columns = self.screen.getmaxyx()
        self.snowflakes = [[None for _ in range(self.columns)] for _ in range(self.rows)]


    def update(self):
        # Create a new snowflake
        column = randint(0, self.columns - 2)
        new_snowflake = Snowflake(0, column)
        self.snowflakes[0][column] = new_snowflake

        self.updated_snowflakes = [[None for _ in range(self.columns)] for _ in range(self.rows)]
        # Iterate over all snowflakes, and run their fall function.
        for row in self.snowflakes:
            for snowflake in row:
                if not snowflake == None:
                    if snowflake.row < self.rows - 1 and self.snowflakes[snowflake.row + 1][snowflake.column] == None:
                        self.updated_snowflakes[snowflake.row][snowflake.column] = None
                        snowflake.fall()
                        self.updated_snowflakes[snowflake.row][snowflake.column] = snowflake
                    else:
                        self.updated_snowflakes[snowflake.row][snowflake.column] = snowflake
        
        self.snowflakes = self.updated_snowflakes



    def draw(self):
        # Set up our draw loop, controlled by character input
        # Ctrl-C will exit the loop.
        while not self.screen.getch() == 3:
            # with open("snow.log", "w") as file:
                self.update()
                self.screen.clear()

                # Iterate over all snowflakes, and run their draw function.

                number_drawn = 0
                for row in self.snowflakes:
                    for snowflake in row:
                        if not snowflake == None:
                            number_drawn += 1
                            # file.write("Drawing {} {} at {} {}\n".format(number_drawn, snowflake.id, snowflake.row, snowflake.column))
                            snowflake.draw(self.screen)



class Snowflake:
    number_of_snowflakes = 0

    def __init__(self, row, column):
        self.id = Snowflake.number_of_snowflakes
        Snowflake.number_of_snowflakes += 1
        self.row = row
        self.column = column
    
    def draw(self, screen):
        screen.addch(self.row, self.column, "*")
        screen.refresh()
    
    def fall(self):
        self.row = self.row + 1


Screen().draw()


'''
row = 0
col = 30


height, width = screen.getmaxyx()

while not screen.getch() == 3:
    screen.clear()
    screen.addch(row, col, "*")

    if row < height - 1:
        row += 1
'''