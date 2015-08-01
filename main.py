#!/usr/bin/env python 
import sys
import random
import pygame as pg

# Importing prepare initializes the display.
import prepare
import actors
import level


class App(object):
    def __init__(self):
        """
        This is the main class that runs the program.
        """
        self.screen = pg.display.get_surface()
        self.screen_rect = self.screen.get_rect()
        self.clock = pg.time.Clock()
        self.fps = 60
        self.keys = pg.key.get_pressed()
        self.done = False
        ship = random.choice(list(prepare.GFX["ships"].values()))
        self.player = actors.Player((0,0), ship)
        self.level = level.Level(self.screen_rect.copy(), self.player)

    def event_loop(self):
        """
        End the program on quit event and update held keys on keyup or keydown.
        """
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.done = True
            elif event.type in (pg.KEYDOWN, pg.KEYUP):
                self.keys = pg.key.get_pressed()

    def display_fps(self):
        """
        Show the program's FPS in the window handle.
        """
        template = "{} - FPS: {:.2f}"
        caption = template.format(prepare.CAPTION, self.clock.get_fps())
        pg.display.set_caption(caption)

    def update(self):
        """
        Update necessary elements; currently only the level.
        """
        self.level.update(self.keys)
        
    def render(self):
        """
        Draw all elements.  Individual actor drawing handled by level instance.
        """
        self.screen.fill(prepare.BACKGROUND_COLOR)
        self.level.draw(self.screen)
        pg.display.update()

    def main_loop(self):
        """
        The main game loop.
        """
        while not self.done:
            self.event_loop()
            self.update()
            self.render()
            self.clock.tick(self.fps)
            self.display_fps()


def main():
    """
    Create an App and start the program.
    """
    App().main_loop()
    pg.quit()
    sys.exit()


if __name__ == "__main__":
    main()
