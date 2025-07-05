import os
import sqlite3

def criar_banco():
    pasta_db = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'db'))
    if not os.path.exists(pasta_db):
        os.makedirs(pasta_db)
    caminho_db = os.path.join(pasta_db, 'torneio.db')

    conn = sqlite3.connect(caminho_db)
    cursor = conn.cursor()

    # criação das tabelas...


    cursor.execute('''
    CREATE TABLE IF NOT EXISTS jogador (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        idade INTEGER,
        nickname TEXT UNIQUE
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS time (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL UNIQUE
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS jogador_time (
        jogador_id INTEGER,
        time_id INTEGER,
        FOREIGN KEY (jogador_id) REFERENCES jogador(id),
        FOREIGN KEY (time_id) REFERENCES time(id)
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS jogo (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        categoria TEXT
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS partida (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        time1_id INTEGER,
        time2_id INTEGER,
        jogo_id INTEGER,
        data TEXT,
        vencedor_id INTEGER,
        FOREIGN KEY (time1_id) REFERENCES time(id),
        FOREIGN KEY (time2_id) REFERENCES time(id),
        FOREIGN KEY (jogo_id) REFERENCES jogo(id),
        FOREIGN KEY (vencedor_id) REFERENCES time(id)
    )
    ''')

    conn.commit()
    conn.close()
    print("Banco criado com sucesso!")

if __name__ == '__main__':
    criar_banco()
