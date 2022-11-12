from __future__ import annotations

from typing import Optional

from new_solutions.classes.feature import Feature


class Features:
    """Allow to stock easily the features of the challenge"""

    def __init__(self, features: list[Feature]):
        """
        Create the "list" of features
        :param features: The list of features
        """
        self.features: list[Feature] = features
        self.remaining: list[Feature] = features.copy()

    def next_one(self) -> Optional[Feature]:
        """
        Get the next feature to implement
        :return: A feature or None if there is no more features
        """
        if len(self.remaining) == 0:
            return None
        return self.remaining[0]

    def next(self, nb: int = 1) -> Feature | list[Feature]:
        """
        Return the next features to implement
        :param nb: The wanted number of next features
        :return: A list of features
        """
        return self.remaining[0 : max(1, nb)]

    def get_all(self) -> list[Feature]:
        return self.features

    def set_done(self, f: Feature):
        self.remaining.remove(f)
