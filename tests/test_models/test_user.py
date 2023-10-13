#!/usr/bin/python3
"""
Testing the User model by unittest
"""

import unittest
from models.user import User
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
        result = style.check_files(['models/user.py'])
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
        boolVal = len(User.__module__.__doc__) > 1
        self.assertTrue(boolVal)

    def test_class_doc(self):
        """
        Test if module documentation exists
        """
        boolVal = len(User.__doc__) > 1
        self.assertTrue(boolVal)

    def test_init_doc(self):
        """
        Test if module documentation exists
        """
        boolVal = len(User.__init__.__doc__) > 1
        self.assertTrue(boolVal)

    def test_str_doc(self):
        """
        Test if module documentation exists
        """
        boolVal = len(User.__str__.__doc__) > 1
        self.assertTrue(boolVal)

    def test_save_doc(self):
        """
        Test if module documentation exists
        """
        boolVal = len(User.save.__doc__) > 1
        self.assertTrue(boolVal)

    def test_to_dict_doc(self):
        """
        Test if module documentation exists
        """
        boolVal = len(User.to_dict.__doc__) > 1
        self.assertTrue(boolVal)


class TestClassAttributes(unittest.TestCase):
    """
    Testing that class attributes are working correctly
    """
    def setUp(self):
        """
        The setup method that will help us
        in testing the instance methods and cleaning up
        the memory each time
        """
        self.Obj1 = User()
        self.Obj2 = User()
        self.ObjKw1 = User(name="test")
        self.ObjKw2 = User(name="test", value=98)
        created_at = "2017-09-28T21:05:54.119427"
        updated_at = "2023-09-28T21:05:54.119427"
        self.Objdt = User(created_at, updated_at)

    def tearDown(self):
        """
        teardown method
        """
        pass

    def test_Inherited_attributes(self):
        """
        testing each attribute's type
        """
        self.assertEqual(User.id.__class__, str)
        self.assertEqual(User.created_at.__class__, datetime)
        self.assertEqual(User.updated_at.__class__, datetime)

    def test_nonInherited_attributes(self):
        """
        testing each user object attribute's type
        """
        self.assertEqual(User.email.__class__, str)
        self.assertEqual(User.password.__class__, str)
        self.assertEqual(User.first_name.__class__, str)
        self.assertEqual(User.last_name.__class__, str)

    def test_is_public(self):
        """
        Test if the attributes are public
        """
        self.Obj1.email = "email@email.com"
        self.assertEqual(self.Obj1.email, "email@email.com")
        self.Obj1.password = "3487@2ksdj"
        self.assertEqual(self.Obj1.password, "3487@2ksdj")
        self.Obj1.first_name = "ayaa"
        self.assertEqual(self.Obj1.first_name, "ayaa")
        self.Obj1.last_name = "ragab"
        self.assertEqual(self.Obj1.last_name, "ragab")


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
        self.Obj1 = User()
        self.Obj2 = User()
        self.ObjKw1 = User(name="test")
        self.ObjKw2 = User(name="test", value=98)
        created_at = "2017-09-28T21:05:54.119427"
        updated_at = "2023-09-28T21:05:54.119427"
        self.Objdt = User(created_at, updated_at)

    def tearDown(self):
        """
        teardown method
        """
        pass

    def test_initialization(self):
        """
        Testing that instances are produced correctly
        """
        self.assertIsInstance(self.Obj1, User)
        self.assertIsInstance(self.Obj2, User)
        self.assertTrue(self.Obj1.id)
        self.assertEqual(self.Obj1.id.__class__, str)
        self.assertTrue(self.Obj1.created_at)
        self.assertEqual(self.Obj1.created_at.__class__, datetime)
        self.assertTrue(self.Obj1.updated_at)
        self.assertEqual(self.Obj1.updated_at.__class__, datetime)

    def test_instances_with_attrs(self):
        """
        test with keyworded attrs
        """
        self.assertEqual(self.ObjKw1.name, "test")
        self.assertEqual(self.ObjKw2.name, "test")
        self.assertEqual(self.ObjKw2.value, 98)

    def test_normal_attribute_type(self):
        """
        tests with random attributes and its values
        """
        self.assertIsInstance(self.ObjKw1.name, str)
        self.assertIsInstance(self.ObjKw2.name, str)
        self.assertIsInstance(self.ObjKw2.value, int)

    def test_kwargsInattrs(self):
        """
        Tests dates of creation and updating converting from string to
        datetime objects
        """
        self.assertFalse(self.Objdt.created_at.__class__ == str)
        self.assertTrue(self.Objdt.created_at.__class__ == datetime)
        self.assertFalse(self.Objdt.updated_at.__class__ == str)
        self.assertTrue(self.Objdt.updated_at.__class__ == datetime)



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
        self.Obj1 = User()
        self.Obj1.first_name = "Betty"
        self.Obj1.last_name = "Bar"
        self.Obj1.email = "airbnb@mail.com"
        self.Obj1.password = "root"
        self.Obj2 = User()
        self.Obj2.first_name = "Betty"
        self.Obj2.last_name = "Bar"
        self.Obj2.email = "airbnb@mail.com"
        self.Obj2.password = "root"
        self.ObjKw1 = User(name="test")
        self.ObjKw2 = User(name="test", value=98)
        created_at = "2017-09-28T21:05:54.119427"
        updated_at = "2023-09-28T21:05:54.119427"
        self.Objdt = User(created_at, updated_at)

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
        self.assertIsInstance(self.Obj1.to_dict(), dict)

    def test_for_correct_keys(self):
        """
        testing for correct keys
        """
        self.assertIn("id", self.Obj1.to_dict())
        self.assertIn("created_at", self.Obj1.to_dict())
        self.assertIn("updated_at", self.Obj1.to_dict())
        self.assertIn("__class__", self.Obj1.to_dict())
        self.assertIn("password", self.Obj1.to_dict())
        self.assertIn("email", self.Obj1.to_dict())
        self.assertIn("first_name", self.Obj1.to_dict())
        self.assertIn("last_name", self.Obj1.to_dict())

    def test_content_returned(self):
        """
        Testing the content of the returned dict
        """
        ourDict = self.Obj2.to_dict()
        expected = dict()
        expected['__class__'] = type(self.Obj2).__name__
        expected['created_at'] = self.Obj2.created_at.isoformat()
        expected['updated_at'] = self.Obj2.updated_at.isoformat()
        expected['email'] = self.Obj2.email
        expected['password'] = self.Obj2.password
        expected['first_name'] = self.Obj2.first_name
        expected['last_name'] = self.Obj2.last_name
        expected['id'] = self.Obj2.id
        self.assertEqual(expected, ourDict)

    def test_with_added_attrs(self):
        """
        Test with added attributes
        """
        self.Obj2.name = "a"
        self.Obj2.mode = "w"
        ourDict = self.Obj2.to_dict()
        expected = dict()
        expected['__class__'] = type(self.Obj2).__name__
        expected['created_at'] = self.Obj2.created_at.isoformat()
        expected['updated_at'] = self.Obj2.updated_at.isoformat()
        expected['email'] = self.Obj2.email
        expected['password'] = self.Obj2.password
        expected['first_name'] = self.Obj2.first_name
        expected['last_name'] = self.Obj2.last_name
        expected['id'] = self.Obj2.id
        expected['name'] = self.Obj2.name
        expected['mode'] = self.Obj2.mode
        self.assertEqual(expected, ourDict)


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
        self.Obj1 = User()
        self.Obj1.first_name = "Betty"
        self.Obj1.last_name = "Bar"
        self.Obj1.email = "airbnb@mail.com"
        self.Obj1.password = "root"
        self.Obj2 = User()
        self.Obj2.first_name = "Betty"
        self.Obj2.last_name = "Bar"
        self.Obj2.email = "airbnb@mail.com"
        self.Obj2.password = "root"
        self.ObjKw1 = User(name="test")
        self.ObjKw2 = User(name="test", value=98)
        created_at = "2017-09-28T21:05:54.119427"
        updated_at = "2023-09-28T21:05:54.119427"
        self.Objdt = User(created_at, updated_at)
    
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
        self.assertIsInstance(str(self.Obj1), str)

    def test_output(self):
        """
        testing the output
        """
        name = self.Obj1.__class__.__name__
        id = self.Obj1.id
        dic = self.Obj1.__dict__
        expected = f"[{name}] ({id}) {dic}"
        self.assertEqual(str(self.Obj1), expected)

    def test_when_printed(self):
        """
        Testing the output of printing an object
        """
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            print(self.Obj1)
        printed_output = mock_stdout.getvalue().strip()
        name = self.Obj1.__class__.__name__
        id = self.Obj1.id
        dic = self.Obj1.__dict__
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
        self.Obj1 = User()
        self.Obj1.first_name = "Betty"
        self.Obj1.last_name = "Bar"
        self.Obj1.email = "airbnb@mail.com"
        self.Obj1.password = "root"
        self.Obj2 = User()
        self.Obj2.first_name = "Betty"
        self.Obj2.last_name = "Bar"
        self.Obj2.email = "airbnb@mail.com"
        self.Obj2.password = "root"
        self.ObjKw1 = User(name="test")
        self.ObjKw2 = User(name="test", value=98)
        created_at = "2017-09-28T21:05:54.119427"
        updated_at = "2023-09-28T21:05:54.119427"
        self.Objdt = User(created_at, updated_at)
    
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
        time_1 = self.Obj1.updated_at
        self.Obj1.save()
        time_2 = self.Obj1.updated_at
        self.assertNotEqual(time_1, time_2)


if __name__ == '__main__':
    unittest.main()
