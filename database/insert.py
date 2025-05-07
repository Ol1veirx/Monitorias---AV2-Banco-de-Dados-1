from db_config import get_connection

def insert_aluno(nome, curso):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO alunos (nome, curso) VALUES (?, ?)", (nome, curso))
    conn.commit()
    conn.close()

def insert_professor(nome):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO professores (nome) VALUES (?)", (nome,))
    conn.commit()
    conn.close()

def insert_disciplina(nome, professor_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO disciplinas (nome, professor_id)VALUES (?, ?)", (nome, professor_id))
    conn.commit()
    conn.close()

def insert_monitoria(aluno_id, disciplina_id, dia, horario, qtd_horas):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO monitorias (aluno_id, disciplina_id, dia, horario, qtd_horas) VALUES (?,?,?,?,?)", (aluno_id, disciplina_id, dia, horario, qtd_horas))
    conn.commit()
    conn.close()