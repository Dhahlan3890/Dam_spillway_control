import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up font
font = pygame.font.Font(None, 36)
font1 = pygame.font.Font(None, 26)
font2 = pygame.font.Font(None, 20)

# Constants
WIDTH, HEIGHT = 1000, 500
BLUE = (0, 0, 255)
SILVER = (192, 192, 192)
GRAY = (255/2, 255/2, 255/2)
RED = (255,0,0)
GREEN = (100,255,0)


box1_color = SILVER
box2_color = SILVER
box3_color = SILVER
box4_color = SILVER
box5_color = SILVER
box6_color = SILVER
box7_color = SILVER
box8_color = SILVER

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Blue Box Game")

# Create the blue box
box_width, box_height = 400, 437.95
box1_width, box1_height = 40, 95
box2_width, box2_height = 40, 95
box3_width, box3_height = 40, 95
box4_width, box4_height = 40, 95
box5_width, box5_height = 40, 95
box6_width, box6_height = 40, 95
box7_width, box7_height = 40, 95
box8_width, box8_height = 40, 95
ls_width, ls_height = 40, 40
box_x, box_y = (WIDTH - box_width) // 2, HEIGHT - box_height - 20
box1_x, box1_y = (WIDTH - box1_width-350) // 2, HEIGHT - box1_height - 300
box2_x, box2_y = (WIDTH - box2_width-250) // 2, HEIGHT - box2_height - 300
box3_x, box3_y = (WIDTH - box3_width-150) // 2, HEIGHT - box3_height - 300
box4_x, box4_y = (WIDTH - box4_width-50) // 2, HEIGHT - box4_height - 300
box5_x, box5_y = (WIDTH - box5_width +50) // 2, HEIGHT - box5_height - 300
box6_x, box6_y = (WIDTH - box6_width +150) // 2, HEIGHT - box6_height - 300
box7_x, box7_y = (WIDTH - box7_width +250) // 2, HEIGHT - box7_height - 300
box8_x, box8_y = (WIDTH - box8_width +350) // 2, HEIGHT - box8_height - 300



#########################################################

water_fall_start1 = -500
water_fall_start2 = -500
water_fall_start3 = -500
water_fall_start4 = -500
water_fall_start5 = -500
water_fall_start6 = -500
water_fall_start7 = -500
water_fall_start8 = -500

class Droplet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((1, 5))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.velocity = random.randint(1, 15)

    def update(self):
        self.rect.y += self.velocity
        if self.rect.y > 1000:
            self.rect.y = box1_y +95
            x_values = [random.randint(water_fall_start1, water_fall_start1+box1_width),
                        random.randint(water_fall_start2, water_fall_start2+box1_width),
                         random.randint(water_fall_start3, water_fall_start3+box1_width),
                          random.randint(water_fall_start4, water_fall_start4+box1_width),
                           random.randint(water_fall_start5, water_fall_start5+box1_width),
                            random.randint(water_fall_start6, water_fall_start6+box1_width),
                             random.randint(water_fall_start7, water_fall_start7+box1_width),
                              random.randint(water_fall_start8, water_fall_start8+box1_width) ]
            self.rect.x = random.choice(x_values)



# Create sprite groups
all_sprites = pygame.sprite.Group()

# Create droplets
for _ in range(20000):
    droplet = Droplet(random.randint(0, 0), random.randint(100, HEIGHT))
    all_sprites.add(droplet)



##############################################################

# Set up clock to control the frame rate
clock = pygame.time.Clock()

L1,L2,L3,L4,L5,L6,L7,L8,L9,L10,L11,L12,L13,L14,L15,L16,L17,L18,L19,L20,L21,L22,L23,L24,L25,L26,L27,L28,L29,L30,L31,L32 = [RED]*32

# Main game loop
while True:

#################################################################################

    """"

    L1,L2,L3,L4,L5,L6,L7,L8,L9,L10,L11,L12,L13,L14,L15,L16,L17,L18,L19,L20,L21,L22,L23,L24,L25,L26,L27,L28,L29,L30,L31,L32 = [RED]*32

    if box_height > 438.65:
        L1, L3,L2,L5, L4,L7, L6, L9, L8, L11, L10, L13, L12, L15, L14, L17, L16, L19, L18, L21, L20, L23, L22, L25, L24, L27, L26, L29, L28, L31, L30, L32 = [GREEN] * 32
        #print("gate L32 opened")
    elif box_height > 438.61:
        L1, L3,L2,L5, L4,L7, L6, L9, L8, L11, L10, L13, L12, L15, L14, L17, L16, L19, L18, L21, L20, L23, L22, L25, L24, L27, L26, L29, L28, L31, L30 = [GREEN] * 31
        #print("gate L30 opened")
    elif box_height > 438.60:
        L1, L3,L2,L5, L4,L7, L6, L9, L8, L11, L10, L13, L12, L15, L14, L17, L16, L19, L18, L21, L20, L23, L22, L25, L24, L27, L26, L29, L28, L31 = [GREEN] * 30
        #print("gate L31 opened")
    elif box_height > 438.57:
        L1, L3,L2,L5, L4,L7, L6, L9, L8, L11, L10, L13, L12, L15, L14, L17, L16, L19, L18, L21, L20, L23, L22, L25, L24, L27, L26, L29, L28 = [GREEN] * 29
        #print("gate L28 opened")
    elif box_height > 438.56:
        L1, L3,L2,L5, L4,L7, L6, L9, L8, L11, L10, L13, L12, L15, L14, L17, L16, L19, L18, L21, L20, L23, L22, L25, L24, L27, L26, L29 = [GREEN] * 28
        #print("gate L29 opened")
    elif box_height > 438.53:
        L1, L3,L2,L5, L4,L7, L6, L9, L8, L11, L10, L13, L12, L15, L14, L17, L16, L19, L18, L21, L20, L23, L22, L25, L24, L27, L26 = [GREEN] * 27
        #print("gate L26 opened")
    elif box_height > 438.52:
        L1, L3,L2,L5, L4,L7, L6, L9, L8, L11, L10, L13, L12, L15, L14, L17, L16, L19, L18, L21, L20, L23, L22, L25, L24, L27 = [GREEN] * 26
        #print("gate L27 opened")
    elif box_height > 438.49:
        L1, L3,L2,L5, L4,L7, L6, L9, L8, L11, L10, L13, L12, L15, L14, L17, L16, L19, L18, L21, L20, L23, L22, L25, L24 = [GREEN] * 25
        #print("gate L24 opened")
    elif box_height > 438.48:
        L1, L3,L2,L5, L4,L7, L6, L9, L8, L11, L10, L13, L12, L15, L14, L17, L16, L19, L18, L21, L20, L23, L22, L25 = [GREEN] * 24
        #print("gate L25 opened")
    elif box_height > 438.45:
        L1, L3,L2,L5, L4,L7, L6, L9, L8, L11, L10, L13, L12, L15, L14, L17, L16, L19, L18, L21, L20, L23, L22 = [GREEN] * 23
        #print("gate L22 opened")
    elif box_height > 438.44:
        L1, L3,L2,L5, L4,L7, L6, L9, L8, L11, L10, L13, L12, L15, L14, L17, L16, L19, L18, L21, L20, L23 = [GREEN] * 22
        #print("gate L23 opened")
    elif box_height > 438.41:
        L1, L3,L2,L5, L4,L7, L6, L9, L8, L11, L10, L13, L12, L15, L14, L17, L16, L19, L18, L21, L20 = [GREEN] * 21
        #print("gate L20 opened")
    elif box_height > 438.40:
        L1, L3,L2,L5, L4,L7, L6, L9, L8, L11, L10, L13, L12, L15, L14, L17, L16, L19, L18, L21 = [GREEN] * 20
        #print("gate L21 opened")
    elif box_height > 438.37:
        L1, L3,L2,L5, L4,L7, L6, L9, L8, L11, L10, L13, L12, L15, L14, L17, L16, L19, L18 = [GREEN] * 19
        #print("gate L18 opened")
    elif box_height > 438.36:
        L1, L3,L2,L5, L4,L7, L6, L9, L8, L11, L10, L13, L12, L15, L14, L17, L16, L19 = [GREEN] * 18
        #print("gate L19 opened")
    elif box_height > 438.33:
        L1, L3,L2,L5, L4,L7, L6, L9, L8, L11, L10, L13, L12, L15, L14, L17, L16 = [GREEN] * 17
        #print("gate L16 opened")
    elif box_height > 438.32:
        L1, L3,L2,L5, L4,L7, L6, L9, L8, L11, L10, L13, L12, L15, L14, L17 = [GREEN] * 16
        #print("gate L17 opened")
    elif box_height > 438.29:
        L1, L3,L2,L5, L4,L7, L6, L9, L8, L11, L10, L13, L12, L15, L14 = [GREEN] * 15
        #print("gate L14 opened")
    elif box_height > 438.28:
        L1, L3,L2,L5, L4,L7, L6, L9, L8, L11, L10, L13, L12, L15 = [GREEN] * 14
        #print("gate L15 opened")
    elif box_height > 438.25:
        L1, L3,L2,L5, L4,L7, L6, L9, L8, L11, L10, L13, L12 = [GREEN] * 13
        #print("gate L12 opened")
    elif box_height > 438.24:
        L1, L3,L2,L5, L4,L7, L6, L9, L8, L11, L10, L13 = [GREEN] * 12
        #print("gate L13 opened")
    elif box_height > 438.21:
        L1, L3,L2,L5, L4,L7, L6, L9, L8, L11, L10 = [GREEN] * 11
        #print("gate L10 opened")
    elif box_height > 438.20:
        L1, L3,L2,L5, L4,L7, L6, L9, L8, L11 = [GREEN] * 10
        #print("gate L11 opened")
    elif box_height > 438.17:
        L1, L3,L2,L5, L4,L7, L6, L9, L8 = [GREEN] * 9
        #print("gate L8 opened")
    elif box_height > 438.16:
        L1, L3,L2,L5, L4,L7, L6, L9 = [GREEN] * 8
        #print("gate L9 opened")
    elif box_height > 438.13:
        L1, L3,L2,L5, L4,L7, L6 = [GREEN] * 7
        #print("gate L6 opened")
    elif box_height > 438.12:
        L1, L3,L2,L5, L4,L7 = [GREEN] * 6
        #print("gate L7 opened")
    elif box_height > 438.09:
        L1, L3,L2,L5, L4 = [GREEN] * 5
        #print("gate L4 opened")
    elif box_height > 438.08:
        L1, L3,L2,L5 = [GREEN] * 4
        #print("gate L5 opened")
    elif box_height > 438.05:
        L1, L3,L2 = [GREEN] * 3
        #print("gate L2 opened")
    elif box_height > 438.04:
        L1, L3 = [GREEN] * 2
        #print("gate L3 opened")
    elif box_height > 438:
        L1 = GREEN
        #print("gate L1 opened")


    """
            
        
        
        
        

        

    

#########################################################################################

    water_fall_start1 = -500
    water_fall_start2 = -500
    water_fall_start3 = -500
    water_fall_start4 = -500
    water_fall_start5 = -500
    water_fall_start6 = -500
    water_fall_start7 = -500
    water_fall_start8 = -500


    box1_level, box2_level, box3_level, box4_level, box5_level, box6_level, box7_level, box8_level = 0,0,0,0,0,0,0,0


    if box_height > 438.04:
        box4_level, box5_level = 7, 7
        water_fall_start4 = box4_x
        water_fall_start5 = box5_x

    if box_height > 438.08:
        box3_level, box6_level = 7, 7
        water_fall_start3 = box3_x
        water_fall_start6 = box6_x

    if box_height > 438.12:
        box2_level, box7_level = 7, 7
        water_fall_start2 = box2_x
        water_fall_start7 = box7_x

    if box_height > 438.16:
        box1_level, box8_level = 7, 7
        water_fall_start1 = box1_x
        water_fall_start8 = box8_x

    if box_height > 438.20:
        box4_level, box5_level = 25, 25

    if box_height > 438.24:
        box3_level, box6_level = 25, 25

    if box_height > 438.28:
        box2_level, box7_level = 25, 25

    if box_height > 438.32:
        box1_level, box8_level = 25, 25

    if box_height > 438.36:
        box4_level, box5_level = 47, 47

    if box_height > 438.40:
        box3_level, box6_level = 47, 47

    if box_height > 438.44:
        box2_level, box7_level = 47, 47

    if box_height > 438.48:
        box1_level, box8_level = 47, 47

    if box_height > 438.52:
        box4_level, box5_level = 95, 95

    if box_height > 438.56:
        box3_level, box6_level = 95, 95

    if box_height > 438.60:
        box2_level, box7_level = 95, 95

    if box_height > 438.64:
        box1_level, box8_level = 95, 95



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    # Increase the height of the box when the up arrow key is pressed
    if keys[pygame.K_UP]:
        box_y -= 0.001
        box_height += 0.001


        if box_height > 438.65:
            L1, L3,L2,L5, L4,L7, L6, L9, L8, L11, L10, L13, L12, L15, L14, L17, L16, L19, L18, L21, L20, L23, L22, L25, L24, L27, L26, L29, L28, L31, L30, L32 = [BLUE] * 32
            #print("gate L32 opened")
        elif box_height > 438.61:
            L1, L3,L2,L5, L4,L7, L6, L9, L8, L11, L10, L13, L12, L15, L14, L17, L16, L19, L18, L21, L20, L23, L22, L25, L24, L27, L26, L29, L28, L31, L30 = [BLUE] * 31
            #print("gate L30 opened")
        elif box_height > 438.60:
            L1, L3,L2,L5, L4,L7, L6, L9, L8, L11, L10, L13, L12, L15, L14, L17, L16, L19, L18, L21, L20, L23, L22, L25, L24, L27, L26, L29, L28, L31 = [BLUE] * 30
            #print("gate L31 opened")
        elif box_height > 438.57:
            L1, L3,L2,L5, L4,L7, L6, L9, L8, L11, L10, L13, L12, L15, L14, L17, L16, L19, L18, L21, L20, L23, L22, L25, L24, L27, L26, L29, L28 = [BLUE] * 29
            #print("gate L28 opened")
        elif box_height > 438.56:
            L1, L3,L2,L5, L4,L7, L6, L9, L8, L11, L10, L13, L12, L15, L14, L17, L16, L19, L18, L21, L20, L23, L22, L25, L24, L27, L26, L29 = [BLUE] * 28
            #print("gate L29 opened")
        elif box_height > 438.53:
            L1, L3,L2,L5, L4,L7, L6, L9, L8, L11, L10, L13, L12, L15, L14, L17, L16, L19, L18, L21, L20, L23, L22, L25, L24, L27, L26 = [BLUE] * 27
            #print("gate L26 opened")
        elif box_height > 438.52:
            L1, L3,L2,L5, L4,L7, L6, L9, L8, L11, L10, L13, L12, L15, L14, L17, L16, L19, L18, L21, L20, L23, L22, L25, L24, L27 = [BLUE] * 26
            #print("gate L27 opened")
        elif box_height > 438.49:
            L1, L3,L2,L5, L4,L7, L6, L9, L8, L11, L10, L13, L12, L15, L14, L17, L16, L19, L18, L21, L20, L23, L22, L25, L24 = [BLUE] * 25
            #print("gate L24 opened")
        elif box_height > 438.48:
            L1, L3,L2,L5, L4,L7, L6, L9, L8, L11, L10, L13, L12, L15, L14, L17, L16, L19, L18, L21, L20, L23, L22, L25 = [BLUE] * 24
            #print("gate L25 opened")
        elif box_height > 438.45:
            L1, L3,L2,L5, L4,L7, L6, L9, L8, L11, L10, L13, L12, L15, L14, L17, L16, L19, L18, L21, L20, L23, L22 = [BLUE] * 23
            #print("gate L22 opened")
        elif box_height > 438.44:
            L1, L3,L2,L5, L4,L7, L6, L9, L8, L11, L10, L13, L12, L15, L14, L17, L16, L19, L18, L21, L20, L23 = [BLUE] * 22
            #print("gate L23 opened")
        elif box_height > 438.41:
            L1, L3,L2,L5, L4,L7, L6, L9, L8, L11, L10, L13, L12, L15, L14, L17, L16, L19, L18, L21, L20 = [BLUE] * 21
            #print("gate L20 opened")
        elif box_height > 438.40:
            L1, L3,L2,L5, L4,L7, L6, L9, L8, L11, L10, L13, L12, L15, L14, L17, L16, L19, L18, L21 = [BLUE] * 20
            #print("gate L21 opened")
        elif box_height > 438.37:
            L1, L3,L2,L5, L4,L7, L6, L9, L8, L11, L10, L13, L12, L15, L14, L17, L16, L19, L18 = [BLUE] * 19
            #print("gate L18 opened")
        elif box_height > 438.36:
            L1, L3,L2,L5, L4,L7, L6, L9, L8, L11, L10, L13, L12, L15, L14, L17, L16, L19 = [BLUE] * 18
            #print("gate L19 opened")
        elif box_height > 438.33:
            L1, L3,L2,L5, L4,L7, L6, L9, L8, L11, L10, L13, L12, L15, L14, L17, L16 = [BLUE] * 17
            #print("gate L16 opened")
        elif box_height > 438.32:
            L1, L3,L2,L5, L4,L7, L6, L9, L8, L11, L10, L13, L12, L15, L14, L17 = [BLUE] * 16
            #print("gate L17 opened")
        elif box_height > 438.29:
            L1, L3,L2,L5, L4,L7, L6, L9, L8, L11, L10, L13, L12, L15, L14 = [BLUE] * 15
            #print("gate L14 opened")
        elif box_height > 438.28:
            L1, L3,L2,L5, L4,L7, L6, L9, L8, L11, L10, L13, L12, L15 = [BLUE] * 14
            #print("gate L15 opened")
        elif box_height > 438.25:
            L1, L3,L2,L5, L4,L7, L6, L9, L8, L11, L10, L13, L12 = [BLUE] * 13
            #print("gate L12 opened")
        elif box_height > 438.24:
            L1, L3,L2,L5, L4,L7, L6, L9, L8, L11, L10, L13 = [BLUE] * 12
            #print("gate L13 opened")
        elif box_height > 438.21:
            L1, L3,L2,L5, L4,L7, L6, L9, L8, L11, L10 = [BLUE] * 11
            #print("gate L10 opened")
        elif box_height > 438.20:
            L1, L3,L2,L5, L4,L7, L6, L9, L8, L11 = [BLUE] * 10
            #print("gate L11 opened")
        elif box_height > 438.17:
            L1, L3,L2,L5, L4,L7, L6, L9, L8 = [BLUE] * 9
            #print("gate L8 opened")
        elif box_height > 438.16:
            L1, L3,L2,L5, L4,L7, L6, L9 = [BLUE] * 8
            #print("gate L9 opened")
        elif box_height > 438.13:
            L1, L3,L2,L5, L4,L7, L6 = [BLUE] * 7
            #print("gate L6 opened")
        elif box_height > 438.12:
            L1, L3,L2,L5, L4,L7 = [BLUE] * 6
            #print("gate L7 opened")
        elif box_height > 438.09:
            L1, L3,L2,L5, L4 = [BLUE] * 5
            #print("gate L4 opened")
        elif box_height > 438.08:
            L1, L3,L2,L5 = [BLUE] * 4
            #print("gate L5 opened")
        elif box_height > 438.05:
            L1, L3,L2 = [BLUE] * 3
            #print("gate L2 opened")
        elif box_height > 438.04:
            L1, L3 = [BLUE] * 2
            #print("gate L3 opened")
        elif box_height > 438:
            L1 = BLUE
            #print("gate L1 opened")



    if keys[pygame.K_DOWN]:
        box_y += 0.001
        box_height -= 0.001


        if box_height <= 437.98:
            L1, L3, L2, L5, L4, L7, L6, L9, L8, L11, L10, L13, L12, L15, L14, L17, L16, L19, L18, L21, L20, L23, L22, L25, L24, L27, L26, L29, L28, L31, L30, L32 =[RED] * 32
            #print("gate L1 closed")
        elif box_height <= 438.02:
            L3, L2, L5, L4, L7, L6, L9, L8, L11, L10, L13, L12, L15, L14, L17, L16, L19, L18, L21, L20, L23, L22, L25, L24, L27, L26, L29, L28, L31, L30, L32 = [RED] * 31
            #print("gate L3 closed")
        elif box_height <= 438.03:
            L2, L5, L4, L7, L6, L9, L8, L11, L10, L13, L12, L15, L14, L17, L16, L19, L18, L21, L20, L23, L22, L25, L24, L27, L26, L29, L28, L31, L30, L32 = [RED] * 30
            #print("gate L2 closed")
        elif box_height <= 438.06:
            L5, L4, L7, L6, L9, L8, L11, L10, L13, L12, L15, L14, L17, L16, L19, L18, L21, L20, L23, L22, L25, L24, L27, L26, L29, L28, L31, L30, L32 = [RED] * 29
            #print("gate L5 closed")
        elif box_height <= 438.07:
            L4, L7, L6, L9, L8, L11, L10, L13, L12, L15, L14, L17, L16, L19, L18, L21, L20, L23, L22, L25, L24, L27, L26, L29, L28, L31, L30, L32 = [RED] * 28
            #print("gate L4 closed")
        elif box_height <= 438.10:
            L7, L6, L9, L8, L11, L10, L13, L12, L15, L14, L17, L16, L19, L18, L21, L20, L23, L22, L25, L24, L27, L26, L29, L28, L31, L30, L32 = [RED] * 27
            #print("gate L7 closed")
        elif box_height <= 438.11:
            L6, L9, L8, L11, L10, L13, L12, L15, L14, L17, L16, L19, L18, L21, L20, L23, L22, L25, L24, L27, L26, L29, L28, L31, L30, L32 = [RED] * 26
            #print("gate L6 closed")
        elif box_height <= 438.14:
            L9, L8, L11, L10, L13, L12, L15, L14, L17, L16, L19, L18, L21, L20, L23, L22, L25, L24, L27, L26, L29, L28, L31, L30, L32 = [RED] * 25
            #print("gate L9 closed")
        elif box_height <= 438.15:
            L8, L11, L10, L13, L12, L15, L14, L17, L16, L19, L18, L21, L20, L23, L22, L25, L24, L27, L26, L29, L28, L31, L30, L32 = [RED] * 24
            #print("gate L8 closed")
        elif box_height <= 438.18:
            L11, L10, L13, L12, L15, L14, L17, L16, L19, L18, L21, L20, L23, L22, L25, L24, L27, L26, L29, L28, L31, L30, L32 = [RED] * 23
            #print("gate L11 closed")
        elif box_height <= 438.19:
            L10, L13, L12, L15, L14, L17, L16, L19, L18, L21, L20, L23, L22, L25, L24, L27, L26, L29, L28, L31, L30, L32 = [RED] * 22
            #print("gate L10 closed")
        elif box_height <= 438.22:
            L13, L12, L15, L14, L17, L16, L19, L18, L21, L20, L23, L22, L25, L24, L27, L26, L29, L28, L31, L30, L32 = [RED] * 21
            #print("gate L13 closed")
        elif box_height <= 438.23:
            L12, L15, L14, L17, L16, L19, L18, L21, L20, L23, L22, L25, L24, L27, L26, L29, L28, L31, L30, L32 = [RED] * 20
            #print("gate L12 closed")
        elif box_height <= 438.26:
            L15, L14, L17, L16, L19, L18, L21, L20, L23, L22, L25, L24, L27, L26, L29, L28, L31, L30, L32 = [RED] * 19
            #print("gate L15 closed")
        elif box_height <= 438.27:
            L14, L17, L16, L19, L18, L21, L20, L23, L22, L25, L24, L27, L26, L29, L28, L31, L30, L32 = [RED] * 18
            #print("gate L14 closed")
        elif box_height <= 438.30:
            L17, L16, L19, L18, L21, L20, L23, L22, L25, L24, L27, L26, L29, L28, L31, L30, L32 = [RED] * 17
            #print("gate L17 closed")
        elif box_height <= 438.31:
            L16, L19, L18, L21, L20, L23, L22, L25, L24, L27, L26, L29, L28, L31, L30, L32 = [RED] * 16
            #print("gate L16 closed")
        elif box_height <= 438.34:
            L19, L18, L21, L20, L23, L22, L25, L24, L27, L26, L29, L28, L31, L30, L32 = [RED] * 15
            #print("gate L19 closed")
        elif box_height <= 438.35:
            L18, L21, L20, L23, L22, L25, L24, L27, L26, L29, L28, L31, L30, L32 = [RED] * 14
            #print("gate L18 closed")
        elif box_height <= 438.38:
            L21, L20, L23, L22, L25, L24, L27, L26, L29, L28, L31, L30, L32 = [RED] * 13
            #print("gate L21 closed")
        elif box_height <= 438.39:
            L20, L23, L22, L25, L24, L27, L26, L29, L28, L31, L30, L32 = [RED] * 12
            #print("gate L20 closed")
        elif box_height <= 438.42:
            L23, L22, L25, L24, L27, L26, L29, L28, L31, L30, L32 = [RED] * 11
            #print("gate L23 closed")
        elif box_height <= 438.43:
            L22, L25, L24, L27, L26, L29, L28, L31, L30, L32 = [RED] * 10
            #print("gate L22 closed")
        elif box_height <= 438.46:
            L25, L24, L27, L26, L29, L28, L31, L30, L32 = [RED] * 9
            #print("gate L25 closed")
        elif box_height <= 438.47:
            L24, L27, L26, L29, L28, L31, L30, L32 = [RED] *8
            #print("gate L24 closed")
        elif box_height <= 438.50:
            L27, L26, L29, L28, L31, L30, L32 = [RED] *7
            #print("gate L27 closed")
        elif box_height <= 438.51:
            L26, L29, L28, L31, L30, L32 = [RED] *6
            #print("gate L26 closed")
        elif box_height <= 438.54:
            L29, L28, L31, L30, L32 = [RED] *5
            #print("gate L29 closed")
        elif box_height <= 438.55:
            L28, L31, L30, L32 = [RED] *4
            #print("gate L28 closed")
        elif box_height <= 438.58:
            L31, L30, L32 = [RED] *3
            #print("gate L31 closed")
        elif box_height <= 438.59:
            L30, L32 = [RED] *2
            #print("gate L30 closed")
        elif box_height <= 438.63:
            L32 = RED
            #print("gate L32 closed")

    
    # Clear the screen
    screen.fill((255, 255, 255))

    # Draw the blue box
    
    pygame.draw.rect(screen, GRAY, (box_x, box_y, box_width, box_height))
    pygame.draw.rect(screen, box1_color, (box1_x, box1_y, box1_width, box1_height))
    height_text1 = font1.render(f"{box1_level/10:.1f}", True, (0, 0, 0))
    screen.blit(height_text1, (box1_x, box1_y-20))
    pygame.draw.rect(screen, BLUE, (box1_x, box1_y + 95-box1_level, box1_width, box1_level))
    pygame.draw.rect(screen, box2_color, (box2_x, box2_y, box2_width, box2_height))
    height_text2 = font1.render(f"{box2_level/10:.1f}", True, (0, 0, 0))
    screen.blit(height_text2, (box2_x, box2_y-20))
    pygame.draw.rect(screen, BLUE, (box2_x, box1_y + 95-box2_level, box1_width, box2_level))
    pygame.draw.rect(screen, box3_color, (box3_x, box3_y, box3_width, box3_height))
    height_text3 = font1.render(f"{box3_level/10:.1f}", True, (0, 0, 0))
    screen.blit(height_text3, (box3_x, box3_y-20))
    pygame.draw.rect(screen, BLUE, (box3_x, box1_y + 95-box3_level, box1_width, box3_level))
    pygame.draw.rect(screen, box4_color, (box4_x, box4_y, box4_width, box4_height))
    height_text4 = font1.render(f"{box4_level/10:.1f}", True, (0, 0, 0))
    screen.blit(height_text4, (box4_x, box4_y-20))
    pygame.draw.rect(screen, BLUE, (box4_x, box1_y + 95-box4_level, box1_width, box4_level))
    pygame.draw.rect(screen, box4_color, (box5_x, box5_y, box5_width, box5_height))
    height_text5 = font1.render(f"{box5_level/10:.1f}", True, (0, 0, 0))
    screen.blit(height_text5, (box5_x, box5_y-20))
    pygame.draw.rect(screen, BLUE, (box5_x, box1_y + 95-box5_level, box1_width, box5_level))
    pygame.draw.rect(screen, box4_color, (box6_x, box6_y, box6_width, box6_height))
    height_text6 = font1.render(f"{box6_level/10:.1f}", True, (0, 0, 0))
    screen.blit(height_text6, (box6_x, box6_y-20))
    pygame.draw.rect(screen, BLUE, (box6_x, box1_y + 95-box6_level, box1_width, box6_level))
    pygame.draw.rect(screen, box4_color, (box7_x, box7_y, box7_width, box7_height))
    height_text7 = font1.render(f"{box7_level/10:.1f}", True, (0, 0, 0))
    screen.blit(height_text7, (box7_x, box7_y-20))
    pygame.draw.rect(screen, BLUE, (box7_x, box1_y + 95-box7_level, box1_width, box7_level))
    pygame.draw.rect(screen, box4_color, (box8_x, box8_y, box8_width, box8_height))
    height_text8 = font1.render(f"{box8_level/10:.1f}", True, (0, 0, 0))
    screen.blit(height_text8, (box8_x, box8_y-20))
    pygame.draw.rect(screen, BLUE, (box8_x, box1_y + 95-box8_level, box1_width, box8_level))

    pygame.draw.rect(screen, L1, (750, 50, ls_width, ls_height))
    pygame.draw.rect(screen, L2, (750+50*1, 50, ls_width, ls_height))
    pygame.draw.rect(screen, L3, (750+50*2, 50, ls_width, ls_height))
    pygame.draw.rect(screen, L4, (750+50*3, 50, ls_width, ls_height))
    pygame.draw.rect(screen, L5, (750+50*4, 50, ls_width, ls_height))
    pygame.draw.rect(screen, L6, (750, 100, ls_width, ls_height))
    pygame.draw.rect(screen, L7, (750+50, 100, ls_width, ls_height))
    pygame.draw.rect(screen, L8, (750+50*2, 100, ls_width, ls_height))
    pygame.draw.rect(screen, L9, (750+50*3, 100, ls_width, ls_height))
    pygame.draw.rect(screen, L10, (750+50*4, 100, ls_width, ls_height))
    pygame.draw.rect(screen, L11, (750, 150, ls_width, ls_height))
    pygame.draw.rect(screen, L12, (750+50*1, 150, ls_width, ls_height))
    pygame.draw.rect(screen, L13, (750+50*2, 150, ls_width, ls_height))
    pygame.draw.rect(screen, L14, (750+50*3, 150, ls_width, ls_height))
    pygame.draw.rect(screen, L15, (750+50*4, 150, ls_width, ls_height))
    pygame.draw.rect(screen, L16, (750, 200, ls_width, ls_height))
    pygame.draw.rect(screen, L17, (750+50*1, 200, ls_width, ls_height))
    pygame.draw.rect(screen, L18, (750+50*2, 200, ls_width, ls_height))
    pygame.draw.rect(screen, L19, (750+50*3, 200, ls_width, ls_height))
    pygame.draw.rect(screen, L20, (750+50*4, 200, ls_width, ls_height))
    pygame.draw.rect(screen, L21, (750, 250, ls_width, ls_height))
    pygame.draw.rect(screen, L22, (750+50*1, 250, ls_width, ls_height))
    pygame.draw.rect(screen, L23, (750+50*2, 250, ls_width, ls_height))
    pygame.draw.rect(screen, L24, (750+50*3, 250, ls_width, ls_height))
    pygame.draw.rect(screen, L25, (750+50*4, 250, ls_width, ls_height))
    pygame.draw.rect(screen, L26, (750, 300, ls_width, ls_height))
    pygame.draw.rect(screen, L27, (750+50*1, 300, ls_width, ls_height))
    pygame.draw.rect(screen, L28, (750+50*2, 300, ls_width, ls_height))
    pygame.draw.rect(screen, L29, (750+50*3, 300, ls_width, ls_height))
    pygame.draw.rect(screen, L30, (750+50*4, 300, ls_width, ls_height))
    pygame.draw.rect(screen, L31, (750, 350, ls_width, ls_height))
    pygame.draw.rect(screen, L32, (750+50, 350, ls_width, ls_height))


    ls1_text = font2.render("LS1", True, (255, 255, 255))
    screen.blit(ls1_text, (755, 65))
    ls1_text = font2.render("LS2", True, (255, 255, 255))
    screen.blit(ls1_text, (805, 65))
    ls1_text = font2.render("LS3", True, (255, 255, 255))
    screen.blit(ls1_text, (805+50, 65))
    ls1_text = font2.render("LS4", True, (255, 255, 255))
    screen.blit(ls1_text, (805+100, 65))
    ls1_text = font2.render("LS5", True, (255, 255, 255))
    screen.blit(ls1_text, (805+150, 65))
    ls1_text = font2.render("LS6", True, (255, 255, 255))
    screen.blit(ls1_text, (805-50, 65+50))
    ls1_text = font2.render("LS7", True, (255, 255, 255))
    screen.blit(ls1_text, (805, 65+50))
    ls1_text = font2.render("LS8", True, (255, 255, 255))
    screen.blit(ls1_text, (805+50, 65+50))
    ls1_text = font2.render("LS9", True, (255, 255, 255))
    screen.blit(ls1_text, (805+100, 65+50))
    ls1_text = font2.render("LS10", True, (255, 255, 255))
    screen.blit(ls1_text, (805+150, 65+50))
    ls1_text = font2.render("LS11", True, (255, 255, 255))
    screen.blit(ls1_text, (805-50, 65+100))
    ls1_text = font2.render("LS12", True, (255, 255, 255))
    screen.blit(ls1_text, (805, 65+100))
    ls1_text = font2.render("LS13", True, (255, 255, 255))
    screen.blit(ls1_text, (805+50, 65+100))
    ls1_text = font2.render("LS14", True, (255, 255, 255))
    screen.blit(ls1_text, (805+100, 65+100))
    ls1_text = font2.render("LS15", True, (255, 255, 255))
    screen.blit(ls1_text, (805+150, 65+100))
    ls1_text = font2.render("LS16", True, (255, 255, 255))
    screen.blit(ls1_text, (805-50, 65+150))
    ls1_text = font2.render("LS17", True, (255, 255, 255))
    screen.blit(ls1_text, (805, 65+150))
    ls1_text = font2.render("LS18", True, (255, 255, 255))
    screen.blit(ls1_text, (805+50, 65+150))
    ls1_text = font2.render("LS19", True, (255, 255, 255))
    screen.blit(ls1_text, (805+100, 65+150))
    ls1_text = font2.render("LS20", True, (255, 255, 255))
    screen.blit(ls1_text, (805+150, 65+150))
    ls1_text = font2.render("LS21", True, (255, 255, 255))
    screen.blit(ls1_text, (805-50, 65+200))
    ls1_text = font2.render("LS22", True, (255, 255, 255))
    screen.blit(ls1_text, (805, 65+200))
    ls1_text = font2.render("LS23", True, (255, 255, 255))
    screen.blit(ls1_text, (805+50, 65+200))
    ls1_text = font2.render("LS24", True, (255, 255, 255))
    screen.blit(ls1_text, (805+100, 65+200))
    ls1_text = font2.render("LS25", True, (255, 255, 255))
    screen.blit(ls1_text, (805+150, 65+200))
    ls1_text = font2.render("LS26", True, (255, 255, 255))
    screen.blit(ls1_text, (805-50, 65+250))
    ls1_text = font2.render("LS27", True, (255, 255, 255))
    screen.blit(ls1_text, (805, 65+250))
    ls1_text = font2.render("LS28", True, (255, 255, 255))
    screen.blit(ls1_text, (805+50, 65+250))
    ls1_text = font2.render("LS29", True, (255, 255, 255))
    screen.blit(ls1_text, (805+100, 65+250))
    ls1_text = font2.render("LS30", True, (255, 255, 255))
    screen.blit(ls1_text, (805+150, 65+250))
    ls1_text = font2.render("LS31", True, (255, 255, 255))
    screen.blit(ls1_text, (805-50, 65+300))
    ls1_text = font2.render("LS32", True, (255, 255, 255))
    screen.blit(ls1_text, (805, 65+300))

    

    # Render and display the blue box height
    height_text = font.render(f"Water Level: {box_height:.3f}", True, (0, 0, 0))
    screen.blit(height_text, (10, 10))

    all_sprites.update()

    all_sprites.draw(screen)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(30)



    #updated_box_height = box_height
