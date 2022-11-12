class Singleton(type):
    """
    Represent a Singleton, that allow a Class to have only one instance even if we call the constructor to have a new one.

    Class Singleton from StackOverflow : https://stackoverflow.com/a/6798042/16027155
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]
