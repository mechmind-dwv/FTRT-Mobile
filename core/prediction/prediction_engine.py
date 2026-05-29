def classify_ftrt(value):
    if value < 0.8:
        return "NORMAL"
    elif value < 1.2:
        return "MODERADO"
    elif value < 1.8:
        return "ELEVADO"
    elif value < 2.5:
        return "CRITICO"
    return "EXTREMO"
