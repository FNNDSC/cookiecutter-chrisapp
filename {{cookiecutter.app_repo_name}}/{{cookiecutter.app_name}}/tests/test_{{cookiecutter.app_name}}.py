
from unittest import TestCase
from unittest import mock
from {{ cookiecutter.app_name }}.{{ cookiecutter.app_name }} import {{ cookiecutter.app_python_class_name }}


class {{ cookiecutter.app_python_class_name }}Tests(TestCase):
    """
    Test {{ cookiecutter.app_python_class_name }}.
    """
    def setUp(self):
        self.app = {{ cookiecutter.app_python_class_name }}()

    def test_run(self):
        """
        Test the run code.
        """
        args = []
        if self.app.TYPE == 'ds':
            args.append('inputdir') # you may want to change this inputdir mock
        args.append('outputdir')  # you may want to change this outputdir mock

        # you may want to add more optional arguments to test your app with
        # eg.
        # args.append('--custom-int')
        # args.append(10)

        options = self.app.parse_args(args)
        self.app.run(options)

        # write your own assertions
        self.assertEqual(options.outputdir, 'outputdir')
