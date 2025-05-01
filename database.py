import sqlite3

def init_db():
    conn = sqlite3.connect('loja.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            preco REAL NOT NULL
        )
    ''')
    
    # Alguns produtos para teste
    produtos = [
        ('Notebook Gamer', 4500.00),
        ('Teclado Mecânico', 250.00),
        ('Mouse Gamer', 150.00),
        ('Monitor 27 Polegadas', 1200.00),
        ('Headset', 300.00)
    ]
    cursor.executemany('INSERT INTO produtos (nome, preco) VALUES (?, ?)', produtos)
    
    conn.commit()
    conn.close()

if __name__ == '__main__':
    init_db()
