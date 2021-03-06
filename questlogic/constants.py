"""
Symbolic constants for questlogic.
"""
from enum import Enum

valid_terrains = set([0, 1, 2, 3, 4, 5, 6, 7, 8])

TERRAIN_NAMES = {
    0: 'Wall',
    1: 'Road',
    2: 'Mountain',
    3: 'Land',
    4: 'Water',
    5: 'Sand',
    6: 'Forest',
    7: 'Swamp',
    8: 'Snow'
}


class Terrain(Enum):
    """ Terrain type constants """
    WALL = 0
    ROAD = 1
    MOUNTAIN = 2
    LAND = 3
    WATER = 4
    SAND = 5
    FOREST = 6
    SWAMP = 7
    SNOW = 8


class MoveDir(Enum):
    """ Character movement constants """
    UP = 1
    DOWN = 2
    RIGHT = 3
    LEFT = 4


class Algorithm(Enum):
    """ Algorithm type constants """
    BFS = 1
    DFS = 2
    IDS = 3


class Heroes(Enum):
    HUMAN = 1
    MONKEY = 2
    OCTOPUS = 3
    CROCODILE = 4
    SASQUATCH = 5
    WEREWOLF = 6


class Missions(Enum):
    KEY = 1
    TEMPLE = 2
    STONES = 3
    FRIEND = 4
    NO_MISSION = 5
