def create_image(width, height, background_color):
    image = []
    
    for y in range(height):
        row = []
        for x in range(width):
                row.append(background_color)
        image.append(row)
    
    return image

def draw_pixel(image, x, y, color):
    image[y][x] = color

# def draw_horizontal_line(image, y, color):
#     width = len(image[0])
#     for x in range(width):
#         image[y][x] = color
        

def draw_brush(image, x, y, color, size=1):
    height, width = give_height_width(image)
    
    for dy in range(-size, size + 1):
        for dx in range(-size, size + 1):
        
            new_x = x + dx
            new_y = y + dy
            
            if 0 <= new_x < width and 0 <= new_y < height:
                 draw_pixel(image, new_x, new_y, color)

def give_height_width(image):
    height = len(image)
    width = len(image[0])
    
    return (height, width)