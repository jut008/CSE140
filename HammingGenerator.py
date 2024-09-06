import random

print("""Hello! This program will randomly generate a 7-bit Hamming code which is composed of 4 message bits and 3 parity bits. 
        They will be in the order of: [m0 m1 m2 p0 m3 p1 p2] - 'm' indicates a message bit and 'p' indicates a parity bit
        p0 will cover m0, m1, m2, and p0. 
        p1 will cover m0, m1, m3, and p1.
        p2 will cover m0, m2, m3, and p2.""")

# Function to generate a random and correct 7-bit Hamming code
def generate_hamming_code():
    bit7 = random.randint(0, 1)         # message bit 0
    bit6 = random.randint(0, 1)         # message bit 1
    bit5 = random.randint(0, 1)         # message bit 2
    bit3 = random.randint(0, 1)         # message bit 3

    # Calculate parity bits based on randomized message bits
    bit4 = (bit7 + bit6 + bit5) % 2     # parity bit 0
    bit2 = (bit7 + bit6 + bit3) % 2     # parity bit 1
    bit1 = (bit7 + bit5 + bit3) % 2     # parity bit 2

    # Combine all bits into a string formated like [m0 m1 m2 p0 m3 p1 p2]
    correct_string = f"{bit7}{bit6}{bit5}{bit4}{bit3}{bit2}{bit1}"
    return correct_string

# Function to flip a random bit in the Hamming code
def flip_bit(hamming_code):
    bit_list = list(hamming_code)  # Convert the string into a list
    flip_index = random.randint(0, 6)  # Select a random index to flip

    # Flip the bit at the selected index
    bit_list[flip_index] = '1' if bit_list[flip_index] == '0' else '0'

    # Convert the list back to a string
    flipped_string = ''.join(bit_list)
    return flipped_string

# Function where the errored hamming code is output into terminal, then the user must enter the corrected code
def user_guess():
    while True:

        # Step 1: Generate a Hamming code
        correct_code = generate_hamming_code()

        # Step 2: Flip one bit in the Hamming code
        flipped_string = flip_bit(correct_code)

        # Step 3: Show the user the flipped Hamming code
        print(f"There is a 1-bit error in this Hamming code: {flipped_string}")

        # Step 4: Ask the user to input the correct Hamming code
        hamming_guess = input("Enter the correct 7-bit Hamming code: ")

        # Step 5: Check if the guess matches the correct Hamming code
        if hamming_guess == correct_code:
            print("Correct! Well done.")
        else:
            print(f"Incorrect. The correct Hamming code was: {correct_code}")

        # Ask if the user wants to practice again
        practice_again = input("Do you want to practice again? (yes/no): ").lower()

        # If the user says no, exit the loop and end the program
        if practice_again != "yes":
            print("Hope that was good practice!")
            break

# Call the main function to start the program
user_guess()
    