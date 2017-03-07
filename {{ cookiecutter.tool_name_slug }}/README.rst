{{ cookiecutter.tool_name }}
{% for x in range((cookiecutter.tool_name|length)) %}={% endfor %}

*{{ cookiecutter.tool_name }}: {{ cookiecutter.brief_description }}*

.. image::  https://github.com/{{ cookiecutter.github_user }}/{{ cookiecutter.github_repo }}/raw/master/doc/source/_static/{{ cookiecutter.tool_name_slug }}-logo.jpg
    :height: 64px
    :width: 64px
    :alt: {{ cookiecutter.tool_name }} logo

+----------------+--------------------------------------------+
|Project site    | https://github.com/{{ cookiecutter.github_user }}/{{ cookiecutter.github_repo }}        |
+----------------+--------------------------------------------+
|Issues          | https://github.com/{{ cookiecutter.github_user }}/{{ cookiecutter.github_repo }}/issues/|
+----------------+--------------------------------------------+
|Documentation   | https://{{ cookiecutter.github_repo }}.readthedocs.org/        |
+----------------+--------------------------------------------+
|Authors         | {{ cookiecutter.author }}      |
+----------------+--------------------------------------------+
|Latest Version  | 1.0.0                                      |
+----------------+--------------------------------------------+
|Python versions | 3.5 or above                               |
+----------------+--------------------------------------------+

What's {{ cookiecutter.tool_name }}
======={% for x in range((cookiecutter.tool_name|length)) %}={% endfor %}

{{ cookiecutter.long_description }}

Documentation
=============

Go to documentation site: https://{{ cookiecutter.github_repo }}.readthedocs.org/

Contributing
============

Any collaboration is welcome!

There're many tasks to do.You can check the `Issues <https://github.com/{{ cookiecutter.github_user }}/{{ cookiecutter.github_repo }}/issues/>`_ and send us a Pull Request.

Also you can read the `TODO <https://github.com/{{ cookiecutter.github_user }}/{{ cookiecutter.github_repo }}/blob/master/TODO.md>`_ file.

License
=======

This project is distributed under `BSD license <https://github.com/{{ cookiecutter.github_user }}/{{ cookiecutter.github_repo }}/blob/master/LICENSE>`_

