import pygame
import random
import sys
import json
import os

# Initialize Pygame
pygame.init()

# Constants
GRID_SIZE = 4
CELL_SIZE = 100
CELL_PADDING = 10
GRID_WIDTH = GRID_SIZE * CELL_SIZE + (GRID_SIZE + 1) * CELL_PADDING
GRID_HEIGHT = GRID_WIDTH
WINDOW_WIDTH = GRID_WIDTH
WINDOW_HEIGHT = GRID_HEIGHT + 100  # Extra space for score

# Colors
COLORS = {
    'background': (187, 173, 160),
    'grid_cell': (205, 193, 180),
    'text_dark': (119, 110, 101),
    'text_light': (249, 246, 242),
    0: (205, 193, 180),
    2: (238, 228, 218),
    4: (237, 224, 200),
    8: (242, 177, 121),
    16: (245, 149, 99),
    32: (246, 124, 95),
    64: (246, 94, 59),
    128: (237, 207, 114),
    256: (237, 204, 97),
    512: (237, 200, 80),
    1024: (237, 197, 63),
    2048: (237, 194, 46),
    4096: (237, 194, 46),
    8192: (237, 194, 46)
}

class Game2048:
    def __init__(self):
        self.grid = [[0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
        self.score = 0
        self.best_score = self.load_best_score()
        self.font = pygame.font.Font(None, 36)
        self.big_font = pygame.font.Font(None, 48)
        self.small_font = pygame.font.Font(None, 24)
        
        # Add initial tiles
        self.add_random_tile()
        self.add_random_tile()
    
    def load_best_score(self):
        """Load best score from file"""
        try:
            if os.path.exists('best_score.json'):
                with open('best_score.json', 'r') as f:
                    data = json.load(f)
                    return data.get('best_score', 0)
        except:
            pass
        return 0
    
    def save_best_score(self):
        """Save best score to file"""
        try:
            with open('best_score.json', 'w') as f:
                json.dump({'best_score': self.best_score}, f)
        except:
            pass
    
    def add_random_tile(self):
        """Add a random tile (2 or 4) to an empty cell"""
        empty_cells = []
        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                if self.grid[i][j] == 0:
                    empty_cells.append((i, j))
        
        if empty_cells:
            i, j = random.choice(empty_cells)
            self.grid[i][j] = 2 if random.random() < 0.9 else 4
    
    def move_left(self):
        """Move and merge tiles to the left"""
        moved = False
        new_grid = [[0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
        
        for i in range(GRID_SIZE):
            # Get non-zero values
            row = [val for val in self.grid[i] if val != 0]
            
            # Merge tiles
            j = 0
            while j < len(row):
                if j + 1 < len(row) and row[j] == row[j + 1]:
                    new_grid[i][j] = row[j] * 2
                    self.score += row[j] * 2
                    row.pop(j + 1)
                else:
                    new_grid[i][j] = row[j]
                j += 1
        
        # Check if anything moved
        if new_grid != self.grid:
            moved = True
            self.grid = new_grid
        
        return moved
    
    def move_right(self):
        """Move and merge tiles to the right"""
        # Reverse, move left, reverse back
        self.grid = [row[::-1] for row in self.grid]
        moved = self.move_left()
        self.grid = [row[::-1] for row in self.grid]
        return moved
    
    def move_up(self):
        """Move and merge tiles up"""
        # Transpose, move left, transpose back
        self.grid = list(map(list, zip(*self.grid)))
        moved = self.move_left()
        self.grid = list(map(list, zip(*self.grid)))
        return moved
    
    def move_down(self):
        """Move and merge tiles down"""
        # Transpose, move right, transpose back
        self.grid = list(map(list, zip(*self.grid)))
        moved = self.move_right()
        self.grid = list(map(list, zip(*self.grid)))
        return moved
    
    def is_game_over(self):
        """Check if game is over (no moves possible)"""
        # Check for empty cells
        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                if self.grid[i][j] == 0:
                    return False
        
        # Check for possible merges
        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                current = self.grid[i][j]
                # Check right neighbor
                if j < GRID_SIZE - 1 and self.grid[i][j + 1] == current:
                    return False
                # Check down neighbor
                if i < GRID_SIZE - 1 and self.grid[i + 1][j] == current:
                    return False
        
        return True
    
    def has_won(self):
        """Check if player has reached 2048"""
        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                if self.grid[i][j] >= 2048:
                    return True
        return False
    
    def reset_game(self):
        """Reset the game"""
        if self.score > self.best_score:
            self.best_score = self.score
            self.save_best_score()
        
        self.grid = [[0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
        self.score = 0
        self.add_random_tile()
        self.add_random_tile()
    
    def draw(self, screen):
        """Draw the game"""
        screen.fill(COLORS['background'])
        
        # Draw score
        score_text = self.font.render(f"Score: {self.score}", True, COLORS['text_dark'])
        best_text = self.font.render(f"Best: {self.best_score}", True, COLORS['text_dark'])
        screen.blit(score_text, (10, 10))
        screen.blit(best_text, (10, 50))
        
        # Draw instructions
        inst_text = self.small_font.render("Use WASD or Arrow Keys. R to restart", True, COLORS['text_dark'])
        screen.blit(inst_text, (WINDOW_WIDTH - 250, 10))
        
        # Draw grid
        start_x = CELL_PADDING
        start_y = 100
        
        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                x = start_x + j * (CELL_SIZE + CELL_PADDING)
                y = start_y + i * (CELL_SIZE + CELL_PADDING)
                
                value = self.grid[i][j]
                color = COLORS.get(value, COLORS[8192])
                
                # Draw cell
                pygame.draw.rect(screen, color, (x, y, CELL_SIZE, CELL_SIZE), border_radius=3)
                
                # Draw number
                if value != 0:
                    text_color = COLORS['text_light'] if value > 4 else COLORS['text_dark']
                    font_size = 48 if value < 100 else (36 if value < 1000 else 24)
                    font = pygame.font.Font(None, font_size)
                    text = font.render(str(value), True, text_color)
                    text_rect = text.get_rect(center=(x + CELL_SIZE // 2, y + CELL_SIZE // 2))
                    screen.blit(text, text_rect)
        
        # Draw game over message
        if self.is_game_over():
            overlay = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
            overlay.set_alpha(128)
            overlay.fill((0, 0, 0))
            screen.blit(overlay, (0, 0))
            
            game_over_text = self.big_font.render("GAME OVER", True, (255, 255, 255))
            restart_text = self.font.render("Press R to restart", True, (255, 255, 255))
            
            screen.blit(game_over_text, 
                       (WINDOW_WIDTH // 2 - game_over_text.get_width() // 2, 
                        WINDOW_HEIGHT // 2 - 50))
            screen.blit(restart_text, 
                       (WINDOW_WIDTH // 2 - restart_text.get_width() // 2, 
                        WINDOW_HEIGHT // 2 + 10))
        
        # Draw win message
        elif self.has_won():
            overlay = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
            overlay.set_alpha(128)
            overlay.fill((255, 215, 0))
            screen.blit(overlay, (0, 0))
            
            win_text = self.big_font.render("YOU WIN!", True, (255, 255, 255))
            continue_text = self.font.render("Continue playing or press R to restart", True, (255, 255, 255))
            
            screen.blit(win_text, 
                       (WINDOW_WIDTH // 2 - win_text.get_width() // 2, 
                        WINDOW_HEIGHT // 2 - 50))
            screen.blit(continue_text, 
                       (WINDOW_WIDTH // 2 - continue_text.get_width() // 2, 
                        WINDOW_HEIGHT // 2 + 10))

def main():
    """Main game loop"""
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("2048")
    clock = pygame.time.Clock()
    
    game = Game2048()
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            elif event.type == pygame.KEYDOWN:
                moved = False
                
                if event.key in [pygame.K_LEFT, pygame.K_a]:
                    moved = game.move_left()
                elif event.key in [pygame.K_RIGHT, pygame.K_d]:
                    moved = game.move_right()
                elif event.key in [pygame.K_UP, pygame.K_w]:
                    moved = game.move_up()
                elif event.key in [pygame.K_DOWN, pygame.K_s]:
                    moved = game.move_down()
                elif event.key == pygame.K_r:
                    game.reset_game()
                    moved = False  # Don't add tile after reset
                
                if moved and not game.is_game_over():
                    game.add_random_tile()
        
        game.draw(screen)
        pygame.display.flip()
        clock.tick(60)
    
    # Save best score before quitting
    if game.score > game.best_score:
        game.best_score = game.score
        game.save_best_score()
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
