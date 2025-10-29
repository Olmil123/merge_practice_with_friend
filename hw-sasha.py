# #

# | Module 1
# #! Task 1
# for number in range(2, 1001):
#     prime = True
#     for i in range(2, number):
#         if number % i == 0:
#             prime = False
#             break
#     if prime:
#         print(number)

#! Task 2

# text = input("Введи строку: ")
# line = {}

# for dict in text:
#     line[dict] = line.get(dict, 0) + 1

# print(line)

# #! Task 3

# dict1 = {"name": "Alex", "age": 27}
# dict2 = {"city": "Khust", "job": "Dr.Max"}
# dict3 = dict2 | dict1
# print(dict3)

#! Task 4

# dict = {"city": "New-York", "name": "Eminem"}

# key = input("Prosim key for the delete: ")

# if key in dict:
#     del dict[key]
#     print("Good!")
# else:
#     print("There is no such key")

# | Module 2

# & Task 5

# user = input("Your text: ")
# user = user.lower()

# words = user.split()
# unique_words = {}

# for word in words:
#     if word in unique_words:
#         unique_words[word] += 1
#     else:
#         unique_words[word] = 1

# print("Number of unique words:", len(unique_words))
# print("Words and how many times they met:")
# for word, count in unique_words.items():
#     print(word, "->", count)


# & Task 6

# words = ["Sasha", "Dog", "Petja", "Pavel"]

# grouped = {}

# for word in words:
#     length = len(word)
#     if length not in grouped:
#         grouped[length] = [word]
#     else:
#         grouped[length].append(word)

# print("Grouping words by length:")
# for length, group in grouped.items():
#     print(length, "->", group)


# & Task 7

# words = {"Sasha": 20, "Natlia": 30, "Sara": 36, "Sendi": 45}

# letter = input("Enter the letter that the keys to delete start with: ")

# new_dict = {}

# for key, value in words.items():
#     if not key.startswith(letter):
#         new_dict[key] = value

# words = new_dict

# print("Updated dictionary:")
# print(words)

# & Task 8

# books = [
#     {
#         "author": "Рей Бредбері",
#         "name": "451° за Фаренгейтом",
#         "year": 1953,
#         "author": "Ліна Костенко",
#         "name": "Маруся Чурай",
#         "year": 1979,
#         "author": "Агата Кристи",
#         "name": "Убивства за абеткою",
#         "year": 1936,
#     }
# ]
# one_book_year = books[0]

# for book in books:
#     if book["year"] < one_book_year["year"]:
#         one_book_year = book


# print(f"Автор: {one_book_year['author']}")
# print(f"Название: {one_book_year['name']}")
# print(f"Год: {one_book_year['year']}")

# & Task 9

# people = [
#     {"name": "Sasha", "height": 175, "age": 20, "weight": 68},
#     {"name": "Ira", "height": 165, "age": 22, "weight": 55},
#     {"name": "Oleh", "height": 182, "age": 19, "weight": 74},
#     {"name": "Nina", "height": 170, "age": 21, "weight": 60},
# ]
# param = input("(height / age / weight): ")

# allowed = {"height", "age", "weight"}
# if param not in allowed:
#     print("Error: Only height, age or weight are allowed.")
# else:
#     best = max(people, key=lambda p: p[param])

#     print(f"Max for '{param}': {best['name']} -> {best[param]}")


# & Task 10

# shops = {
#     "Store_1": [{"name": "water", "price": 25}, {"name": "coca-cola", "price": 30}],
#     "Store_2": [
#         {"name": "iphone17", "price": 23000},
#         {"name": "xiaomi15T", "price": 15000},
#     ],
#     "Store_3": [{"name": "chocolate", "price": 40}, {"name": "cake", "price": 45}],
# }

# cheapest_item = None
# cheapest_price = float("inf")
# store_name = ""

# for shop, items in shops.items():
#     for item in items:
#         if item["price"] < cheapest_price:
#             cheapest_price = item["price"]
#             cheapest_item = item["name"]
#             store_name = shop

# print(f"{cheapest_item} — {cheapest_price} Kč for store {store_name}")

# & Task 11

# countries = {
#     "Ukraine": {"population": 38000000, "area": 603700},
#     "Czechia": {"population": 10500000, "area": 78865},
#     "Luxembourg": {"population": 640000, "area": 2586},
#     "France": {"population": 68000000, "area": 551695},
# }

# smallest_country = None
# smallest_area = float("inf")

# for country, info in countries.items():
#     if info["area"] < smallest_area:
#         smallest_area = info["area"]
#         smallest_country = country
# print(f"{smallest_country} — {smallest_area} км²")

# # & Task 12
# text = input("Enter pls: ")
# chars = []

# for char in text:
#     if text.count(char) == 1:
#         chars.append(char)
# print("Unique symbols:")
# for c in chars:
#     print(c)


# & Task 13

text = input("Enter pls: ")
words = text.split()

unique_words = set(words)
sorted_words = sorted(unique_words)

print("Unique symbols for the ABC:")
for word in sorted_words:
    print(word)
