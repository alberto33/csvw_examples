from rdflib import ConjunctiveGraph
from csvwlib import CSVWConverter


def main():

    # Convert the CSVW to RDF
    rdf_output = CSVWConverter.to_rdf('data.csv', 'metadata.json')

    # Parse the RDF data with rdflib
    g = ConjunctiveGraph()
    g.parse(data=rdf_output, format='turtle')

    # Serialize the graph to JSON-LD
    jsonld_data = g.serialize(format='json-ld', indent=4).decode('utf-8')

    print(jsonld_data)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
