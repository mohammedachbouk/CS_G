from new_solutions.classes.engineer import Engineer
from new_solutions.classes.engineers import Engineers
from new_solutions.classes.feature import Feature


class Challenge:
    """Represents the given challenge with all given information in the parsed file."""

    def __init__(
        self,
        days: int,
        engineers: int,
        nb_features: int,
        nb_services: int,
        days_for_binary: int,
    ):
        """
        Create and initialise the Challenge
        :param days: the number of days given to resolve the challenge
        :param engineers: the number of engineers to resolve the challenge
        :param nb_features: the number of features in the challenge
        :param nb_services: the number of services
        :param days_for_binary: the number of days needed to create a new binary
        """
        from new_solutions.classes.binary import Binary

        self.days: int = days
        self.engineers: int = engineers
        self.days_for_binary: int = days_for_binary
        self.nb_features: int = nb_features
        self.nb_services: int = nb_services
        self.binaries: list[Binary] = []

    def __str__(self):
        string: str = (
            f"\nChallenge\n"
            f" - Days : {self.days}\n"
            f" - Engineers : {self.engineers}\n"
            f" - Days for bin : {self.days_for_binary}"
            f"{self.binaries}"
        )
        string = string.replace("[", "")
        string = string.replace("]", "")
        string = string.replace(",", "")
        return string

    def get_score(self, features: list[Feature]) -> int:
        """
        Calculate the score of the challenge at any time.
        :param features: the list of feature of the challenge
        :return: The actual score of the challenge
        """
        score: int = 0
        for feature in features:
            if len(feature.get_remaining_services()) == 0:
                score += feature.daily_users * max(
                    0, self.days - feature.last_day_implemented
                )
        return score

    def is_implentable(
        self, feature: Feature, engineers: Engineers
    ) -> tuple[bool, int]:
        """
        If the feature is implementable in the rest of the given time.
        If it cant be, the result is (False, 0)
        Else it's True and the score if the feature will be implemented
        :param feature: The feature that want to be tested
        :param engineers: The list of engineers
        :return: A tuple (implementable, score)
        """
        e_days: list[int] = []
        last_day_impl: int = 0
        for e in engineers.get_all():
            e_days.append(e.days_past)
        for b in feature.get_binaries():
            min_past: int = min(e_days)
            days: int = (
                len(b.services) + feature.difficulty + min_past + b.occuped[min_past]
            )
            if days >= self.days:
                return False, 0
            idx: int = e_days.index(min_past)
            e_days[idx] += days
            last_day_impl = max(last_day_impl, e_days[idx])
        return True, min(0, self.days - last_day_impl) * feature.daily_users

    @staticmethod
    def print_trace(features: list[Feature], engineers: list[Engineer]):
        """
        Print in the terminal for every feature if it has been implemented or not.
        And for every engineer what they do.
        :param features: The list of the features
        :param engineers: The list of the engineers
        """
        for f in features:
            len_impl = len(f.implemented_services)
            len_total = len(f.services)
            print(f"Feature {f.name} is implemented in ({len_impl}/{len_total}):")
            for ss in f.implemented_services:
                print(f"\t + {ss.name} (bin{ss.binary.number})")
            for ss in f.get_remaining_services():
                print(f"\t - {ss.name} (bin{ss.binary.number})")
        print()
        for e in engineers:
            print(f"Engineer {e.id} finished in {e.days_past} days.")
            for a in e.actions:
                print(f"\t - {a}")
