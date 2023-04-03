def print_header():
      print("Thanks, now I'll print your string reversed, and twice")
def print_twice(input: str):
    str = input
    print(str*2)
if __name__ == "__main__":
    s = input()
    print_header()
    print_reversed(s)
    print_twice(s)