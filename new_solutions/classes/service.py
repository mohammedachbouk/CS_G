class Service:
    """Represents a Service of the challenge"""

    from new_solutions.classes.binary import Binary

    def __init__(self, name: str, binary: Binary):
        """
        Create a new Service
        :param name: The name of the service
        :param binary: The binary where the service is stored
        """
        from new_solutions.classes.feature import Feature
        from new_solutions.classes.binary import Binary

        self.name: str = name
        self.features: list[Feature] = []
        self.binary: Binary = binary

    def __str__(self):
        return f"\n\t\t - Service {self.name} " f"{self.features}"

    def __repr__(self):
        return self.__str__()
