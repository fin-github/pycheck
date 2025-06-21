# pycheck beta v0

class Anything: ...
class SchemaTools: # do not use as initilized!!!
    def gettype(tocheck):
        return type(tocheck)
    def istypeof(tocheck, validtype):
        return SchemaTools.gettype(tocheck) is validtype
    def isatypeof(tocheck, validtypes: list):
        for validtype in validtypes:
            if SchemaTools.istypeof(tocheck, validtype):
                return True
        return False
    
    def handle(schema, tovalidate) -> bool:
        if SchemaTools.istypeof(schema, list):
            return SchemaTools.Handlers.handle_list(schema, tovalidate)
        
        if SchemaTools.istypeof(schema, str):
            return SchemaTools.Handlers.handle_str(schema, tovalidate)
        
        if SchemaTools.istypeof(schema, int):
            return SchemaTools.Handlers.handle_int(schema, tovalidate)
        
        if SchemaTools.istypeof(schema, bool):
            return SchemaTools.Handlers.handle_bool(schema, tovalidate)
        
    class Handlers:
        def handle_str(schema, tovalidate):
            if isinstance(schema, str):
                return schema == tovalidate
            
            return SchemaTools.istypeof(tovalidate, str)
        
        def handle_int(schema, tovalidate):
            if isinstance(schema, int):
                return schema == tovalidate
            
            return SchemaTools.istypeof(tovalidate, int)
        
        def handle_bool(schema, tovalidate):
            if isinstance(schema, bool):
                return schema is tovalidate
            
            return SchemaTools.istypeof(tovalidate, bool)
        
        def handle_list(schema, tovalidate):
            ...
    
        
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
        
        # check if type is supported
        if not self.schematools.isatypeof(tocheck, self.valid_types):
            raise TypeError(f"pycheck: {tocheck} is not a valid type to check.")
        
        return self.schematools.handle(self.schema, tocheck)
        

__all__ = ["Schema", "Anything"]