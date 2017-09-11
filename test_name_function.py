import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """Tests for 'name_function.py'."""
    
    def test_first_name_last_name(self): 
        """Do names like 'Janis Joplin' work?"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')
        
    def test_first_last_middle_name(self):
        """Do names like 'John Lee Hooker' work?"""
        formatted_name = get_formatted_name('john', 'hooker', middle='lee')
        self.assertEqual(formatted_name, 'John Lee Hooker')
        
unittest.main()
