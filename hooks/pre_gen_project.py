def main():
    # Set default parameters
    default_project_name = "A lowercase with hyphens name, e.g. my-new-project"
    default_project_description = "Your project description"

    # Verify project name
    if "{{cookiecutter.project_name}}" == default_project_name:
        raise Exception("The project_name can't be blank!")
    elif "{{cookiecutter.project_name}}".find("_") >= 0:
        raise Exception("The project_name can't contain underscores!")

    # Verify project description
    if "{{cookiecutter.project_description}}" == default_project_description:
        raise Exception("The project_description can't be blank!")

if __name__ == "__main__":
    main()
