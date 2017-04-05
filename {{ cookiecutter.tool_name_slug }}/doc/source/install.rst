Install {{ cookiecutter.tool_name }}
======={% for x in range((cookiecutter.tool_name|length)) %}={% endfor %}

Install {{ cookiecutter.tool_name }} is very simple, depending of the
release you want, you can install:

- stable version (**recomended**).
- development version.

Stable version
--------------

.. code-block:: bash

    > python3.5 -m pip install {{ cookiecutter.tool_name_slug }}

Development version
-------------------

.. code-block:: bash

    > python3.5 -m pip install https://github.com/{{ cookiecutter.github_user }}/{{ cookiecutter.github_repo }}/archive/develop.zip
