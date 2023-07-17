from csvwlib import CSVWConverter

# convert csv and csvw to RDF triples
rdf_output = CSVWConverter.to_rdf('person.csv', metadata_url='person.json')

# write the RDF triples to a file
with open('output.ttl', 'w') as file:
    file.write(str(rdf_output))

# now convert the RDF to JSON-LD
jsonld_output = CSVWConverter.to_json('output.ttl')

# write the JSON-LD to a file
with open('output.jsonld', 'w') as file:
    file.write(jsonld_output)