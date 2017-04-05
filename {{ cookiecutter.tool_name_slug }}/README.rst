{{ cookiecutter.tool_name }}
{% for x in range((cookiecutter.tool_name|length)) %}={% endfor %}

*{{ cookiecutter.tool_name }}: {{ cookiecutter.brief_description }}*

.. image::  https://github.com/{{ cookiecutter.github_user }}/{{ cookiecutter.github_repo }}/raw/master/doc/source/_static/{{ cookiecutter.tool_name_slug }}-logo.jpg
    :height: 64px
    :width: 64px
    :alt: {{ cookiecutter.tool_name }} logo

.. image:: https://travis-ci.org//{{ cookiecutter.github_user }}/{{ cookiecutter.github_repo }}.svg?branch=master
    :target: https://travis-ci.org/{{ cookiecutter.github_user }}/{{ cookiecutter.github_repo }}

.. image:: https://img.shields.io/pypi/l/Django.svg
    :target: https://github.com/{{ cookiecutter.github_user }}/{{ cookiecutter.github_repo }}/blob/master/LICENSE

.. image:: https://img.shields.io/pypi/status/Django.svg
    :target: https://pypi.python.org/pypi/{{ cookiecutter.github_repo }}/1.0.0

.. image:: https://codecov.io/gh//{{ cookiecutter.github_user }}/{{ cookiecutter.github_repo }}/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/{{ cookiecutter.github_user }}/{{ cookiecutter.github_repo }}

.. image:: https://readthedocs.org/projects/{{ cookiecutter.github_user }}/badge/?version=latest
    :target: http://{{ cookiecutter.github_repo }}.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

+----------------+--------------------------------------------+
|Project site    | https://github.com/{{ cookiecutter.github_user }}/{{ cookiecutter.github_repo }}        |
+----------------+--------------------------------------------+
|Issues          | https://github.com/{{ cookiecutter.github_user }}/{{ cookiecutter.github_repo }}/issues/|
+----------------+--------------------------------------------+
|Documentation   | https://{{ cookiecutter.github_repo }}.readthedocs.io/ |
+----------------+--------------------------------------------+
|Authors         | {{ cookiecutter.author }}      |
+----------------+--------------------------------------------+
|Latest Version  | 1.0.0-alpha                                |
+----------------+--------------------------------------------+
|Python versions | 3.5 or above                               |
+----------------+--------------------------------------------+

What's {{ cookiecutter.tool_name }}
======={% for x in range((cookiecutter.tool_name|length)) %}={% endfor %}

{{ cookiecutter.long_description }}

Documentation
=============

Go to documentation site: https://{{ cookiecutter.github_repo }}.readthedocs.io/

Contributors
------------

Contributors are welcome. You can find a list ot TODO tasks in the `TODO.md
<https://github.com/{{ cookiecutter.github_user }}/{{ cookiecutter.github_repo }}/blob/master/TODO.md>`_ at the project file.

All contributors will be added to the `CONTRIBUTORS.md
<https://github.com/{{ cookiecutter.github_user }}/{{ cookiecutter.github_repo }}/blob/master/CONTRIBUTORS.md>`_ file.

Thanks in advance if you're planning to contribute to the project! :)

License
=======

This project is distributed under `BSD license <https://github.com/{{ cookiecutter.github_user }}/{{ cookiecutter.github_repo }}/blob/master/LICENSE>`_

