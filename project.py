from tkinter import *  #for main menu interface
from PIL import Image, ImageTk    #for main menu background
import pygame   
import random

bg=pygame.image.load('bg.png')
food_image=pygame.image.load('hm.png')
game_over_img=pygame.image.load('end.bmp')
wallImage = pygame.image.load('wood.png')

#-------------------------LEVEL 1 (ONLY FUNCTIONS)----------------------------#
def GameOne():
    window.destroy()

    pygame.init()

    screen = pygame.display.set_mode((800, 600))

    fps = pygame.time.Clock()
    # snake has a little body first
    snake_pos = [100, 50]
    body = [[100, 50], [90, 50]]

    # food will be spawned randomly
    food_pos = [random.randrange(1, (800//10)) * 10, random.randrange(1, (600//10)) * 10]
    food_give = True

    direction = 'DOWN'

    navigate = direction

    score = 0


    def result():
        score_font = pygame.font.SysFont('Impact', 30)
        score_text = score_font.render('S C O R E : ' + str(score), True, (0,0,0))
        screen.blit(score_text, (630,10))

    def game_over():
        my_font = pygame.font.SysFont('times new roman', 85)
        over_text = my_font.render('GAME OVER...', True, (255,0,0))
        food_pos[0]=2000 #food will not be seem after game
        
        screen.blit(over_text, (170,250))

    #IF SNAKE GOES OUT OF GAME FIELD
    def out():
        if snake_pos[0] < 0 or snake_pos[0] > 800-10:
            game_over()
        if snake_pos[1] < 0 or snake_pos[1] > 600-10:
            game_over()

    #IF SNAKE COLLIDES WITH SELF
    def autokill():
        for part in body[1:]:
            if snake_pos[0] == part[0] and snake_pos[1] == part[1]:
                game_over()

    run=True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run=False
            
            if event.type == pygame.KEYDOWN:
            
                if event.key == pygame.K_UP:
                    navigate = 'UP'
                if event.key == pygame.K_DOWN:
                    navigate = 'DOWN'
                if event.key == pygame.K_LEFT:
                    navigate = 'LEFT'
                if event.key == pygame.K_RIGHT :
                    navigate = 'RIGHT'
            
                if event.key == pygame.K_ESCAPE:
                    run=False

        if navigate == 'UP' :
            direction = 'UP'
        if navigate == 'DOWN':
            direction = 'DOWN'
        if navigate == 'LEFT' :
            direction = 'LEFT'
        if navigate == 'RIGHT' :
            direction = 'RIGHT'

        if direction == 'UP':
            snake_pos[1] -= 10
        if direction == 'DOWN':
            snake_pos[1] += 10
        if direction == 'LEFT':
            snake_pos[0] -= 10
        if direction == 'RIGHT':
            snake_pos[0] += 10

        body.insert(0, list(snake_pos))
        
        #COLLISION WITH FOOD
        if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
            score += 1
            food_give = False
        else:
            body.pop()

        if food_give == False:
            food_pos = [random.randrange(1, (800//10)) * 10, random.randrange(1, (600//10)) * 10]
        food_give = True

        screen.fill((0,0,0))

        #DRAWING SNAKE
        for pos in body:
            pygame.draw.rect(screen, (0,255,0), pygame.Rect(pos[0], pos[1], 10, 10))

        #DRAWING FOOD
        pygame.draw.rect(screen, (255,255,255), pygame.Rect(food_pos[0], food_pos[1], 10, 10))


        result()
        out()
        autokill()
        pygame.display.update()

        fps.tick(15)
def GameTwo():
    window.destroy()
    
    screen = pygame.display.set_mode((800, 600))
    pygame.init()


    class Snake:
        def __init__(self):
            self.size = 1
            self.parts = [[100, 100]]
            self.dx = 5 
            self.dy = 0
            self.is_add = False
            self.score=0
            self.color=(70,60,71)

        def draw(self):
            for element in self.parts:
                #pygame.draw.circle(screen, (self.color), element, self.radius)
                pygame.draw.rect(screen, (0,0,0), pygame.Rect(element[0], element[1], 10, 10))

        def move(self):
            if self.is_add:
                self.size += 1
                self.parts.append([0, 0])
                self.is_add = False

            for i in range(len(self.parts) - 1, 0, -1):
                self.parts[i][0] = self.parts[i - 1][0]
                self.parts[i][1] = self.parts[i - 1][1]
             
            self.parts[0][0] += self.dx
            self.parts[0][1] += self.dy
        def out(self):
            if self.parts[0][0]>=800 or self.parts[0][0]<=0 or self.parts[0][1]<=0 or self.parts[0][1]>=600:
                return True
            return False    
        def autokill(self):
            for part in self.parts[1:]:
                if self.parts[0][0] == part[0] and self.parts[0][1] == part[1]:
                    return True
            return False

        def show_score(self):
            font = pygame.font.SysFont("Impact", 37)
            score = font.render("S C O R E: " + str(self.score), True, (0,0,0))
            screen.blit(score, (615, 20))

        def the_end(self):
        
            self.dx = 0
            self.dy = 0
            
            food.x=3000
        
        
    class Food:
        def __init__(self):
            self.x = random.randint(20,740)
            self.y = random.randint(20,540)
        def draw(self):
            screen.blit(food_image, (self.x, self.y))    
        def Collision(self,Snake):
            if (self.x >= Snake.parts[0][0]-20 and self.x < Snake.parts[0][0]+20) and  (self.y >= Snake.parts[0][1] -20 and self.y<Snake.parts[0][1] +20):
                Snake.is_add = True  
                if Snake.is_add == True:
                    Snake.score += 1
                    self.x = random.randint(10, 750)
                    self.y = random.randint(10, 550)

    class Wall:

            def __init__(self,x,y):
                self.x = x
                self.y = y     
                self.width = 25
                self.height = 25

            def draw(self):
                screen.blit( wallImage,(self.x,self.y))
            
            def hits(self,Snake):
                if Snake.parts[0][0] in range (self.x-5,self.x+30):
                    if Snake.parts[0][1] in range (self.y-5,self.y+30):
                        return True
                return False
            def notInFood(self,Food):
                if Food.x in range(self.x-10, self.x+35) :
                    if  Food.y in range(self.y - 10, self.y + 35):
                         Food.x = random.randint(10, 750)
                         Food.y = random.randint(10, 550)
                    


    snake = Snake()
    food=Food()
    playing = True
    score=0
    d = 3
    walls = []
    X1,Y1 = 170,150
    for i in (range (18)):
        walls.append(Wall(X1,Y1))
        X1 += 25
    X2,Y2 = 170,175
    for i in (range(12)):
        walls.append(Wall(X2,Y2))
        Y2 += 25
    X3,Y3= 170, 475
    for i in (range (19)):
        walls.append(Wall(X3,Y3))
        X3 += 25

    FPS = 30

    clock = pygame.time.Clock()

    while playing:
            screen.blit(bg, (0, 0))
            mill = clock.tick(FPS) 
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    playing = False 
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE: 
                        playing = False 
                    if event.key == pygame.K_RIGHT: 
                        snake.dx = d 
                        snake.dy = 0 
                    if event.key == pygame.K_LEFT: 
                        snake.dx = -d 
                        snake.dy = 0 
                    if event.key == pygame.K_UP: 
                        snake.dx = 0 
                        snake.dy = -d 
                    if event.key == pygame.K_DOWN: 
                        snake.dx = 0 
                        snake.dy = d 
            if snake.out()==True or snake.autokill()==True :
                snake.the_end()
                screen.blit(game_over_img,(0,0))

              
            for wall in walls:

                wall.draw()
                wall.notInFood(food)
                if wall.hits(snake)==True:
                    snake.the_end()
                    screen.blit(game_over_img,(0,0))
            
            snake.move()
            food.Collision(snake)
            food.draw()
            snake.draw()
            snake.show_score()
            
            pygame.display.update()
def GameThree():
    window.destroy()
    
    screen = pygame.display.set_mode((800, 600))
    pygame.init()


    class Snake:
        def __init__(self):
            self.size = 1
            self.parts = [[100, 100]]
            self.dx = 5 
            self.dy = 0
            self.is_add = False
            self.score=0
            self.color=(40,40,50)

        def draw(self):
            for element in self.parts:
                #pygame.draw.circle(screen, (self.color), element, self.radius)
                pygame.draw.rect(screen, (0,0,0), pygame.Rect(element[0], element[1], 10, 10))

        def move(self):
            if self.is_add:
                self.size += 1
                self.parts.append([0, 0])
                self.is_add = False

            for i in range(len(self.parts) - 1, 0, -1):
                self.parts[i][0] = self.parts[i - 1][0]
                self.parts[i][1] = self.parts[i - 1][1]

            self.parts[0][0] += self.dx
            self.parts[0][1] += self.dy
        def out(self):
            if self.parts[0][0]>=800 or self.parts[0][0]<=0 or self.parts[0][1]<=0 or self.parts[0][1]>=600:
                return True
            return False    
        def autokill(self):
            for part in self.parts[1:]:
                if self.parts[0][0] == part[0] and self.parts[0][1] == part[1]:
                    return True
            return False

        def show_score(self):
            font = pygame.font.SysFont("Impact", 37)
            score = font.render("S C O R E: " + str(self.score), True, (50,50,50))
            screen.blit(score, (615, 20))

        def the_end(self):
            self.dx = 0
            self.dy = 0
            
            food.x=3000
        
        
    class Food:
        def __init__(self):
            self.x = random.randint(20,740)
            self.y = random.randint(20,540)
        def draw(self):
            screen.blit(food_image, (self.x, self.y))    
        def Collision(self,Snake):
            if (self.x >= Snake.parts[0][0]-20 and self.x < Snake.parts[0][0]+20) and  (self.y >= Snake.parts[0][1] -20 and self.y<Snake.parts[0][1] +20):
                Snake.is_add = True  
                if Snake.is_add == True:
                    Snake.score += 1
                    self.x = random.randint(10, 750)
                    self.y = random.randint(10, 550)

    class Wall:

            def __init__(self,x,y):
                self.x = x
                self.y = y     
                self.width = 25
                self.height = 25

            def draw(self):
                screen.blit( wallImage,(self.x,self.y))
            
            def hits(self,Snake):
                if Snake.parts[0][0] in range (self.x-5,self.x+23):
                    if Snake.parts[0][1] in range (self.y-5,self.y+30):
                        return True
            def notInFood(self,Food):
                if Food.x in range(self.x-5,self.x+25) and  Food.y in range(self.y,self.y+25):
                    Food.x = random.randint(10, 750)
                    Food.y = random.randint(10, 550)
    snake = Snake()
    food=Food()
    playing = True
    score=0
    d = 4
    walls = []
    X1,Y1 = 140,120
    for i in (range (17)):
        walls.append(Wall(X1,Y1))
        Y1 += 25
    X2,Y2 = 165,120
    for i in (range(6)):
        walls.append(Wall(X2,Y2))
        X2 += 25

    X3,Y3= 315,120
    for i in (range (17)):
        walls.append(Wall(X3,Y3))
        Y3 += 25

    X4, Y4 = 315,520
    for i in (range (9)):
        walls.append(Wall(X4,Y4))
        X4 += 25
    X5,Y5=540,120
    for i in (range (17)):
        walls.append(Wall(X5,Y5))
        Y5 += 25

    FPS = 30

    clock = pygame.time.Clock()

    while playing:
            mill = clock.tick(FPS) 
            screen.blit(bg, (0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    playing = False 
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE: 
                        playing = False 
                    if event.key == pygame.K_RIGHT: 
                        snake.dx = d 
                        snake.dy = 0 
                    if event.key == pygame.K_LEFT: 
                        snake.dx = -d 
                        snake.dy = 0 
                    if event.key == pygame.K_UP: 
                        snake.dx = 0 
                        snake.dy = -d 
                    if event.key == pygame.K_DOWN: 
                        snake.dx = 0 
                        snake.dy = d 
            if snake.out()==True or snake.autokill()==True :
                snake.the_end()
                screen.blit(game_over_img,(0,0))

             
            for wall in walls:
                wall.notInFood(food)
                wall.draw()
                if wall.hits(snake)==True:
                    snake.the_end()
                    screen.blit(game_over_img,(0,0))
            
            snake.move()
            food.Collision(snake)
            food.draw()
            snake.draw()
            snake.show_score()
            wall.notInFood(food)
            
            pygame.display.flip()
window = Tk()
window.geometry('800x600')
window.title('SNAKE GAME')                                                                                              
load = Image.open("paper.png")
render = ImageTk.PhotoImage(load)
img = Label(window, image=render)
img.image = render
img.place(x=0, y=0)

One = Button(window, text="     L E V E L  O N E     ",  command=GameOne,bg='yellow',fg='black',width=25,height=5,font='Elephant')
One.pack()
One.place(bordermode=INSIDE, x=180,y=100,height=50, width=400)

Two = Button(window, text="      L E V E L   T W O    ", command=GameTwo,bg='yellow',fg='black', width=25, height=5,font='Elephant')
Two.pack()
Two.place(bordermode=INSIDE, x=180,y=250,height=50, width=400)

Three = Button(window, text="      L E V E L    T H R E E    ", command=GameThree,bg='yellow',fg='black', width=25, height=5,font='Elephant')
Three.pack()
Three.place(bordermode=INSIDE, x=180,y=400,height=50, width=400)



window.mainloop()