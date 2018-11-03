from ..base.context import Context
from ..base.game_constants import SpriteType
from .. import res
from ..base.game_constants import Facing
from ..util.path_finder import get_border_with_obstacles, find_path, ActionType
from .enemy import Enemy

import pygame


class EnemyShielder(Enemy):
    __BASE_UP_SURFACE: pygame.Surface = None
    __BASE_DOWN_SURFACE: pygame.Surface = None
    __BASE_LEFT_SURFACE: pygame.Surface = None
    __BASE_RIGHT_SURFACE: pygame.Surface = None

    __SURFACE_UP: pygame.Surface = None
    __SURFACE_DOWN: pygame.Surface = None
    __SURFACE_LEFT: pygame.Surface = None
    __SURFACE_RIGHT: pygame.Surface = None

    _WIDTH = 1
    _HEIGHT = 1
    _ANIMATION_LENGTH = 4
    _MILISECONDS_PER_FRAME = 200
    _MOVE_COOLDOWN = 400

    def __init__(self):
        super().__init__([1, 1])
        if not EnemyShielder.__BASE_UP_SURFACE:
            EnemyShielder.__BASE_UP_SURFACE = pygame.image.load(res.IMG_DIR + "enemy/shielder/walk/up.png").convert_alpha()
            EnemyShielder.__BASE_DOWN_SURFACE = pygame.image.load(res.IMG_DIR + "enemy/shielder/walk/down.png").convert_alpha()
            EnemyShielder.__BASE_LEFT_SURFACE = pygame.image.load(res.IMG_DIR + "enemy/shielder/walk/left.png").convert_alpha()
            EnemyShielder.__BASE_RIGHT_SURFACE = pygame.image.load(res.IMG_DIR + "enemy/shielder/walk/right.png").convert_alpha()


        self.animation_i = 0
        self.frame_cooldown = 0

        self.lifes = 4
        self.max_lifes = 4

    @property
    def image(self):
        img = None
        if self.facing == Facing.FACING_UP:
            img = EnemyShielder.__SURFACE_UP
        elif self.facing == Facing.FACING_DOWN:
            img = EnemyShielder.__SURFACE_DOWN
        if self.facing == Facing.FACING_LEFT:
            img = EnemyShielder.__SURFACE_LEFT
        elif self.facing == Facing.FACING_RIGHT:
            img = EnemyShielder.__SURFACE_RIGHT

        return img.subsurface(
            pygame.Rect(
                self.tile_size * self.animation_i,
                0,
                self.tile_size,
                self.tile_size
            )
        )

    @property
    def sprite_type(self) -> SpriteType:
        return SpriteType.ENEMY

    @classmethod
    def update_render_context(cls, render_context):
        cls.__SURFACE_UP = pygame.transform.smoothscale(
            cls.__BASE_UP_SURFACE,
            (
                cls._WIDTH * cls.tile_size * cls._ANIMATION_LENGTH,
                cls._HEIGHT * cls.tile_size
            )
        )
        cls.__SURFACE_DOWN = pygame.transform.smoothscale(
            cls.__BASE_DOWN_SURFACE,
            (
                cls._WIDTH * cls.tile_size * cls._ANIMATION_LENGTH,
                cls._HEIGHT * cls.tile_size
            )
        )
        cls.__SURFACE_LEFT = pygame.transform.smoothscale(
            cls.__BASE_LEFT_SURFACE,
            (
                cls._WIDTH * cls.tile_size * cls._ANIMATION_LENGTH,
                cls._HEIGHT * cls.tile_size
            )
        )
        cls.__SURFACE_RIGHT = pygame.transform.smoothscale(
            cls.__BASE_RIGHT_SURFACE,
            (
                cls._WIDTH * cls.tile_size * cls._ANIMATION_LENGTH,
                cls._HEIGHT * cls.tile_size
            )
        )
