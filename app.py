import sqlite3 
from database.setup import create_tables
from database.connection import get_db_connection
from models.article import Article
from models.author import Author
from models.magazine import Magazine

def main():
    
    create_tables()

    
    
    author_name = input("Enter author's name: ")
    magazine_name = input("Enter magazine name: ")
    magazine_category = input("Enter magazine category: ")
    article_title = input("Enter article title: ")
    article_content = input("Enter article content: ")

    
    conn = get_db_connection()
    conn.row_factory = sqlite3.Row  
    cursor = conn.cursor()

   
    cursor.execute('INSERT INTO authors (name) VALUES (?)', (author_name,))
    author_id = cursor.lastrowid
    author = Author(author_id, author_name) 
    
    cursor.execute('INSERT INTO magazines (name, category) VALUES (?, ?)', (magazine_name, magazine_category))
    magazine_id = cursor.lastrowid
    magazine = Magazine(magazine_id, magazine_name, magazine_category)

    
    cursor.execute(
        'INSERT INTO articles (title, content, author_id, magazine_id) VALUES (?, ?, ?, ?)',
        (article_title, article_content, author_id, magazine_id)
    )
    article_id = cursor.lastrowid
    article = Article(article_id, article_title, article_content, author_id, magazine_id)

    conn.commit()

   
    cursor.execute('SELECT * FROM magazines')
    magazines = cursor.fetchall()
    print("\nMagazines:")
    for mag in magazines:
        print(Magazine(mag["id"], mag["name"], mag["category"]))

    cursor.execute('SELECT * FROM authors')
    authors = cursor.fetchall()
    print("\nAuthors:")
    for auth in authors:
        print(Author(auth["id"], auth["name"]))

    cursor.execute('SELECT * FROM articles')
    articles = cursor.fetchall()
    print("\nArticles:")
    for art in articles:
        print(Article(art["id"], art["title"], art["content"], art["author_id"], art["magazine_id"]))

    conn.close()

if __name__ == "__main__":
    main()

