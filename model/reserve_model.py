from connections.connection_db import ConnectionDB
from scripts.read_file import jsonify


class ReserveModel(ConnectionDB):
    
    def __init__(self):
        super().__init__()
        self.params_db(jsonify())
        self.__conn = self.connection_db()

    
    def find_by_machine(self, machine_id):


        query = """select count(sp.id), g.name from public.statistic_profiles sp 
                        inner join public.reservations r on
                        r.statistic_profile_id = sp.id
                        inner join public.slots_reservations sr on
                        sr.reservation_id = r.id 
                        inner join public.slots s on
                        sr.slot_id = s.id
                        inner join public."groups" g on
                        g.id = sp.group_id
                        inner join public.machines m on
                        m.id = r.reservable_id 
                        where r.reservable_type ='Machine' and r.created_at > '2022-01-01 08:00:00' and m.id = %s
                        group by g.name"""
        
        cursor = self.__conn.cursor()
        cursor.execute(query,(machine_id,))
        result = cursor.fetchall()
        return result
    
    def all_machines(self):
        query = "select m.id, m.name from public.machines m"
        cursor = self.__conn.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        return result


    def _clsose(self):
        self.__conn.close()

