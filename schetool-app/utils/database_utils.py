import sqlite3
from typing import Any, List, Tuple, Optional



class Database:
    def __init__(self, db_name: str):
        """Inicializa la clase con el nombre de la base de datos."""
        self.db_name = db_name

    def execute_query(self, query: str, params: Optional[Tuple[Any, ...]] = ()) -> None:
        """Ejecuta una consulta (INSERT, UPDATE, DELETE) y confirma los cambios."""
        try:
            with sqlite3.connect(self.db_name) as connection:
                cursor = connection.cursor()
                cursor.execute(query, params)
                connection.commit()
        except sqlite3.Error as e:
            """Añadir logs"""
            connection.rollback()
            raise

    def fetch_one(self, query: str, params: Optional[Tuple[Any, ...]] = ()) -> Optional[Tuple[Any, ...]]:
        """Ejecuta una consulta y devuelve un solo resultado."""
        try:
            with sqlite3.connect(self.db_name) as connection:
                cursor = connection.cursor()
                cursor.execute(query, params)
                return cursor.fetchone()
        except sqlite3.Error as e:
            """Añadir logs"""
            raise

    def fetch_all(self, query: str, params: Optional[Tuple[Any, ...]] = ()) -> List[Tuple[Any, ...]]:
        """Ejecuta una consulta y devuelve todos los resultados."""
        try:
            with sqlite3.connect(self.db_name) as connection:
                cursor = connection.cursor()
                cursor.execute(query, params)
                return cursor.fetchall()
        except sqlite3.Error as e:
            """Añadir logs"""
            raise

    def execute_transaction(self, queries: List[Tuple[str, Tuple[Any, ...]]]) -> None:
        with sqlite3.connect(self.db_name) as connection:
            try:
                cursor = connection.cursor()
                for query, params in queries:
                    cursor.execute(query, params)
                connection.commit()
            except sqlite3.Error as e:
                """Añadir logs"""
                connection.rollback()
                raise
