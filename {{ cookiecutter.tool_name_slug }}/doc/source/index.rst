Welcome to {{ cookiecutter.tool_name }}'s documentation!
{% for x in range((cookiecutter.tool_name|length) + 28) %}={% endfor %}

+----------------+------------------------------------+
{%- if cookiecutter.github_repo and cookiecutter.github_user %}
|Project site    | http://github.com/bbva/apitest     |
+----------------+------------------------------------+
|Author          | {{ cookiecutter.author }}  |
+----------------+------------------------------------+
{%- endif %}
|Documentation   | http://{{ cookiecutter.tool_name_slug }}.readthedocs.org     |
+----------------+------------------------------------+
|Last Version    | {{ cookiecutter.project_version }}                              |
+----------------+------------------------------------+
|Python versions | 3.5 or above                       |
+----------------+------------------------------------+

{{ cookiecutter.brief_description }}

Contents
++++++++

.. toctree::
   :maxdepth: 2

   quickstart

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

