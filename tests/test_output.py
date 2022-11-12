import os
from new_solutions.main.parser import parse_input

def check_output(out: str, inp: str):
    """Check the correctness of the output file
    Parameters
    ----------
    inp : str
        name of the input file in the data folder
    out : str
    name of the output file in the data folder
    """
    with open(os.path.join(out), "r") as f:
        file = f.read().strip()
    lines = file.split("\n")
    first_line = lines[0].split()
    challenge= parse_input(inp)[0]

    # Number of engineers actually working and is a number
    assert challenge.engineers == int(first_line[0]) and first_line[0].isnumeric()

    # Any line should be typically composed of operation, feature/service, and a number
    for line in lines:
        assert len(line.split()) <= 3, "Can't have two operations at the same time"
        if len(line.split()) > 1:
            # Check validity of operations
            assert line.split()[0] in [
                "impl",
                "move",
                "wait",
                "new",
            ], "Output contains unrecognized operations"
            # Check the congruency of the number of binaries
            assert int(line.split()[2]) <= len(
                challenge.binaries
            ), "Extra binaries were found but not declared"


def test_outputs():
    """Test all the output file present in the solution folder
     compared to the input present in data"""

    check_output("new_solutions/solutions/Users.txt", "data/an_example.txt")
