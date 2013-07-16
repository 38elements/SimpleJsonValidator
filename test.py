# coding: utf-8

from unittest import TestCase, main
from simple_json_validator import SimpleJsonValidator, SchemaError, ValidationError

class SchemaTest(TestCase):

    def setUp(self):
        pass

    def test_schema_type(self):
        self.assertRaises((SchemaError), SimpleJsonValidator, unicode)

    def test_check_schema_dict(self):
        sjv = SimpleJsonValidator(str)
        self.assertRaises((SchemaError), sjv.check_schema_dict, {(1,2): "1"}, "")
        self.assertTrue(sjv.check_schema_dict({"d": 1}, ""))
        self.assertTrue(sjv.check_schema_dict({u"d": 1}, ""))

    def test_check_schema_list(self):
        sjv = SimpleJsonValidator(str)
        self.assertRaises((SchemaError), sjv.check_schema_list, [int, int], "")
        self.assertTrue(sjv.check_schema_list([int], ""))

    def test_check_schema(self):
        SimpleJsonValidator([int])
        SimpleJsonValidator({"foo":int})
        SimpleJsonValidator({
                                "foo":int,
                                "bar": [str],
                                "hoge": {
                                        "foo": {
                                            "foo": str,
                                            "bar": int,
                                        },
                                        "bar": [str]
                                    }
                                })


class ValidationTest(TestCase):

    def setUp(self):
        pass

    def test_validate(self):
        schema = {
                    "name": str,
                    u"age": int,
                    "bool": bool,
                    "float": float,
                    "card_id": [int],
                    "friends": [
                                    {
                                        "name": str,
                                        "card_id": [int]
                                    }
                                ]
                 
                    }
        data = {
                    "name": "foo",
                    u"age": 22,
                    "bool": True,
                    "float": 1.22,
                    "card_id": [1,2,3,4,5],
                    "friends": [
                                    {
                                        "name": "ffff",
                                        "card_id": [2,3,4]
                                    },
                                    {
                                        "name": "feff",
                                        "card_id": [22,32,42]
                                    }
                                ]
                 
                    }
        sjv = SimpleJsonValidator(schema)
        self.assertTrue(sjv.validate(data))




if __name__ == '__main__':
    main()
