"""Singleton Module."""


class Singleton(object):
    """Singleton Class."""

    def __new__(cls, *args, **kargs):
        """インスタンスが生成されてなければ生成する."""
        if not hasattr(cls, "_instance"):
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance
