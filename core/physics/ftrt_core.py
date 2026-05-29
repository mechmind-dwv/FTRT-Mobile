import math
from datetime import datetime

PLANETS = {
    "Mercury": 0.055,
    "Venus": 0.815,
    "Earth": 1.0,
    "Mars": 0.107,
    "Jupiter": 317.8,
    "Saturn": 95.2
}

def calculate_demo_ftrt():
    now = datetime.utcnow().timestamp()
    return round(1.5 + math.sin(now / 1000000), 3)
