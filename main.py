from art import logo
print(logo)
character = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '.', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '`', '~', ',', '<', '>', '?', '/', ':', ';', '[', ']', '{', '}', "'", '"', '|', '\\', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    # negates the addition of shift
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        #keeps tab and enter and space
        if(char == '\n'):
            end_text += '\n'
            continue
        if(char == '\t'):
            end_text += '\t'
            continue
        if(char == ' '):
            end_text += ' '
            continue
        # module ensures number isn't larger than list
        index = (character.index(char) + shift_amount) % 94
        end_text += character[index]
    
    print(f"Here's the {cipher_direction}d result: {end_text}")

should_continue = True

#reruns the code
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n")
    shift = int(input("Type the shift number:\n"))
    shift = shift
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
    again = input("Type 'yes' if you want to go again. Otherwise, type 'no'.").lower()
    if again == "no":
        should_continue = False
        print('Goodbye')