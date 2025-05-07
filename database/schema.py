from db_config import get_connection

def create_tables():
    conn = get_connection()
    cursor = conn.cursor()

    # Tabela alunos
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS alunos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        curso TEXT NOT NULL
    )
    ''')

    # Tabela professores
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS professores (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL
    )
    ''')

    # Tabela disciplinas
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS disciplinas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        professor_id INTEGER,
        FOREIGN KEY(professor_id) REFERENCES professores(id)
    )
    ''')

    # Tabela monitoria
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS monitorias (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        aluno_id INTEGER,
        disciplina_id INTEGER,
        dia TEXT,
        horario TEXT,
        qtd_horas INTEGER,
        FOREIGN KEY(aluno_id) REFERENCES alunos(id),
        FOREIGN KEY(disciplina_id) REFERENCES disciplinas(id)
    )
    ''')

    conn.commit()
    conn.close()