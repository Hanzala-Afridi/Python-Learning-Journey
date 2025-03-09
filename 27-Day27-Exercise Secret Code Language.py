import random

def generate_random_chars():
    return ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=3))

def encode_word(word):
    if len(word) >= 3:
        new_word = word[1:] + word[0]  # Move first letter to the end
        random_prefix = generate_random_chars()
        random_suffix = generate_random_chars()
        return random_prefix + new_word + random_suffix
    else:
        return word[::-1]  # Reverse if length < 3

def decode_word(word):
    if len(word) < 3:
        return word[::-1]  # Reverse if length < 3
    else:
        core_word = word[3:-3]  # Remove 3 random characters from start and end
        return core_word[-1] + core_word[:-1]  # Move last letter to the beginning

def encode_message(message):
    words = message.split()
    encoded_words = [encode_word(word) for word in words]
    return ' '.join(encoded_words)

def decode_message(message):
    words = message.split()
    decoded_words = [decode_word(word) for word in words]
    return ' '.join(decoded_words)

def main():
    choice = input("Do you want to encode or decode? (e/d): ").strip().lower()
    if choice not in ['e', 'd']:
        print("Invalid choice! Please enter 'e' for encode or 'd' for decode.")
        return
    
    message = input("Enter your message: ")
    
    if choice == 'e':
        print("Encoded Message:", encode_message(message))
    else:
        print("Decoded Message:", decode_message(message))

if __name__ == "__main__":
    main()
