"""
In this script, we will build a simple library management system using Python and a MySQL database. 
This system will allow us to store information about books (title, author, ISBN) and perform basic operations like adding new books, searching by title, and listing all books in the library
"""

#import all relevant libraries
import pymysql
from backend.my_details import password

#establishing connection with my database
library_database = pymysql.connect(
    host='localhost',
    user='root',
    passwd=password,
    database='lavender'
)
# saving connection as an object
library_obj = library_database.cursor()



# #creating our first library table: Books
library_obj.execute("""
    CREATE TABLE IF NOT EXISTS books(
    id INT Auto_Increment primary key,
    title VARCHAR(255) NOT NULL,
    author VARCHAR(255),
    ISBN VARCHAR(255)
    )
""")

#inserting new records into book table
input = 'INSERT INTO books (title, author, ISBN) VALUES (%s, %s, %s)'
book_values = ("To Kill a Mockingbird", "Harper Lee", "9780060888695")
library_obj.execute(input, book_values)
library_database.commit()

#inserting another new records into book table
input = 'INSERT INTO books (title, author, ISBN) VALUES (%s, %s, %s)'
book_values = ("Alice in Wonderland", "Lewis Caroll", "9780194227230")
library_obj.execute(input, book_values)
library_database.commit()

#inserting another new records into book table
input = 'INSERT INTO books (title, author, ISBN) VALUES (%s, %s, %s)'
book_values = ("Pride and Prejudice ", "Jane Austen", "")
library_obj.execute(input, book_values)
library_database.commit()

#inserting another new records into book table
input = 'INSERT INTO books (title, author, ISBN) VALUES (%s, %s, %s)'
book_values = ("The Da Vinci Code", "", "")
library_obj.execute(input, book_values)
library_database.commit()

# Searching Books by user input and printing out details of the book
search = 'SELECT * FROM books WHERE title = %s'
book_title = input('Enter book title: ')
library_obj.execute(search, book_title)
library_database.commit()
print(f"Number of Books matching {book_title}: {library_obj.execute(search, book_title)}")
 

print('Book Details:')
book_details = 'SELECT title, author, ISBN FROM books WHERE title = %s'
library_obj.execute(book_details, book_title)
print_out = library_obj.fetchall()
print(print_out)

# Listing all books
print('All Books in our Databse:')
all_book = 'SELECT * FROM books'
library_obj.execute(all_book)
print_all = library_obj.fetchall()
print(print_all)

# Deleting a book by title
delete_book = 'DELETE FROM books WHERE title = %s'
delete_book_title = input('Enter book title you want to delete: ')
library_obj.execute(delete_book, delete_book_title)
print(f'{delete_book_title} has been successfully deleted from the database.')


#closing connection with the database
library_obj.close()
library_database.close()

print("Database connection closed.")
