<h1 style="margin-top: 1em; text-align: center;">
  <p> <img src="https://media.giphy.com/media/hvRJCLFzcasrR4ia7z/giphy.gif" alt="Waving Hand" width="25px" height="25px"> Welcome to Tubonge!</p>
</h1>

Tubonge is a blogging application built primarily in django. This README aims to provide comprehensive information about the project including:
- Project description
- Project setup
- Project structure
- License information
- Acknowledgments, and links to other important files.

<hr>

## Table of Contents

- [Project Description](#project-description)
- [Project Set Up](#project-set-up)
- [Project Structure](#project-structure)
- [License Information](#license-information)
- [Acknowledgments](#acknowledgments)
- [Links to Other Important Files](#links-to-other-important-files)

## Project Description

Tubonge is a mini social media application that allows users to share blogs on various happenings world wide. Built using django it has the following features:

> **TO BE ADDED**

## Project Set Up

Follow these steps to get the project up and running on your local machine:

1. **Clone the repository**

   Open your terminal and run the following command:

   ```bash
   $ git clone https://github.com/mbuguadouglas/tubonge.git
   ```

2. **Navigate into the directory**

   Change your current directory and move into the project's directory:

   ```bash
   $ cd tubonge
   ```

3. **Create a virtual environment and install the neccesary packages**

   Run the following command to create a virtual environment:

   ```bash
   $ python -m venv .venv
   ```

   Once created, you need to download all the neccessary packages:

   ```bash
   $ pip install -r requirements.txt
   ```

> This only works on a Linux OS. if using a Windows or Mac, figure out how to activate it [here](https://chatgpt.com)


4. **Start the development server**

   Now you can navigate to the top level of your repository and start the server:

   ```bash
   $ cd tubonge
   $ python manage.py runserver
   ```

   The project should now be running at http://127.0.0.1:8000/blog 

## Project Structure

The project follows a standard directory structure:

```
.
├── docs
│   └── CONTRIBUTING.md
├── LICENSE
├── README.md
├── requirements.txt
├── tree.txt
└── tubonge
    ├── blog
    │   ├── admin.py
    │   ├── apps.py
    │   ├── forms.py
    │   ├── __init__.py
    │   ├── migrations
    │   │   ├── 
    │   ├── models.py
    │   ├── __pycache__
    │   │   ├── 
    │   ├── static
    │   │   └── css
    │   ├── templates
    │   │   ├── blog
    │   │   └── pagination.html
    │   ├── tests.py
    │   ├── urls.py
    │   └── views.py
    ├── db.sqlite3
    ├── manage.py
    └── tubonge
        ├── asgi.py
        ├── __init__.py
        ├── __pycache__
        │   ├── 
        ├── settings.py
        ├── urls.py
        └── wsgi.py

13 directories, 46 files

```

- `docs` contains documents on the project documenation
- `tubonge` is the main project directory
- `tubonge/tubonge` is the main application within the project. It is the top most level
- `tubonge/blog` is a reusable component within the project. Contains funtionality for main blogging activities.

## Communication Channels

- **[GitHub Issues](https://github.com/mbuguadouglas/tubonge/issues)**: Use GitHub Issues to report bugs, track feature requests, and discuss specific issues related to the project.

## License Information

The project is licensed under the [GPL-3.0 License](https://www.gnu.org/licenses/gpl-3.0.en.html). For more details, please refer to the [LICENSE](https://github.com/mbuguadouglas/tubonge/blob/main/LICENSE) file.


## Contributing

Please refer to the [Contributing Guidelines](docs/CONTRIBUTING.md) for detailed information on how to contribute to the project.


## Tech Stacks Used for Development:

![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)

[//]: # "https://github.com/Ileriayo/markdown-badges"


## Acknowledgments

I would like to acknowledge the following individuals and resources for their contributions and support during the development of this project:

- [Antonnnio-Meele](https://github.com/zenx)
- [Django-4-By-Example-Book](https://djangobyexample.com/)
- [Django-4-By-Example-Github](https://github.com/PacktPublishing/Django-4-by-example)


# Contributors

[![Contributors](https://contrib.rocks/image?repo=mbuguadouglas/tubonge)](https://github.com/mbuguadouglas/tubonge/graphs/contributors)
