import os
import sqlite3

def conectar():
    caminho_db = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'db', 'torneio.db'))
    print(f"Tentando conectar ao banco: {caminho_db}")
    return sqlite3.connect(caminho_db)

# --- Jogadores ---

def adicionar_jogador(nome, idade, nickname):
    conn = None
    try:
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO jogador (nome, idade, nickname) VALUES (?, ?, ?)", (nome, idade, nickname))
        conn.commit()
        print(f"Jogador '{nickname}' adicionado com sucesso!")
    except sqlite3.IntegrityError:
        print("Erro: Nickname já existe.")
    except Exception as e:
        print(f"Erro inesperado: {e}")
    finally:
        if conn:
            conn.close()


def listar_jogadores():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT id, nome, idade, nickname FROM jogador")
    jogadores = cursor.fetchall()
    conn.close()
    return jogadores

# --- Times ---

def adicionar_time(nome):
    try:
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO time (nome) VALUES (?)", (nome,))
        conn.commit()
        print(f"Time '{nome}' adicionado com sucesso!")
    except sqlite3.IntegrityError:
        print("Erro: Nome do time já existe.")
    finally:
        conn.close()

def listar_times():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT id, nome FROM time")
    times = cursor.fetchall()
    conn.close()
    return times

def vincular_jogador_time(jogador_id, time_id):
    try:
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO jogador_time (jogador_id, time_id) VALUES (?, ?)", (jogador_id, time_id))
        conn.commit()
        print(f"Jogador {jogador_id} vinculado ao time {time_id} com sucesso!")
    except sqlite3.IntegrityError:
        print("Erro ao vincular jogador ao time (talvez vínculo já exista).")
    finally:
        conn.close()

def listar_jogadores_do_time(time_id):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT jogador.id, jogador.nome, jogador.nickname FROM jogador
        JOIN jogador_time ON jogador.id = jogador_time.jogador_id
        WHERE jogador_time.time_id = ?
    """, (time_id,))
    jogadores = cursor.fetchall()
    conn.close()
    return jogadores

# --- Jogos ---

def adicionar_jogo(nome, categoria):
    try:
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO jogo (nome, categoria) VALUES (?, ?)", (nome, categoria))
        conn.commit()
        print(f"Jogo '{nome}' adicionado com sucesso!")
    except sqlite3.IntegrityError:
        print("Erro: Jogo já existe.")
    finally:
        conn.close()

def listar_jogos():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT id, nome, categoria FROM jogo")
    jogos = cursor.fetchall()
    conn.close()
    return jogos

# --- Partidas ---

def adicionar_partida(time1_id, time2_id, jogo_id, data, vencedor_id):
    try:
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO partida (time1_id, time2_id, jogo_id, data, vencedor_id)
            VALUES (?, ?, ?, ?, ?)
        """, (time1_id, time2_id, jogo_id, data, vencedor_id))
        conn.commit()
        print("Partida registrada com sucesso!")
    except sqlite3.IntegrityError:
        print("Erro ao registrar partida.")
    finally:
        conn.close()

def listar_partidas():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT p.id, t1.nome, t2.nome, j.nome, p.data, t3.nome
        FROM partida p
        JOIN time t1 ON p.time1_id = t1.id
        JOIN time t2 ON p.time2_id = t2.id
        JOIN jogo j ON p.jogo_id = j.id
        LEFT JOIN time t3 ON p.vencedor_id = t3.id
    """)
    partidas = cursor.fetchall()
    conn.close()
    return partidas
