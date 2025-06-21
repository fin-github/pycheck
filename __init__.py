# pycheck beta v0

class Schema:
    def __init__(self, schema):
        self.valid_types: list = [str, int, bool, dict]
        self.schema = schema
    
    def check(self, tocheck):
        ...

__all__ = ["Schema"]