import tkinter as tk
import random

WIDTH = 400
HEIGHT = 400
CELL_SIZE = 20

class SnakeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Snake (tkinter)")

        self.canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="black")
        self.canvas.pack()

        self.snake = [(100, 100), (80, 100), (60, 100)]
        self.snake_dir = (CELL_SIZE, 0)
        self.food = self.place_food()
        self.running = True
        self.score = 0

        self.root.bind("<KeyPress>", self.change_direction)
        self.update_game()

    def place_food(self):
        x = random.randrange(0, WIDTH, CELL_SIZE)
        y = random.randrange(0, HEIGHT, CELL_SIZE)
        return (x, y)

    def change_direction(self, event):
        key = event.keysym
        if key == "Up" and self.snake_dir != (0, CELL_SIZE):
            self.snake_dir = (0, -CELL_SIZE)
        elif key == "Down" and self.snake_dir != (0, -CELL_SIZE):
            self.snake_dir = (0, CELL_SIZE)
        elif key == "Left" and self.snake_dir != (CELL_SIZE, 0):
            self.snake_dir = (-CELL_SIZE, 0)
        elif key == "Right" and self.snake_dir != (-CELL_SIZE, 0):
            self.snake_dir = (CELL_SIZE, 0)

    def update_game(self):
        if not self.running:
            return

        new_head = (self.snake[0][0] + self.snake_dir[0],
                    self.snake[0][1] + self.snake_dir[1])

        if (new_head[0] < 0 or new_head[0] >= WIDTH or
            new_head[1] < 0 or new_head[1] >= HEIGHT or
            new_head in self.snake):
            self.running = False
            self.canvas.create_text(WIDTH//2, HEIGHT//2, text="GAME OVER",
                                    fill="red", font=("Arial", 24))
            return

        self.snake.insert(0, new_head)

        if new_head == self.food:
            self.score += 1
            self.food = self.place_food()
        else:
            self.snake.pop()

        self.draw()
        self.root.after(120, self.update_game)

    def draw(self):
        self.canvas.delete("all")

        x, y = self.food
        self.canvas.create_rectangle(x, y, x+CELL_SIZE, y+CELL_SIZE,
                                    fill="red")

        for i, (x, y) in enumerate(self.snake):
            color = "green" if i > 0 else "lime"
            self.canvas.create_rectangle(x, y, x+CELL_SIZE, y+CELL_SIZE,
                                        fill=color)

        self.canvas.create_text(40, 10, text=f"Score: {self.score}",
                                fill="white", font=("Arial", 12))

root = tk.Tk()
game = SnakeGame(root)
root.mainloop()