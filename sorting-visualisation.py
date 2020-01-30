import arcade
from sorting import data, bubble


def map_value(value, prev_min, prev_max, new_min, new_max):
    previous_range = prev_max - prev_min
    new_range = new_max - new_min
    position_of_value = (value - prev_min) / previous_range
    new_value = position_of_value * new_range
    return new_value + new_min


class Window(arcade.Window):
    def __init__(self):
        super().__init__(800, 500, "Bubble Sort Visualisation")
        arcade.set_background_color(arcade.color.WHITE)

        # self.bars = []
        # for d in data:
        #     self.bars.append(Bar(self.width / len(data), d))

        self.bars = [Bar(
            self.width / len(data),
            map_value(d, 0, 100, 50, self.height)
            ) for d in data]
        self.j = 0
        self.i = 0

    def on_draw(self):
        arcade.start_render()
        for i, bar in enumerate(self.bars):
            bar.set_x_position(i * bar.width)
            bar.draw()
    
    def on_update(self, delta_time):
        self.j, self.i = bubble(self.bars, self.j, self.i)


class Bar(arcade.Sprite):
    def __init__(self, width, height):
        super().__init__("blue.png")
        self.width = width
        self.height = height
        self.bottom = 0

    def set_x_position(self, left):
        self.left = left

    def __gt__(self, other):
        return self.height > other.height



Window()
arcade.run()
