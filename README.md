# Personal Address Book

This is a Python program that allows you to manage your personal address book. The address book is stored as a dictionary, where each entry contains the name, address, phone number, and email address of a person. The program provides various operations such as inserting a new entry, deleting an entry, finding matching entries by partial name, finding an entry by phone number or email, and merging address books with your friends.

## Prerequisites

Make sure you have Python installed on your system. This program is compatible with Python 3.

## Getting Started

1. Clone the repository or copy the code into a Python file (e.g., ` python "Personal Address Book.py"`).
2. Open a terminal or command prompt and navigate to the directory where the file is located.

## Usage

Run the Python program using the following command:

```python
python address_book.py
```


The program will display a menu with options for managing your address book. Enter the corresponding number to select an option.

### Menu Options

1. **Insert a new entry**: Allows you to add a new entry to your address book. Enter the name, address, phone number, and email address when prompted.

2. **Delete an entry**: Lets you delete an existing entry from your address book. Enter the name of the entry you want to delete.

3. **Find by partial name**: Searches for entries in your address book that match a partial name. Enter a partial name to find matching entries.

4. **Find entry by email or phone number**: Searches for an entry in your address book based on an email address or phone number. Enter the email address or phone number to find matching entries.

5. **Merge another address book**: Allows you to merge the address book of your friend with yours. You will be prompted to enter the file path of the address book to merge.

6. **Exit**: Terminates the program and saves the current address book to a file (`addrbook.txt`).

## Data Storage

The address book is stored in a file named `addrbook.txt`. When the program starts, it reads the existing address book from this file. When the program exits, it writes the current address book to the same file, ensuring that your entries are saved for future use.

## Note

The program assumes that people in your address book have unique names. However, if you have multiple persons with the same name, the program handles this by storing the entries as a list of dictionaries, where each dictionary represents an individual with the same name.

Feel free to modify and enhance the program according to your needs!

Happy managing your address book!
