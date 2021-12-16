import sqlite3
from sqlite3.dbapi2 import Cursor, Error

class NotesDbContext:
    def __init__(self, con_str: str) -> None:
        self.__connection = sqlite3.connect(con_str)
        self._cursor = self.__connection.cursor()

    def init_db_with_notes(self):
        self._cursor.execute(
            'CREATE TABLE notes (id integer PRIMARY KEY AUTOINCREMENT, note text)'
        )

    def __del__(self):
        self.close_connection()

    def get_notes(self):
        return list(self._cursor.execute(
            'SELECT * FROM notes'
        ))
    
    def post_note(self, text: str) -> None:
        self._cursor.execute('''INSERT INTO notes (note) VALUES (:text)''',
            {'text': text}
        )
        self._commit()

    def put_note(self, id: int, note: str) -> None:
        self._cursor.execute('UPDATE notes SET note=:note WHERE id = :id', 
            {'note': note, 'id': id}
        )
        self._commit()
    
    def delete_note(self, id: int) -> None:
        self._cursor.execute('DELETE FROM notes WHERE id = :id', 
            {'id': id}
        )
        self._commit()
    
    def delete_note_by_value(self, value: str) -> None:
        self._cursor.execute('DELETE FROM notes WHERE id = (SELECT id FROM notes WHERE note = :value LIMIT 1)', 
            {'value': value}
        )
        self._commit()

    def delete_all(self) -> None:
        self._cursor.execute('DELETE FROM notes')
        self._commit()

    def _commit(self):
        self.__connection.commit()

    def close_connection(self) -> None:
        self.__connection.close()