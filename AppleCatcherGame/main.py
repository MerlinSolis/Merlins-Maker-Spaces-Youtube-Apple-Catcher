from raylib import *
from pyray import *
from os.path import join

class Player:
    def __init__(self,texture,position,speed):
        self.texture = texture
        self.position = position
        self.speed = speed
        self.direction = Vector2()

    def update(self,delta_time):

        # if is_key_down(KEY_A):
        #     self.direction.x = -1
        # elif is_key_down(KEY_D):
        #     self.direction.x = 1
        # else:
        #     self.direction.x = 0

        self.direction.x = is_key_down(KEY_D) - is_key_down(KEY_A)


        self.position.x += self.speed * self.direction.x * delta_time

        if self.position.x < 0:
            self.position.x = 0
        elif self.position.x + self.texture.width > get_screen_width():
            self.position.x = get_screen_width() - self.texture.width


    def draw(self):
        draw_texture_v(self.texture,self.position,WHITE)

class Game:
    def __init__(self):
        self.screen_width = 1600
        self.screen_height = 900
        self.title = "Apple Catcher Game"
        self.fps_cap = 60
        init_window(self.screen_width,self.screen_height,self.title)
        set_target_fps(self.fps_cap)

        player_texture = load_texture(join("assets","images","basket.png"))
        player_texture.width //= 2
        player_texture.height //= 2

        self.player_basket = Player(player_texture,Vector2(self.screen_width/2 - player_texture.width/2,self.screen_height * 0.85),600)

        bg_texture = load_texture(join("assets","images","bg_forest_image.png"))
        # self.bg_texture.width = self.screen_width
        # self.bg_texture.height = self.screen_height
        temp_img = load_image_from_texture(bg_texture)
        image_resize_nn(temp_img,self.screen_width,self.screen_height)
        self.bg_texture_resized = load_texture_from_image(temp_img)


    def draw_background(self):
        draw_texture(self.bg_texture_resized,0,0,WHITE)

    def update(self):
        delta_time = get_frame_time()
        print(delta_time)
        self.player_basket.update(delta_time)


    def draw(self):
        begin_drawing()
        clear_background(PURPLE)
        self.draw_background()
        self.player_basket.draw()
        # draw_fps(100,100)
        end_drawing()

    def run(self):
        while not window_should_close():
            self.update()
            self.draw()
            

        unload_texture(self.bg_texture_resized)
        close_window()




if __name__ == "__main__":
    game = Game()
    game.run()