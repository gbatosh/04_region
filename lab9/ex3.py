import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()
    
    radius = 15
    mode = 'blue'
    points = []
    draw = True
    cirrect = True
    
    while True:
        
        pressed = pygame.key.get_pressed()
        
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]
        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    return
                if event.key == pygame.K_F4 and alt_held:
                    return
                if event.key == pygame.K_ESCAPE:
                    return
                if event.key == pygame.K_r:
                    mode = 'red'
                elif event.key == pygame.K_g:
                    mode = 'green'
                elif event.key == pygame.K_b:
                    mode = 'blue'
                if event.key == pygame.K_SPACE:
                    draw = not draw
                    points = []
                if event.key == pygame.K_z:
                    cirrect = not cirrect
                if event.key == pygame.K_s:
                    draw_square(screen, points, radius, mode, cirrect)
                if event.key == pygame.K_t:
                    draw_right_triangle(screen, points, radius, mode, cirrect)
                if event.key == pygame.K_e:
                    draw_equilateral_triangle(screen, points, radius, mode, cirrect)
                if event.key == pygame.K_d:
                    draw_rhombus(screen, points, radius, mode, cirrect)
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: 
                    radius = min(200, radius + 1)
                elif event.button == 3: 
                    radius = max(1, radius - 1)
            
            if event.type == pygame.MOUSEMOTION:
                position = event.pos
                points = points + [position]
                points = points[-256:]
        
        i = 0
        while i < len(points) - 1 and draw:
            drawLineBetween(screen, i, points[i], points[i + 1], radius, mode, cirrect)
            i += 1
        
        pygame.display.flip()
        
        clock.tick(60)

def drawLineBetween(screen, index, start, end, width, color_mode, cirrect):
    c1 = max(0, min(255, 2 * index - 256))
    c2 = max(0, min(255, 2 * index))
    
    if color_mode == 'blue':
        color = (c1, c1, c2)
    elif color_mode == 'red':
        color = (c2, c1, c1)
    elif color_mode == 'green':
        color = (c1, c2, c1)
    
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))
    
    for i in range(iterations):
        progress = 1.0 * i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        if cirrect:
            pygame.draw.circle(screen, color, (x, y), width)
        else:
            pygame.draw.rect(screen, color, (x-width, y-width, 2*width, 2*width))   

def draw_square(screen, points, radius, mode, cirrect):
    if len(points) == 4:
        if cirrect:
            pygame.draw.polygon(screen, (255, 255, 255), points)
            pygame.draw.polygon(screen, (0, 0, 0), points, width=2)
        else:
            pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(points[0], (points[2][0] - points[0][0], points[2][1] - points[0][1])))
            pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(points[0], (points[2][0] - points[0][0], points[2][1] - points[0][1])), width=2)
        
        points.clear()

def draw_right_triangle(screen, points, radius, mode, cirrect):
    if len(points) == 3:
        if cirrect:
            pygame.draw.polygon(screen, (255, 255, 255), points)
            pygame.draw.polygon(screen, (0, 0, 0), points, width=2)
        else:
            rect = pygame.Rect(points[0], (points[2][0] - points[0][0], points[2][1] - points[0][1]))
            pygame.draw.polygon(screen, (255, 255, 255), [(rect.left, rect.top), (rect.right, rect.bottom), (rect.left, rect.bottom)])
            pygame.draw.polygon(screen, (0, 0, 0), [(rect.left, rect.top), (rect.right, rect.bottom), (rect.left, rect.bottom)], width=2)
        
        points.clear()

def draw_equilateral_triangle(screen, points, radius, mode, cirrect):
    if len(points) == 3:
        if cirrect:
            pygame.draw.polygon(screen, (255, 255, 255), points)
            pygame.draw.polygon(screen, (0, 0, 0), points, width=2)
        else:
            x0, y0 = points[0]
            x2, y2 = points[2]
            x1 = x0 + (x2 - x0) / 2
            y1 = y0 - (x2 - x0) * 3 ** 0.5 / 2
            pygame.draw.polygon(screen, (255, 255, 255), [(x0, y0), (x1, y1), (x2, y2)])
            pygame.draw.polygon(screen, (0, 0, 0), [(x0, y0), (x1, y1), (x2, y2)], width=2)
        
        points.clear()

def draw_rhombus(screen, points, radius, mode, cirrect):
    if len(points) == 4:
        if cirrect:
            pygame.draw.polygon(screen, (255, 255, 255), points)
            pygame.draw.polygon(screen, (0, 0, 0), points, width=2)
        else:
            rect = pygame.Rect(points[0], (points[2][0] - points[0][0], points[2][1] - points[0][1]))
            pygame.draw.polygon(screen, (255, 255, 255), [(rect.left, rect.top), ((rect.left + rect.right) / 2, rect.top), (rect.right, rect.bottom), ((rect.left + rect.right) / 2, rect.bottom)])
            pygame.draw.polygon(screen, (0, 0, 0), [(rect.left, rect.top), ((rect.left + rect.right) / 2, rect.top), (rect.right, rect.bottom), ((rect.left + rect.right) / 2, rect.bottom)], width=2)
        
        points.clear()

main()
