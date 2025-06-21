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
        if self.schematools.isatypeof(tocheck, self.single_types):
            print("pycheck: Using a schema for a singular type (str, int, bool, etc.) is bloated and may be unefficient.\npycheck: Switching to istype is reccomended.")

__all__ = ["Schema"]