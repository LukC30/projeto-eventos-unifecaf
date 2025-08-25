import sqlite3
import os

DB_FOLDER = os.path.dirname(__file__)
DB_PATH =  os.path.join(DB_FOLDER,  'unifecaf_eventos.db')

def create_database():
    """
    função criada para gerar o banco de dados
    """

    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()


        # --- Tabela de Eventos ---
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS tbl_evento (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                data TEXT NOT NULL,
                descricao TEXT,
                max_participantes INTEGER NOT NULL,
                FOREIGN KEY (id_usuario) REFERENCES tbl_usuario (id) ON DELETE CASCADE,
            )
        """)

        # --- Tabela de Usuários ---
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS tbl_usuario (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                tipo TEXT NOT NULL CHECK(tipo IN ('aluno', 'coordenador'))
            )
        ''')

        # --- Tabela de Inscrições ---
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS tbl_inscricoes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                id_evento INTEGER NOT NULL,
                id_usuario INTEGER NOT NULL,
                FOREIGN KEY (id_evento) REFERENCES tbl_evento (id) ON DELETE CASCADE,
                FOREIGN KEY (id_usuario) REFERENCES tbl_usuario (id) ON DELETE CASCADE,
                (id_evento, id_usuario) UNIQUE
            )
        ''')
        conn.commit()
        print(f"banco e tabelas criados com sucesso em: {DB_PATH}")

    except sqlite3.Error as e:
        print(f"Ocorreu um erro na criação do banco de dados")
        conn.rollback()
    finally:
        if conn:
            conn.close()

if __name__ == '__main__':
    if os.path.exists(DB_PATH):
        os.remove(DB_PATH)
        print("Antigo banco de dados removido")

    create_database()
