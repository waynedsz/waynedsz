from graphix import Line, Point, Window, Polygon, Rectangle

# layout and colouring(3):
# p design is the arrow
# f design is the lines

def get_patch_colour(i, j, win_factor, colours):
    if i == win_factor // 2 or j == win_factor // 2:
        return colours[1]
    elif (i < win_factor // 2 and j < win_factor // 2) or (i > win_factor // 2 and j > win_factor // 2):
        return colours[0]
    else:
        return colours[2]
    
def draw_patch_work(win_factor, win, colours):
    y = -100
    for i in range(win_factor):
        x = 0
        y += 100
        for j in range(win_factor):
            colour = get_patch_colour(i, j, win_factor, colours)
            if j % 2 == 0:
                draw_line_patch(win, x, y, colour)
            elif win_factor - 1 >  i > 0 and j % 2 == 1:
                draw_arrow_patch(win, win_factor, x, y, colour)
            else:
                draw_blank_patch(win, x, y, colour)
            x += 100

def draw_line_patch(win, x, y, colour):
    br_x = x + 100
    br_y = y + 100
    for i in range(10):
        line = Line(Point(x, y), Point(br_x, br_y))
        line.outline_colour = colour
        line.draw(win)
        x += 10
        br_x -= 10
    for i in range(10):
        line = Line(Point(x, y), Point(br_x, br_y))
        line.outline_colour = colour
        line.draw(win)
        y += 10
        br_y -= 10

def get_single_arrow(win, tl_x, tl_y, tm_x, tm_y, tr_x, colour):
    points = [Point(tl_x, tl_y), Point(tm_x, tm_y), Point(tr_x, tl_y), Point(tr_x, tl_y + 10), Point(tm_x, tm_y + 10), Point(tl_x, tl_y + 10)]
    arrow = Polygon(points)
    arrow.fill_colour = colour
    arrow.outline_colour = colour
    return arrow
         
def draw_arrow_patch(win, win_factor, x, y, colour):
    y -= 10
    x += 100
    for i in range(5):
        x -= 100
        y += 20
        for j in range(5):
            arrow = get_single_arrow(win, x, y, x + 10, y - 10, x + 20, colour)
            if win_factor - 1 > i > 0 and j % 2 == 1:
                arrow.fill_colour = "white"
            arrow.draw(win)
            x += 20

def draw_blank_patch(win, x, y, colour):
    rect = Rectangle(Point(x, y), Point(x + 100, y + 100))
    rect.fill_colour = colour
    rect.outline_colour = colour
    rect.draw(win)
    
def get_win_factor():
    sizes = [5, 7, 9]
    while True:
        win_factor = input("Enter the window size (5,7,9): ")
        if win_factor.isdigit() and int(win_factor) in sizes:
            break 
        else:
            print("Invalid. Enter a valid window size.")
    return int(win_factor)
   
def get_colours():
    valid_colours = ["red", "green", "orange", "magenta", "blue", "purple"]
    colours = []
    while len(colours) != 3:
        colour = input("Enter 3 colours for the patchwork (blue, green, red, orange, magenta, purple): ").lower()
        if colour in valid_colours and colour not in colours:
            colours.append(colour)
        else:
            print("Invalid. Enter only the appropriate colours and do not repeat them.")
    return colours

def main():
    win_factor = get_win_factor()
    colours = get_colours()
    win = Window("Coursework", 100 * win_factor, 100 * win_factor)
    draw_patch_work(win_factor, win, colours)

main()