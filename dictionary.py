Python :.137 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
import json

# --- Global Data Storage ---
# We use a standard Python dictionary to store the words and definitions.
# Key = Word (string)
# Value = Definition (string)
DICTIONARY = {}

def add_word():
    """Prompts the user for a new word and its definition and adds it to the DICTIONARY."""
    print("\n--- Add New Word ---")
    word = input("Enter the word: ").strip().lower()
    
    if not word:
        print("Error: Word cannot be empty.")
        return

    # Check if the word already exists
    if word in DICTIONARY:
        print(f"'{word}' is already in the dictionary. Current definition: '{DICTIONARY[word]}'")
        overwrite = input("Do you want to overwrite it? (yes/no): ").strip().lower()
        if overwrite != 'yes':
            print("Addition canceled.")
            return
    
    definition = input(f"Enter the definition for '{word}': ").strip()
    
    if not definition:
        print("Error: Definition cannot be empty. Addition canceled.")
        return

    DICTIONARY[word] = definition
    print(f"Success! '{word}' has been added/updated.")

def lookup_word():
    """Prompts the user for a word and displays its definition if found."""
    print("\n--- Look Up Word ---")
    word_to_find = input("Enter the word to look up: ").strip().lower()

    if not word_to_find:
        print("Error: Word cannot be empty.")
        return

    # Use the .get() method to safely retrieve the value
    definition = DICTIONARY.get(word_to_find)
    
    if definition:
        print(f"\nWord: {word_to_find.upper()}")
        print(f"Definition: {definition}")
    else:
        print(f"Sorry, '{word_to_find}' was not found in the dictionary.")

def list_all():
    """Prints all words and their definitions currently stored in the DICTIONARY."""
    print("\n--- All Dictionary Entries ---")
    if not DICTIONARY:
        print("The dictionary is currently empty.")
        return

    # Sort the words alphabetically for better readability
...     sorted_words = sorted(DICTIONARY.keys())
...     
...     for i, word in enumerate(sorted_words):
...         definition = DICTIONARY[word]
...         # Format output neatly
...         print(f"{i+1}. {word.title()}: {definition}")
...     
...     print(f"\nTotal entries: {len(DICTIONARY)}")
... 
... def main_menu():
...     """Displays the main menu and handles the application loop."""
...     print("Welcome to the Simple Python Dictionary!")
...     
...     while True:
...         print("\n--- Main Menu ---")
...         print("1. Add/Update Word")
...         print("2. Look Up Word")
...         print("3. List All Words")
...         print("4. Exit")
...         
...         choice = input("Enter your choice (1-4): ").strip()
...         
...         if choice == '1':
...             add_word()
...         elif choice == '2':
...             lookup_word()
...         elif choice == '3':
...             list_all()
...         elif choice == '4':
...             print("\nThank you for using the Simple Dictionary. Goodbye!")
...             break
...         else:
...             print("\nInvalid choice. Please enter a number between 1 and 4.")
... 
... # --- Application Entry Point ---
... if __name__ == "__main__":
...     # Ensure the main menu function is called only when the script is executed directly
...     main_menu()
