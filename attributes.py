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
    UP = 0
    FLAT = 1
    DOWN = 2

class HeartAttack(Enum):
    Likely = 1
    NotLikely = 0

class Thalassemia(Enum):
    NULL = 0
    FIXED_DEFECT = 1
    NORMAL = 2
    REVERSABLE_DEFECT = 3

class BloodSugarLevel(Enum):
    DIABETE = 1
    NORMAL = 0

class ExerciseInducedAngina(Enum):
    YES = 1
    NO = 0