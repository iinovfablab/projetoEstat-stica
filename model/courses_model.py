from connections.connection_db import ConnectionDB
from scripts.read_file import jsonify




class CoursesModel(ConnectionDB):

    
    def courses_name(self):
        self.params_db(jsonify())
        conn = self.connection_db()
        query = """select g.id, g.name from public.groups g
                    where g.id != 5
                    """

        cursor = conn.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        conn.close()
        return result