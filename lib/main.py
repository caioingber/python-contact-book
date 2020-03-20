from peewee import *

db = PostgresqlDatabase('contacts', user='caio', password='',
                        host='localhost', port=5432)
db.connect()

class BaseModel(Model):
    class Meta:
        database = db

class Contact(BaseModel):
    contact_id = AutoField(primary_key=True)
    first_name = CharField()
    last_name = CharField()
    phone_number = CharField()


# db.drop_tables([Contact])
db.create_tables([Contact])


# Contact(first_name='Caio', last_name='Ingber', phone_number='202-555-1234').save()
# Contact(first_name='Baba', last_name='Yaga', phone_number='703-555-9090').save()
# Contact(first_name='CheeChee', last_name='Fufu', phone_number='301-555-9090').save()
# Contact(first_name='Mr', last_name='NiceGuy', phone_number='703-234-0987').save()

# User runs app in the command line, initial contacts seed. User is then prompted by a few choices
# Create Contact, Look for Contact, delete contact, update contact
# If user selects Look for contact, prompted to then enter a first name, if there is a match, the contact's info is printed#

class App:
    def __init__(self):
        self.length = 0
    
    def intro(self):
        option = input("""Welcome to the Contact Book. Choose from the following options: \n 
        (a) Look for a contact\n 
        (b) Add a new contact\n
        (c) Show all contacts\n
        (d) Leave\n """)
        if option == 'a':
            self.search()
        elif option == 'b':
            self.create()
        elif option == 'c':
            self.show_all()
        elif option == 'd':
            quit()
        else:
            print("Invalid Input")
            self.home()

    def show_all(self):
        query = Contact.select()
        query = list(query)
        for contact in query:
            print(f"{query.index(contact) + 1}. Name: {contact.first_name} {contact.last_name}\n Number: {contact.phone_number}\n")
        self.home()

    def search(self):
        search_name = input("Please Enter a First Name: ")
        query = Contact.select().where(Contact.first_name ** f"%{search_name}%")
        if query.exists() and search_name != '':
            query = list(query)
            if len(query) > 1:
                for contact in query:
                    print(f"{query.index(contact) + 1}. Name: {contact.first_name} {contact.last_name}\n Number: {contact.phone_number}\n")
                # return query
                self.home()
            else:
                for contact in query:
                    print(f"Name: {contact.first_name} {contact.last_name}\nNumber: {contact.phone_number}\n")
                # return query
                self.home()
        else:
            cant_find = input("Sorry, we couldn't find that contact. Wan't to do another search? Y/N ")
            if cant_find == 'Y':
                self.search()
            else:
                self.intro()
        
    
    def home(self):
        error = input('Enter "home" to go back or "exit" to leave the application ')
        if error == 'home':
            self.intro()
        elif error == 'exit':
            quit()
        else:
            self.home()

    def create(self):
        first = input('Enter a First Name: ')
        second = input('Enter a Last Name: ')
        number = input('Enter a Phone Number: ')
        Contact(first_name=first, last_name=second, phone_number=number).save()
        self.intro()


start = App()
start.intro()