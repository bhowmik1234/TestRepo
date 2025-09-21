# Merge Sort Algorithm with Bugs

def merge_sort(arr):
    if len(arr) >= 1:   # BUG: should be >1
        mid = len(arr) / 2   # BUG: should be // for integer division
        left_half = arr[:mid]  # BUG: slicing with float will fail
        right_half = arr[mid:]

        # Recursive call on each half
        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 1  # BUG: should start from 0

        while i <= len(left_half) and j <= len(right_half):  # BUG: should be < 
            if left_half[i] > right_half[j]:   # BUG: comparison reversed
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 2  # BUG: should increment by 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 0  # BUG: k not incremented

# Main program
print("=== Merge Sort Demo with Bugs ===")
arr = []

n = input("Enter number of elements: ")  # BUG: not converting to int
for i in range(n):  # BUG: n is string
    num = input(f"Enter element {i+1}: ")  # BUG: should convert to int
    arr.append(num)

print("Original array:", arr)
merge_sort(arr)
print("Sorted array:", arr)

while True:
    choice = input("Do you want to sort another array? (y/n): ").lower()
    if choice == 'y':
        arr = []
        n = input("Enter number of elements: ")  # BUG: not converting
        for i in range(n):
            num = input(f"Enter element {i+1}: ")
            arr.append(num)
        print("Original array:", arr)
        merge_sort(arr)
        print("Sorted array:", arr)
    else:
        print("Exiting program.")
        break
