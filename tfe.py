#!/usr/bin/env python

#from BeautifulSoup import BeautifulSoup
import os
import re
import requests

# Tabs
tabs = [
    "summary",
    "structure",
    "tfbs",
    "targets",
    "protein",
    "interactions",
    "genetics",
    "expression",
    "ontologies",
    "papers"
]

# Codes
codes = [
    "authors",
    "child-tf",
    "class-family",
    "class-group",
    "class-subfamily",
    "description",
    "ensembl-gene-id",
    "entrez-gene-id",
    "gene-ontology",
    "homologs",
    "interators",
    "ligands",
    "mesh-all",
    "mesh-disease",
    "mgi-phenotype",
    "omim-id",
    "papers",
    "parent-tf",
    "refseq-id",
    "regulators",
    "score",
    "species",
    "symbol",
    "synonyms",
    "targets",
    "tfbs",
    "uniprot-id"
]

# Request TF ids
url = "http://www.cisreg.ca/cgi-bin/tfe/api.pl?code=all-tfids"
r = requests.get(url)
tfids = re.findall("\d+", r.text) 

# For each TF id...
for tfid in tfids:
    # Create dir for TF id
    if not os.path.isdir(tfid):
        os.mkdir(tfid)
    else:
	continue
    # For each tab...
    for tab in tabs:
        # Request tab for TF id
        url = "http://www.cisreg.ca/cgi-bin/tfe/articles.pl?tfid=%s&tab=%s" % (
            str(tfid), tab
        )
        r = requests.get(url)
        #soup = BeautifulSoup(r.text)
        #texts = soup.findAll(text=True)
        # Write tab
        tab_file = os.path.join(
            tfid,
            "%s.html" % tab
        )
        with open(tab_file, "w") as f:
            f.write(r.content)
    # Write info
    info_file = os.path.join(
        tfid,
        "info.txt"
    )
    with open(info_file, "w") as f:
        # For each code...
        for code in codes:
            # Request code for TF id
            url = "http://www.cisreg.ca/cgi-bin/tfe/api.pl?tfid=%s&code=%s" % (
                str(tfid), code
            )
            r = requests.get(url)
            f.write(
                ">%s\n%s//" % \
                (
                    code,
                    r.content
                )
            )
