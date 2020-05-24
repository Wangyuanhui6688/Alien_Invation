import sys

import pygame

from settings import Settings

from ship import Ship

class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init() #初始化所有Pygame模块，主要为了安全
        self.settings = Settings() #创建一个Settings类的实例，这样在程序中就可以引用Settings中的属性了

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height)) # display 是一个模块，set_mode 是该模块内部的功能，创建了Pygame.Surface该类的实例，并返回该实例。

        pygame.display.set_caption("Alien Invasion") # 创建窗口的标题栏

        self.ship = Ship(self) #创建战舰这个类的实例

    def run_game(self):
        """Start the main loop for the game"""
        while True:
            # Watch for keyboard and mouse events.
            for event in pygame.event.get(): # pygame.event.get()返回事件的列表
                if event.type == pygame.QUIT:
                    sys.exit()

            # Redraw the screen during each pass through the loop.
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()
            # Make the most recently drawn screen visible.
            pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()
