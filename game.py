import pygame
import os
import image

# Windows caption
pygame.display.set_caption("Catch Money")

# Set display width and height
screen_width = 3840  # 4K width
screen_height = 2160  # 4K height

# Create a Pygame screen (fullscreen)
screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)

# Get the center coordinates of the screen
center_x = screen_width // 2
center_y = screen_height // 2

# Set the window position to center it on the screen
os.environ['SDL_VIDEO_WINDOW_POS'] = f"{center_x - (screen_width // 2)}," \
                                    f"{center_y - (screen_height // 2)}"

# Windows background
background = image.load("BACKGROUND.jpg", size = (screen_width, screen_height), convert ="default")

while True:



    
    image.draw(screen, background, (screen_width//2 , screen_width//2))

    pygame.display.update()