DOME 4.0 interface to OpenModel
===============================


Installation
------------
It is recommended that you install Python 3.11.

Create a virtual Python environment (for more info, see [venv documentation](https://docs.python.org/3/library/venv.html)).

In short, create the environment with

    python -m venv .venv

where `.venv` is the directory where you want to store your virtual environment.
Activate the environment with one of the following commands, depending on your shell:

    # bash
    source </path/to/new/virtual/environment>/bin/activate

    # Windows cmd.exe
    .venv\Scripts\activate.bat

Install requirements

    pip install -r requirements.txt



Test querying the data
----------------------
In the repo contains a knowledge base serialised to the turtle file
`kb.ttl`, which describes some datasets used in the OpenModel success
story 3 on aluminium-reinforced concrete.

The script `queries.py` is a Python script that access the knowledge
base and perform some SPARQL queries.  Run it with:

    python queries.py

Running the script, you should get the following output:

> DataSet individuals:
>   -  http://open-model.eu/ontologies/ss3kb#abaqus_config1
>   -  http://open-model.eu/ontologies/ss3kb#abaqus_materialcard_al1
>   -  http://open-model.eu/ontologies/ss3kb#abaqus_materialcard_concrete1
>   -  http://open-model.eu/ontologies/ss3kb#alloy_composition1
>   -  http://open-model.eu/ontologies/ss3kb#alloy_heat_treatment1
>   -  http://open-model.eu/ontologies/ss3kb#tabulated_elastoplastic1
>   -  http://open-model.eu/ontologies/ss3kb#yieldstrength1
>
> AlloyComposition dataset:
>   -  http://open-model.eu/ontologies/ss3kb#alloy_composition1
>
> How to access the AlloyComposition dataset:
>   - dataset: http://open-model.eu/ontologies/ss3kb#alloy_composition1
>   - url: https://github.com/H2020-OpenModel/SS3_wrappers/raw/main/tests/testfiles/input_data/alloy_composition.csv
>   - mediaType: application/vnd.dlite-parse
