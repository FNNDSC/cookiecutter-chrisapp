import os
import unittest
import pathlib
from yaml import safe_load
from tempfile import TemporaryDirectory
from cookiecutter.main import cookiecutter

class TestCookiecutterChrisapp(unittest.TestCase):
    def setUp(self):
        self.location = os.getenv(
            'GITHUB_WORKSPACE',
            str(pathlib.Path(__file__).parent.parent.absolute())
        )
        self.testdir = TemporaryDirectory()
        os.chdir(self.testdir.name)

    def tearDown(self):
        os.chdir(self.location)
        self.testdir.cleanup()

    def test_yaml_is_valid(self):
        user_input = {
            'app_repo_name': 'pl-validate_yaml'
        }
        cookiecutter(self.location, no_input=True, extra_context=user_input)

        self.assertTrue(os.path.isfile('pl-validate_yaml/.github/workflows/ci.yml'))

        with open('pl-validate_yaml/.github/workflows/ci.yml') as f:
            result = safe_load(''.join(f.readlines()))

        self.assertIn('jobs', result)
        self.assertIn('test', result['jobs'])
        self.assertNotIn('if', result['jobs']['test'])

    def test_tests_can_be_skipped(self):
        user_input = {
            'app_repo_name': 'pl-skip_tests',
            'test_automatically': 'no'
        }
        cookiecutter(self.location, no_input=True, extra_context=user_input)

        with open('pl-skip_tests/.github/workflows/ci.yml') as f:
            result = safe_load(''.join(f.readlines()))

        self.assertIn('jobs', result)
        self.assertIn('test', result['jobs'])
        self.assertIn('if', result['jobs']['test'])
        self.assertEqual('false', str(result['jobs']['test']['if']).lower())

if __name__ == '__main__':
    unittest.main()
