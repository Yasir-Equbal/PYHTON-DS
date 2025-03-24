items = ["apple", "banana", "grapes", "apple", "wine", "banana", "kela"]

unique_item = set()
duplicates = set()

for item in items:
    if item in unique_item:
        duplicates.add(item)
    unique_item.add(item)

print("Duplicates are:", duplicates)
