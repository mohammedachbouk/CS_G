"""
    Module for parsing entry files for the project
"""
from new_solutions.classes.binary import Binary
from new_solutions.classes.challenge import Challenge
from new_solutions.classes.feature import Feature
from new_solutions.classes.service import Service


def parse_input(filename: str) -> tuple[Challenge, list[Feature]]:
    """
    Extracting informations from a data file
    """
    with open(filename, "r") as outfile:
        content = outfile.read()

    line_list = [line.split(" ") for line in content.split("\n")]
    # pprint(line_list)

    first_line = line_list[0]

    challenge: Challenge = Challenge(
        int(first_line[0]),
        int(first_line[1]),
        int(first_line[4]),
        int(first_line[2]),
        int(first_line[5]),
    )
    services: list[Service] = []

    for binary in range(int(first_line[3])):
        challenge.binaries.append(Binary(binary))

    i = 1
    for i in range(1, len(line_list)):
        line = line_list[i]
        if len(line) != 2:
            break
        else:
            service = Service(line[0], challenge.binaries[int(line[1])])
            services.append(service)
            challenge.binaries[int(line[1])].services.append(service)

    features: list[Feature] = []

    for j in range(i, len(line_list) - 1, 2):  # pas de 2
        line1 = line_list[j]
        line2 = line_list[j + 1]
        feature: Feature = Feature(line1[0], int(line1[2]), int(line1[3]))
        features.append(feature)
        for k in line2:
            service = (list(filter(lambda s: s.name == k, services)))[
                0
            ]  # s est le nom d'un service
            service.features.append(feature)
            feature.services.append(service)
    # print(challenge)
    return challenge, features
