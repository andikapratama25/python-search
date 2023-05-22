def sequential_search_phone_book(phone_book, name):
    for entry in phone_book:
        if entry[0] == name:
            return entry[1]
    return None

phone_book = [
    ["John Doe", "081234567890"],
    ["Jane Smith", "089876543210"],
    ["Michael Johnson", "087811223344"],
    ["Emily Davis", "082122232425"]
]

name = "Jane Smith"
phone_number = sequential_search_phone_book(phone_book, name)

if phone_number:
    print("Nomor Telepon Jane:", phone_number) #Menampilkan nomor telepon Jane
else:
    print("Nomor Telepon Jane tidak ditemukan.")
