import importlib
import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


class TestTranslations(unittest.TestCase):
    def test_load_all_languages(self):
        COLOR_GREEN = '\033[92m'
        COLOR_RED = '\033[91m'
        COLOR_RESET = '\033[0m'

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
            'cn': 'Chinese',
        }

        lang_categories = [d for d in os.listdir(os.path.dirname(__file__)) if os.path.isdir(os.path.join(os.path.dirname(__file__), d)) and d not in ['__pycache__', '.vscode']]

        for category in lang_categories:
            category_path = os.path.join(os.path.dirname(__file__), category)
            lang_files = [f for f in os.listdir(category_path) if f.endswith('.py') and f != '__init__.py' and f != 'main.py']
            print(f"\n{category} testing languages...")
            passed_count = 0
            total_files = len(lang_files)

            for lang_file in lang_files:
                lang_code = lang_file[:-3]
                module_name = f"{category}.{lang_code}"
                sys.stdout.write(f"  - {lang_code}: checking...{' ' * 10}\r")
                sys.stdout.flush()

                with self.subTest(lang=lang_code, category=category):
                    try:
                        module = importlib.import_module(module_name)
                        class_name = lang_class_names.get(lang_code)
                        if not class_name:
                            self.fail(f"No class name mapping for language code: {lang_code}")

                        self.assertTrue(hasattr(module, class_name), f"Module {module_name} does not have a class named {class_name}.")
                        lang_class = getattr(module, class_name)

                        self.assertTrue(hasattr(lang_class, 'strings'), f"Class {class_name} in {module_name} does not have a 'strings' attribute.")
                        self.assertIsInstance(lang_class.strings, dict, f"'strings' attribute in {class_name} of {module_name} is not a dictionary.")

                        sys.stdout.write(f"  - {lang_code}: {COLOR_GREEN}passed{COLOR_RESET}{' ' * 10}\n")
                        sys.stdout.flush()
                        passed_count += 1

                    except ImportError as e:
                        sys.stdout.write(f"  - {lang_code}: {COLOR_RED}failed ({e}){COLOR_RESET}{' ' * 10}\n")
                        sys.stdout.flush()
                        self.fail(f"Could not import {module_name}: {e}")

                    except Exception as e:
                        sys.stdout.write(f"  - {lang_code}: {COLOR_RED}failed ({e}){COLOR_RESET}{' ' * 10}\n")
                        sys.stdout.flush()
                        self.fail(f"Error loading {module_name}: {e}")

            main_module_name = f"{category}.main"
            expected_string_var = f"{category}_strings"
            if category == "gen_html":
                expected_string_var = "generate_html_strings"

            sys.stdout.write(f"  - main.py: checking...{' ' * 10}\r")
            sys.stdout.flush()
            with self.subTest(lang="main.py", category=category):
                try:
                    main_module = importlib.import_module(main_module_name)
                    self.assertTrue(hasattr(main_module, expected_string_var), f"Module {main_module_name} does not have a '{expected_string_var}' attribute.")
                    self.assertIsInstance(getattr(main_module, expected_string_var), dict, f"'{expected_string_var}' attribute in {main_module_name} is not a dictionary.")
                    sys.stdout.write(f"  - main.py: {COLOR_GREEN}passed{COLOR_RESET}{' ' * 10}\n")
                    sys.stdout.flush()
                    passed_count += 1
                    total_files += 1

                except ImportError as e:
                    sys.stdout.write(f"  - main.py: {COLOR_RED}failed ({e}){COLOR_RESET}{' ' * 10}\n")
                    sys.stdout.flush()
                    self.fail(f"Could not import {main_module_name}: {e}")

                except Exception as e:
                    sys.stdout.write(f"  - main.py: {COLOR_RED}failed ({e}){COLOR_RESET}{' ' * 10}\n")
                    sys.stdout.flush()
                    self.fail(f"Error loading {main_module_name}: {e}")

            if passed_count == total_files:
                print(f"Plugin: {category} all {COLOR_GREEN}{passed_count}/{total_files} languages passed.{COLOR_RESET}")
            else:
                print(f"Plugin: {category} {COLOR_RED}{passed_count}/{total_files} languages passed, but some failed.{COLOR_RESET}")


if __name__ == '__main__':
    unittest.main()
