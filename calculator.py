import pygame
import math

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Calculator")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
DARK_GRAY = (100, 100, 100)
BLUE = (0, 120, 255)

# Fonts
FONT = pygame.font.Font(None, 40)
LARGE_FONT = pygame.font.Font(None, 60)

# Calculator state
current_input = ""
history = ""

# Button layout
buttons = [
    {"label": "7", "x": 20, "y": 200}, {"label": "8", "x": 110, "y": 200}, {"label": "9", "x": 200, "y": 200}, {"label": "/", "x": 290, "y": 200},
    {"label": "4", "x": 20, "y": 280}, {"label": "5", "x": 110, "y": 280}, {"label": "6", "x": 200, "y": 280}, {"label": "*", "x": 290, "y": 280},
    {"label": "1", "x": 20, "y": 360}, {"label": "2", "x": 110, "y": 360}, {"label": "3", "x": 200, "y": 360}, {"label": "-", "x": 290, "y": 360},
    {"label": "0", "x": 20, "y": 440}, {"label": ".", "x": 110, "y": 440}, {"label": "=", "x": 200, "y": 440}, {"label": "+", "x": 290, "y": 440},
    {"label": "C", "x": 20, "y": 520}, {"label": "%", "x": 110, "y": 520}, {"label": "\u221A", "x": 200, "y": 520}, {"label": "^", "x": 290, "y": 520},
]

def draw_text(text, x, y, font, color=BLACK):
    """Draw text on the screen."""
    render = font.render(text, True, color)
    screen.blit(render, (x, y))

def draw_buttons():
    """Draw calculator buttons."""
    for button in buttons:
        pygame.draw.rect(screen, GRAY, (button["x"], button["y"], 80, 60), border_radius=5)
        draw_text(button["label"], button["x"] + 25, button["y"] + 15, FONT)

def evaluate_expression(expression):
    """Safely evaluate a mathematical expression."""
    try:
        return str(eval(expression))
    except Exception:
        return "Error"

# Main loop
running = True
while running:
    screen.fill(WHITE)

    # Draw display
    pygame.draw.rect(screen, DARK_GRAY, (20, 20, 360, 160), border_radius=5)
    draw_text(history, 30, 30, FONT, WHITE)
    draw_text(current_input, 30, 100, LARGE_FONT, WHITE)

    # Draw buttons
    draw_buttons()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            for button in buttons:
                if button["x"] < mouse_x < button["x"] + 80 and button["y"] < mouse_y < button["y"] + 60:
                    label = button["label"]
                    if label == "C":
                        current_input = ""
                        history = ""
                    elif label == "=":
                        history = current_input
                        current_input = evaluate_expression(current_input)
                    elif label == "\u221A":
                        try:
                            current_input = str(math.sqrt(float(current_input)))
                        except Exception:
                            current_input = "Error"
                    elif label == "^":
                        current_input += "**"
                    else:
                        current_input += label

    pygame.display.flip()

pygame.quit()
