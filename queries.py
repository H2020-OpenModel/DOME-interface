from pathlib import Path

from tripper import SKOS, Namespace, Triplestore


thisdir = Path(__file__).resolve().parent

# EMMO namespace with access by prefLabel/altLabel
EMMO = Namespace(
    iri="https://w3id.org/emmo#",
    label_annotations=True,
    check=True,
)


ts = Triplestore(backend="rdflib")
ts.parse(thisdir / "kb.ttl")


# Find all emmo:DataSet individuals
# Note how Tripper allow us
query1 = f"""
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

SELECT ?dataset
WHERE {{
  ?dataset rdf:type <{EMMO.DataSet}> .
}}
"""
result1 = ts.query(query1)
print("DataSet individuals:")
for r, in result1:
    print("  - ", r)


# Find dataset AlloyComposition
query2 = f"""
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX ss3:  <http://open-model.eu/ontologies/ss3#>
PREFIX dm:   <http://onto-ns.com/meta/calm/0.1/>

SELECT ?dataset
WHERE {{
  ?dataset rdf:type dm:AlloyComposition .
}}
"""
result2 = ts.query(query2)
print()
print("AlloyComposition dataset")
print(result2)


#  ?dataset dcat:distribution ?dist .
#  ?dist dcat:downloadURL ?url .




query3 = f"""
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX ss3:  <http://open-model.eu/ontologies/ss3#>
PREFIX dm:   <http://onto-ns.com/meta/calm/0.1/>

SELECT ?dataset
WHERE {{
  ?dataset rdf:type dm:AlloyComposition .
  ?dataset rdf:type ?dm .
  ?dm skos:prefLabel "AlloyComposition"@en .
}}
"""
