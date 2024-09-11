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
# Note how Tripper allow us write readable SPARQL queries with EMMO prefLabel's.
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

SELECT ?dataset
WHERE {{
  ?dataset rdf:type <http://onto-ns.com/meta/calm/0.1/AlloyComposition> .
}}
"""
result2 = ts.query(query2)
print()
print("AlloyComposition dataset:")
for r, in result2:
    print("  - ", r)


# How to access the AlloyComposition dataset
query3 = f"""
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX dcat: <http://www.w3.org/ns/dcat#>
PREFIX ss3:  <http://open-model.eu/ontologies/ss3#>
PREFIX dm:   <http://onto-ns.com/meta/calm/0.1/>

SELECT ?dataset ?url ?mediaType
WHERE {{
  ?dataset rdf:type dm:AlloyComposition .
  ?dataset dcat:distribution ?dist .
  ?dist dcat:downloadURL ?url .
  ?dist dcat:mediaType ?mediaType .
}}
"""
result3 = ts.query(query3)
print()
print("How to access the AlloyComposition dataset:")
dataset, url, mediaType = result3[0]
print("  - dataset:", dataset)
print("  - downloadURL:", url)
#print("  - mediaType:", mediaType)
