.. oc_lettings_site documentation master file, created by
   sphinx-quickstart on Wed Nov 19 17:41:10 2025.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to OC Lettings Site's documentation!
============================================

.. Add your content using ``reStructuredText`` syntax. See the
.. `reStructuredText <https://www.sphinx-doc.org/en/master/usage/restructuredtext/index.html>`_
.. documentation for details.


.. .. toctree::
..    :maxdepth: 2
..    :caption: Contents:


.. toctree::
   :maxdepth: 2
   :caption: Contents:

   installation
   architecture
   usage
   api_reference

About
-----

This project is a modular Django site comprising several applications:

- **oc_lettings_site** : entry point of the Django project
- **profiles** : manages user profiles
- **lettings** : manages rental listings


The project's goal is to ensure maintainability and scalability of the architecture while adhering to best practices in CI/CD and documentation.

Indices
-------

- This documentation is built with **Sphinx** and published on **Read The Docs**.
- Technical documentation (classes, functions…) is automatically generated from **docstrings** using `sphinx.ext.autodoc`.

Useful indices for navigation:

- For installation steps: see the *Installation* section
- For the code architecture: see the *Architecture* section
- For using the project: see *Usage*
- For details of the Python API: see *API Reference*
