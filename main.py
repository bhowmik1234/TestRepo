# Merge Sort Algorithm in Python

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Recursive call on each half
        merge_sort(left_half)
        merge_sort(right_half)

        # Merge the sorted halves


        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Copy remaining elements of left_half
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        # Copy remaining elements of right_half
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Main program
print("=== Merge Sort Demo ===")
arr = []

n = int(input("Enter number of elements: "))
for i in range(n):
    num = int(input(f"Enter element {i+1}: "))
    arr.append(num)

print("Original array:", arr)
merge_sort(arr)
print("Sorted array:", arr)

# Extra: Ask user if they want to sort another array
while True:
    choice = input("Do you want to sort another array? (y/n): ").lower()
    if choice == 'y':
        arr = []
        n = int(input("Enter number of elements: "))
        for i in range(n):
            num = int(input(f"Enter element {i+1}: "))
            arr.append(num)
        print("Original array:", arr)
        merge_sort(arr)
        print("Sorted array:", arr)
    else:
        print("Exiting program.")
        break
