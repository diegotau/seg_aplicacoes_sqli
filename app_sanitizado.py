from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('page.html')

@app.route('/search', methods=['POST'])
def search():
    query_text = request.form['query']
    
    conn = sqlite3.connect('loja.db')
    cursor = conn.cursor()
    
    # CORRETO: Parametrização segura
    query = "SELECT * FROM produtos WHERE nome LIKE ?"
    cursor.execute(query, (f'%{query_text}%',))
    produtos = cursor.fetchall()
    conn.close()
    
    if produtos:
        return render_template('page.html', produtos=produtos)
    else:
        return render_template('page.html', message="Nenhum produto encontrado.")

if __name__ == '__main__':
    app.run(debug=True)
