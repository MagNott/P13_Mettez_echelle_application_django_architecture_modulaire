Installation
============

To install and run the project locally:

1. Clone the repository
2. Create a virtual environment and activate it
3. Install dependencies

.. code-block:: bash

   git clone <https://github.com/MagNott/P13_Mettez_echelle_application_django_architecture_modulaire>
   cd P13_Mettez_echelle_application_django_architecture_modulaire
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt

4. Apply migrations and launch server

.. code-block:: bash

   python manage.py migrate
   python manage.py runserver
