# pycheck beta v0

class Schema:
    def __init__(self, schema):
        self.schema = schema
    
    def check(self, tocheck):
        ...

__all__ = ["Schema"]