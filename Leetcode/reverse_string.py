def reverse_string(s):
    chars = list(s)  # Convert to list because strings are immutable
    left, right = 0, len(chars) - 1

    while left < right:
        chars[left], chars[right] = chars[right], chars[left]
        left += 1
        right -= 1

    return ''.join(chars)

         
def main():
    text = "Hello, World"
    
    print(reverse_string(text))    


if __name__ == "__main__":
    main()
