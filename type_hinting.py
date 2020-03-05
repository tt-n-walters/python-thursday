
# Good enough Python

def add(a, b):
    return a + b


# Better Python
def add(a: float, b: float) -> float:
    return a + b



def str_startswith_abc(string: str) -> bool:
    return string.startswith("abc")


str_startswith_abc("abc hello")
