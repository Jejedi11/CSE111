def main():
  # Create and print a list named fruit.
  fruit_list = ["pear", "banana", "apple", "mango"]
  print(f"original: {fruit_list}")

  fruit_list.reverse()
  print(f"reversed: {fruit_list}")

  fruit_list.append("orange")
  print(fruit_list)

  i = int(fruit_list.index("apple"))
  fruit_list.insert(i, "cherry")
  print(fruit_list)

  i = int(fruit_list.index("banana"))
  fruit_list.pop(i)
  print(fruit_list)

  removed = fruit_list[len(fruit_list) - 1]
  fruit_list.pop(len(fruit_list) - 1)
  print(removed)
  print(fruit_list)

  fruit_list.sort()
  print(fruit_list)

  fruit_list.clear()
  print(fruit_list)

if __name__ == "__main__":
    main()