#!/usr/bin/python3
"""
Testing the base model by unittest
"""

import unittest
from models.base_model import BaseModel
import pycodestyle
from datetime import datetime
from io import StringIO
from unittest.mock import patch


class TestPycodestyle(unittest.TestCase):
    """
    test that we conform to PEP-8
    """
    def test_checking(self):
        """Testing
        pycodestyle"""
        style = pycodestyle.StyleGuide(quit=True)
        result = style.check_files(['models/base_model.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")


class TestDocuemntationOfAll(unittest.TestCase):
    """
    This class will have the unittesting of that the
    whole module is well documented
    """
    def test_module_doc(self):
        """
        Test if module documentation exists
        """
        boolVal = len(BaseModel.__module__.__doc__) > 1
        self.assertTrue(boolVal)

    def test_class_doc(self):
        """
        Test if module documentation exists
        """
        boolVal = len(BaseModel.__doc__) > 1
        self.assertTrue(boolVal)

    def test_init_doc(self):
        """
        Test if module documentation exists
        """
        boolVal = len(BaseModel.__init__.__doc__) > 1
        self.assertTrue(boolVal)

    def test_str_doc(self):
        """
        Test if module documentation exists
        """
        boolVal = len(BaseModel.__str__.__doc__) > 1
        self.assertTrue(boolVal)

    def test_save_doc(self):
        """
        Test if module documentation exists
        """
        boolVal = len(BaseModel.save.__doc__) > 1
        self.assertTrue(boolVal)

    def test_to_dict_doc(self):
        """
        Test if module documentation exists
        """
        boolVal = len(BaseModel.to_dict.__doc__) > 1
        self.assertTrue(boolVal)

# test is public
class TestClassAttributes(unittest.TestCase):
    """
    Testing that class attributes are working correctly
    """
    def test_attributes(self):
        """
        testing each attribute's type
        """
        self.assertEqual(BaseModel.id.__class__, str)
        self.assertEqual(BaseModel.created_at.__class__, datetime)
        self.assertEqual(BaseModel.updated_at.__class__, datetime)


class TestConstructorMethod(unittest.TestCase):
    """
    Testing the __init__ method
    """
    def setUp(self):
        """
        The setup method that will help us
        in testing the instance methods and cleaning up
        the memory each time
        """
        self.testObject1 = BaseModel()
        self.testObject2 = BaseModel()
        self.testObjKwarg1 = BaseModel(name="test")
        self.testObjKwarg2 = BaseModel(name="test", value=98)
        created_at = "2017-09-28T21:05:54.119427"
        updated_at = "2023-09-28T21:05:54.119427"
        self.testObjdate = BaseModel(created_at, updated_at)

    def tearDown(self):
        """
        The setup method that will help us
        in testing the instance methods and cleaning up
        the memory each time
        """
        pass

    def test_initialization(self):
        """
        Testing that instances are produced correctly
        """
        self.assertIsInstance(self.testObject1, BaseModel)
        self.assertIsInstance(self.testObject2, BaseModel)
        self.assertTrue(self.testObject1.id)
        self.assertEqual(self.testObject1.id.__class__, str)
        self.assertTrue(self.testObject1.created_at)
        self.assertEqual(self.testObject1.created_at.__class__, datetime)
        self.assertTrue(self.testObject1.updated_at)
        self.assertEqual(self.testObject1.updated_at.__class__, datetime)

    def test_instances_with_attrs(self):
        """
        test with keyworded attrs
        """
        self.assertEqual(self.testObjKwarg1.name, "test")
        self.assertEqual(self.testObjKwarg2.name, "test")
        self.assertEqual(self.testObjKwarg2.value, 98)

    def test_normal_attribute_type(self):
        """
        tests with random attributes and its values
        """
        self.assertIsInstance(self.testObjKwarg1.name, str)
        self.assertIsInstance(self.testObjKwarg2.name, str)
        self.assertIsInstance(self.testObjKwarg2.value, int)

    def test_kwargsInattrs(self):
        """
        Tests dates of creation and updating converting from string to
        datetime objects
        """
        self.assertFalse(self.testObjdate.created_at.__class__ == str)
        self.assertTrue(self.testObjdate.created_at.__class__ == datetime)
        self.assertFalse(self.testObjdate.updated_at.__class__ == str)
        self.assertTrue(self.testObjdate.updated_at.__class__ == datetime)


class TestStrMagicMethod(unittest.TestCase):
    """
    Testing __str__ magic method
    """
    def setUp(self):
        """
        The setup method that will help us
        in testing the instance methods and cleaning up
        the memory each time
        """
        self.testObject1 = BaseModel()
        self.testObject2 = BaseModel()
        self.testObjKwarg1 = BaseModel(name="test")
        self.testObjKwarg2 = BaseModel(name="test", value=98)
        created_at = "2017-09-28T21:05:54.119427"
        updated_at = "2023-09-28T21:05:54.119427"
        self.testObjdate = BaseModel(created_at, updated_at)

    def tearDown(self):
        """
        The setup method that will help us
        in testing the instance methods and cleaning up
        the memory each time
        """
        pass

    def test_type_output(self):
        """
        testing the type of output
        """
        self.assertIsInstance(str(self.testObject1), str)

    def test_output(self):
        """
        testing the output
        """
        name = self.testObjKwarg1.__class__.__name__
        id = self.testObjKwarg1.id
        dic = self.testObjKwarg1.__dict__
        expected = f"[{name}] ({id}) {dic}"
        self.assertEqual(str(self.testObjKwarg1), expected)

    def test_when_printed(self):
        """
        Testing the output of printing an object
        """
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            print(self.testObjKwarg1)
        printed_output = mock_stdout.getvalue().strip()
        name = self.testObjKwarg1.__class__.__name__
        id = self.testObjKwarg1.id
        dic = self.testObjKwarg1.__dict__
        pattern = f"[{name}] ({id}) {dic}"
        self.assertEqual(printed_output, pattern)


class TestSaveMethod(unittest.TestCase):
    """
    Testing the save method
    """
    def setUp(self):
        """
        The setup method that will help us
        in testing the instance methods and cleaning up
        the memory each time
        """
        self.testObject1 = BaseModel()
        self.testObject2 = BaseModel()
        self.testObjKwarg1 = BaseModel(name="test")
        self.testObjKwarg2 = BaseModel(name="test", value=98)
        created_at = "2017-09-28T21:05:54.119427"
        updated_at = "2023-09-28T21:05:54.119427"
        self.testObjdate = BaseModel(created_at, updated_at)

    def tearDown(self):
        """
        The setup method that will help us
        in testing the instance methods and cleaning up
        the memory each time
        """
        pass

    def test_if_time_is_updated(self):
        """
        Testing for the time of updating
        """
        time_1 = self.testObjKwarg1.updated_at
        self.testObjKwarg1.save()
        time_2 = self.testObjKwarg1.updated_at
        self.assertNotEqual(time_1, time_2)


class TestToDictMethod(unittest.TestCase):
    """
    testing to_dict() method
    """
    def setUp(self):
        """
        The setup method that will help us
        in testing the instance methods and cleaning up
        the memory each time
        """
        self.testObject1 = BaseModel()
        self.testObject2 = BaseModel()
        self.testObjKwarg1 = BaseModel(name="test")
        self.testObjKwarg2 = BaseModel(name="test", value=98)
        created_at = "2017-09-28T21:05:54.119427"
        updated_at = "2023-09-28T21:05:54.119427"
        self.testObjdate = BaseModel(created_at, updated_at)

    def tearDown(self):
        """
        The setup method that will help us
        in testing the instance methods and cleaning up
        the memory each time
        """
        pass

    def test_type_returned(self):
        """
        Testing that the return value is dict
        """
        self.assertIsInstance(self.testObject1.to_dict(), dict)

    def test_for_correct_keys(self):
        """
        testing for correct keys
        """
        self.assertIn("id", self.testObject1.to_dict())
        self.assertIn("created_at", self.testObject1.to_dict())
        self.assertIn("updated_at", self.testObject1.to_dict())
        self.assertIn("__class__", self.testObject1.to_dict())

    def test_content_returned(self):
        """
        Testing the content of the returned dict
        """
        ourDict = self.testObject2.to_dict()
        expected = dict()
        expected['__class__'] = type(self.testObject2).__name__
        expected['created_at'] = self.testObject2.created_at.isoformat()
        expected['updated_at'] = self.testObject2.updated_at.isoformat()
        expected['id'] = self.testObject2.id
        self.assertEqual(expected, ourDict)

    def test_with_added_attrs(self):
        """
        Test with added attributes
        """
        self.testObjdate.name = "a"
        self.testObjdate.mode = "w"
        ourDict = self.testObjdate.to_dict()
        expected = dict()
        expected['__class__'] = type(self.testObjdate).__name__
        expected['created_at'] = self.testObjdate.created_at.isoformat()
        expected['updated_at'] = self.testObjdate.updated_at.isoformat()
        expected['id'] = self.testObjdate.id
        expected['name'] = self.testObjdate.name
        expected['mode'] = self.testObjdate.mode
        self.assertEqual(expected, ourDict)


if __name__ == '__main__':
    unittest.main()
