from new_solutions.classes.engineer import Engineer


class Engineers:
    """Allow to stock all the engineers"""

    def __init__(self, number, days_for_binary, challenge_days):
        """
        Create the "list" of engineers and create all the engineers.
        :param number: The number of engineers of the challenge
        :param days_for_binary: The number of days to create a binary
        :param challenge_days: The number of days given to resolve the challenge
        """
        self.engineers: list[Engineer] = [
            Engineer(i, days_for_binary) for i in range(number)
        ]
        self.challenge_days: int = challenge_days

    def get_engineer(self) -> Engineer:
        """
        Get the engineer that work the less. The one with days_past minimal
        :return: An engineer
        """
        self.engineers.sort(key=lambda e: e.days_past)
        return self.engineers[0]

    def get_all(self) -> list[Engineer]:
        """
        Get all the engineers
        :return: Engineers
        """
        self.engineers.sort(key=lambda e: e.id)
        return self.engineers

    def finished(self) -> bool:
        """
        Allow to know if all the engineers exceed the days of the challenge or not.
        :return: True if all engineers exceed the number of days of the challenge, False instead.
        """
        for e in self.engineers:
            if e.days_past < self.challenge_days:
                return False
        return True
