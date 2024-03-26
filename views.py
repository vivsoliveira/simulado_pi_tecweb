from urllib.parse import unquote_plus
from utils import load_data, load_template, add_note, build_response, conta_notas

def index(request, file='index.html'):
    # A string de request sempre começa com o tipo da requisição (ex: GET, POST)
    if request.startswith('POST'):
        request = request.replace('\r', '')  # Remove caracteres indesejados
        # Cabeçalho e corpo estão sempre separados por duas quebras de linha
        partes = request.split('\n\n')
        corpo = partes[1]
        params = {}
        for chave_valor in corpo.split('&'):
            chave, valor = chave_valor.split('=')
            unquote_plus(valor, encoding='utf-8', errors='replace')
            params[chave] = valor
        add_note(params)
        return build_response(code=303, reason='See Other', headers='Location: /')
    # Cria uma lista de <li>'s para cada anotação
    # Se tiver curiosidade: https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
    note_template = load_template('components/note.html')
    notes_li = [
        note_template.format(title=dados.title, details=dados.content, id=dados.id)
        for dados in load_data()
    ]
    notes = '\n'.join(notes_li)
    quantidade_notas = conta_notas()
    return build_response(body=load_template(file).format(notes=notes, quantidade=quantidade_notas))