from database.schema import create_tables
from database.insert import (
        insert_aluno,
        insert_disciplina,
        insert_monitoria,
        insert_professor
    )
from database.queries import (
    horas_por_disciplina,
    list_monitorias_com_info,
    media_horas_por_aluno,
    quantidade_monitorias,
    menor_hora,
    maior_hora
)

from database.update_delete import (
    atualizar_monitoria,
    excluir_monitoria
)

def main():
    #create_tables()
    #print('Banco e tabelas criadas com sucesso.')

    # OBS: Os codigos estão comentados, pois os dados já foram inseridos no banco
    #insert_professor("Profª Mariane")
    #insert_professor("Prof Vilker")
    #insert_professor("Prof Gabriel")

    #insert_aluno("Liedson", "Sistemas de Informação")
    #insert_aluno("Ferreira", "Engenharia de Computação")
    #insert_aluno("Maria", "Ciências da Computação")

    #insert_disciplina("Banco de Dados", 1)
    #insert_disciplina("Redes de Computadores", 2)
    #insert_disciplina("Inteligência Artificial", 3)

    #insert_monitoria(1, 1, "Segunda-Feira", "14:30", 2)
    #insert_monitoria(2, 3, "Terça-Feira", "15:00", 3)
    #insert_monitoria(3, 2, "Sexta-Feira", "09:00", 2)
    #print('Dados inseridos com sucesso!')

    print("Listar monitorias com informação:")
    for linha in list_monitorias_com_info():
        print(linha)

    print("Horas por disciplina:")
    for linha in horas_por_disciplina():
        print(linha)

    print("Médias de horas por aluno:")
    for linha in media_horas_por_aluno():
        print(linha)

    print("Quantidade de monitorias:")
    for linha in quantidade_monitorias():
        print(linha)

    print("Menor horário da monitoria: ")
    for linha in menor_hora():
        print(linha)

    print("Maior horário da monitoria: ")
    for linha in maior_hora():
        print(linha)

    atualizar_monitoria(1,novas_horas=1)
    #atualizar_monitoria(2, dia="Quarta-Feira")

    # Aqui inserimos apenas para testar o delete
    #insert_monitoria(2, 3, "Domingo", "14:00", 5)

    #excluir_monitoria(4)


if __name__ == '__main__':
    main()