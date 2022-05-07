from pandas import DataFrame

class Dataset():
    """ Classe para lidar com dois tipos de dataframe:
    sentence -> list<tag>
    token -> tag

    TODO: Deve ser capaz de transformar um dataframe no outro,
    ou então generalizar as operações o suficiente para que isso
    seja desnecessário.

    Criada para auxiliar no balanceamento de datasets NER.

    Idealmente, a classe deve conseguir lidar com qualquer tipo
    de dataframe NER.
    (e.g. token -> list<tags>)
    """
    def __init__(self, df: DataFrame):
        self.df = df
        self.text = df['text']
        self.tags = df['tags']
        pass
