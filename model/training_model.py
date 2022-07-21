from connections.connection_db import ConnectionDB
from scripts.read_file import jsonify


class TrainingModel(ConnectionDB):

    
    def __init__(self):
        super().__init__()
        self.params_db(jsonify())
        self.__conn = self.connection_db()

    def find_all(self, date_to, date_at):
        query = """select count(u.id), g."name"  from public.users u
                        inner join public.statistic_profiles sp on
                        u.id = sp.user_id
                        inner join public.statistic_profile_trainings spt on
                        sp.id = spt.statistic_profile_id
                        inner join public.trainings t on
                        t.id = spt.training_id 
                        inner join public."groups" g on
                        sp.group_id = g.id and g.id != 5
                        where spt.created_at >= %s and spt.created_at < %s
                        group by g."name"
                    """

        cursor = self.__conn.cursor()
        cursor.execute(query,(date_to, date_at,))
        result = cursor.fetchall()
        return result
    
    def find_by_training(self, date_to, date_at, machine):
        query = """select count(u.id), g."name"  from public.users u
                        inner join public.statistic_profiles sp on
                        u.id = sp.user_id
                        inner join public.statistic_profile_trainings spt on
                        sp.id = spt.statistic_profile_id and spt.training_id = %s
                        inner join public.trainings t on
                        t.id = spt.training_id 
                        inner join public."groups" g on
                        sp.group_id = g.id 
                        where spt.updated_at >= %s and spt.updated_at < %s
                        group by g."name"
                    """

        cursor = self.__conn.cursor()
        cursor.execute(query,(machine, date_to, date_at,))
        result = cursor.fetchall()
        return result

    def find_by_course(self, date_to, date_at, course):
        query = """select count(u.id), g."name"  from public.users u
                        inner join public.statistic_profiles sp on
                        u.id = sp.user_id
                        inner join public.statistic_profile_trainings spt on
                        sp.id = spt.statistic_profile_id
                        inner join public.trainings t on
                        t.id = spt.training_id 
                        inner join public."groups" g on
                        sp.group_id = g.id and g.id = %s
                        where spt.updated_at >= %s and spt.updated_at < %s
                        group by g."name"
                    """

        cursor = self.__conn.cursor()
        cursor.execute(query,(course, date_to, date_at,))
        result = cursor.fetchall()
        return result
    
    def all_courses(self):
        query = """select t.id, t.name from public.trainings t"""

        cursor = self.__conn.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        return result

    def _clsose(self):
        self.__conn.close()