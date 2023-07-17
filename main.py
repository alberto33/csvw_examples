from rdflib import ConjunctiveGraph, Graph, URIRef, Literal
import csvwlib
import pandas as pd
import csv
import json
import tempfile
import os

def convert_with_pandas():

    # Load CSV data
    data = pd.read_csv('person_backup.csv')

    # Create an RDF graph
    g = Graph()

    # Loop over DataFrame rows
    for _, row in data.iterrows():
        # Create RDF triples based on DataFrame rows
        subject = URIRef(f'http://example.com/person/{row["id"]}')
        g.add((subject, URIRef('http://schema.org/name'), Literal(row['name'])))
        g.add((subject, URIRef('http://schema.org/age'), Literal(row['age'])))

    # print(g.)

    # Serialize the graph to RDF (turtle format)
    # output = g.serialize(format='turtle')
    # if isinstance(output, bytes):
    #     output = output.decode('utf-8')

    output = g.serialize(format='json-ld', indent=4)
    if isinstance(output, bytes):
        output = output.decode('utf-8')


    print(output)


def convert_with_csvwlib2():

    # Load the CSVW file.
    dataset = csvwlib.load_dataset('person.json')

    # Load the CSV file.
    with open('person.csv', 'r') as f:
        reader = csv.reader(f, delimiter=',')
        data = list(reader)

    # Combine the CSVW file with the CSV file.
    combined_data = dataset.combine_with_csv(data)

    # Convert the combined data to RDF triples in Turtle syntax.
    combined_data.to_rdf('turtle')


def convert_with_csvwlib():
    # Open the metadata file and load it into a Python dict
    with open('person.json') as f:
        metadata = json.load(f)

    # Write the modified metadata to a temporary file
    # with tempfile.NamedTemporaryFile(suffix=".json", delete=False, mode='w') as temp:
    #     json.dump(metadata, temp)
    #     temp_path = temp.name
    #
    # # Now you can use temp_path as the metadata file path
    # rdf_output = csvwlib.CSVWConverter.to_rdf('person.csv', temp_path)

    # Convert the CSVW to RDF
    # rdf_output = CSVWConverter.to_rdf('person.csv', 'https://raw.githubusercontent.com/alberto33/csvw_examples/main/metadata.json')

    x = csvwlib.load_csvw('person.json')
    rdf_output = csvwlib.CSVWConverter.to_rdf('person.csv', 'person.json')

    # Parse the RDF data with rdflib
    g = ConjunctiveGraph()
    g.parse(data=rdf_output, format='turtle')

    # Serialize the graph to JSON-LD
    jsonld_data = g.serialize(format='json-ld', indent=4).decode('utf-8')

    print(jsonld_data)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    convert_with_csvwlib()

