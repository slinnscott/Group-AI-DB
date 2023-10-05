sql_create_author_table = """
    create table author (
        id INT PRIMARY KEY,
        first_name VARCHAR(50),
        last_name VARCHAR(50),
        email VARCHAR(50),
        gender VARCHAR(50)
    );
"""

sql_create_book_table = """
    create table book (
        id INT PRIMARY KEY,
        book_title VARCHAR(50),
        author_id INT,
        genre VARCHAR(50),
        total_copies INT,
        available_copies INT,
        date_acquired DATE,
        price DECIMAL(5,2)
    );
"""

sql_create_checkout_table = """
    create table checkout (
        id INT PRIMARY KEY,
        book_id INT,
        patron_id INT,
        checkout_date DATE,
        return_date DATE
    );
"""

sql_create_hold_table = """
    create table hold (
        id INT PRIMARY KEY,
        book_id INT,
        patron_id INT,
        hold_date DATE
    );
"""

sql_create_patron_table = """
    create table patron (
        id INT PRIMARY KEY,
        first_name VARCHAR(50),
        last_name VARCHAR(50),
        email VARCHAR(50),
        gender VARCHAR(50),
        address VARCHAR(50)
    );
"""


def get_schema():
    schema = f"{sql_create_patron_table}{sql_create_author_table}{sql_create_book_table}{sql_create_checkout_table}{sql_create_hold_table}"
    return schema
