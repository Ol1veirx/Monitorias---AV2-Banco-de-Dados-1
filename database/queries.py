from db_config import get_connection

def list_monitorias_com_info():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute('''
    SELECT
        m.id,
        a.nome AS aluno,
        d.nome AS disciplina,
        p.nome AS professor,
        m.dia,
        m.horario,
        m.qtd_horas
    FROM monitorias m
    JOIN alunos a ON m.aluno_id = a.id
    JOIN disciplinas d ON m.disciplina_id = d.id
    JOIN professores p ON d.professor_id = p.id
    ''')

    resultados = cursor.fetchall()
    conn.close()
    return resultados

def horas_por_disciplina():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute('''
    SELECT
        d.nome AS disciplina,
        SUM(m.qtd_horas) AS total_horas
    FROM monitorias m
    JOIN disciplinas d ON m.disciplina_id = d.id
    GROUP BY d.nome
    ''')

    resultados = cursor.fetchall()
    conn.close()
    return resultados

def media_horas_por_aluno():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute('''
    SELECT
        a.nome AS aluno,
        AVG(m.qtd_horas) AS media_horas
    FROM monitorias m
    JOIN alunos a ON m.aluno_id = a.id
    GROUP BY a.nome
    ''')

    resultados = cursor.fetchall()
    conn.close()
    return resultados

def quantidade_monitorias():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute('''
    SELECT COUNT(*) AS qtd_monitorias
    FROM monitorias
    ''')

    resultados = cursor.fetchall()
    conn.close()
    return resultados

def maior_hora():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute('''
    SELECT MAX(qtd_horas) AS maior_horario
    FROM monitorias
    ''')

    resultados = cursor.fetchall()
    cursor = conn.close()
    return resultados

def menor_hora():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute('''
    SELECT MIN(qtd_horas) AS menor_hora
    FROM monitorias
    ''')

    resultados = cursor.fetchall()
    conn.close()
    return resultados