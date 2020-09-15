from .{{ cookiecutter.app_name }} import {{ cookiecutter.app_python_class_name }}


def main():
    chris_app = {{ cookiecutter.app_python_class_name }}()
    chris_app.launch()


if __name__ == "__main__":
    main()
