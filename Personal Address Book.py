def insert_a_new_entry():
    with open('addrbook.txt' , "a")as f:
        name=input("Enter name: ")
        address=input("Enter address: ")
        phone=int(input("Enter phone number: "))
        email=input("Enter email: ")
        p='name: '+name+"<address: "+address+'<phone: '+str(phone)+"<email: "+email
        f.write(p)
        f.write(" \n")
    f.close()
    print("Entry added successfully.")
def delete_an_entry():
    with open('addrbook.txt', "r") as f:
        lines = f.readlines()
    if not lines:
        print("File is empty.")
        return
    k = input("Enter the name of the entry you want to delete: ")
    with open('addrbook.txt', "w") as f:
        deleted = False
        for line in lines:
            if k not in line.split(":")[1]:
                f.write(line)
            else:
                deleted = True
        if deleted:
            print("Entry deleted successfully.")
        else:
            print("No entry found with the given name.")
def find_by_partial_name():
    partial_name=input("Enter a partial name: ")
    with open('addrbook.txt', "r") as f:
        lines = f.readlines()
        match_count = 0
        match_lines = []
        for line in lines:
            values = line.strip().split(":")
            p=values[1].split("<")
            if len(values) == 5:
                if partial_name in p[0]:
                    match_count += 1
                    match_lines.append(line.replace("<"," "))
        if match_count > 0:
            print("Matching Entries:")
            for match in match_lines:
                print(match)
        else:
            print("No matching entries found.")

def find_entry_by_email_or_phone_number():
    partial_name=input("Enter an email or phone number: ")
    with open('addrbook.txt', "r") as f:
        lines = f.readlines()
        match_count = 0
        match_lines = []
        for line in lines:
            values = line.strip().split(":")
            p=values[2].split("<")
            l=values[3].split("<")
            if len(values) == 5:
                if partial_name in p[0] or partial_name in l[0]:
                    match_count += 1
                    match_lines.append(line)
        if match_count > 0:
            print("Matching Entries:")
            for match in match_lines:
                print(match)
        else:
            print("No matching entries found.")
def merge_address_book():
    merge_file = input("Enter the file path of the address book to merge: ")
    entries_to_add = []
    duplicates = []
    with open(merge_file, "r") as f:
        merge_lines = f.readlines()
    with open('addrbook.txt', "r") as f:
        main_lines = f.readlines()
    for merge_line in merge_lines:
        duplicate = False
        for main_line in main_lines:
            if merge_line == main_line:
                duplicate = True
                duplicates.append(merge_line)
                break
        if not duplicate:
            entries_to_add.append(merge_line)
    if duplicates:
        print("Duplicate entries found:")
        for duplicate in duplicates:
            print(duplicate)
        while True:
            overwrite = input("Do you want to overwrite these entries? (yes/no) ")
            if overwrite.lower() == "yes":
                break
            elif overwrite.lower() == "no":
                for duplicate in duplicates:
                    entries_to_add.append(duplicate)
                break
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")
    with open('addrbook.txt', "a") as f:
        for entry in entries_to_add:
            f.write(entry)
    print("Address book merged successfully.")

while True:
    print("Phone Book")
    print("1. Insert a new entry")
    print("2. Delete an entry")
    print("3. Find by partial name")
    print("4. Find entry by email or phone number")
    print("5. Merge another address book")
    print("6. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        insert_a_new_entry()
    elif choice == '2':
        delete_an_entry()
    elif choice == '3':
        find_by_partial_name()
    elif choice == '4':
        find_entry_by_email_or_phone_number()
    elif choice == '5':
        merge_address_book()
    elif choice == '6':
        break
    else:
        print("Invalid choice. Please try again.")
