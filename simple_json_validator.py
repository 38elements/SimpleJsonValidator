# coding: utf-8
import pprint

class SimpleJsonValidator(object):

    def __init__(self, schema):
        self.__schema = schema
        self.__types = (int, float, bool, str)
        self.__target_types = (int, long, float, bool, str, unicode)
        self.__structures = (list, dict)
        self.check_schema(schema)

    def is_number(self, data):
        return isinstance(data, (int, long)) and not isinstance(data, bool)

    def is_float(self, data):
        return isinstance(data, float)

    def is_bool(self, data):
        return isinstance(data, bool)

    def is_string(self, data):
        return isinstance(data, (str, unicode))

    def is_list(self, data):
        return isinstance(data, list)

    def is_dict(self, data):
        return isinstance(data, dict)

    def check_schema_dict(self, dict_data, path):
        for key in dict_data:
            if not self.is_string(key) and len(key) > 0:
                raise SchemaError("InValid key: %s is not string. path=%s" % (key, path))
        return True

    def check_schema_list(self, list_data, path):
        if not len(list_data) == 1:
            raise SchemaError("InValid lengh: list len is not 1. path=%s" % (path,))
        return True

    def check_schema(self, data, key="", path=""):
        key = str(key)
        path += "." + key
        if not isinstance(data, self.__structures) and not data in self.__types:
            raise SchemaError("InValid type at key='%s' path='%s'.  schema is %s" % (key, path, pprint.pformat(data)))
        if self.is_dict(data):
            self.check_schema_dict(data, path)
            for target_key, target_data in data.iteritems():
                self.check_schema(target_data, target_key, path)
        elif self.is_list(data):
            self.check_schema_list(data, path)
            self.check_schema(data[0], "[0]", path)
        return True

        

    def validate(self, data, schema=None):
        schema = self.schema if schema == None else schema




class ValidationError(Exception):
    pass


class SchemaError(Exception):
    pass
