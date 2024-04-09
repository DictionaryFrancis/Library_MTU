###### IMPORTS ######
import datetime

####### GLOBAL########
book_names = []
membership_list = []


####### HANDLE BORROW BOOK ######
def handle_borrow(name:str, membership_number:int,book):
    # here we are open the file as reading, then split each part and appending it in the array
    with open('book_inventory.txt', 'r') as document:
        for line in document:
            parts = line.split(',', 1)
            book_name = parts[0].strip()
            book_names.append(book_name)

    # transform the int in string
    membership_str = str(membership_number)
    if len(membership_str) != 6:
        print('Membership number must be exactly 6 digits, try again!')
        return None
    
    print(f'Name: {name}, Membership Number: {membership_number}')

    more_than_4 = membership_list.count(membership_str)
    # Here, we are checking if the user has more than 4 or not, if he/she has more they cannot borrow anymore
    if book in book_names:
        print(f'{book} is in the inventory, you can borrow it!')
        while True:
            if more_than_4 > 4:
                print(f'Sorry, you cannot borrow anymore, you borrowed more than 4 books.')
                break
            else:
                print(f'You borrowed less than 4 books, so you are available to borrow!')
            borrow = input('Would you like to borrow it? (yes/no)')
            if borrow.lower == 'yes':
                print('done')
                with open('borrowed_books.txt', 'a') as document:
                    while True:
                        today = datetime.date.today()
                        date_today = today.strftime("%Y-%m-%d")
                        document.write(f'{name}, {membership_number}, {book}, {date_today}\n')
                        print(f'Information was saved successfully!')
                        break
                break
            elif borrow.lower() == 'no':
                print('ok, thank you')
                break
            else:
                print('Please enter a valid command (yes or no)')
    else:
        print(f'Sorry, {book} is not in the inventory.')

    return name, membership_number, book        


################################