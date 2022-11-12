import os
from new_solutions.main.parser import parse_input

def check_input(file_name: str):
    """Check the correctness of an input file
    Parameters
    ----------
    file_name : str
        name of the input file in the data folder
    """

    with open(os.path.join(file_name), "r") as f:
        inp = f.read().strip()
    lines = inp.split("\n")
    first_line = lines[0].split()
    challenge, features = parse_input(file_name)

    # Number of main params should be six
    assert len(first_line) == 6, "Six parameters are required"

    # Number of features in the first line must be the same of the retrieved features
    assert challenge.nb_features == len(features)

    # Check that the input have the correct number of lines
    assert len(lines) == 1 + int(first_line[2]) + 2 * int(
        first_line[4]
    ), f"File {file_name}: Wrong number of lines in the input"

    # The number of listed binaries should be the same as the actual binaries at the start
    assert len(challenge.binaries) == int(first_line[3])

    # Any service should be implemented in at least on existing binary
    for val in features:
        for val2 in val.services:
            assert val2.binary.number < int(
                first_line[3]
            ), "Services should contained in at least one binary"

    # Checking if the values are logical
    # Number of engineers must be at least one
    assert challenge.engineers > 0, "Impossible with 0 engineers"

    # Number of services can't be less than number of binaries to begin with
    assert len(challenge.binaries) <= challenge.nb_services

    # Users of the features can't be 0
    for feature in features:
        assert feature.daily_users > 1, "No need for a feature with no users"


def test_inputs():
    """Test all the input file present in the folder data"""

    for filename in os.listdir("data"):
        check_input("data/" + filename)
    # check_input('data/an_example.txt')
