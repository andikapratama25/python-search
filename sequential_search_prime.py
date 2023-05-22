def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def sequential_search_primes(numbers):
    primes = []
    for num in numbers:
        if is_prime(num):
            primes.append(num)
    return primes

numbers = [7, 10, 13, 6, 17, 22, 19] #Daftar bilangan
prime_numbers = sequential_search_primes(numbers) #Mencari bilangan prima

print("Bilangan prima yang ditemukan: ", prime_numbers) #Menampilkan bilangan prima yang ditemukan
