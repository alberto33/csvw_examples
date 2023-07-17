from rdflib import ConjunctiveGraph, URIRef, BNode, Literal
import rdflib
from rdflib.namespace import Namespace, NamespaceManager
import csv
import json

# Define namespaces
n = Namespace("http://example.org/people/")
schema = Namespace("http://schema.org/")

# Create a new RDF graph
g = rdflib.Graph()

# Add namespaces to graph
namespace_manager = NamespaceManager(g)
namespace_manager.bind('n', n, override=False)
namespace_manager.bind('schema', schema, override=False)

# Load CSVW metadata
with open('person.json') as f:
    metadata_dict = json.load(f)

# Create a dictionary to map column names to property URLs
column_mappings = {column['name']: URIRef(column['propertyUrl']) for column in metadata_dict['tableSchema']['columns']}

# Process CSV file using CSVW metadata
with open('person.csv', 'r') as data_file:
    csv_reader = csv.DictReader(data_file)
    for row in csv_reader:
        # Create a new RDF triple for each row
        person = BNode()
        for column_name, column_value in row.items():
            property_url = column_mappings[column_name]
            g.add((person, property_url, Literal(column_value)))

# And continue with the rest of your script...
