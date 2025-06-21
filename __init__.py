# pycheck beta v0

class Anything: ...
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
        """
        Examples Schemas:
        
        str = Expecting a str value
        int = Expecting a int value
        etc.
        
        [str, int, bool] = Expecting a list with the types being str, int, bool
        ["Abc", 123, True] = Expecting a list with the exact values of "Abc", 123, and True
        ["Abc", int, True] = Expecting a list with the exact values of "Abc", an int, and True
        [Anything, int, Anything] = Expecting a list with any item, then an int, then any item  (WARNING: Anything is an actual class within pycheck)
        *Same with a tuple
        
        {
            str: "a",
            "a": int
        } = 
        Expecting a string value to the string "a", then the string "a" to an int
        """
        # statics
        self.valid_types: list = [str, int, bool, dict]
        self.single_types: list = [str, int, bool]
        self.schematools = SchemaTools
        
        # argument handlers
        self.schema = schema
    
    def check(self, tocheck):
        if self.schematools.isatypeof(tocheck, self.single_types):
            print("pycheck: Using a schema for a singular type (str, int, bool, etc.) is bloated and may be unefficient.\npycheck: Switching to istype is reccomended.")
        

__all__ = ["Schema", "Anything"]