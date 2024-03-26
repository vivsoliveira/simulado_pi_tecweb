import sqlite3
from database import Database, Note
import json
import database
def extract_route(req):
    return req.split(' ')[1][1:] 

def read_file(path):
    with open(path, 'rb') as file:  
        content = file.read()
    return content

def load_data():
    db = Database("notes")  
    notes = db.get_all()
    return notes 

def load_template(file):
    with open(f"templates/{file}", 'r', encoding='utf-8') as file:
        texto = file.read()
    return texto

def add_note(note_data):
    db = Database('notes') 
    note = Note(title=(note_data['titulo']).replace('+', ' '), content=(note_data['detalhes']).replace('+', ' '))
    db.add(note)
    return note
    
def build_response(body='', code=200, reason='OK', headers=''):
    if headers:
        return f'HTTP/1.1 {code} {reason}\n{headers}\n\n{body}'.encode()
    return f'HTTP/1.1 {code} {reason}{headers}\n\n{body}'.encode()

def delete_note(note_id):
    db = Database('notes') 
    db.delete(note_id)

def conta_notas():
    db = Database('notes') 
    return len(db.get_all())