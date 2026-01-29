from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(logo)

def caesar(original_text, shift_amount, shift_direction):
    length = len(alphabet)
    output = ""
    for letter in original_text:
        if letter in alphabet:
            index = alphabet.index(letter)
            if shift_direction == 'encode':
                output += alphabet[(index + shift_amount) % length]
            elif shift_direction == 'decode':
                output += alphabet[(index - shift_amount) % length]
        else:
            output += letter
    print(f"Here is your {shift_direction}d word: {output}")

bruhh_continue = True

while bruhh_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ").lower()
    if direction != "encode" and direction != "decode":
        print("Wrong input. Try again.")
    else:
        text = input("Type your message: ").lower()
        try:
            shift = int(input("Type the shift number: "))
            caesar(original_text=text, shift_amount=shift, shift_direction=direction)
            response = input("Type 'yes' if you want to go again. Otherwise type 'no': ").lower()
            if response == "no":
                bruhh_continue = False
                break
        except ValueError:
            print("Wrong input. Please enter a valid number.")



