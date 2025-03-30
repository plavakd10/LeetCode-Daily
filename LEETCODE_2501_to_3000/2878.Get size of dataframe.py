import pandas as pd
def getDataframeSize(players: pd.DataFrame):
    return [players.shape[0],players.shape[1]]