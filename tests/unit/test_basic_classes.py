import unittest
import os

from psaspotter.extract import ExtractPlatformSpecificDir
from psaspotter.projects import Project

class TestCallForFunctions(unittest.TestCase):

    def test_simple(self):
        result_value = 4
        expect_value = 4
        self.assertEqual(result_value, expect_value)
    
    def test_length(self):
        directory = f"tests{os.sep}classes" # only one file
        project = Project.build(directory, "repository_name", "commit", "psaspotter/apis-all.json")
        extract = ExtractPlatformSpecificDir(project)
        apis = extract.touch()
        self.assertEqual(14, len(apis))
    
    def test_contains(self):
        directory = f"tests{os.sep}classes" # only one file
        project = Project.build(directory, "name", "hash", "psaspotter/apis-all.json")
        extract = ExtractPlatformSpecificDir(project)
        apis = extract.touch()

        call_one = ['name','hash', 'asyncio.Task', 'Emscripten:False,WASI:False', '/treat_custom_class.py', 5, 'https://github.com/name/blob/hash/treat_custom_class.py#L5', False]
        call_two = ['name','hash', 'asyncio.wait', 'Emscripten:False,WASI:False', '/treat_custom_class.py', 6, 'https://github.com/name/blob/hash/treat_custom_class.py#L6', False]
        call_three = ['name','hash', 'asyncio.Task', 'Emscripten:False,WASI:False', '/treat_custom_class.py', 7, 'https://github.com/name/blob/hash/treat_custom_class.py#L7', False]
        
        self.assertIn(call_one, apis)    
        self.assertIn(call_two, apis)    
        self.assertIn(call_three, apis)    

if __name__ == '__main__':
    unittest.main()