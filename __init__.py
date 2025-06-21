# pycheck beta v0

class SchemaTools: # do not use as initilized!!!
    def istypeof(tocheck, validtype):
        return type(tocheck) is validtype
    def isatypeof(tocheck, validtypes: list):
        for validtype in validtypes:
            if SchemaTools.istypeof(tocheck, validtype):
                return True
        return False
        
class Schema:
    def __init__(self, schema):
        # statics
        self.valid_types: list = [str, int, bool, dict]
        self.single_types: list = [str, int, bool]
        self.schematools = SchemaTools
        
        # argument handlers
        self.schema = schema
    
    def check(self, tocheck):
        ...

__all__ = ["Schema"]