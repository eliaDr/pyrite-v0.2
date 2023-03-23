import pygame

from .entity import Entity

class Player(Entity):
    def __init__(self, pos, size, type=None, image_info=None, movement=None):
        """
        pos = player spawn
        size = player size
        type = None ?Playable or moved
        image_info = None ?img_path, is_animated bool
        """
        if movement:
            super().__init__(pos, size, movement)
        else:
            super().__init__(pos, size)
        
        if image_info:
            self.load_images(image_info[0], image_info[1], (self.width, self.height), image_info[2])
            
        self.animation = 'idle'
        self.animation_loader.set_animation(self.animation)
        self.animation_loader.update(self)
        self.rect = self.image.get_rect()
        
    def update(self, keys, dt):
        self.move(self, keys, dt)
        self.animation_loader.update(self)