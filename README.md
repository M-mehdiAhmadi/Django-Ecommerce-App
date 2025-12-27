
# Reusable Django App Template

A minimal and fully standard template for building **reusable Django applications**.  
This structure follows the official Django documentation on creating reusable apps and is intended to be cloned, renamed, and extended for any standalone Django component (uploaders, widgets, payment modules, utilities, etc.).

Official Django guide:  
https://docs.djangoproject.com/en/stable/intro/reusable-apps/

---

## Project Structure (Django Official Standard)

```

Reusable-Django-App-Template/
│
├── your_app_name/
│   ├── __init__.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── forms.py
│   ├── admin.py
│   ├── test.py
│   │
│   ├── templates/
│   │   └── your_app_name/
│   │       └── index.html
│   │
│   └── static/
│       └── your_app_name/
│           ├── css/
│           ├── js/
│           └── img/
│
├── pyproject.toml
├── LICENSE
├── README.md
├── README.rst
├── setup.py
└── MANIFEST.in


```

This structure matches Django's recommended layout for reusable applications.

---

## What You Must Rename After Cloning

After cloning the repository, you need to update several placeholders to match your actual package name.

### 1. Rename the main app directory to your real app name:


```

your_app_name/

```

### 2. Update the package name in `pyproject.toml`

Inside `pyproject.toml`:

```toml
[project]
name = "your-app-name"
````

### 3. Update template and static paths

Change folders containing the placeholder:

```
templates/your_app_name/
static/your_app_name/
```


### 4. Update the Django AppConfig

In `apps.py`:

```python
class YourAppNameConfig(AppConfig):
    name = "your_app_name"
```
### 5. Update the MANIFEST.in

```
recursive-include your_app_name/templates *
recursive-include your_app_name/static *
```
---

## `pyproject.toml` Explained

This file contains metadata and packaging configuration used by `setuptools` and PyPI.

Example included in the template:

```toml
[build-system]
requires = ["setuptools", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "your-app-name"
version = "0.1.0"
description = "A reusable Django application."
readme = "README.md"
requires-python = ">=3.10"
authors = [{ name="Your Name", email="email@example.com" }]
license = { file = "LICENSE" }
dependencies = ["Django>=5.0"]

[tool.setuptools.packages.find]
where = ["."]
```

You only need to edit the package name and author information.

---
## Installation (using git)
```
pip install git+https://github.com/M-mehdiAhmadi/Reusable-Django-App-Template.git
```

## Installation (after publishing)

```bash
pip install your-app-name
```

Add the app to your Django settings:

```python
INSTALLED_APPS = [
    ...
    "your_app_name",
]
```

Add URLs if your app provides them:

```python
path("your-app/", include("your_app_name.urls")),
```

---

## Publishing to PyPI (optional)

Build:

```bash
python -m build
```

Upload:

```bash
twine upload dist/*
```

---

## License

This template is licensed under the MIT License.
Feel free to modify and use it in your personal or commercial projects.

---

## Purpose of This Template

This repository is designed for developers who need:

* A clean Django-standard reusable app structure
* A starting point for components that can be installed via `pip`
* Consistent template/static organization
* Packaging support via `pyproject.toml`
* A reliable structure for open-source or internal reusable modules

Simply clone it, rename the placeholders, and begin building your component.
