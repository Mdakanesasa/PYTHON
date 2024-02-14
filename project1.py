#import modules
import argparse
import string
import random


#function

def generate(length,uppercase,lowercase,symbol,digits):
    character = ''
    if uppercase:
        character+= string.ascii_uppercase
    if lowercase:
        character+= string.ascii_lowercase
    if symbol:
        character+= string.punctuation
    if digits:
        character+= string.digits

    if not character:
        raise ValueError('at least one character must be selected')
                         
    return ''.join(random.choice(character) for _ in range(length))
    
def main():
    print("Welcome to the Command Line Password Generator!")
    length = int(input("Enter the length of the password: "))
    uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
    digits = input("Include digits? (y/n): ").lower() == 'y'
    symbols = input("Include symbols? (y/n): ").lower() == 'y'

    password = generate(length, uppercase, lowercase, digits, symbols)
    print("Generated Password:", password)

if __name__ == '__main__':
    main()        
