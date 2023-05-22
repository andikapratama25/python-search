def binary_search_definition(dictionary, target):
    left = 0
    right = len(dictionary) - 1

    while left <= right:
        mid = (left + right) // 2
        if dictionary[mid][0] == target:
            return dictionary[mid][1]
        elif dictionary[mid][0] < target:
            left = mid + 1
        else:
            right = mid - 1

    return "Definisi kata tidak ditemukan."

dictionary = [
    ["Apple", "Buah Apel"],
    ["Banana", "Buah Pisang"],
    ["Cat", "Kucing"],
    ["Duck", "Bebek"],
    ["Elephant", "Gajah"]
]

target = input("Masukkan kata yang ingin dicari: ")
definition = binary_search_definition(dictionary, target)

print(f"Definisi kata '{target}': {definition}")
