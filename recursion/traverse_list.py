
def traverse_list(item_list):
    count = 0
    print(f"List: {item_list}")
    for item in item_list:
        if isinstance(item, list):
            print("Encountered sublist")
            count += traverse_list(item)
        else:
            count += 1
            print(f"Counted leaf item \"{item}\"; count: {count}")
    print(f"-> Returning count {count}")
    return count


def count_leaf_items(item_list):
    count = 0
    stack = []
    current_list = item_list
    i = 0

    while True:
        if i == len(current_list):
            if current_list == item_list:
                return count
            else:
                current_list, i = stack.pop()
                i += 1
                continue

        if isinstance(current_list[i], list):
            stack.append([current_list, i])
            current_list = current_list[i]
            i = 0
        else:
            count += 1
            print(f"Counted leaf item; count: {count}")
            i += 1


names = ["Adam", ["Bob", ["Chet", "Cat", ], "Barb", "Bert"], "Alex", ["Bea", "Bill"], "Ann"]

names_length = traverse_list(names)

print(f"The list length is: {names_length}")

names_length2 = count_leaf_items(names)

print(f"The list length is: {names_length2}")



