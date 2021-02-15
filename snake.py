import pygame 
import random # This is to generate the apples x and y coordinates
import sys # Used to exit the system

pygame.init() # Initializing pygame

width, height = 600, 600 # Width and the height for the screen
closed = True # This variable tells the program if the user pressed the close button or not

# All of the rgb colors that are used in the game or for testing
white = (255, 255, 255)
blue = (0, 0, 255)
red = (255, 0, 0)
green = (0, 255, 0)
black = (0, 0, 0)

# Display
win = pygame.display.set_mode((width, height)) # Uses width and height
pygame.display.set_caption('Snake') # Setting the title to 'Snake'

icon = pygame.image.load('icon.png') # Load the image so it's a surface object
pygame.display.set_icon(icon) # Setting the icon

pygame.font.init() # Initialize the pygame font (used to show the score)
font = pygame.font.SysFont(None, 30) # Create a font object and make its font-size 30

def show_score(msg, color): # A show score function to display it on the top left corner
	score_text = font.render(msg, True, color)
	win.blit(score_text, (0, 0))


def draw_snake(snake_list): # Draws the snake with the given snake_list array
	for xny in snake_list:
		pygame.draw.rect(win, green, (xny[0], xny[1], 10, 10))



# This checks if the snake colided with it self
def check_if_col(head_x, head_y, snake_list): # It takes in the heads x and y because the head is the only thing that can possibly colide with the body
	check_list = [head_x, head_y] # Make a check list to see if its in any of the other coordinates in the snake_list
	if check_list in snake_list[1:]:
		return True


def get_direction(keys): # This gets the directions from W A S D and UP DOWN RIGHT LEFT arrow keys
	global switch

	if keys[pygame.K_a] or keys[pygame.K_LEFT]: # Left
		switch = 'LEFT'

	elif keys[pygame.K_d] or keys[pygame.K_RIGHT]: # Right
		switch = 'RIGHT'

	elif keys[pygame.K_w] or keys[pygame.K_UP]: # Up
		switch = 'UP'

	elif keys[pygame.K_s] or keys[pygame.K_DOWN]: # Down
		switch = 'DOWN'

# The main game loop
def game_loop():
	global switch
	global closed

	running = True
	snake_speed = 10
	snake_list = []
	snake_length = 10
	snake_growth = 1

	# We want the snake to spawn in the middle of the screen so divide the width and height by 2
	head_x = width // 2
	head_y = height // 2


	# Randomly generate the apples x and y
	apple_x = round(random.randint(0, width - snake_speed) // 10) * 10
	apple_y = round(random.randint(0, width - snake_speed) // 10) * 10

	# Fps count and clock rate
	fps = 15
	clock = pygame.time.Clock()

	# Direction the snake starts off with and where it switches to
	direction = 'RIGHT'
	switch = direction

	# The amount of apples the user has ate
	apples_eaten = 0

	# Check if its running and see if its closed
	while running and closed:
		clock.tick(fps)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				closed = False
				break

		# Set the background color to black
		win.fill(black)

		# Get all the keys that were pressed
		keys = pygame.key.get_pressed()


		# Make a head array
		snake_head = []

		# Get the heads x and y
		snake_head.append(head_x)
		snake_head.append(head_y)

		# Add it to the snake_list
		snake_list.append(snake_head)

		# Draw it out
		draw_snake(snake_list)

		# Draw the apple with its randomly generated x and y
		apple = pygame.draw.rect(win, red, (apple_x, apple_y, 10, 10))

		# Check if where the snake is going
		if switch == 'UP' and direction != 'DOWN': # If its up then we can't go down so set it to up
			direction = 'UP'

		if switch == 'DOWN' and direction != 'UP': # If its down then we can't go up so set it to down
			direction = 'DOWN'

		if switch == 'RIGHT' and direction != 'LEFT': # If its right then we can't go left so set it to right
			direction = 'RIGHT'

		if switch == 'LEFT' and direction != 'RIGHT': # If its left then we can't go right so set it to right
			direction = 'LEFT'


		if direction == 'RIGHT': # If its right then add to x
			head_x += snake_speed

		if direction == 'LEFT': # If its left then minus to x
			head_x -= snake_speed

		if direction == 'UP': # If its up then minus to y
			head_y -= snake_speed		

		if direction == 'DOWN': # If its down then add to y
			head_y += snake_speed


		if head_x >= width or head_x < 0 or head_y >= height or head_y < 0: # Check if the snake goes outside the screen
			game_loop()


		if head_x == apple_x and head_y == apple_y: # Check if the snake has eaten the apple
			apple_x = round(random.randint(0, width - snake_speed) // 10) * 10
			apple_y = round(random.randint(0, width - snake_speed) // 10) * 10
			snake_length += snake_growth
			apples_eaten += 1 # if so then add one to the amount of apples eaten


		if check_if_col(head_x, head_y, snake_list): # Check if the snake collided with itself
			game_loop()

		



		if len(snake_list) > snake_length: # If the length of the snake is greater than the length its meant to be, get rid of the head
			del snake_list[0]

		show_score('Score: ' + str(apples_eaten), red) # Show the score with the apples_eaten variable
		get_direction(keys) # Get the directions the snake is headed in

		pygame.display.update() # Keep updating the screen

game_loop()
pygame.quit() # Quit from pygame
sys.exit() # This terminates the background proccess for the game
