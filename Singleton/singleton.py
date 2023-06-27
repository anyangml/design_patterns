class Singleton():
    def __new__(cls):
        if not hasattr(cls, "_instance"):
            cls._instance = super().__new__(cls)
        return cls._instance

if __name__ == "__main__":
    s1 = Singleton()
    s2 = Singleton()
    print(s1)
    print(s2)
    print(s1 == s2)
    print(id(s1))
    print(id(s2))