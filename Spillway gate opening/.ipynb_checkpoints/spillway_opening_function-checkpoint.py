import matplotlib.pyplot as plt
"""
def create_boxes(gates, level):
    # Create a figure and axis
    fig, ax = plt.subplots()

    # Set the axis limits
    ax.set_xlim(0, 32)  # Adjusted to include spaces between the boxes
    ax.set_ylim(0, 9.4)

    # Set the width of each box and the spacing between them
    box_width = 3.6
    box_spacing = 0.4

    # Create rectangles with red color and spaces
    for i in range(8):
        x_position = i * (box_width + box_spacing)
        if i in gates:
            # Make the first box half red-colored
            rectangle_red = plt.Rectangle((x_position, level), box_width, 9.4 - level, fc='red')
            ax.add_patch(rectangle_red)
            rectangle_blue = plt.Rectangle((x_position, 0), box_width, level, fc='blue')
            ax.add_patch(rectangle_blue)
        else:
            rectangle = plt.Rectangle((x_position, 0), box_width, 9.4, fc='red')
            ax.add_patch(rectangle)

    # Set the aspect ratio to 'equal' for square boxes
    ax.set_aspect('equal', adjustable='box')

    # Remove axis ticks
    ax.set_xticks([])
    ax.set_yticks([])

    # Return the figure
    return fig

# Store the figure in a variable

"""

def control_gates(heights):
    
    L1,L2,L3,L4,L5,L6,L7,L8,L9,L10,L11,L12,L13,L14,L15,L16,L17,L18,L19,L20,L21,L22,L23,L24,L25,L26,L27,L28,L29,L30,L31,L32 = 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
    
    for i in range(len(heights)):

        water_height = heights[i]
        
        if i == 0:
            continue
    
        elif water_height < 437.98:
            gates = [0]*32

        #elif water_height > 438.65:
           #S gates = [1]*32
            
        elif heights[i-1] < heights[i]:
            
            if water_height > 438.65:
                L1, L3,L2,L5, L4,L7, L6, L9, L8, L11, L10, L13, L12, L15, L14, L17, L16, L19, L18, L21, L20, L23, L22, L25, L24, L27, L26, L29, L28, L31, L30, L32 = 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1
                #print("gate L32 opened")
            elif water_height > 438.61:
                L1, L3,L2,L5, L4,L7, L6, L9, L8, L11, L10, L13, L12, L15, L14, L17, L16, L19, L18, L21, L20, L23, L22, L25, L24, L27, L26, L29, L28, L31, L30 = 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1
                #print("gate L30 opened")
            elif water_height > 438.60:
                L1, L3,L2,L5, L4,L7, L6, L9, L8, L11, L10, L13, L12, L15, L14, L17, L16, L19, L18, L21, L20, L23, L22, L25, L24, L27, L26, L29, L28, L31 = 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1
                #print("gate L31 opened")
            elif water_height > 438.57:
                L1, L3,L2,L5, L4,L7, L6, L9, L8, L11, L10, L13, L12, L15, L14, L17, L16, L19, L18, L21, L20, L23, L22, L25, L24, L27, L26, L29, L28 = 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1
                #print("gate L28 opened")
            elif water_height > 438.56:
                L1, L3,L2,L5, L4,L7, L6, L9, L8, L11, L10, L13, L12, L15, L14, L17, L16, L19, L18, L21, L20, L23, L22, L25, L24, L27, L26, L29 = 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1
                #print("gate L29 opened")
            elif water_height > 438.53:
                L1, L3,L2,L5, L4,L7, L6, L9, L8, L11, L10, L13, L12, L15, L14, L17, L16, L19, L18, L21, L20, L23, L22, L25, L24, L27, L26 = 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1
                #print("gate L26 opened")
            elif water_height > 438.52:
                L1, L3,L2,L5, L4,L7, L6, L9, L8, L11, L10, L13, L12, L15, L14, L17, L16, L19, L18, L21, L20, L23, L22, L25, L24, L27 = 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1
                #print("gate L27 opened")
            elif water_height > 438.49:
                L1, L3,L2,L5, L4,L7, L6, L9, L8, L11, L10, L13, L12, L15, L14, L17, L16, L19, L18, L21, L20, L23, L22, L25, L24 = 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1
                #print("gate L24 opened")
            elif water_height > 438.48:
                L1, L3,L2,L5, L4,L7, L6, L9, L8, L11, L10, L13, L12, L15, L14, L17, L16, L19, L18, L21, L20, L23, L22, L25 = 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1
                #print("gate L25 opened")
            elif water_height > 438.45:
                L1, L3,L2,L5, L4,L7, L6, L9, L8, L11, L10, L13, L12, L15, L14, L17, L16, L19, L18, L21, L20, L23, L22 = 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1
                #print("gate L22 opened")
            elif water_height > 438.44:
                L1, L3,L2,L5, L4,L7, L6, L9, L8, L11, L10, L13, L12, L15, L14, L17, L16, L19, L18, L21, L20, L23 = 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1
                #print("gate L23 opened")
            elif water_height > 438.41:
                L1, L3,L2,L5, L4,L7, L6, L9, L8, L11, L10, L13, L12, L15, L14, L17, L16, L19, L18, L21, L20 = 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1
                #print("gate L20 opened")
            elif water_height > 438.40:
                L1, L3,L2,L5, L4,L7, L6, L9, L8, L11, L10, L13, L12, L15, L14, L17, L16, L19, L18, L21 = 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1
                #print("gate L21 opened")
            elif water_height > 438.37:
                L1, L3,L2,L5, L4,L7, L6, L9, L8, L11, L10, L13, L12, L15, L14, L17, L16, L19, L18 = 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1
                #print("gate L18 opened")
            elif water_height > 438.36:
                L1, L3,L2,L5, L4,L7, L6, L9, L8, L11, L10, L13, L12, L15, L14, L17, L16, L19 = 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1
                #print("gate L19 opened")
            elif water_height > 438.33:
                L1, L3,L2,L5, L4,L7, L6, L9, L8, L11, L10, L13, L12, L15, L14, L17, L16 = 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1
                #print("gate L16 opened")
            elif water_height > 438.32:
                L1, L3,L2,L5, L4,L7, L6, L9, L8, L11, L10, L13, L12, L15, L14, L17 = 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1
                #print("gate L17 opened")
            elif water_height > 438.29:
                L1, L3,L2,L5, L4,L7, L6, L9, L8, L11, L10, L13, L12, L15, L14 = 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1
                #print("gate L14 opened")
            elif water_height > 438.28:
                L1, L3,L2,L5, L4,L7, L6, L9, L8, L11, L10, L13, L12, L15 = 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1
                #print("gate L15 opened")
            elif water_height > 438.25:
                L1, L3,L2,L5, L4,L7, L6, L9, L8, L11, L10, L13, L12 = 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1
                #print("gate L12 opened")
            elif water_height > 438.24:
                L1, L3,L2,L5, L4,L7, L6, L9, L8, L11, L10, L13 = 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1
                #print("gate L13 opened")
            elif water_height > 438.21:
                L1, L3,L2,L5, L4,L7, L6, L9, L8, L11, L10 = 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1
                #print("gate L10 opened")
            elif water_height > 438.20:
                L1, L3,L2,L5, L4,L7, L6, L9, L8, L11 = 1, 1, 1, 1, 1, 1, 1, 1, 1, 1
                #print("gate L11 opened")
            elif water_height > 438.17:
                L1, L3,L2,L5, L4,L7, L6, L9, L8 = 1, 1, 1, 1, 1, 1, 1, 1, 1
                #print("gate L8 opened")
            elif water_height > 438.16:
                L1, L3,L2,L5, L4,L7, L6, L9 = 1, 1, 1, 1, 1, 1, 1, 1
                #print("gate L9 opened")
            elif water_height > 438.13:
                L1, L3,L2,L5, L4,L7, L6 = 1, 1, 1, 1, 1, 1, 1
                #print("gate L6 opened")
            elif water_height > 438.12:
                L1, L3,L2,L5, L4,L7 = 1, 1, 1, 1, 1, 1
                #print("gate L7 opened")
            elif water_height > 438.09:
                L1, L3,L2,L5, L4 = 1, 1, 1, 1, 1
                #print("gate L4 opened")
            elif water_height > 438.08:
                L1, L3,L2,L5 = 1, 1, 1, 1
                #print("gate L5 opened")
            elif water_height > 438.05:
                L1, L3,L2 = 1, 1, 1
                #print("gate L2 opened")
            elif water_height > 438.04:
                L1, L3 = 1, 1
                #print("gate L3 opened")
            elif water_height > 438:
                L1 = 1
                #print("gate L1 opened")
            
            
        elif heights[i-1] > heights[i]:
            
            if water_height <= 437.98:
                L1, L3, L2, L5, L4, L7, L6, L9, L8, L11, L10, L13, L12, L15, L14, L17, L16, L19, L18, L21, L20, L23, L22, L25, L24, L27, L26, L29, L28, L31, L30, L32 = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
                #print("gate L1 closed")
            elif water_height <= 438.02:
                L3, L2, L5, L4, L7, L6, L9, L8, L11, L10, L13, L12, L15, L14, L17, L16, L19, L18, L21, L20, L23, L22, L25, L24, L27, L26, L29, L28, L31, L30, L32 = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
                #print("gate L3 closed")
            elif water_height <= 438.03:
                L2, L5, L4, L7, L6, L9, L8, L11, L10, L13, L12, L15, L14, L17, L16, L19, L18, L21, L20, L23, L22, L25, L24, L27, L26, L29, L28, L31, L30, L32 = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
                #print("gate L2 closed")
            elif water_height <= 438.06:
                L5, L4, L7, L6, L9, L8, L11, L10, L13, L12, L15, L14, L17, L16, L19, L18, L21, L20, L23, L22, L25, L24, L27, L26, L29, L28, L31, L30, L32 = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
                #print("gate L5 closed")
            elif water_height <= 438.07:
                L4, L7, L6, L9, L8, L11, L10, L13, L12, L15, L14, L17, L16, L19, L18, L21, L20, L23, L22, L25, L24, L27, L26, L29, L28, L31, L30, L32 = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
                #print("gate L4 closed")
            elif water_height <= 438.10:
                L7, L6, L9, L8, L11, L10, L13, L12, L15, L14, L17, L16, L19, L18, L21, L20, L23, L22, L25, L24, L27, L26, L29, L28, L31, L30, L32 = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
                #print("gate L7 closed")
            elif water_height <= 438.11:
                L6, L9, L8, L11, L10, L13, L12, L15, L14, L17, L16, L19, L18, L21, L20, L23, L22, L25, L24, L27, L26, L29, L28, L31, L30, L32 = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
                #print("gate L6 closed")
            elif water_height <= 438.14:
                L9, L8, L11, L10, L13, L12, L15, L14, L17, L16, L19, L18, L21, L20, L23, L22, L25, L24, L27, L26, L29, L28, L31, L30, L32 = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
                #print("gate L9 closed")
            elif water_height <= 438.15:
                L8, L11, L10, L13, L12, L15, L14, L17, L16, L19, L18, L21, L20, L23, L22, L25, L24, L27, L26, L29, L28, L31, L30, L32 = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
                #print("gate L8 closed")
            elif water_height <= 438.18:
                L11, L10, L13, L12, L15, L14, L17, L16, L19, L18, L21, L20, L23, L22, L25, L24, L27, L26, L29, L28, L31, L30, L32 = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
                #print("gate L11 closed")
            elif water_height <= 438.19:
                L10, L13, L12, L15, L14, L17, L16, L19, L18, L21, L20, L23, L22, L25, L24, L27, L26, L29, L28, L31, L30, L32 = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
                #print("gate L10 closed")
            elif water_height <= 438.22:
                L13, L12, L15, L14, L17, L16, L19, L18, L21, L20, L23, L22, L25, L24, L27, L26, L29, L28, L31, L30, L32 = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
                #print("gate L13 closed")
            elif water_height <= 438.23:
                L12, L15, L14, L17, L16, L19, L18, L21, L20, L23, L22, L25, L24, L27, L26, L29, L28, L31, L30, L32 = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
                #print("gate L12 closed")
            elif water_height <= 438.26:
                L15, L14, L17, L16, L19, L18, L21, L20, L23, L22, L25, L24, L27, L26, L29, L28, L31, L30, L32 = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
                #print("gate L15 closed")
            elif water_height <= 438.27:
                L14, L17, L16, L19, L18, L21, L20, L23, L22, L25, L24, L27, L26, L29, L28, L31, L30, L32 = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
                #print("gate L14 closed")
            elif water_height <= 438.30:
                L17, L16, L19, L18, L21, L20, L23, L22, L25, L24, L27, L26, L29, L28, L31, L30, L32 = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
                #print("gate L17 closed")
            elif water_height <= 438.31:
                L16, L19, L18, L21, L20, L23, L22, L25, L24, L27, L26, L29, L28, L31, L30, L32 = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
                #print("gate L16 closed")
            elif water_height <= 438.34:
                L19, L18, L21, L20, L23, L22, L25, L24, L27, L26, L29, L28, L31, L30, L32 = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
                #print("gate L19 closed")
            elif water_height <= 438.35:
                L18, L21, L20, L23, L22, L25, L24, L27, L26, L29, L28, L31, L30, L32 = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
                #print("gate L18 closed")
            elif water_height <= 438.38:
                L21, L20, L23, L22, L25, L24, L27, L26, L29, L28, L31, L30, L32 = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
                #print("gate L21 closed")
            elif water_height <= 438.39:
                L20, L23, L22, L25, L24, L27, L26, L29, L28, L31, L30, L32 = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
                #print("gate L20 closed")
            elif water_height <= 438.42:
                L23, L22, L25, L24, L27, L26, L29, L28, L31, L30, L32 = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
                #print("gate L23 closed")
            elif water_height <= 438.43:
                L22, L25, L24, L27, L26, L29, L28, L31, L30, L32 = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
                #print("gate L22 closed")
            elif water_height <= 438.46:
                L25, L24, L27, L26, L29, L28, L31, L30, L32 = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
                #print("gate L25 closed")
            elif water_height <= 438.47:
                L24, L27, L26, L29, L28, L31, L30, L32 = 0, 0, 0, 0, 0, 0, 0, 0, 0
                #print("gate L24 closed")
            elif water_height <= 438.50:
                L27, L26, L29, L28, L31, L30, L32 = 0, 0, 0, 0, 0, 0, 0, 0
                #print("gate L27 closed")
            elif water_height <= 438.51:
                L26, L29, L28, L31, L30, L32 = 0, 0, 0, 0, 0, 0
                #print("gate L26 closed")
            elif water_height <= 438.54:
                L29, L28, L31, L30, L32 = 0, 0, 0, 0, 0
                #print("gate L29 closed")
            elif water_height <= 438.55:
                L28, L31, L30, L32 = 0, 0, 0, 0
                #print("gate L28 closed")
            elif water_height <= 438.58:
                L31, L30, L32 = 0, 0, 0
                #print("gate L31 closed")
            elif water_height <= 438.59:
                L30, L32 = 0, 0
                #print("gate L30 closed")
            elif water_height <= 438.63:
                L32 = 0
                #print("gate L32 closed")
    
        gates = [L1,L2,L3,L4,L5,L6,L7,L8,L9,L10,L11,L12,L13,L14,L15,L16,L17,L18,L19,L20,L21,L22,L23,L24,L25,L26,L27,L28,L29,L30,L31,L32]
        #gates = "Level 1 : " + str(L1) + "\n" + "Level 2 : " + str(L2) + "\n" + "Level 3 : " + str(L3) + "\n" + "Level 4 : " + str(L4) + "\n" + "Level 5 : " + str(L5) + "\n" + "Level 6 : " + str(L6) + "\n" + "Level 7 : " + str(L7) + "\n" + "Level 8 : " + str(L8) + "\n" + "Level 9 : " + str(L9) + "\n" + "Level 10 : " + str(L10) + "\n" + "Level 11 : " + str(L11) + "\n" + "Level 12 : " + str(L12) + "\n" + "Level 13 : " + str(L13) + "\n" + "Level 14 : " + str(L14) + "\n" + "Level 15 : " + str(L15) + "\n" + "Level 16 : " + str(L16) + "\n" + "Level 17 : " + str(L17) + "\n" + "Level 18 : " + str(L18) + "\n" + "Level 19 : " + str(L19) + "\n" + "Level 20 : " + str(L20) + "\n" + "Level 21 : " + str(L21) + "\n" + "Level 22 : " + str(L22) + "\n" + "Level 23 : " + str(L23) + "\n" + "Level 24 : " + str(L24) + "\n" + "Level 25 : " + str(L25) + "\n" + "Level 26 : " + str(L26) + "\n" + "Level 27 : " + str(L27) + "\n" + "Level 28 : " + str(L28) + "\n" + "Level 29 : " + str(L29) + "\n" + "Level 30 : " + str(L30) + "\n" + "Level 31 : " + str(L31) + "\n" + "Level 32 : " + str(L32) 
        """
        gate_status = create_boxes([], 0)

        if gates[31] == 1:
            gate_status = [3, 4, 2, 5 ,1, 6 , 0, 7]
            level = 9.4
        elif gates[29] == 1:
            gate_status = [3, 4, 2, 5 ,1, 6]
            level = 9.4
        elif gates[27] == 1:
            gate_status = [3, 4, 2, 5]
            level = 9.4
        elif gates[25] == 1:
            gate_status = [3, 4]
            level = 9.4
        elif gates[23] == 1:
            gate_status = [3, 4, 2, 5 ,1, 6 , 0, 7]
            level = 4.7
        elif gates[21] == 1:
            gate_status = [3, 4, 2, 5 ,1, 6]
            level = 4.7
        elif gates[19] == 1:
            gate_status = [3, 4, 2, 5]
            level = 4.7
        elif gates[17] == 1:
            gate_status = [3, 4]
            level = 4.7
        elif gates[15] == 1:
            gate_status = [3, 4, 2, 5 ,1, 6 , 0, 7]
            level = 2.5
        elif gates[13] == 1:
            gate_status = [3, 4, 2, 5 ,1, 6]
            level = 2.5
        elif gates[11] == 1:
            gate_status = [3, 4, 2, 5]
            level = 2.5
        elif gates[9] == 1:
            gate_status = [3, 4], 
            level = 2.5
        elif gates[7] == 1:
            gate_status = [3, 4, 2, 5 ,1, 6 , 0, 7]
            level = 0.7
        elif gates[5] == 1:
            gate_status = [3, 4, 2, 5 ,1, 6]
            level = 0.7
        elif gates[3] == 1:
            gate_status = [3, 4, 2, 5] 
            level = 0.7
        elif gates[1] == 1:
            gate_status = [2, 5]
            level = 0.7
        else:
            gate_status = []
            level = 0
        
            
    return create_boxes(gate_status, level)
    """
        return gates
