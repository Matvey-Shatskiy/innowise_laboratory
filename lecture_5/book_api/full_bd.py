import sqlite3

db_path = "books.db"

books = [
    ("Hard to Be a God", "Arkady and Boris Strugatsky", 1964),
    ("The Master and Margarita", "Mikhail Bulgakov", 1967),
    ("Crime and Punishment", "Fyodor Dostoevsky", 1866),
    ("War and Peace", "Leo Tolstoy", 1869),
    ("Roadside Picnic", "Arkady and Boris Strugatsky", 1972),
    ("The Idiot", "Fyodor Dostoevsky", 1869),
    ("A Hero of Our Time", "Mikhail Lermontov", 1840),
    ("The White Guard", "Mikhail Bulgakov", 1925),
    ("Dead Souls", "Nikolai Gogol", 1842),
    ("Fathers and Sons", "Ivan Turgenev", 1862),
    ("Heart of a Dog", "Mikhail Bulgakov", 1925),
    ("The Captain's Daughter", "Alexander Pushkin", 1836),
    ("Inhabited Island", "Arkady and Boris Strugatsky", 1969),
    ("The Snail on the Slope", "Arkady and Boris Strugatsky", 1968),
    ("Netochka Nezvanova", "Fyodor Dostoevsky", 1849),
    ("Life and Fate", "Vasily Grossman", 1980),
    ("Doctor Zhivago", "Boris Pasternak", 1957),
    ("We", "Yevgeny Zamyatin", 1920),
    ("Chevengur", "Andrei Platonov", 1928),
    ("The Trial", "Franz Kafka", 1925)
]

conn = sqlite3.connect(db_path)
cur = conn.cursor()

cur.executemany(
    "INSERT INTO books (title, author, year) VALUES (?, ?, ?)",
    books
)

conn.commit()
conn.close()

print("Database successfully filled with 20 English book records!")
