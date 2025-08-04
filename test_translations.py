import unittest
import os
import sys
import importlib

# Add the parent directory to the sys.path to allow importing modules from 'lang'
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

class TestTranslations(unittest.TestCase):
    def test_load_all_languages(self):
        # Mapping of language codes to their class names
        lang_class_names = {
            'ar': 'Arabic',
            'de': 'German',
            'en': 'English',
            'es': 'Spanish',
            'fr': 'French',
            'hi': 'Hindi',
            'id': 'Indonesian',
            'it': 'Italian',
            'ja': 'Japanese',
            'ko': 'Korean',
            'nl': 'Dutch',
            'pl': 'Polish',
            'pt': 'Portuguese',
            'ru': 'Russian',
            'tr': 'Turkish',
            'vi': 'Vietnamese',
            'cn': 'Chinese', # Changed from zh_cn to cn
        }

        # List all subdirectories in 'lang/' which represent language categories
        lang_categories = [d for d in os.listdir(os.path.dirname(__file__)) if os.path.isdir(os.path.join(os.path.dirname(__file__), d)) and d != '__pycache__']

        for category in lang_categories:
            category_path = os.path.join(os.path.dirname(__file__), category)
            # List all language files (e.g., en.py, de.py) in each category
            lang_files = [f for f in os.listdir(category_path) if f.endswith('.py') and f != '__init__.py' and f != 'main.py']
            
            print(f"\nPlugin: {category} testing languages...")
            passed_count = 0
            total_files = len(lang_files)

            for lang_file in lang_files:
                lang_code = lang_file[:-3]  # Remove .py extension
                module_name = f"lang.{category}.{lang_code}"
                with self.subTest(lang=lang_code, category=category):
                    try:
                        # Dynamically import the module
                        module = importlib.import_module(module_name)
                        
                        # Get the correct class name from the mapping
                        class_name = lang_class_names.get(lang_code)
                        if not class_name:
                            self.fail(f"No class name mapping for language code: {lang_code}")

                        self.assertTrue(hasattr(module, class_name), f"Module {module_name} does not have a class named {class_name}.")
                        lang_class = getattr(module, class_name)

                        # Check if the 'strings' attribute exists within the class
                        self.assertTrue(hasattr(lang_class, 'strings'), f"Class {class_name} in {module_name} does not have a 'strings' attribute.")
                        # Optionally, check if 'strings' is a dictionary
                        self.assertIsInstance(lang_class.strings, dict, f"'strings' attribute in {class_name} of {module_name} is not a dictionary.")
                        passed_count += 1
                    except ImportError as e:
                        self.fail(f"Could not import {module_name}: {e}")
                    except Exception as e:
                        self.fail(f"Error loading {module_name}: {e}")
            
            if passed_count == total_files:
                print(f"Plugin: {category} all {passed_count}/{total_files} languages passed.")
            else:
                print(f"Plugin: {category} {passed_count}/{total_files} languages passed, but some failed.")

if __name__ == '__main__':
    unittest.main()