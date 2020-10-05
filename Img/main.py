import tkinter as tk
from random import randint
H = 300
W = 300


class Ball():

    def __init__(self):
        self.R = randint(20, 30)
        self.x = randint(self.R, W - self.R)
        self.y = randint(self.R, H - self.R)
        self.dx, self.dy = (+1, +1)

        self.ball_id = canvas.create_oval(self.x - self.R,
                                          self.y - self.R,
                                          self.x + self.R,
                                          self.x + self.R, fill='red',outline='white')
        #self.ball_id = canvas.create_oval(10, 10, 90, 90, fill='red', outline='white')

    def move(self):
        self.x += self.dx
        self.y += self.dy

        if self.y + self.R > H or self.y - self.R <= 0:
            self.dy = -self.dy
        if self.x + self.R > W or self.x - self.R <= 0:
            self.dx = -self.dx


    def draw(self):
        canvas.move(self.ball_id, self.x, self.y)


    def check_mouse_coord(self):
        pass

def tick():
    ball.move()
    ball.draw()

    root.after(200, tick)
    print(ball.x, ball.y, ball.dx, ball.dy)

def canvas_click_handler(event):
    print(event.x,event.y)

def main():
    global root, canvas, ball
    root = tk.Tk()
    root.geometry(str(W)+'x'+str(H))

    # создали канву
    canvas = tk.Canvas(root)
    canvas.pack(anchor="nw",  fill=tk.BOTH)
    canvas.bind('<Button-1>', canvas_click_handler)

    # создали шарик
    ball = Ball()

    tick()
    root.mainloop()


if __name__ == '__main__':
    main()

