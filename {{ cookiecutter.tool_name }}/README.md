{{ cookiecutter.tool_name }}
{% for x in range((cookiecutter.tool_name|length)) %}={% endfor %}

![Logo](doc/images/logo.jpg)

*{{ cookiecutter.tool_name }}: {{ cookiecutter.brief_description }}*

Code | {{ cookiecutter.project_site }}
---- | ----------------------------------------------
Issues | {{ cookiecutter.project_site }}/issues/
Python version | Python 3.5 and above

What's {{ cookiecutter.tool_name }}
-------{% for x in range((cookiecutter.tool_name|length)) %}-{% endfor %}

{{ cookiecutter.long_description }}

What's new?
-----------

This {{ cookiecutter.tool_name }} version, add a lot of new features and fixes, like:

Version {{ cookiecutter.project_version }}
++++++++{% for x in range((cookiecutter.project_version|length)) %}+{% endfor %}

- First version released

You can read entire list in CHANGELOG file.

Installation
------------

Simple
++++++

Install {{ cookiecutter.tool_name }} is so easy:

```
$ python -m pip install {{ cookiecutter.tool_name }}
```

With extra performance
++++++++++++++++++++++

{{ cookiecutter.tool_name | capitalize }} also includes some optional dependencies to add extra performance but requires a bit different installation, because they (usually) depends of C extensions.

To install the tool with extra performance you must do:

```
$ python -m pip install '{{ cookiecutter.tool_name }}[performance]'
```

**Remember that {{ cookiecutter.tool_name }} only runs in Python 3.5 and above**.

Quick start
-----------

You can display inline help writing:

From cloned project
+++++++++++++++++++

```bash

python {{ cookiecutter.tool_name }}.py -h
```

From pip installation
+++++++++++++++++++++

```bash

{{ cookiecutter.tool_name }} -h
```