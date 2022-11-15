from enum import Enum

class Sex(Enum):
    MALE = 1
    FEMALE = 0

class ChestPain(Enum):
    TYPICAL_ANGINA = 0
    ATYPICAL_ANGINA = 1
    NON_ANGINAL_PAIN = 2
    ASYMPTOMATIC = 3

class ECG(Enum):
    NORMAL = 0
    ABNORMAL = 1
    HYPERTROPHY = 2

class Slope(Enum):
    UP = 1
    FLAT = 2
    DOWN = 3

class HeartAttack(Enum):
    Likely = 1
    NotLikely = 0
