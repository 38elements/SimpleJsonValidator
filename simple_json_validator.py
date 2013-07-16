# coding: utf-8


class SimpleJsonValidator(object):

    def __init__(self, schema):
        self.check_schema(schema)
        self.__schema = schema
        self.__types = (int, long, float, bool, str, unicode, list, dict)

    def check_schema(schema):
        pass

    def validate(self, data):
        pass



class ValidationError(Error):
    pass


class SchemaError(Error):
    pass
