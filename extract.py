"""Extract data on near-Earth objects and close approaches from CSV and JSON files.

The `load_neos` function extracts NEO data from a CSV file, formatted as
described in the project instructions, into a collection of `NearEarthObject`s.

The `load_approaches` function extracts close approach data from a JSON file,
formatted as described in the project instructions, into a collection of
`CloseApproach` objects.

The main module calls these functions with the arguments provided at the command
line, and uses the resulting collections to build an `NEODatabase`.

You'll edit this file in Task 2.
"""
import csv
import json

from models import NearEarthObject, CloseApproach


def load_neos(neo_csv_path):
    """Read near-Earth object information from a CSV file.

    :param neo_csv_path: A path to a CSV file containing data about near-Earth objects.
    :return: A collection of `NearEarthObject`s.
    """
    # TODO: Load NEO data from the given CSV file.
    neosArr = []
    with open(neo_csv_path, 'r') as neosFile:
        neos = csv.DictReader(neosFile)
        for neo in neos:
            d = neo["diameter"] or 'nan'
            pha = True if neo["pha"] == 'Y' else False
            name = neo["name"] if neo["name"] else None
            neosArr.append(NearEarthObject(pdes=neo["pdes"], name=name, diameter=d, pha=pha))
    return neosArr


def load_approaches(cad_json_path):
    """Read close approach data from a JSON file.

    :param cad_json_path: A path to a JSON file containing data about close approaches.
    :return: A collection of `CloseApproach`es.
    """
    # TODO: Load close approach data from the given JSON file.
    casArr = []
    with open(cad_json_path, 'r') as caFile:
        cas = json.load(caFile)  # Parse JSON data into a Python object. (A)
        for ca in cas["data"]:
            casArr.append(CloseApproach(des=ca[0], cd=ca[3], dist=ca[4], v_rel=ca[7]))

    return casArr
