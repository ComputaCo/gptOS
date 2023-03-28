class Singleton:
    __instances = {}

    def __new__(cls):
        if cls not in Singleton.__instances:
            Singleton.__instances[cls] = super().__new__(Singleton)
        return Singleton.__instances[cls]

    @classmethod
    def Singleton(cls):
        if cls not in Singleton.__instances:
            cls.__new__()
        return Singleton.__instances[cls]
