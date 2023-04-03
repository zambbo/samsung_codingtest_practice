
'''
def permutations(arr: list[int], n: int) -> list[list]:
    
    result = []

    if n == 0:
        return [[]]

    for i in range(len(arr)):
        for rest in permutations(arr[:i] + arr[i+1:], n-1):
            result.append([arr[i]] + rest)
    
    return result

def combinations(arr: list[int], n: int) -> list[list]:
    
    result = []

    if n == 0:
        return [[]]

    for i in range(len(arr)):
        for rest in combinations(arr[i+1:], n-1):
            result.append([arr[i]] + rest)

    return result
'''



def permutations(arr: list[int], n:int, prefix=[]) -> None:
    if n == 0:
        print(prefix)

    for i in range(len(arr)):
        new_arr = arr[:i] + arr[i+1:]
        new_prefix = prefix + [arr[i]]
        permutations(new_arr, n-1, new_prefix)

def combinations(arr: list[int], n:int, prefix=[]) -> None:
    if n == 0:
        print(prefix)

    for i in range(len(arr)):
        new_arr = arr[i+1:]
        new_prefix = prefix + [arr[i]]
        combinations(new_arr, n-1, new_prefix)

permutations([1,2,3,4], 2)
combinations([1,2,3,4], 2)

    
