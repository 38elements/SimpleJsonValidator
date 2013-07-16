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
            raise SchemaError("InValid type at key=%s path=%s.  schema is %s" % (key, path, pprint.pformat(data)))
        if self.is_dict(data):
            self.check_schema_dict(data, path)
            for target_key, target_data in data.iteritems():
                self.check_schema(target_data, target_key, path)
        elif self.is_list(data):
            self.check_schema_list(data, path)
            self.check_schema(data[0], "[0]", path)
        return True

    def validate_dict(self, data, schema, key, path):
        pass

    def validate_list(self, data, schema, key, path):
        pass

    def validate_string(self, data, schema, key, path):
        if not self.is_string(data):
            raise ValidationError("ValidationError: %s is not string. key=%s, path=%s, data=%s" % (key, path, str(data)))

    def validate_number(self, data, schema, key, path):
        if not self.is_number(data):
            raise ValidationError("ValidationError: %s is not number. key=%s, path=%s, data=%s" % (key, path, str(data)))

    def validate_float(self, data, schema, key, path):
        if not self.is_float(data):
            raise ValidationError("ValidationError: %s is not float. key=%s, path=%s, data=%s" % (key, path, str(data)))

    def validate_bool(self, data, key, path):
        if not self.is_bool(data):
            raise ValidationError("ValidationError: %s is not bool. key=%s, path=%s, data=%s" % (key, path, str(data)))

    def validate(self, data, schema=None, key="", path=""):
        schema = self.schema if schema == None else schema
        key = str(key)
        path += "." + key
        if is_dict(schema):
            pass
        elif is_list(schema):
            pass
        elif schema in (int, long):
            self.validate_number(data, key, path)
        elif schema in (float,):
            self.validate_float(data, key, path)
        elif schema in (bool,):
            self.validate_bool(data, key, path)
        elif schema in (str, unicode):
            self.validate_string(data, key, path)
        else:
            ValidationError("Not Support type: type is %s" % (str(schema),))
        return True


class ValidationError(Exception):
    pass


class SchemaError(Exception):
    pass
