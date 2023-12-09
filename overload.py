class NotSpecifiedReturn():
    ...


class OverLoad():
    def __init__(self) -> None:
        self.functions = {}

    def add(self, func):
        types = func.__annotations__.copy()
        try:
            types.pop("return")
        except KeyError:
            ...
        types = tuple(types.values())
        hashed_value = hash(types)
        self.functions[hashed_value] = func
        return self

    def __call__(self, *args):
        args_classes = tuple([x.__class__ for x in args])
        hashed_value = hash(args_classes)
        try:
            f = self.functions[hashed_value]

            return_type = f.__annotations__.get("return", NotSpecifiedReturn())
            result = f(*args)
            if not isinstance(return_type, NotSpecifiedReturn) and not isinstance(result, return_type):
                raise TypeError("return type doesnt match")
            return result
        except KeyError:
            raise Exception("found no function for these arguments:", args)
        except TypeError as e:
            raise Exception(e)
        except Exception as e:
            raise Exception(e)


class methods():
    sum = OverLoad()

    @sum.add
    def sum(num1: int, num2: int):
        return num1+num2

    @sum.add
    def sum(string1: str, string2: str) -> str:
        return "concat:" + string1 + string2


m = methods()
r1 = m.sum(5, 2)
print(r1)
r2 = m.sum("a", "b")
print(r2)
