from src.baseclient import BaseClient

class Assortiment:
    def __init__(self, base: BaseClient):
        self.base = base
        self.assortiment_prefix = "assortiment"
