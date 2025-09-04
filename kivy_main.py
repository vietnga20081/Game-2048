from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.graphics import Color, Rectangle, RoundedRectangle
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.metrics import dp
from kivy.animation import Animation
from kivy.core.audio import SoundLoader
import random
import json
import os

# Colors for different tile values
TILE_COLORS = {
    0: (0.8, 0.76, 0.71, 1),      # Empty cell
    2: (0.93, 0.89, 0.85, 1),     # Light
    4: (0.93, 0.88, 0.78, 1),
    8: (0.95, 0.69, 0.47, 1),     # Orange
    16: (0.96, 0.58, 0.39, 1),
    32: (0.96, 0.49, 0.37, 1),
    64: (0.96, 0.37, 0.23, 1),    # Red
    128: (0.93, 0.81, 0.45, 1),   # Yellow
    256: (0.93, 0.8, 0.38, 1),
    512: (0.93, 0.78, 0.31, 1),
    1024: (0.93, 0.77, 0.25, 1),
    2048: (0.93, 0.76, 0.18, 1),  # Gold
    4096: (0.24, 0.24, 0.24, 1),  # Dark
}

class TileWidget(Widget):
    def __init__(self, value=0, **kwargs):
        super(TileWidget, self).__init__(**kwargs)
        self.value = value
        self.label = Label(
            text=str(value) if value > 0 else '',
            font_size='20sp',
            color=(0.47, 0.43, 0.4, 1) if value <= 4 else (0.98, 0.96, 0.95, 1),
            bold=True
        )
        self.add_widget(self.label)
        
        with self.canvas.before:
            self.color = Color(*TILE_COLORS.get(value, TILE_COLORS[4096]))
            self.rect = RoundedRectangle(
                pos=self.pos,
                size=self.size,
                radius=[dp(3)]
            )
        
        self.bind(pos=self.update_graphics, size=self.update_graphics)
    
    def update_graphics(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size
        self.label.center = self.center
        
        # Adjust font size based on number length
        if self.value >= 1000:
            self.label.font_size = '16sp'
        elif self.value >= 100:
            self.label.font_size = '18sp'
        else:
            self.label.font_size = '20sp'
    
    def set_value(self, value):
        if self.value != value:
            self.value = value
            self.label.text = str(value) if value > 0 else ''
            
            # Update color
            self.color.rgba = TILE_COLORS.get(value, TILE_COLORS[4096])
            
            # Update text color
            self.label.color = (0.47, 0.43, 0.4, 1) if value <= 4 else (0.98, 0.96, 0.95, 1)
            
            # Animate tile appearance
            if value > 0:
                anim = Animation(opacity=0, duration=0.1) + Animation(opacity=1, duration=0.1)
                anim.start(self)

class GameBoard(GridLayout):
    def __init__(self, **kwargs):
        super(GameBoard, self).__init__(**kwargs)
        self.cols = 4
        self.rows = 4
        self.spacing = dp(5)
        self.padding = dp(10)
        
        # Initialize game state
        self.grid = [[0 for _ in range(4)] for _ in range(4)]
        self.tiles = []
        
        # Create tile widgets
        for i in range(16):
            tile = TileWidget()
            self.tiles.append(tile)
            self.add_widget(tile)
        
        # Add initial tiles
        self.add_random_tile()
        self.add_random_tile()
        self.update_display()
    
    def add_random_tile(self):
        empty_cells = []
        for i in range(4):
            for j in range(4):
                if self.grid[i][j] == 0:
                    empty_cells.append((i, j))
        
        if empty_cells:
            i, j = random.choice(empty_cells)
            self.grid[i][j] = 2 if random.random() < 0.9 else 4
    
    def update_display(self):
        for i in range(4):
            for j in range(4):
                tile_index = i * 4 + j
                self.tiles[tile_index].set_value(self.grid[i][j])
    
    def move_left(self):
        moved = False
        score_gained = 0
        new_grid = [[0 for _ in range(4)] for _ in range(4)]
        
        for i in range(4):
            row = [val for val in self.grid[i] if val != 0]
            
            j = 0
            while j < len(row):
                if j + 1 < len(row) and row[j] == row[j + 1]:
                    new_grid[i][j] = row[j] * 2
                    score_gained += row[j] * 2
                    row.pop(j + 1)
                else:
                    new_grid[i][j] = row[j]
                j += 1
        
        if new_grid != self.grid:
            moved = True
            self.grid = new_grid
        
        return moved, score_gained
    
    def move_right(self):
        self.grid = [row[::-1] for row in self.grid]
        moved, score = self.move_left()
        self.grid = [row[::-1] for row in self.grid]
        return moved, score
    
    def move_up(self):
        self.grid = list(map(list, zip(*self.grid)))
        moved, score = self.move_left()
        self.grid = list(map(list, zip(*self.grid)))
        return moved, score
    
    def move_down(self):
        self.grid = list(map(list, zip(*self.grid)))
        moved, score = self.move_right()
        self.grid = list(map(list, zip(*self.grid)))
        return moved, score
    
    def is_game_over(self):
        # Check for empty cells
        for i in range(4):
            for j in range(4):
                if self.grid[i][j] == 0:
                    return False
        
        # Check for possible merges
        for i in range(4):
            for j in range(4):
                current = self.grid[i][j]
                if j < 3 and self.grid[i][j + 1] == current:
                    return False
                if i < 3 and self.grid[i + 1][j] == current:
                    return False
        
        return True
    
    def has_won(self):
        for i in range(4):
            for j in range(4):
                if self.grid[i][j] >= 2048:
                    return True
        return False
    
    def reset_game(self):
        self.grid = [[0 for _ in range(4)] for _ in range(4)]
        self.add_random_tile()
        self.add_random_tile()
        self.update_display()

class Game2048Widget(BoxLayout):
    def __init__(self, **kwargs):
        super(Game2048Widget, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.spacing = dp(10)
        self.padding = dp(20)
        
        # Game state
        self.score = 0
        self.best_score = self.load_best_score()
        self.game_won = False
        self.game_over = False
        
        # Header with scores
        header = BoxLayout(orientation='horizontal', size_hint_y=None, height=dp(60))
        
        self.score_label = Label(
            text=f'Score: {self.score}',
            font_size='18sp',
            bold=True,
            color=(0.47, 0.43, 0.4, 1)
        )
        
        self.best_label = Label(
            text=f'Best: {self.best_score}',
            font_size='18sp',
            bold=True,
            color=(0.47, 0.43, 0.4, 1)
        )
        
        header.add_widget(self.score_label)
        header.add_widget(self.best_label)
        
        # Game board
        self.board = GameBoard()
        
        # Control buttons
        controls = BoxLayout(orientation='horizontal', size_hint_y=None, height=dp(50))
        
        self.restart_btn = Button(
            text='Restart',
            size_hint_x=0.5,
            background_color=(0.93, 0.69, 0.47, 1)
        )
        self.restart_btn.bind(on_press=self.restart_game)
        
        controls.add_widget(self.restart_btn)
        controls.add_widget(Widget())  # Spacer
        
        # Instructions
        instructions = Label(
            text='Swipe to move tiles. Combine tiles with same numbers to reach 2048!',
            font_size='14sp',
            text_size=(None, None),
            halign='center',
            color=(0.47, 0.43, 0.4, 1),
            size_hint_y=None,
            height=dp(40)
        )
        
        # Add all widgets
        self.add_widget(header)
        self.add_widget(self.board)
        self.add_widget(controls)
        self.add_widget(instructions)
        
        # Touch handling
        self.touch_start = None
        
        # Keyboard binding (for desktop)
        Window.bind(on_keyboard=self.on_keyboard)
        
        # Background color
        with self.canvas.before:
            Color(0.98, 0.96, 0.95, 1)
            self.bg = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self.update_bg, pos=self.update_bg)
    
    def update_bg(self, *args):
        self.bg.size = self.size
        self.bg.pos = self.pos
    
    def load_best_score(self):
        try:
            if os.path.exists('best_score.json'):
                with open('best_score.json', 'r') as f:
                    data = json.load(f)
                    return data.get('best_score', 0)
        except:
            pass
        return 0
    
    def save_best_score(self):
        try:
            with open('best_score.json', 'w') as f:
                json.dump({'best_score': self.best_score}, f)
        except:
            pass
    
    def on_keyboard(self, window, key, *args):
        # Handle keyboard input for desktop
        moved = False
        score_gained = 0
        
        if key == 97 or key == 276:  # 'a' or left arrow
            moved, score_gained = self.board.move_left()
        elif key == 100 or key == 275:  # 'd' or right arrow
            moved, score_gained = self.board.move_right()
        elif key == 119 or key == 273:  # 'w' or up arrow
            moved, score_gained = self.board.move_up()
        elif key == 115 or key == 274:  # 's' or down arrow
            moved, score_gained = self.board.move_down()
        elif key == 114:  # 'r' for restart
            self.restart_game()
            return True
        
        if moved:
            self.make_move(score_gained)
        
        return True
    
    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            self.touch_start = touch.pos
            return True
        return super(Game2048Widget, self).on_touch_down(touch)
    
    def on_touch_up(self, touch):
        if self.touch_start and self.collide_point(*touch.pos):
            # Calculate swipe direction
            dx = touch.pos[0] - self.touch_start[0]
            dy = touch.pos[1] - self.touch_start[1]
            
            if abs(dx) > abs(dy) and abs(dx) > dp(30):
                # Horizontal swipe
                if dx > 0:
                    moved, score_gained = self.board.move_right()
                else:
                    moved, score_gained = self.board.move_left()
            elif abs(dy) > dp(30):
                # Vertical swipe
                if dy > 0:
                    moved, score_gained = self.board.move_up()
                else:
                    moved, score_gained = self.board.move_down()
            else:
                moved = False
                score_gained = 0
            
            if moved:
                self.make_move(score_gained)
            
            self.touch_start = None
            return True
        
        return super(Game2048Widget, self).on_touch_up(touch)
    
    def make_move(self, score_gained):
        # Update score
        self.score += score_gained
        if self.score > self.best_score:
            self.best_score = self.score
            self.save_best_score()
        
        self.score_label.text = f'Score: {self.score}'
        self.best_label.text = f'Best: {self.best_score}'
        
        # Add new tile
        if not self.board.is_game_over():
            self.board.add_random_tile()
        
        # Update display
        self.board.update_display()
        
        # Check game status
        if self.board.has_won() and not self.game_won:
            self.game_won = True
            # Could show win dialog here
            
        if self.board.is_game_over():
            self.game_over = True
            # Could show game over dialog here
    
    def restart_game(self, *args):
        self.score = 0
        self.game_won = False
        self.game_over = False
        self.score_label.text = f'Score: {self.score}'
        self.board.reset_game()

class Game2048App(App):
    def build(self):
        self.title = '2048'
        return Game2048Widget()
    
    def on_start(self):
        # Set window size for desktop
        if Window.size[0] < 400:
            Window.size = (400, 600)

if __name__ == '__main__':
    Game2048App().run()
