import turtle
import random


class Shape:
    def __init__(self, sides, length, angle, pos, color, thickness):
        self.sides = sides
        self.length = length
        self.angle = angle
        self.pos = pos
        self.color = color
        self.thickness = thickness

    def render(self):
        turtle.penup()
        turtle.goto(self.pos[0], self.pos[1])
        turtle.setheading(self.angle)
        turtle.pensize(self.thickness)
        turtle.color(self.color)
        turtle.pendown()

        for _ in range(self.sides):
            turtle.forward(self.length)
            turtle.left(360 / self.sides)

        turtle.penup()

def random_rgb():
    return (
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255)
    )

def random_position():
    return [
        random.randint(-300, 300),
        random.randint(-250, 250)
    ]

def draw_single(sides):
    length = random.randint(30, 150)
    angle = random.randint(0, 360)
    color = random_rgb()
    width = random.randint(1, 6)
    pos = random_position()

    Shape(sides, length, angle, pos, color, width).render()


class ArtMaker:
    def __init__(self):
        turtle.bgcolor("black")
        turtle.speed(0)
        turtle.colormode(255)
        turtle.tracer(0)

    def repeated(self, count, callback):
        for _ in range(count):
            callback()

    def triangles(self):
        self.repeated(35, lambda: draw_single(3))

    def squares(self):
        self.repeated(35, lambda: draw_single(4))

    def pentagons(self):
        self.repeated(35, lambda: draw_single(5))

    def mixed_basic(self):
        self.repeated(40, lambda: draw_single(random.choice([3, 4, 5])))

    def nested(self, sides, min_layers=3, max_layers=6):
        base = random.randint(60, 150)
        angle = random.randint(0, 360)
        pos = random_position()
        col = random_rgb()
        layers = random.randint(min_layers, max_layers)

        size = base
        for i in range(layers):
            width = 3 if i == 0 else 1
            Shape(sides, size, angle, pos, col, width).render()

            size *= 0.7
            angle += random.randint(-12, 12)

    def nested_tri(self):
        for _ in range(30):
            self.nested(3, 3, 5)

    def nested_sq(self):
        for _ in range(30):
            self.nested(4, 4, 6)

    def nested_penta(self):
        for _ in range(30):
            self.nested(5, 4, 6)

    def nested_mix(self):
        for _ in range(30):
            self.nested(random.choice([3, 4, 5]), 4, 6)

    def free_mix(self):
        for _ in range(40):
            draw_single(random.choice([3, 4, 5]))



def main():
    print("\nChoose an art pattern:")
    print("1. Triangles")
    print("2. Squares")
    print("3. Pentagons")
    print("4. Mixed basic polygons")
    print("5. Nested triangles")
    print("6. Nested squares")
    print("7. Nested pentagons")
    print("8. Mixed nested polygons")
    print("9. Free mixed pattern")

    choice = int(input("\nEnter choice (1–9): "))

    art = ArtMaker()

    actions = {
        1: art.triangles,
        2: art.squares,
        3: art.pentagons,
        4: art.mixed_basic,
        5: art.nested_tri,
        6: art.nested_sq,
        7: art.nested_penta,
        8: art.nested_mix,
        9: art.free_mix
    }

    if choice in actions:
        actions[choice]()
    else:
        print("Invalid option.")
        return

    turtle.update()
    turtle.done()


main()