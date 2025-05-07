from pygame import *
from random import randint, choice
from time import sleep
width = 700
height = 500
window = display.set_mode((width, height))
display.set_caption('Ping-Pong')
background = transform.scale(image.load('pole.jpg'), (width,height))
speed = 10 
ball_skins = ['egg.png', 'nagiev.png']
speed_x = choice((3,-3))
speed_y = choice((3,-3))

score = 0

font.init()
font1 = font.SysFont('Arial',50)
font2 = font.Font(None, 50)
lose1 = font1.render('PLAYER 1 LOSE!', True, (255,0,0))
lose2 = font1.render('PLAYER 2 LOSE!', True, (255,0,0))

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x,size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < height - 160:
            self.rect.y += self.speed

    def update_r(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < height - 160:
            self.rect.y += self.speed        

sprite1= Player('lopata.png',0, 170, 20, 160, 7)   
sprite2= Player('palka.png',665, 170, 20, 160, 7)   
sprite3= GameSprite('egg.png', 315, 220, 60, 60, 7 )        
#! sssssssssss

def change_skin(object, img_skin):
    new_skin = transform.scale(image.load(img_skin), (object.rect.width, object.rect.height))
    object.image = new_skin
    

    

game = True
finish = False
clock = time.Clock()
FPS = 60

while game:
    
    for e in event.get():
        if e.type == QUIT:
            game = False
        if e.type == KEYDOWN and e.key == K_q:
            num = randint(0, len(ball_skins)-1)
            change_skin(sprite3, ball_skins[num])

    if finish != True:
        window.blit(background, (0,0))



        sc = font2.render(str(score), True, (0,225,0))   
        window.blit(sc, (10,10))
        sprite1.update_l()
        sprite2.update_r()
        sprite3.update()

        sprite3.reset()
        sprite2.reset()
        sprite1.reset()

        sprite3.rect.x += speed_x
        sprite3.rect.y += speed_y

        if sprite3.rect.y > 500-60 or sprite3.rect.y < 0:
            speed_y *= -1.1
        if sprite.collide_rect(sprite3, sprite1) or sprite.collide_rect(sprite3, sprite2):
            speed_x *= -1.1
            score +=1 

        if sprite3.rect.x <0:
            window.blit(lose1, (200, 200))
            finish = True

        if sprite3.rect.x >640:
            window.blit(lose2, (200, 200))
            finish = True
        display.update()
    else:
        sleep(3)
        finish = False
        speed_x = choice((3,-3))
        speed_y = choice((3,-3))
        score = 0
        sprite1.rect.x = 0
        sprite1.rect.y = 170
        sprite2.rect.x = 665
        sprite2.rect.y = 170
        sprite3.rect.x = 315
        sprite3.rect.y = 220
    clock.tick(FPS)
