Weather Data ETL Pipeline
=========================

A minimal yet functional ETL pipeline built in Python to extract weather data from the OpenWeatherMap API, transform it into a clean tabular format using Pandas, and load it as Parquet files.

This project demonstrates essential data engineering skills, including:

- API integration
- Environment variable management (.env)
- Data transformation and cleaning
- File-based data storage (Parquet)
- Python project structure with Poetry

Project Structure
-----------------

.. code-block:: text

    nombre_del_proyecto/
    ├── src/
    │   └── nombre_del_proyecto/
    │       ├── __init__.py
    │       └── main.py
    ├── tests/
    │   ├── __init__.py
    │   └── test_nombre_del_proyecto.py
    ├── data/
    ├── .env
    ├── .gitignore
    ├── README.rst
    └── pyproject.toml

Quickstart
----------

1. Clone the repo:

.. code-block:: bash

    git clone https://github.com/your-username/nombre_del_proyecto.git
    cd nombre_del_proyecto

2. Install dependencies with Poetry:

.. code-block:: bash

    poetry install

3. Create a `.env` file in the project root with your OpenWeatherMap API key:

.. code-block:: text

    OPENWEATHER_API_KEY=your_api_key_here

4. Run the ETL pipeline:

.. code-block:: bash

    poetry run python src/nombre_del_proyecto/main.py

Output files are saved as Parquet under the `data/` folder.

Author
------

Edisson Mogollon | Software Engineer & Data Engineer 
