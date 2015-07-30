"""
This module contains the Player class for the user controlled character.
"""

import pygame as pg

import prepare


class Player(pg.sprite.Sprite):
    """
    This class represents our user controlled character.
    """
    def __init__(self, pos, image, speed=7, *groups):
        super(Player, self).__init__(*groups)
        self.speed = speed
        self.image = pg.transform.rotozoom(image, 90, prepare.SCALE_FACTOR)
        self.rect = self.image.get_rect(center=pos)

    def update(self, keys, bounding):
        """
        Updates the players position based on currently held keys.
        """
        move = self.check_keys(keys)
        self.rect.move_ip(*move)
        self.rect.clamp_ip(bounding)

    def check_keys(self, keys):
        """
        Find the players movement vector from key presses.
        """
        move = [0, 0]
        for key in prepare.DIRECT_DICT:
            if keys[key]:
                for i in (0, 1):
                    move[i] += prepare.DIRECT_DICT[key][i]*self.speed
        return move

    def draw(self, surface):
        """
        Basic draw function. (not  used if drawing via groups)
        """
        surface.blit(self.image, self.rect)
