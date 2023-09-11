import os
import pathlib


def main():
    # Set global variables
    project_directory = os.path.realpath(os.path.curdir)
    #project_directory = os.path.dirname(os.path.abspath(__file__))

    # Set requests flag
    requests_flag = "{{cookiecutter.requests_flag}}"

    # Verify requests flag
    if requests_flag in ["Y", "y"]:
        # Update requirements file
        requirements_path = os.path.join(project_directory, "requirements.txt")

        with open(requirements_path, "a+") as f:
            requirements_content = f.read()
            requirements_content += "requests==2.31.0\n"
            f.write(requirements_content)

        # Update main file
        main_path = os.path.join(project_directory, "main.py")

        with open(main_path, "a+") as f:
            main_content = f.read()
            main_content += "import requests\n"
            f.write(main_content)

if __name__ == "__main__":
    main()
