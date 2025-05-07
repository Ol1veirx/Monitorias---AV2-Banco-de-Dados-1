from db_config import get_connection

def atualizar_monitoria(monitoria_id, dia=None, novas_horas=None):
    conn = get_connection()
    cursor = conn.cursor()

    if dia:
        cursor.execute("UPDATE monitorias SET dia = ? WHERE id = ?", (dia, monitoria_id))
    if novas_horas is not None:
        cursor.execute("UPDATE monitorias SET qtd_horas = ? WHERE id = ?", (novas_horas, monitoria_id))

    conn.commit()
    conn.close()

def excluir_monitoria(monitoria_id):
    conn = get_connection()
    cursor = conn.cursor()

    if monitoria_id != None:
        cursor.execute("DELETE FROM monitorias WHERE id = ?", (monitoria_id,))
        conn.commit()
        conn.close()
    else:
        print("Você não forneceu o id da monitoria.")
