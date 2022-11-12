from new_solutions.classes.challenge import Challenge
from new_solutions.classes.engineers import Engineers
from new_solutions.classes.feature import Feature
from new_solutions.classes.features import Features
from new_solutions.utils.utils import FeatureRatio


def solve(challenge: Challenge, features: FeatureRatio):
    """
    Solve a given challenge.
    The strategy used is to get the feature in a certain order. (ratios)
    Then we take the first feature and we split the differents binaries to implement with the
    engineers that worked the least.
    :param challenge: The given challenge
    :param features: A sorted list of features
    """

    engineers = Engineers(
        challenge.engineers, challenge.days_for_binary, challenge.days
    )
    for i in range(len(features)):
        feature: Feature = features[i][0]
        for j in range(len(feature.get_binaries())):
            if engineers.finished():
                return
            bin = feature.get_binaries()[j]
            engineers.get_engineer().implement(feature, bin)
    return


def solve2(challenge: Challenge, features: Features):
    """
    Solve a given challenge.
    The strategy used is to sort the feature in a certain order.
    Then we take the firsts features and calculate the score produced by them and implement the best of them.
    For the choosen one, we split the differents binaries to implement with the engineers that worked the least.
    If a feature cannot be implemented during the challenge days, we skip it.
    :param challenge: The given challenge
    :param features: A sorted list of features
    """

    engineers = Engineers(
        challenge.engineers, challenge.days_for_binary, challenge.days
    )

    while True:
        next_features = features.next(5)
        if len(next_features) == 0:
            return
        feat_score = []
        for f in next_features:
            is_implentable, score = challenge.is_implentable(f, engineers)
            if not is_implentable:
                features.set_done(f)
            else:
                feat_score.append((f, score))
        if len(feat_score) == 0:
            continue
        feature = max(feat_score, key=lambda fc: fc[1])[0]
        features.set_done(feature)
        for j in range(len(feature.get_binaries())):
            if engineers.finished():
                return
            bin = feature.get_binaries()[j]
            engineers.get_engineer().implement(feature, bin)
