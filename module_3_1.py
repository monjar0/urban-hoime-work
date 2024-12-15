calls = 0
#counting other functions
def count_calls():
    global calls
    calls += 1


#string info function
def string_info(string):
    count_calls()
    return (len(string),string.upper(),string.lower())

#is_contains
def is_contains(string, list_to_search):
    count_calls()
    string_lower = string.lower()
    list_lower = [item.lower for item in list_to_search]
    return string_lower in list_lower
# Примеры вызова функций
info1 = string_info("Hello, World!")
info2 = string_info("Python")
contains1 = is_contains("urban", ["City", "Urban", "Village"])
contains2 = is_contains("python", ["java", "PYTHON", "C++"])

# Вывод результатов
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)