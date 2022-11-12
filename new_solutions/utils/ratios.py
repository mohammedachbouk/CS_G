from typing import Callable

from new_solutions.classes.challenge import Challenge
from new_solutions.classes.feature import Feature
from new_solutions.utils.utils import FeatureRatio

RatioLambda = Callable[[Feature, Challenge], FeatureRatio]

sorting_ratios: list[tuple[RatioLambda, str]] = [
    (lambda f, c: [(f, f.daily_users) for f in f], "Users"),
    (lambda f, c: [(f, f.difficulty) for f in f], "Difficulty"),
    (lambda f, c: [(f, len(f.get_binaries())) for f in f], "Bin"),
    (lambda f, c: [(f, len(f.services)) for f in f], "Services"),
    (lambda f, c: [(f, f.daily_users / f.difficulty) for f in f], "Users/Diff"),
    (lambda f, c: [(f, f.daily_users / len(f.get_binaries())) for f in f], "Users/Bin"),
    (lambda f, c: [(f, f.daily_users / len(f.services)) for f in f], "Users/Services"),
    (lambda f, c: [(f, f.difficulty / len(f.services)) for f in f], "Diff/Services"),
    (lambda f, c: [(f, f.difficulty / len(f.get_binaries())) for f in f], "Diff/Bin"),
    (
        lambda f, c: [(f, len(f.get_binaries()) / len(f.services)) for f in f],
        "Bin/Services",
    ),
    (
        lambda f, c: [(f, f.daily_users / f.difficulty / len(f.services)) for f in f],
        "Users/Diff/Services",
    ),
    (
        lambda f, c: [
            (f, f.daily_users / f.difficulty / len(f.get_binaries())) for f in f
        ],
        "Users/Diff/Bin",
    ),
    (
        lambda f, c: [
            (f, f.difficulty / len(f.get_binaries()) / len(f.services)) for f in f
        ],
        "Diff/Bin/Services",
    ),
]
"""
List of lambda/name of the ratio.

The lambda stored allows the features to be sorted in a certain order.
The different lambda are called by us as a ratio. Some of them have 
a explaination and other just have been created by pure hazard.
"""
