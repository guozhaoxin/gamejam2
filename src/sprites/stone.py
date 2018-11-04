import pygame

from src import RenderContext
from ..base.context import Context
from ..base.game_constants import SpriteType
from ..base.sprite import Sprite
from ..base.position import Position
from ..res import IMG_DIR


class Stone(Sprite):
    __BASE_SURFACE: pygame.Surface = None
    __SURFACE: pygame.Surface = None

    def __init__(self, x: int, y: int):
        super().__init__()
        self.width = 1
        self.height = 1
        self.position = Position(x, y)

    def update(self, context: Context):
        pass

    @property
    def image(self) -> pygame.Surface:
        return Stone.__SURFACE

    @property
    def sprite_type(self) -> SpriteType:
        return SpriteType.STATIC

    @classmethod
    def update_render_context(cls, render_context: RenderContext):
        if not cls.__BASE_SURFACE:
            cls.__BASE_SURFACE = pygame.image.load(IMG_DIR + "room/stone/stone.png")
        cls.__SURFACE = pygame.transform.smoothscale(
            cls.__BASE_SURFACE,
            (
                cls.tile_size,
                cls.tile_size
            )
        )


class BreakableStone(Sprite):
    __BASE_SURFACE: pygame.Surface = None
    __SURFACE: pygame.Surface = None

    def __init__(self, x: int, y: int):
        super().__init__()
        self.width = 1
        self.height = 1
        self.position = Position(x, y)

    def update(self, context: Context):
        pass

    @property
    def image(self) -> pygame.Surface:
        return BreakableStone.__SURFACE

    @property
    def sprite_type(self) -> SpriteType:
        return SpriteType.STATIC

    @classmethod
    def update_render_context(cls, render_context: RenderContext):
        if not cls.__BASE_SURFACE:
            cls.__BASE_SURFACE = pygame.image.load(IMG_DIR + "room/stone/stone_breakable.png")
        cls.__SURFACE = pygame.transform.smoothscale(
            cls.__BASE_SURFACE,
            (
                cls.tile_size,
                cls.tile_size
            )
        )


class MovableStone(Sprite):
    __BASE_SURFACE: pygame.Surface = None
    __SURFACE: pygame.Surface = None

    def __init__(self, x: int, y: int):
        super().__init__()
        self.width = 1
        self.height = 1
        self.position = Position(x, y)

    def update(self, context: Context):
        pass

    @property
    def image(self) -> pygame.Surface:
        return Stone.__SURFACE

    @property
    def sprite_type(self) -> SpriteType:
        return SpriteType.STATIC

    @classmethod
    def update_render_context(cls, render_context: RenderContext):
        if not cls.__BASE_SURFACE:
            cls.__BASE_SURFACE = pygame.image.load(IMG_DIR + "room/stone/stone_moveable.png")
        cls.__SURFACE = pygame.transform.smoothscale(
            cls.__BASE_SURFACE,
            (
                cls.tile_size,
                cls.tile_size
            )
        )
