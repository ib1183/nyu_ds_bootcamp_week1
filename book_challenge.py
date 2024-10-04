books = [
    {
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "genre": "Fiction",
        "rating": 4.2
    },
    {
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "genre": "Classic",
        "rating": 4.5
    },
    {
        "title": "1984",
        "author": "George Orwell",
        "genre": "Dystopian",
        "rating": 4.8
    },
    {
        "title": "Pride and Prejudice",
        "author": "Jane Austen",
        "genre": "Romance",
        "rating": 4.7
    },
    {
        "title": "Harry Potter and the Sorcerer's Stone",
        "author": "J.K. Rowling",
        "genre": "Fantasy",
        "rating": 4.9
    },
    {
        "title": "The Catcher in the Rye",
        "author": "J.D. Salinger",
        "genre": "Coming-of-age",
        "rating": 4.1
    }
]
def check_rating(book):
    if book["rating"] > 4.5:
        return 'high'
    elif book["rating"] > 4.0:
        return 'medium'
    else:
        return 'low'
def average_rating_by_genre(books, genre):
    count = 0
    total_rating = 0
    for book in books:
        if book["genre"] == genre:
            count += 1
            total_rating += book["rating"]
    if count == 0:
        return genre + " does not exist!"
    else:
        average_rating = total_rating / count
        return average_rating

def books_by_author(books, author):
    bibliography = []
    for book in books:
        if book["author"] == author:
            bibliography.append(book["title"])
    if not bibliography:
        return author + " has no bibliography!"
    else:
        return bibliography

if __name__ == "__main__":
    for book in books:
        print( book["title"] + "'s rating is " + check_rating(book))

    genre_list = []
    for book in books:
        if book["genre"] not in genre_list:
            genre_list.append(book["genre"])
    for genre in genre_list:
        print(genre + "'s average rating is " + str(average_rating_by_genre(books, genre)))
    print(average_rating_by_genre(books, "Sci-fi"))

    author_list = []
    for book in books:
        if book["author"] not in author_list:
            author_list.append(book["author"])
    for author in author_list:
        print(author + " has written " + " ".join(books_by_author(books, author)))
    print(books_by_author(books, "Sally Rooney"))

