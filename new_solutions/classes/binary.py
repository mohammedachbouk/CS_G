from typing import Optional


class Binary:
    """Represents a binary of the challenge."""

    __number_of_binaries: int = 0
    """Used to keep trace of the total number of the binaries."""

    def __init__(self, number: Optional[int]):
        """
        Create a new empty Binary.
        :param number: The number of the binary or None to auto-calculate it.
        """
        from new_solutions.classes.service import Service

        if number is None:
            self.number: int = Binary.__number_of_binaries
        else:
            self.number: int = number

        self.services: list[Service] = []
        self.occuped: list[Optional[int]] = (
            [0] * 1000 * 2
        )  # max theorical time multiplied by security coef of 2
        """Int array representing how many engineers work on the binary on the day symbolised by the index."""
        Binary.__number_of_binaries += 1

    def __str__(self):
        return f"\n\n\t\tBinary n°{self.number} " f"{self.services}"

    def __repr__(self):
        return self.__str__()
