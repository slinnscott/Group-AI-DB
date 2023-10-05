import os

from db import create_table, create_connection
from schema import *


def select_all_from_author(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM author")

    rows = cur.fetchall()

    for row in rows:
        print(row)

def insert_to_author(conn):
    """
    Create a new project into the projects table
    :param conn:
    :param project:
    :return: project id
    """
    sql = """
         insert into author (id, first_name, last_name, email, gender) values
         (1, 'Dietrich', 'Ferras', 'dferras0@mayoclinic.com', 'Male'),
         (2, 'Locke', 'Maleby', 'lmaleby1@globo.com', 'Male'),
         (3, 'Masha', 'Ridsdale', 'mridsdale2@seattletimes.com', 'Female'),
         (4, 'Maddy', 'McLay', 'mmclay3@godaddy.com', 'Female'),
         (5, 'Aland', 'Goodwill', 'agoodwill4@domainmarket.com', 'Male'),
         (6, 'Livvyy', 'Syson', 'lsyson5@themeforest.net', 'Female'),
         (7, 'Annette', 'Boarder', 'aboarder6@europa.eu', 'Female'),
         (8, 'Rubina', 'Radleigh', 'rradleigh7@a8.net', 'Female'),
         (9, 'Uri', 'Molesworth', 'umolesworth8@blog.com', 'Male'),
         (10, 'Noland', 'O'' Clovan', 'noclovan9@tamu.edu', 'Male');
    """

    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    return cur.lastrowid

def insert_to_book(conn):
    sql = """
        insert into book (id, book_title, author_id, genre, total_copies, available_copies, date_acquired, price) values
        (1, 'Evelyn', 1, 'Drama', 22, 20, '10/28/2014', 18.96),
        (2, 'Harry Potter and the Chamber of Secrets', 1, 'Adventure|Fantasy', 16, 2, '10/2/2002', 46.0),
        (3, 'Prince of Central Park, The', 2, 'Action|Adventure|Drama', 28, 10, '12/30/2006', 99.68),
        (4, 'Life with Father', 2, 'Comedy', 34, 15, '9/18/2022', 42.83),
        (5, 'Regeneration', 3, 'Crime|Drama|Romance', 33, 14, '8/11/2023', 39.38),
        (6, 'What to Do in Case of Fire (Was tun, wenn''s brennt?),', 3, 'Comedy|Drama', 24, 25, '9/9/2021', 7.02),
        (7, 'The Little Kidnappers', 3, 'Drama|Romance|War', 15, 23, '10/23/2002', 33.66),
        (8, 'Mr. Lucky', 3, 'Comedy|Romance', 19, 20, '1/16/2002', 65.82),
        (9, 'Manitou, The', 4, 'Horror', 34, 24, '1/27/2019', 145.1),
        (10, 'Rent-A-Cop', 4, 'Action|Comedy|Crime', 4, 23, '6/6/2017', 9.85),
        (11, 'American Yakuza', 4, 'Action|Drama|Thriller', 25, 14, '6/2/2003', 72.48),
        (12, 'Malice N Wonderland', 4, 'Drama|Musical', 33, 13, '6/6/2016', 37.69),
        (13, 'Good Year, A', 5, 'Comedy|Drama|Romance', 36, 24, '11/15/2007', null),
        (14, 'The Suspended Step of the Stork', 5, 'Drama|Romance', 45, 7, '12/12/2010', 145.36),
        (15, 'Nobody''s Children (I figli di nessuno),', 5, 'Drama|Romance', 29, 12, '3/9/2020', 24.72),
        (16, 'Injury to One, An', 6, 'Documentary', 6, 8, '11/16/2017', null),
        (17, 'Shoppen ', 6, 'Comedy|Romance', 27, 11, '4/3/2011', 18.94),
        (18, 'Young Americans, The', 7, 'Crime|Drama', 24, 18, '10/25/2010', 140.77),
        (19, 'Act of Aggression', 8, 'Crime|Drama', 50, 1, '8/25/2016', 93.06),
        (20, 'Alien Raiders', 8, 'Mystery|Sci-Fi|Thriller', 23, 2, '12/30/2010', 70.72),
        (21, 'Halloween: The Curse of Michael Myers (Halloween 6: The Curse of Michael Myers),', 8, 'Horror|Thriller', 19, 18, '7/14/2013', 43.21),
        (22, 'Ink', 8, 'Action|Fantasy|Sci-Fi', 40, 7, '2/29/2012', 23.95),
        (23, 'From Above', 8, 'Drama|Romance', 41, 14, '8/17/2022', 32.21),
        (24, '7th Floor', 9, 'Mystery|Thriller', 46, 16, '2/16/2004', null),
        (25, 'Forgiving Dr. Mengele', 9, 'Documentary', 35, 23, '10/28/2020', null),
        (26, 'Raincoat', 'Lynne Melladew', 'Drama|Romance', 42, 15, '11/12/2000', 95.81),
        (27, 'The Returned', 10, 'Drama|Horror|Thriller', 30, 23, '7/7/2018', 8.83),
        (28, 'Superman/Batman: Apocalypse', 10, 'Animation', 50, 20, '10/26/2003', 108.37),
        (29, 'Tomorrow at Dawn (Demain dès l''aube),', 10, 'Drama', 24, 17, '6/18/2015', 130.43),
        (30, 'Hard Times', 10, 'Action|Drama', 37, 25, '1/1/2019', 63.78);
    """
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    return cur.lastrowid


def insert_to_checkout(conn):

    sql = """
         insert into checkout (id, book_id, patron_id, checkout_date, return_date) values
         (1, 16, 14, '1/29/2023', '2/19/2023'),
         (2, 30, 4, '5/16/2023', '11/8/2023'),
         (3, 19, 13, '3/23/2023', '4/11/2023'),
         (4, 6, 7, '2/2/2023', '3/6/2023'),
         (5, 21, 7, '3/3/2023', '4/29/2023'),
         (6, 7, 9, '3/10/2022', '4/19/2023'),
         (7, 20, 4, '8/26/2023', '10/24/2023'),
         (8, 3, 4, '12/10/2022', '5/23/2023'),
         (9, 8, 1, '10/5/2022', '10/5/2023'),
         (10, 24, 1, '6/24/2023', '9/5/2023'),
         (11, 27, 15, '2/15/2022', '10/22/2022'),
         (12, 7, 8, '6/6/2023', '9/15/2023'),
         (13, 10, 2, '11/10/2022', '8/27/2023'),
         (14, 23, 10, '3/30/2023', '8/14/2023'),
         (15, 14, 3, '10/28/2023', '12/1/2023');
    """
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    return cur.lastrowid


def insert_to_hold(conn):
    sql = """
         insert into hold (id, book_id, patron_id, hold_date) values
         (1, 6, 2, '2023-08-04 16:18:00'),
         (2, 10, 1, '2023-08-25 03:06:47'),
         (3, 7, 26, '2023-08-24 16:50:14'),
         (4, 5, 19, '2023-08-14 12:01:53'),
         (5, 2, 29, '2023-09-05 10:09:41'),
         (6, 15, 25, '2023-08-17 02:25:43'),
         (7, 5, 11, '2023-09-08 18:53:24'),
         (8, 2, 24, '2023-09-19 15:14:21'),
         (9, 18, 17, '2023-09-27 10:13:16'),
         (10, 10, 25, '2023-08-24 18:55:51'),
         (11, 13, 14, '2023-09-02 15:50:23'),
         (12, 25, 22, '2023-08-25 04:07:40'),
         (13, 26, 18, '2023-09-13 15:06:15'),
         (14, 16, 15, '2023-08-27 18:50:01'),
         (15, 26, 21, '2023-08-31 04:12:34'),
         (16, 24, 19, '2023-08-30 22:51:55'),
         (17, 14, 16, '2023-09-21 23:33:46'),
         (18, 5, 23, '2023-09-22 00:37:00'),
         (19, 12, 12, '2023-09-17 04:28:59'),
         (20, 30, 21, '2023-08-31 21:46:29');
    """
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    return cur.lastrowid

def insert_to_patrons(conn):

    sql = """
        insert into patron (id, first_name, last_name, email, gender, address) values
        (1, 'Mischa', 'Trice', 'mtrice0@sun.com', 'Male', '42 Stone Corner Circle'),
        (2, 'Britt', 'Norquoy', 'bnorquoy1@earthlink.net', 'Female', '2 Westerfield Road'),
        (3, 'Junette', 'Kusick', 'jkusick2@geocities.com', 'Female', '71 Ohio Parkway'),
        (4, 'Doralynne', 'Ginglell', 'dginglell3@fema.gov', 'Female', '3087 Killdeer Drive'),
        (5, 'Maddy', 'Parmenter', 'mparmenter4@creativecommons.org', 'Female', '7 Jay Center'),
        (6, 'Blakeley', 'Bibey', 'bbibey5@mlb.com', 'Female', '12157 Westerfield Avenue'),
        (7, 'Graeme', 'Haldenby', 'ghaldenby6@auda.org.au', 'Genderfluid', '36 Fuller Drive'),
        (8, 'Humberto', 'Pescud', 'hpescud7@creativecommons.org', 'Male', '8 Doe Crossing Avenue'),
        (9, 'Cassi', 'Pirdue', 'cpirdue8@123-reg.co.uk', 'Female', '2 Vera Street'),
        (10, 'Aleece', 'Mainston', 'amainston9@geocities.com', 'Non-binary', '25095 Manufacturers Lane'),
        (11, 'Maison', 'Risson', 'mrissona@cdbaby.com', 'Male', '960 Elka Place'),
        (12, 'Esme', 'Lamberti', 'elambertib@hubpages.com', 'Male', '32 Blackbird Avenue'),
        (13, 'Celisse', 'Veart', 'cveartc@prlog.org', 'Female', '2 Dexter Way'),
        (14, 'Monti', 'Shalcros', 'mshalcrosd@cargocollective.com', 'Polygender', '55429 Maywood Hill'),
        (15, 'Hally', 'Le Franc', 'hlefrance@berkeley.edu', 'Female', '07542 John Wall Court'),
        (16, 'Wye', 'Newall', 'wnewallf@chicagotribune.com', 'Male', '575 Hanson Drive'),
        (17, 'Oswell', 'Negri', 'onegrig@usa.gov', 'Male', '505 Starling Place'),
        (18, 'Murial', 'Connock', 'mconnockh@irs.gov', 'Female', '462 Sunnyside Plaza'),
        (19, 'Chas', 'Osboldstone', 'cosboldstonei@bigcartel.com', 'Male', '2 Buell Lane'),
        (20, 'Carce', 'De la Yglesia', 'cdelayglesiaj@cnet.com', 'Male', '80301 Ryan Alley'),
        (21, 'Harwilll', 'Neles', 'hnelesk@washington.edu', 'Bigender', '21 Maple Wood Circle'),
        (22, 'Hercule', 'Dainty', 'hdaintyl@homestead.com', 'Male', '84626 Fairfield Point'),
        (23, 'Ida', 'Yellowlees', 'iyellowleesm@cocolog-nifty.com', 'Female', '7 Shelley Avenue'),
        (24, 'Gavan', 'Argyle', 'gargylen@trellian.com', 'Polygender', '1 Hayes Plaza'),
        (25, 'Renie', 'Adamolli', 'radamollio@umn.edu', 'Genderfluid', '9 Oriole Circle'),
        (26, 'Othelia', 'Rolley', 'orolleyp@google.com.au', 'Female', '24 Schmedeman Road'),
        (27, 'Moss', 'Krishtopaittis', 'mkrishtopaittisq@google.cn', 'Male', '0 Springview Pass'),
        (28, 'Keelia', 'Scollan', 'kscollanr@cafepress.com', 'Female', '8321 Harbort Pass'),
        (29, 'Elenore', 'Bysshe', 'ebysshes@vk.com', 'Female', '688 Tomscot Lane'),
        (30, 'Anett', 'Cranney', 'acranneyt@cpanel.net', 'Female', '47 Packers Way'),
    """
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    return cur.lastrowid


def main():
    database = "./pythonsqlite.db"

    # create a database connection
    conn = create_connection(database)
    create_table(conn, sql_create_author_table)
    insert_to_author(conn)
    create_table(conn, sql_create_book_table)
    insert_to_book(conn)
    create_table(conn, sql_create_checkout_table)
    insert_to_checkout(conn)
    create_table(conn, sql_create_hold_table)
    insert_to_hold(conn)
    create_table(conn, sql_create_patron_table)
    insert_to_patrons(conn)

    print("Database build successful!")


if __name__ == "__main__":
    main(),


