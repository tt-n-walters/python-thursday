from typing import Any, Optional, Callable, Union, Text

def binary_search(data: list, needle: Any, key: Optional[Callable[Any, Any]] = None) -> Any:
    left_index = 0
    right_index = len(data)

    while right_index - left_index > 1:
        middle_index = (right_index - left_index) // 2 + left_index
        if key:
            datum = key(data[middle_index])
            
        if datum > needle:
            right_index = middle_index
        elif datum < needle:
            left_index = middle_index
        else:
            return middle_index


def main(needle):
    with open("data_nums_1000000.txt", "r") as file:
        numbers = list(map(int, file.read().splitlines()))
        numbers.sort()



if __name__ == "__main__":
    print(main(6666666))
    
    binary_search()