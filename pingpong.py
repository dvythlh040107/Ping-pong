from pygame import *

class GameSprite (sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, wight, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (wight, height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
        
class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
            
back = (200, 255, 255)
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
window.fill(back)

game = True
finish = False
clock = time.Clock()
FPS = 60

score1 = 0
score2 = 0
max_score = 3

racket1 = Player('racket.png', 30, 200, 4, 40, 120)  
racket2 = Player('racket.png', 520, 200, 4, 40, 120) 
ball = GameSprite('tenis_ball.png', 200, 200, 4, 50, 50) 

font.init()
font = font.Font(None, 35)

speed_x = 3
speed_y = 3

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
            
    if finish != True:
        window.fill(back)
        racket1.update_l()
        racket2.update_r()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
            
        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
            speed_x *= -1
            speed_y *= 1
                
        if ball.rect.y > win_height-50 or ball.rect.y < 0:
            speed_y *= -1
                
        if ball.rect.x < 0:
            score2 += 1
            ball.rect.x, ball.rect.y = win_width // 2, win_height // 2
            speed_x *= -1
                
        if ball.rect.x > win_width:
            score1 += 1
            ball.rect.x, ball.rect.y = win_width // 2, win_height // 2  
            speed_x *= -1
        
        if score1 == max_score:
            finish = True
            window.blit(font.render('PLAYER 1 WINS!', True, (0, 180, 0)), (200, 250))
            
        if score2 == max_score:
            finish = True
            window.blit(font.render('PLAYER 2 WINS!', True, (0, 180, 0)), (200, 250))
        
        score_text = font.render(f"Score: {score1} - {score2}", True, (0, 0, 0))
        window.blit(score_text, (10, 10))
                
        racket1.reset()
        racket2.reset()
        ball.reset()
            
    display.update()
    clock.tick(FPS)