# Task 1
# class Massiv:
#     def __init__(self, arr) -> None:
#         self.arr = arr

#     def summa(self):
#         return sum(self.arr)
    
#     def mul(self):
#         result = 1
#         for i in self.arr:
#             result *= i
#         return result
    
#     def max_num(self):
#         return max(self.arr)
    
#     def min_num(self):
#         return min(self.arr)
    
# array = [1,2,3,4,5]
# m = Massiv(array)

# print(m.summa())
# print(m.mul())
# print(m.max_num())
# print(m.min_num())


# Task 2
# class Massiv:
#     def __init__(self, arr):
#         self.arr = arr

#     def max_index(self):
#         max_in = max(self.arr)
#         return self.arr.index(max_in)
            
    
# array = [1,2,3,4,5]
# m = Massiv(array)

# print(m.max_index())


# Task 3
# class Massiv:
#     def __init__(self, arr) -> None:
#         self.arr = arr

#     def place(self):
#         negative_nums = [i for i in self.arr if i < 0]
#         positive_nums = [i for i in self.arr if i >= 0]
#         return negative_nums + positive_nums
    
# array = [-3, 7, -2, 9, -5, 0, 4]
# m = Massiv(array)

# print(m.place())


# Task 4
# class Massiv:
#     def __init__(self, arr) -> None:
#         self.arr = arr

#     def pos_neg_numbers(self):
#         negative_nums = sum(1 for i in self.arr if i < 0)
#         positive_nums = sum(1 for i in self.arr if i >= 0)
#         return negative_nums, positive_nums
    
# array = [-3, 7, -2, 9, -5, 0, 4]
# m = Massiv(array)

# print(m.pos_neg_numbers())


# Task 5////////////////////////////
# class Massiv:
#     def __init__(self, arr) -> None:
#         self.arr = arr

#     def change_place(self, k):
#         n = len(self.arr)
#         return self.arr[n - k:] + self.arr[:n - k]
    
# array = [1, 2, 3, 4, 5]
# m = Massiv(array)
# k = 3

# new_array = m.change_place(k)
# print(new_array)


# # Task 6
# class Massiv:
#     def __init__(self, arr) -> None:
#         self.arr = arr

#     def change_back(self, k):
#         n = len(self.arr)
#         return self.arr[k:] + self.arr[:k]
    
# array = [1, 2, 3, 4, 5]
# m = Massiv(array)
# k = 3

# new_array = m.change_back(k)
# print(new_array)


# Task 7
# class Bank:
#     def __init__(self, A, B) -> None:
#         self.A = A
#         self.B = B

#     def calc_profit(self):
#         total_profit = 0
#         for i in range(len(self.A)):
#             profit = (self.A[i] * self.B[i]) / 100
#             total_profit += profit
#         return total_profit
    
# A = [1000, 2000, 3000, 4000]
# B = [5, 3, 4, 6]

# bank = Bank(A, B)
# profit = bank.calc_profit()
# print(profit)


# Task 8
# class Supermarket:
#     def __init__(self, A, B, S) -> None:
#         self.A = A
#         self.B = B
#         self.S = S

#     def calc(self, sold_amount):
#         total_sold = 0
#         total_remaining = 0

#         for i in range(len(self.A)):
#             sold_units = min(self.A[i], sold_amount // self.B[i])
#             total_sold += sold_units
#             total_remaining += self.A[i] - sold_units

#         return total_sold, total_remaining
    
# A = [10, 20, 30]
# B = [5, 10, 15]
# S = [25, 15, 20]

# supermarket = Supermarket(A, B, S)
# sold_amount = 100
# sold, remaining = supermarket.calc(sold_amount)
# print(sold)
# print(remaining)


# Task 9
# class CircleCounter:
#     def __init__(self, arr) -> None:
#         self.arr = arr

#     def count_occurances(self, k):
#         count = 0
#         for num in self.arr:
#             if num == k:
#                 count += 1
#         return count
        
# A = [1, 2, 3, 4, 3, 3, 5, 6, 7, 3]
# k = 3

# circle_counter = CircleCounter(A)
# result = circle_counter.count_occurances(k)
# print(result)


# Task 10
# class Reverse:
#     def __init__(self, arr) -> None:
#         self.arr = arr

#     def reverse_func(self):
#         return list(reversed(self.arr))
    
# A = [1, 2, 3, 4, 5]  # Berilgan massiv

# reversed_array = Reverse(A)
# reversed_result = reversed_array.reverse_func()

# print("Teskarisiga joylashtirilgan massiv:", reversed_result)


# Ex 1
# class Sanoq_sistema:
#     def __init__(self, num) -> None:
#         self.num = num

#     def to_binary(self):
#         return bin(self.num)
    
#     def to_octal(self):
#         return oct(self.num)
    
#     def to_hexidecimal(self):
#         return hex(self.num)
    
# n = 42
# res = Sanoq_sistema(n)
# print(res.to_binary())
# print(res.to_octal())
# print(res.to_hexidecimal())


# Ex 2
# class KOMPLEKS:
#     def __init__(self, real, imaginary):
#         self.real = real
#         self.imaginary = imaginary

#     def add(self, other):
#         real_sum = self.real + other.real
#         imaginary_sum = self.imaginary + other.imaginary
#         return KOMPLEKS(real_sum, imaginary_sum)

#     def subtract(self, other):
#         real_diff = self.real - other.real
#         imaginary_diff = self.imaginary - other.imaginary
#         return KOMPLEKS(real_diff, imaginary_diff)

#     def multiply(self, other):
#         real_product = self.real * other.real - self.imaginary * other.imaginary
#         imaginary_product = self.real * other.imaginary + self.imaginary * other.real
#         return KOMPLEKS(real_product, imaginary_product)

#     def divide(self, other):
#         denominator = other.real**2 + other.imaginary**2
#         real_quotient = (self.real * other.real + self.imaginary * other.imaginary) / denominator
#         imaginary_quotient = (self.imaginary * other.real - self.real * other.imaginary) / denominator
#         return KOMPLEKS(real_quotient, imaginary_quotient)

#     def __str__(self):
#         return f"{self.real} + {self.imaginary}i"

# a = KOMPLEKS(3, 4)
# b = KOMPLEKS(5, 6)

# print("a =", a)
# print("b =", b)
# print("a + b =", a.add(b))
# print("a - b =", a.subtract(b))
# print("a * b =", a.multiply(b))
# print("a / b =", a.divide(b))


# Ex 3
# class Matrix:
#     def __init__(self, matrix):
#         self.matrix = matrix

#     def find_max(self):
#         max_element = max(map(max, self.matrix))
#         return max_element

#     def find_min(self):
#         min_element = min(map(min, self.matrix))
#         return min_element

#     def is_symmetric(self):
#         n = len(self.matrix)
#         for i in range(n):
#             for j in range(i + 1, n):
#                 if self.matrix[i][j] != self.matrix[j][i]:
#                     return False
#         return True

#     def transpose(self):
#         transposed_matrix = [[self.matrix[j][i] for j in range(len(self.matrix))] for i in range(len(self.matrix[0]))]
#         return transposed_matrix

# A = [[1, 2, 3],
#      [2, 4, 5],
#      [3, 5, 6]]

# matritsa = Matrix(A)

# print(matritsa.find_max())
# print(matritsa.find_min())
# print(matritsa.is_symmetric())
# print("Matritsa transponlangan ko'rinishi:")
# transposed = matritsa.transpose()
# for row in transposed:
#     print(row)


# Ex 4
# import math

# class VEKTOR2_3D:
#     def __init__(self, x, y, z):
#         self.x = x
#         self.y = y
#         self.z = z

#     def add(self, other):
#         return VEKTOR2_3D(self.x + other.x, self.y + other.y, self.z + other.z)

#     def subtract(self, other):
#         return VEKTOR2_3D(self.x - other.x, self.y - other.y, self.z - other.z)

#     def dot_product(self, other):
#         return self.x * other.x + self.y * other.y + self.z * other.z

#     def length(self):
#         return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

#     def angle_cosine(self, other):
#         dot_product = self.dot_product(other)
#         self_length = self.length()
#         other_length = other.length()
#         return dot_product / (self_length * other_length)

# vector1 = VEKTOR2_3D(1, 2, 3)
# vector2 = VEKTOR2_3D(4, 5, 6)

# sum_vector = vector1.add(vector2)
# difference_vector = vector1.subtract(vector2)
# scalar_product = vector1.dot_product(vector2)
# length_vector1 = vector1.length()
# length_vector2 = vector2.length()
# angle_cosine = vector1.angle_cosine(vector2)
# print(sum_vector.x, sum_vector.y, sum_vector.z)
# print(difference_vector.x, difference_vector.y, difference_vector.z)
# print(scalar_product)
# print(length_vector1)
# print(length_vector2)
# print(angle_cosine)


# Ex 5
# class KO_PHAD:
#     def __init__(self, degree, coefficients):
#         self.degree = degree
#         self.coefficients = coefficients

#     def evaluate(self, x):
#         result = 0
#         for i in range(len(self.coefficients)):
#             result += self.coefficients[i] * (x ** (self.degree - i))
#         return result

#     def derivative(self):
#         derivative_coefficients = []
#         for i in range(1, len(self.coefficients)):
#             derivative_coefficients.append(self.coefficients[i] * (self.degree - i))
#         return KO_PHAD(self.degree - 1, derivative_coefficients[::-1])

# degree = 3 
# coefficients = [2, -3, 4, 5]  

# ko_phad = KO_PHAD(degree, coefficients)

# x_value = 2 
# result = ko_phad.evaluate(x_value)
# print(result)

# derivative = ko_phad.derivative()
# print(derivative.coefficients)
# print(derivative.degree)

# ////////////////////Ex 6//////////
# class UY_KUTUBXONASI:
#     def __init__(self):
#         self.books = []

#     def search_book(self, keyword):
#         found_books = []
#         for book in self.books:
#             if keyword.lower() in [book['title'].lower(), book['author'].lower(), str(book['year'])]:
#                 found_books.append(book)

#         return found_books
    
#     def add_book(self, title, author, year):
#         self.books.append[{'title': title, 'author': author, 'year': year}]
#         print(f"{title} nomli kitob kutubxonga qo'shildi")

#     def remove_books(self, title):
#         for book in self.books:
#             if book['title'].lower() == title.lower():
#                 self.books.remove(book)
#                 print(f'{title} book is removed from library')
#                 return
#         print(f'{title} named book is not found')

#     def display_books(self):
#         if not self.books:
#             print('Kutubxonada kitob mavjud emas')
#         else:
#             print("Kutubxonadagi kitoblar: ")
#             for book in self.books:
#                 print(f"{book['title']} - {book['author']} ({book['year']})")

# library = UY_KUTUBXONASI()
# library.add_book('Python', 'Liz', 2020)
# found_books = library.search_book('python')
# for book in found_books:
#     print(f"{book['title']} - {book['author']} ({book['year']})")
# library.remove_books('python')
# library.display_books()


# Ex 7
# class YON_DAFTAR:
#     def __init__(self):
#         self.entries = []

#     def search_entry(self, keyword):
#         found_entries = []
#         for entry in self.entries:
#             if keyword.lower() in [entry["name"].lower(), entry["year_of_birth"], entry["phone_number"]]:
#                 found_entries.append(entry)
#         return found_entries

#     def add_entry(self, name, year_of_birth, phone_number):
#         self.entries.append({"name": name, "year_of_birth": year_of_birth, "phone_number": phone_number})
#         print(f"{name} nomli yozuv yon daftarga qo'shildi.")

#     def remove_entry(self, name):
#         for entry in self.entries:
#             if entry["name"].lower() == name.lower():
#                 self.entries.remove(entry)
#                 print(f"{name} nomli yozuv yon daftardan o'chirildi.")
#                 return
#         print(f"{name} nomli yozuv topilmadi yon daftardan o'chirishda.")

#     def display_entries(self):
#         if not self.entries:
#             print("Hozircha yon daftarda hech qanday yozuv mavjud emas.")
#         else:
#             print("Yon daftardagi yozuvlar:")
#             for entry in self.entries:
#                 print(f"{entry['name']} - {entry['year_of_birth']} - {entry['phone_number']}")

# address_book = YON_DAFTAR()

# address_book.add_entry("Fotima", 1985, "+1234567890")
# address_book.add_entry("Zuhra", 1990, "+9876543210")
# address_book.add_entry("Name", 1980, "+2468013579")

# found_entries = address_book.search_entry("john")
# print("Qidiruv natijalari:")
# for entry in found_entries:
#     print(f"{entry['name']} - {entry['year_of_birth']} - {entry['phone_number']}")

# address_book.remove_entry("Fotima")

# address_book.display_entries()


# Ex 8
# class TALABA_GURUHI:
#     def __init__(self):
#         self.students = []

#     def search_student(self, keyword):
#         found_students = []
#         for student in self.students:
#             if keyword.lower() in [student["last_name"].lower(), student["year_of_birth"], student["phone_number"]]:
#                 found_students.append(student)
#         return found_students

#     def add_student(self, last_name, year_of_birth, phone_number):
#         self.students.append({"last_name": last_name, "year_of_birth": year_of_birth, "phone_number": phone_number})
#         print(f"{last_name} familiyasi talabalar guruhiga qo'shildi.")

#     def remove_student(self, last_name):
#         for student in self.students:
#             if student["last_name"].lower() == last_name.lower():
#                 self.students.remove(student)
#                 print(f"{last_name} familiyasi talabalar guruhidan o'chirildi.")
#                 return
#         print(f"{last_name} familiyasi talabalar guruhida topilmadi.")

#     def sort_students(self):
#         self.students.sort(key=lambda x: x["last_name"].lower())

#     def display_students(self):
#         if not self.students:
#             print("Hozircha talabalar guruhida hech qanday talaba yo'q.")
#         else:
#             print("Talabalar guruhidagi talabalar:")
#             for student in self.students:
#                 print(f"{student['last_name']} - {student['year_of_birth']} - {student['phone_number']}")

# students_group = TALABA_GURUHI()

# students_group.add_student("Fotima", 2000, "+1234567890")
# students_group.add_student("Zuhra", 1999, "+9876543210")
# students_group.add_student("Someone", 2001, "+2468013579")

# found_students = students_group.search_student("john")
# print("Qidiruv natijalari:")
# for student in found_students:
#     print(f"{student['last_name']} - {student['year_of_birth']} - {student['phone_number']}")

# students_group.remove_student("Zuhra")

# students_group.sort_students()

# students_group.display_students()


# Ex 9
# class POPULYATSIYA:
#     def __init__(self, x0, y0):
#         self.x = x0
#         self.y = y0

#     def update(self, n):
#         for i in range(1, n + 1):
#             next_x = self.y + 2 * self.x - self.x**2
#             next_y = self.x + 2 * self.y - self.y**2
#             self.x, self.y = next_x, next_y
#             print(f"Yil {i}: x = {self.x}, y = {self.y}")

# x0 = 0.1 
# y0 = 0.1  
# n = 10 

# population = POPULYATSIYA(x0, y0)
# population.update(n)


# Ex 10
# class STEK:
#     def __init__(self):
#         self.stack = []

#     def push(self, item):
#         self.stack.append(item)

#     def pop(self):
#         if not self.is_empty():
#             return self.stack.pop()

#     def is_empty(self):
#         return len(self.stack) == 0

#     def __str__(self):
#         return str(self.stack)


# def find_path(matrix):
#     if not matrix or not matrix[0]:
#         return []

#     rows, cols = len(matrix), len(matrix[0])
#     visited = set()
#     stack = STEK()
#     stack.push((0, 0))
#     directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Sag, past, chap, yuqori

#     while not stack.is_empty():
#         row, col = stack.pop()
#         if row == rows - 1 and col == cols - 1:
#             return stack.stack + [(row, col)]

#         visited.add((row, col))

#         for dr, dc in directions:
#             new_row, new_col = row + dr, col + dc
#             if 0 <= new_row < rows and 0 <= new_col < cols and (new_row, new_col) not in visited and matrix[new_row][new_col] == 1:
#                 stack.push((row, col))
#                 stack.push((new_row, new_col))
#                 break

#     return []


# # Test qismi
# maze = [
#     [1, 0, 0, 0],
#     [1, 1, 1, 0],
#     [0, 0, 1, 0],
#     [0, 1, 1, 1]
# ]

# path = find_path(maze)
# if path:
#     print("Topilgan yo'l:")
#     for row, col in path:
#         print(f"({row}, {col})")
# else:
#     print("Yo'l topilmadi.")


# Ex 11
# class YUGURUVCHI:
#     def __init__(self, familiya, initsiallar, jamoa, vaqt):
#         self.familiya = familiya
#         self.initsiallar = initsiallar
#         self.jamoa = jamoa
#         self.vaqt = vaqt

#     def __str__(self):
#         return f"{self.familiya} ({self.initsiallar}), {self.jamoa}, {self.vaqt} sekund"

# def sort_by_time(competitors):
#     return sorted(competitors, key=lambda x: x.vaqt)

# def average_time_by_group(competitors):
#     groups = {}
#     for competitor in competitors:
#         if competitor.jamoa not in groups:
#             groups[competitor.jamoa] = []
#         groups[competitor.jamoa].append(competitor.vaqt)

#     average_times = {}
#     for jamoa, times in groups.items():
#         average_times[jamoa] = sum(times) / len(times)

#     return average_times

# def top_3_groups_by_average_time(average_times):
#     sorted_average_times = sorted(average_times.items(), key=lambda x: x[1])
#     return [group[0] for group in sorted_average_times[:3]]

# competitors = [
#     YUGURUVCHI("Smith", "J.S.", "A", 120),
#     YUGURUVCHI("Johnson", "A.M.", "B", 150),
#     YUGURUVCHI("Williams", "R.D.", "A", 100),
#     YUGURUVCHI("Brown", "M.P.", "C", 200),
#     YUGURUVCHI("Jones", "T.L.", "B", 180),
#     YUGURUVCHI("Garcia", "E.J.", "C", 220)
# ]

# sorted_competitors = sort_by_time(competitors)
# print("Tartiblangan yuguruvchilar:")
# for competitor in sorted_competitors:
#     print(competitor)

# average_times = average_time_by_group(competitors)
# top_3 = top_3_groups_by_average_time(average_times)
# print("\nYuqori 3 jamoa o'rtacha yugurish vaqti:")
# for group in top_3:
#     print(group)


# Ex 12
# class FUTBOL:
#     def __init__(self, jamoa_nomi, galabalar_soni, duranglar_soni, maglubiyatlar_soni, kiritgan_toplar_soni, otkazgan_toplar_soni):
#         self.jamoa_nomi = jamoa_nomi
#         self.galabalar_soni = galabalar_soni
#         self.duranglar_soni = duranglar_soni
#         self.maglubiyatlar_soni = maglubiyatlar_soni
#         self.kiritgan_toplar_soni = kiritgan_toplar_soni
#         self.otkazgan_toplar_soni = otkazgan_toplar_soni

#     def __str__(self):
#         return f"{self.jamoa_nomi}: Galabalar: {self.galabalar_soni}, Duranglar: {self.duranglar_soni}, Mag'lubiyatlar: {self.maglubiyatlar_soni}, Kiritgan to'plar: {self.kiritgan_toplar_soni}, O'tkazgan to'plar: {self.otkazgan_toplar_soni}"

# def calculate_scores(teams):
#     scores = {}
#     for team in teams:
#         score = team.galabalar_soni * 3 + team.duranglar_soni * 1
#         scores[team.jamoa_nomi] = score
#     return scores

# def print_standings(scores):
#     sorted_standings = sorted(scores.items(), key=lambda x: x[1], reverse=True)
#     print("Jadval:")
#     for i, (team, score) in enumerate(sorted_standings, start=1):
#         print(f"{i}. {team}: {score} ochko")

# teams = [
#     FUTBOL("Barcelona", 20, 5, 2, 50, 45),
#     FUTBOL("Real Madrid", 18, 4, 3, 48, 50),
#     FUTBOL("Manchester United", 15, 6, 4, 40, 42),
#     FUTBOL("Bayern Munich", 20, 3, 2, 55, 40),
# ]

# scores = calculate_scores(teams)
# print_standings(scores)


# Ex 13
# class AVTOMOBILCHI:
#     def __init__(self, egasi_familiyasi, avtomobil_rusumi, avtomobil_nomeri):
#         self.egasi_familiyasi = egasi_familiyasi
#         self.avtomobil_rusumi = avtomobil_rusumi
#         self.avtomobil_nomeri = avtomobil_nomeri

#     def __str__(self):
#         return f"{self.egasi_familiyasi} ({self.avtomobil_rusumi}), {self.avtomobil_nomeri}"

# def sort_by_owner(autos):
#     return sorted(autos, key=lambda x: x.egasi_familiyasi)

# def find_info_by_car_name(autos, car_name):
#     for auto in autos:
#         if auto.avtomobil_rusumi == car_name:
#             return auto
#     return None

# def print_owner_by_car_info(autos, car_name):
#     auto = find_info_by_car_name(autos, car_name)
#     if auto:
#         print(f"{auto.avtomobil_rusumi} avtomobilining egasi: {auto.egasi_familiyasi}")
#     else:
#         print(f"{car_name} rusumli avtomobil topilmadi.")

# cars = [
#     AVTOMOBILCHI("Smith J.", "BMW", "123ABC"),
#     AVTOMOBILCHI("Johnson A.", "Toyota", "456DEF"),
#     AVTOMOBILCHI("Williams R.", "Audi", "789GHI"),
#     AVTOMOBILCHI("Brown M.", "Mercedes", "ABC123"),
# ]

# sorted_cars = sort_by_owner(cars)
# print("Avtomobil egalarining alfavit bo'yicha joylashuvi:")
# for car in sorted_cars:
#     print(car.egasi_familiyasi)

# car_name = "Toyota"
# print(f"\n{car_name} rusumidagi avtomobil egalarining ma'lumotlari:")
# print_owner_by_car_info(cars, car_name)

# car_name = "BMW"
# print(f"\n{car_name} rusumi va nomeri bo‘yicha avtomobil egasining familiyasi:")
# print_owner_by_car_info(cars, car_name)


# Ex 14
# def evaluate_formula(expression):
#     stack = []
#     operators = set(['+', '-', '*'])

#     for char in expression:
#         if char.isdigit():
#             stack.append(int(char))
#         elif char in operators:
#             operator = char
#             operand2 = stack.pop()
#             operand1 = stack.pop()
#             if operator == '+':
#                 stack.append(operand1 + operand2)
#             elif operator == '-':
#                 stack.append(operand1 - operand2)
#             elif operator == '*':
#                 stack.append(operand1 * operand2)

#     return stack.pop()

# expressions = ["5", "((2-4)*6)"]

# for expression in expressions:
#     result = evaluate_formula(expression)
#     print(f"Formula: {expression}, Qiymat: {result}")


# Ex 16
# class TO_RTBURCHAK:
#     def __init__(self, a, b, c, d):
#         self.a = a
#         self.b = b
#         self.c = c
#         self.d = d

#     def mavjudligi(self):
#         if self.a == self.b == self.c == self.d:
#             return True
#         return False

#     def yuza(self):
#         if self.mavjudligi():
#             return self.a * self.b
#         return None

#     def perimetr(self):
#         if self.mavjudligi():
#             return 2 * (self.a + self.b)
#         return None

#     def tur(self):
#         if self.mavjudligi():
#             if self.a == self.b:
#                 return "To‘g‘riburchak"
#             else:
#                 return "Kvadrat"
#         else:
#             if self.a == self.c and self.b == self.d:
#                 return "Parallellogram"
#         return None

# to_rtb1 = TO_RTBURCHAK(3, 3, 3, 3) 
# to_rtb2 = TO_RTBURCHAK(4, 3, 4, 3) 
# to_rtb3 = TO_RTBURCHAK(4, 3, 5, 3) 

# print("1. To'g'riburchak")
# print("Mavjudligi:", to_rtb1.mavjudligi())
# print("Yuzasi:", to_rtb1.yuza())
# print("Perimetri:", to_rtb1.perimetr())
# print("Tur:", to_rtb1.tur())

# print("\n2. To'g'riburchak")
# print("Mavjudligi:", to_rtb2.mavjudligi())
# print("Yuzasi:", to_rtb2.yuza())
# print("Perimetri:", to_rtb2.perimetr())
# print("Tur:", to_rtb2.tur())

# print("\n3. Parallellogram")
# print("Mavjudligi:", to_rtb3.mavjudligi())
# print("Yuzasi:", to_rtb3.yuza())
# print("Perimetri:", to_rtb3.perimetr())
# print("Tur:", to_rtb3.tur())


# Ex 17
# import math

# class RATSIONAL:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b

#     def tekshirish(self, other):
#         return self.a == other.a and self.b == other.b

#     def yigindi(self, other):
#         result_a = self.a * other.b + self.b * other.a
#         result_b = self.b * other.b
#         return self.kisqartirilgan(RATSIONAL(result_a, result_b))

#     def kisqartirilgan(self, rational):
#         gcd = math.gcd(rational.a, rational.b)
#         return RATSIONAL(rational.a // gcd, rational.b // gcd)

#     @staticmethod
#     def eng_katta(rationals):
#         max_rational = rationals[0]
#         for rational in rationals:
#             if rational.a / rational.b > max_rational.a / max_rational.b:
#                 max_rational = rational
#         return max_rational

# rationals = [
#     RATSIONAL(1, 2),
#     RATSIONAL(3, 4),
#     RATSIONAL(2, 3)
# ]

# a = RATSIONAL(1, 2)
# b = RATSIONAL(1, 2)
# print("a va b ratsional sonlarining tengligi:", a.tekshirish(b))

# r = a.yigindi(b)
# print("a va b ratsional sonlarining yig'indisi:", r.a, "/", r.b)

# print("Kisqartirilgan r:", r.kisqartirilgan(r))

# print("Eng katta ratsional son:", RATSIONAL.eng_katta(rationals))


# vorislik
# *7
# class MATN:
#     def __init__(self, text):
#         self.text = text

#     def oqish(self):
#         return self.text

#     def saqlash(self, text):
#         self.text = text

#     def chop_qilish(self):
#         return self.text


# class SHIFRLASH(MATN):
#     def __init__(self, text):
#         super().__init__(text)

#     def shifrlash(self, *shifts):
#         alphabet = 'abcdefghijklmnopqrstuvwxyz'
#         result = ''

#         for i, char in enumerate(self.text):
#             if char.isalpha():
#                 index = alphabet.index(char.lower())
#                 shift = shifts[i % len(shifts)]
#                 new_index = (index + shift) % len(alphabet)
#                 if char.isupper():
#                     result += alphabet[new_index].upper()
#                 else:
#                     result += alphabet[new_index]
#             else:
#                 result += char

#         return result


# matn = "hello world"
# shifrlash_obj = SHIFRLASH(matn)

# shifts = [5, 3, 2, 4]
# shifr_matn = shifrlash_obj.shifrlash(*shifts)

# print("Boshlang'ich matn:", matn)
# print("Shifrlangan matn:", shifr_matn)


# *8
# class TAXTA:
#     def __init__(self):
#         self.taxta = [[None] * 8 for _ in range(8)]

#     def katak_joylash(self, koordinata, belgi):
#         column = ord(koordinata[0]) - ord('a')
#         row = 8 - int(koordinata[1])
#         self.taxta[row][column] = belgi

#     def chop_qilish(self):
#         for row in self.taxta:
#             print(" ".join([cell if cell else '0' for cell in row]))
#         print("\n")


# class FARZIN(TAXTA):
#     def __init__(self):
#         super().__init__()

#     def uradigan_katak(self, koordinata):
#         column = ord(koordinata[0]) - ord('a')
#         row = 8 - int(koordinata[1])
#         self.taxta[row][column] = 'X'

# farzin_taxta = FARZIN()
# farzin_taxta.uradigan_katak('a2')
# farzin_taxta.uradigan_katak('g5')

# farzin_taxta.katak_joylash('b3', 'X')
# farzin_taxta.katak_joylash('c4', 'X')
# farzin_taxta.katak_joylash('f7', 'X')
# farzin_taxta.katak_joylash('h8', 'X')

# farzin_taxta.chop_qilish()


# *9
# class HABAR:
#     def __init__(self, text):
#         self.text = text

#     def junatish(self):
#         result = []
#         for char in self.text:
#             result.extend([char]*3)
#         return result

#     def qabul_qilish(self):
#         result = []
#         i = 0
#         while i < len(self.text):
#             count = self.text.count(self.text[i])
#             if count > len(self.text) // 2:
#                 result.append(self.text[i])
#             i += count
#         return result


# class XABARNI_SHIFRLASH(HABAR):
#     def __init__(self, text):
#         super().__init__(text)

#     def shifrlash(self):
#         result = []
#         for char in self.text:
#             result.append(str(ord(char)))
#         return result

# matn = "101"
# xabar = XABARNI_SHIFRLASH(matn)

# junatilgan_xabar = xabar.junatish()
# print("Jo'natilgan xabar:", junatilgan_xabar)

# qabul_qilinadigan_xabar = xabar.qabul_qilish()
# print("Qabul qilinayotgan xabar:", qabul_qilinadigan_xabar)

# shifrlangan_xabar = xabar.shifrlash()
# print("Shifrlangan xabar:", shifrlangan_xabar)


# *10
# import math

# class Tayanch:
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c

#     def Turi(self):
#         if self.a == self.b == self.c:
#             return "Teng tomonli uchburchak"
#         elif self.a == self.b or self.a == self.c or self.b == self.c:
#             return "Teng tomonli uchburchak"
#         else:
#             return "Tog'riburchak"

#     def Yuza(self):
#         s = (self.a + self.b + self.c) / 2
#         return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

#     def Perimetr(self):
#         return self.a + self.b + self.c


# class T_UCHBURCHAK(Tayanch):
#     def __init__(self, a, b, c):
#         super().__init__(a, b, c)

#     def Turi(self):
#         return "Tog'riburchak"


# class TT_UCHBURCHAK(Tayanch):
#     def __init__(self, a):
#         super().__init__(a, a, a)


# class TY_UCHBURCHAK(Tayanch):
#     def __init__(self, a, b):
#         super().__init__(a, b, math.sqrt(a**2 + b**2))

#     def Turi(self):
#         return "Teng yonli uchburchak"

# t_uchburchak = T_UCHBURCHAK(3, 4, 5)
# print("T_UCHBURCHAK: ", t_uchburchak.Turi(), ", Yuza: ", t_uchburchak.Yuza(), ", Perimetr: ", t_uchburchak.Perimetr())

# tt_uchburchak = TT_UCHBURCHAK(5)
# print("TT_UCHBURCHAK: ", tt_uchburchak.Turi(), ", Yuza: ", tt_uchburchak.Yuza(), ", Perimetr: ", tt_uchburchak.Perimetr())

# ty_uchburchak = TY_UCHBURCHAK(3, 4)
# print("TY_UCHBURCHAK: ", ty_uchburchak.Turi(), ", Yuza: ", ty_uchburchak.Yuza(), ", Perimetr: ", ty_uchburchak.Perimetr())


# *11
# class Tayanch:
#     def __init__(self, A, B, C, D):
#         self.A = A
#         self.B = B
#         self.C = C
#         self.D = D

#     def Mavjud(self):
#         return True

#     def Yuza(self):
#         x1, y1 = self.A
#         x2, y2 = self.B
#         x3, y3 = self.C
#         x4, y4 = self.D

#         return abs((x1 * y2 + x2 * y3 + x3 * y4 + x4 * y1 - y1 * x2 - y2 * x3 - y3 * x4 - y4 * x1) / 2)

#     def Perimetr(self):
#         AB = ((self.B[0] - self.A[0])**2 + (self.B[1] - self.A[1])**2)**0.5
#         BC = ((self.C[0] - self.B[0])**2 + (self.C[1] - self.B[1])**2)**0.5
#         CD = ((self.D[0] - self.C[0])**2 + (self.D[1] - self.C[1])**2)**0.5
#         DA = ((self.A[0] - self.D[0])**2 + (self.A[1] - self.D[1])**2)**0.5
#         return AB + BC + CD + DA


# class ROMB(Tayanch):
#     def __init__(self, A, B, C, D):
#         super().__init__(A, B, C, D)

#     def Turi(self):
#         return "ROMB"


# class PARALELLOGRAM(Tayanch):
#     def __init__(self, A, B, C, D):
#         super().__init__(A, B, C, D)

#     def Turi(self):
#         return "PARALELLOGRAM"


# class KVADRAT(Tayanch):
#     def __init__(self, A, B, C, D):
#         super().__init__(A, B, C, D)

#     def Turi(self):
#         return "KVADRAT"


# romb = ROMB((1, 1), (2, 2), (3, 3), (4, 4))
# print("ROMB: ", romb.Turi(), ", Yuza: ", romb.Yuza(), ", Perimetr: ", romb.Perimetr())

# parallellogram = PARALELLOGRAM((1, 1), (3, 1), (4, 3), (2, 3))
# print("PARALELLOGRAM: ", parallellogram.Turi(), ", Yuza: ", parallellogram.Yuza(), ", Perimetr: ", parallellogram.Perimetr())

# kvadrat = KVADRAT((1, 1), (2, 1), (2, 2), (1, 2))
# print("KVADRAT: ", kvadrat.Turi(), ", Yuza: ", kvadrat.Yuza(), ", Perimetr: ", kvadrat.Perimetr())


# Polimorfizm

# Task 1
# class Progressiya:
#     def init(self, a, d_or_q):
#         self.a = a
#         self.d_or_q = d_or_q

#     def get_term(self, n):
#         pass

#     def sum_of_terms(self, n):
#         pass

# class ArifmProgress(Progressiya):
#     def init(self, a, d):
#         super().init(a, d)

#     def get_term(self, n):
#         return self.a + (n - 1) * self.d

#     def sum_of_terms(self, n):
#         return n * (2 * self.a + (n - 1) * self.d) // 2

# class GeomProgress(Progressiya):
#     def init(self, a, q):
#         super().init(a, q)

#     def get_term(self, n):
#         return self.a * self.d_or_q  (n - 1)

#     def sum_of_terms(self, n):
#         if self.d_or_q == 1:
#             return n * self.a
#         else:
#             return self.a*(1 - self.d_or_q  n) // (1 - self.d_or_q)



# # Task 2
# class SanokSistema10:
#     def init(self, son):
#         self.son = son

#     def oqish(self):
#         return self.son

#     def saqlash(self, son):
#         self.son = son

#     def chop_qilish(self):
#         return f"San: {self.son}, Sanoq sistema 2 da: {bin(self.son)}, Sanoq sistema 8 da: {oct(self.son)}, Sanoq sistema 16 da: {hex(self.son)}"


# class SanokSistema2(SanokSistema10):
#     def init(self, son):
#         super().init(son)

#     def chop_qilish(self):
#         return f"San: {self.son}, Sanoq sistema 2 da: {bin(self.son)}"


# class SanokSistema8(SanokSistema10):
#     def init(self, son):
#         super().init(son)

#     def chop_qilish(self):
#         return f"San: {self.son}, Sanoq sistema 8 da: {oct(self.son)}"


# class SanokSistema16(SanokSistema10):
#     def init(self, son):
#         super().init(son)

#     def chop_qilish(self):
#         return f"San: {self.son}, Sanoq sistema 16 da: {hex(self.son)}"


# son = int(input("Son kiriting: "))
# sanoq_sistema_10 = SanokSistema10(son)
# sanoq_sistema_2 = SanokSistema2(son)
# sanoq_sistema_8 = SanokSistema8(son)
# sanoq_sistema_16 = SanokSistema16(son)

# print(sanoq_sistema_10.chop_qilish())
# print(sanoq_sistema_2.chop_qilish())
# print(sanoq_sistema_8.chop_qilish())
# print(sanoq_sistema_16.chop_qilish())


# # Task 3
# import math
# class Kvadrat:
#     def init(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c

#     def Kv_ildiz(self):
#         pass

# class BIKVADRAT(Kvadrat):
#     def init(self, a, b, c):
#         super().init(a, b, c)

#     def Kv_ildiz(self):
#         D = self.b**2 - 4 * self.a * self.c
#         if D < 0:
#             return "Tenglama ildizi yo'q"
#         elif D == 0:
#             x = -self.b / (2 * self.a)
#             return f"1 ildiz bor: x = {x}"
#         else:
#             x1 = (-self.b + math.sqrt(D)) / (2 * self.a)
#             x2 = (-self.b - math.sqrt(D)) / (2 * self.a)
#             return f"2 ildiz bor: x1 = {x1}, x2 = {x2}"

# a = 1
# b = -3
# c = 2

# kv = BIKVADRAT(a, b, c)
# print(kv.Kv_ildiz())


# # Task 4
# # Ishlolmadim


# # Task 5
# # Ishlolmadim


# # Task 6
# # Ishlolmadim


# # Task 7
# class TARIF:
#     def init(self, kiruvchi_qo_ngiroqlar, chiquvchi_qo_ngiroqlar):
#         self.kiruvchi_qo_ngiroqlar = kiruvchi_qo_ngiroqlar
#         self.chiquvchi_qo_ngiroqlar = chiquvchi_qo_ngiroqlar

#     def oylik_xarajat(self):
#         pass

# class UNIVERSAL(TARIF):
#     def init(self, kiruvchi_qo_ngiroqlar, chiquvchi_qo_ngiroqlar):
#         super().init(kiruvchi_qo_ngiroqlar, chiquvchi_qo_ngiroqlar)

#     def oylik_xarajat(self):
#         n = self.kiruvchi_qo_ngiroqlar
#         m = self.chiquvchi_qo_ngiroqlar
#         A = 0
#         B = 0.03
#         return n * A + m * B

# class PROGRESS(TARIF):
#     def init(self, kiruvchi_qo_ngiroqlar, chiquvchi_qo_ngiroqlar):
#         super().init(kiruvchi_qo_ngiroqlar, chiquvchi_qo_ngiroqlar)

#     def oylik_xarajat(self):
#         n = self.kiruvchi_qo_ngiroqlar
#         m = self.chiquvchi_qo_ngiroqlar
#         A = 0.01
#         if m <= 50:
#             B = 0.03
#         elif 50 < m <= 100:
#             B = 0.02
#         else:
#             B = 0.01
#         return n * A + m * B

# # Test qismi
# kiruvchi_qo_ngiroqlar = 80
# chiquvchi_qo_ngiroqlar = 70

# universal_tarif = UNIVERSAL(kiruvchi_qo_ngiroqlar, chiquvchi_qo_ngiroqlar)
# progress_tarif = PROGRESS(kiruvchi_qo_ngiroqlar, chiquvchi_qo_ngiroqlar)

# print("Universal tarif bo'yicha oylik xarajat:", universal_tarif.oylik_xarajat())
# print("Progress tarif bo'yicha oylik xarajat:", progress_tarif.oylik_xarajat())


# # Task 8
# class SOLIQ:
#     def init(self, Min_IH, DM):
#         self.Min_IH = Min_IH
#         self.DM = DM

#     def Daromat_soliq(self):
#         pass

# class SOLIQ_NOGIRON(SOLIQ):
#     def init(self, Min_IH, DM):
#         super().init(Min_IH, DM)

#     def Daromat_soliq(self):
#         if self.DM >= 1 * self.Min_IH and self.DM <= 4 * self.Min_IH:
#             return 0
#         elif self.DM >= 4 * self.Min_IH + 1 and self.DM <= 5 * self.Min_IH:
#             return 0.09
#         elif self.DM >= 5 * self.Min_IH + 1 and self.DM <= 10 * self.Min_IH:
#             return 0.17
#         else:
#             return 0.22

# # Test qismi
# Min_IH = 1000
# DM = 6000

# soliq = SOLIQ_NOGIRON(Min_IH, DM)
# print("Daromat solig'i:", soliq.Daromat_soliq())



# # Task 9
# class TURTBURCHAK:
#     def init(self, a, b, c, d, h):
#         self.a = a
#         self.b = b
#         self.c = c
#         self.d = d
#         self.h = h

#     def YUZA(self):
#         pass

# class ROMB(TURTBURCHAK):
#     def init(self, a, h):
#         super().init(a, a, a, a, h)

#     def YUZA(self):
#         return self.a * self.h

# class KVADRAT(TURTBURCHAK):
#     def init(self, a):
#         super().init(a, a, a, a, a)

#     def YUZA(self):
#         return self.a ** 2

# class TTURTBURCHAK(TURTBURCHAK):
#     def init(self, a, b, h):
#         super().init(a, b, a, b, h)

#     def YUZA(self):
#         return (self.a + self.b) * self.h / 2

# class TRAPETSIYA(TURTBURCHAK):
#     def init(self, a, b, c, d, h):
#         super().init(a, b, c, d, h)

#     def YUZA(self):
#         return (self.a + self.b) * self.h / 2

# class PARALLELOGRAM(TURTBURCHAK):
#     def init(self, a, b, h):
#         super().init(a, b, a, b, h)

#     def YUZA(self):
#         return self.a * self.h

# # Test qismi
# romb = ROMB(4, 5)
# kvadrat = KVADRAT(3)
# tturtburchak = TTURTBURCHAK(4, 6, 5)
# trapetsiya = TRAPETSIYA(3, 4, 5, 6, 7)
# parallelogram = PARALLELOGRAM(4, 5, 6)

# print("Romblan yuzasi:", romb.YUZA())
# print("Kvadrat yuzasi:", kvadrat.YUZA())
# print("Tortburchak yuzasi:", tturtburchak.YUZA())
# print("Trapetsiya yuzasi:", trapetsiya.YUZA())
# print("Parallelogram yuzasi:", parallelogram.YUZA())
