import time


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()

        print(f"{func.__name__} took {end - start:.4f}s")
        return result

    return wrapper


@timer
def find_element(arr, element):
    for index in range(len(arr)):
        if arr[index] == element:
            return index
    return -1


@timer
def main():
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    element = 10

    print(find_element(nums, element))


if __name__ == "__main__":
    main()
