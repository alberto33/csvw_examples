import csvw
import rdflib
from rdflib.namespace import Namespace, NamespaceManager
from rdflib import ConjunctiveGraph, URIRef, BNode, Literal
import csv
import json

# Define namespaces
n = Namespace("http://example.org/people/")
schema = Namespace("http://schema.org/")
name = URIRef("http://schema.org/name")
age = URIRef("http://schema.org/age")
city = URIRef("http://schema.org/address")

# Create a new RDF graph
g = rdflib.Graph()

# Add namespaces to graph
namespace_manager = NamespaceManager(g)
namespace_manager.bind('n', n, override=False)
namespace_manager.bind('schema', schema, override=False)

# Load CSVW metadata
with open('metadata.json') as f:
    metadata_dict = json.load(f)
metadata = csvw.Table(url=metadata_dict['url'], tableSchema=metadata_dict['tableSchema'])

# Process CSV file using CSVW metadata
with open('data.csv', 'r') as data_file:
    csv_reader = csv.DictReader(data_file)
    for row in csv_reader:
        # Create a new RDF triple for each row
        person = BNode()
        g.add((person, name, Literal(row['name'])))
        g.add((person, age, Literal(row['age'])))
        g.add((person, city, Literal(row['city'])))

# Serialize the graph to RDF (turtle format)
rdf = g.serialize(format='turtle')
print("BEG-RDF")
print(rdf)
print("END-RDF")

# Parse the RDF data with rdflib
g = ConjunctiveGraph()
g.parse(data=rdf, format='turtle')

# Define the context for JSON-LD serialization
context = {
    "schema": str(schema)
}

# Serialize the graph to JSON-LD
jsonld_data = g.serialize(format='json-ld', context=context, indent=4).decode('utf-8')

print("BEG-JSON")
print(jsonld_data)
print("END-JSON")
