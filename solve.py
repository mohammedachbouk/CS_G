from new_solutions.main.parser import parse_input
from new_solutions.main.solver import solve2
from new_solutions.utils.ratios import sorting_ratios
from new_solutions.utils.utils import sort_features
from new_solutions.utils.writer import Writer


def strategie(file_path: str):
    results = []
    for ratio in sorting_ratios:
        for reverse in [False, True]:
            challenge, features = parse_input(file_path)
            solve2(challenge, sort_features(ratio[0], features, challenge, reverse))
            results.append(
                (
                    challenge.get_score([f for f in features]),
                    f"{ratio[1]} {'reverse' if reverse else ''}",
                )
            )
            Writer().writeToFile(
                f"solutions/{ratio[1].replace('/', '-')}{' reverse' if reverse else ''}.txt"
            )
    results.sort(key=lambda res: res[0], reverse=True)
    r = results[-1]

    print(f"--> {r[1]}")


strategie("data/an_example.txt")
