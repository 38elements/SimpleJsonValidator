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
        self.schema =  {
                    "name": str,
                    u"age": int,
                    "bool": bool,
                    "float": float,
                    "card_ids": [int],
                    "data" : {
                                "name": str,
                                "age": int
                            },
                    "friends": [
                                    {
                                        "name": str,
                                        "card_id": [int]
                                    }
                                ]

                    }

        self.data = {
                    "name": "foo",
                    u"age": 22,
                    "bool": True,
                    "float": 1.22,
                    "card_ids": [1,2,3,4,5],
                    "data" : {
                                "name": "foo",
                                "age": 12
                            },
                    "friends": [
                                    {
                                        "name": u"FFFF",
                                        "card_id": []
                                    },
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
        self.sjv = SimpleJsonValidator(self.schema)

    def test_validate(self):
        self.assertTrue(self.sjv.validate(self.data))

    def test_validate_str_type(self):
        """ strの型が合わない """
        self.data["str"] = 123
        self.assertRaises((ValidationError), self.sjv.validate, self.data)

    def test_validate_float_type(self):
        """ floatの型が合わない """
        self.data["float"] = 1
        self.assertRaises((ValidationError), self.sjv.validate, self.data)

    def test_validate_int_type(self):
        """ intの型が合わない """
        self.data[u"age"] = 1.09
        self.assertRaises((ValidationError), self.sjv.validate, self.data)

    def test_validate_bool_type(self):
        """ boolの型が合わない """
        self.data["bool"] = 1
        self.assertRaises((ValidationError), self.sjv.validate, self.data)

    def test_validate_list_type(self):
        """ リストの型が合わない """
        self.data["card_ids"] = "[]"
        self.assertRaises((ValidationError), self.sjv.validate, self.data)

    def test_validate_list_child_type(self):
        """ リストの要素の型が合わない """
        self.data["card_ids"].append("6")
        self.assertRaises((ValidationError), self.sjv.validate, self.data)

    def test_validate_dict_type(self):
        """ dictの型が合わない """
        self.data["data"] = "[]"
        self.assertRaises((ValidationError), self.sjv.validate, self.data)

    def test_validate_dict_key(self):
        """ dictのkeyの数が合わない """
        self.data["data"]["foo"] = "1"
        self.assertRaises((ValidationError), self.sjv.validate, self.data)

    def test_validate_dict_value(self):
        """ dictのvalueが合わない """
        self.data["data"]["age"] = "1"
        self.assertRaises((ValidationError), self.sjv.validate, self.data)


if __name__ == '__main__':
    main()
