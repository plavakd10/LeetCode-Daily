def finalPositionOfSnake(n: int, commands) -> int:
    d = {"LEFT":-1,
        "RIGHT":1,
        "UP":-n,
        "DOWN":n
    }

    return sum(map(lambda x: d[x], commands))

