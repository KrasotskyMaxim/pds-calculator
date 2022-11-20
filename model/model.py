from os import curdir
import sqlite3


class Model:
    WATER_USE_TYPES = [
        "A", "B", "C", "D"
    ]
    POLLUTANT_GROUPS = [
        "A", "B", "C", "D"
    ]
    POLLUTANT_DANGER_CLASSES = [
        "easy",
        "normal",
        "hard",
        "insane"
    ]
    
    def __init__(self) -> None:
        self.connect_db()
        
    def connect_db(self):
        print("connect to db...")
        try:
            self.conn = sqlite3.connect('model/pbz-2.db')
            self.cur = self.conn.cursor()
        except:
            print("connection error!")
        print("connection success!")
    
    # COMPANY
    def get_company_name(self):
        self.cur.execute("""SELECT name FROM Company""")
        return self.cur.fetchall()
    
    def get_company_id(self, name):
        self.cur.execute(f"""SELECT id FROM Company
                            WHERE name = '{name}'""")
        return self.cur.fetchone()
    
    def get_company_detail(self, name):
        self.cur.execute(f"""SELECT name, water_use_type 
                         FROM Company
                         WHERE name = '{name}'""")
        return self.cur.fetchone()
    
    def add_company(self, context):
        name = context["name"]
        self.cur.execute(f"""INSERT INTO Company
                            (name, water_use_type)
                            VALUES
                            ('{name}', '{context["water_use_type"]}')""")
        self.conn.commit()
        return name 
    
    def update_company(self, context):
        new_name = context["name"]
        self.cur.execute(f"""UPDATE Company
                            SET name = '{new_name}',
	                            water_use_type = '{context["water_use_type"]}'
                            WHERE name = '{context["old_name"]}'""")
        self.conn.commit()
        return new_name 
    
    def delete_company(self, name):
        self.cur.execute(f"""DELETE FROM Company
                            WHERE name = '{name}'""")
        self.conn.commit()
        return True 
    
    # CANALIZATION    
    def get_canalization_name(self):
        self.cur.execute("""SELECT name FROM Canalization""")
        return self.cur.fetchall()
    
    def get_canalization_id(self, name):
        self.cur.execute(f"""SELECT id FROM Canalization
                            WHERE name = '{name}'""")
        return self.cur.fetchone()
    
    def get_control_gate_name(self):
        self.cur.execute("""SELECT name FROM ControlGate""")
        return self.cur.fetchall()
    
    def get_control_gate_id(self, name):
        self.cur.execute(f"""SELECT id FROM ControlGate
                            WHERE name = '{name}'""")
        return self.cur.fetchone()
        
    def get_canalization_detail(self, name):
        self.cur.execute(f"""SELECT Canalization.name, Company.name, ControlGate.name, height, 
                            shore_distance, control_gate_distance, water_waste, angle, min_water_speed, hole_diameter
                            FROM Canalization JOIN Company ON Canalization.company_id = Company.id
					        JOIN ControlGate ON Canalization.control_gate_id = ControlGate.id 
                            WHERE Canalization.name = '{name}'""")
        return self.cur.fetchone()
    
    def add_canalization(self, context):
        name = context["name"]
        company_id = self.get_company_id(name=context["company"])[0]
        control_gate_id = self.get_control_gate_id(name=context["control_gate"])[0]
        self.cur.execute(f"""INSERT INTO Canalization
                            (name, company_id, control_gate_id, height, shore_distance, control_gate_distance, water_waste,
                                angle, min_water_speed, hole_diameter)
                            VALUES
                            ('{name}', {company_id}, {control_gate_id}, {context["height"]}, {context["shore_distance"]}, 
                                {context["control_gate_distance"]}, {context["water_waste"]}, {context["angle"]},
                                {context["min_water_speed"]}, {context["hole_diameter"]})""")
        self.conn.commit()
        return name 
    
    def update_canalization(self, context):
        new_name = context["name"]
        company_id = self.get_company_id(name=context["company"])[0]
        control_gate_id = self.get_control_gate_id(name=context["control_gate"])[0]
        self.cur.execute(f"""UPDATE Canalization
                            SET name = '{new_name}', 
                                company_id = {company_id}, 
                                control_gate_id = {control_gate_id}, 
                                height = {context["height"]}, 
                                shore_distance = {context["shore_distance"]}, 
                                control_gate_distance = {context["control_gate_distance"]}, 
                                water_waste = {context["water_waste"]}, 
                                angle = {context["angle"]},
                                min_water_speed = {context["min_water_speed"]}, 
                                hole_diameter = {context["hole_diameter"]}
                            WHERE name = '{context["old_name"]}'""")
        self.conn.commit()
        return new_name
    
    def delete_canalization(self, name):
        self.cur.execute(f"""DELETE FROM Canalization
                            WHERE name = '{name}'""")
        self.conn.commit()
        return True 
    
    # POLLUTANTS
    def add_pollutant(self, context):
        name = context["name"]
        canalization_id = self.get_canalization_id(name=context["canalization"])[0]
        self.cur.execute(f"""INSERT INTO Pollutant
                            (name, canalization_id, 'group', danger_class, knk, lfv, pds)
                            VALUES
                            ('{name}', {canalization_id}, '{context["group"]}', '{context["danger_class"]}',
                            {context["knk"]}, {context["lfv"]}, {context["pds"]})""")
        self.conn.commit()
        return name 
    
    def add_date(self, context):
        date = context["date"]
        pollutant_id = self.get_pollutant_id(name=context["pollutant"])[0]
        self.cur.execute(f"""INSERT INTO Dates
                         (date, pollutant_id, control_gate_bc, canalization_bc, pdk)
                         VALUES
                         ('{date}', {pollutant_id}, {context["control_gate_bc"]},
                         {context["canalization_bc"]}, {context["pdk"]})""")
        self.conn.commit()
        return date
                                
    def get_task_three_data(self):
        self.cur.execute("""SELECT Canalization.name, date, Pollutant.name, canalization_bc
                            FROM Canalization JOIN Pollutant ON Canalization.id = Pollutant.canalization_id
					        JOIN Dates ON Pollutant.id = Dates.pollutant_id
                            ORDER BY Canalization.id""")
        return self.cur.fetchall()
    
    def get_task_four_data(self):
        self.cur.execute("""SELECT ControlGate.name, Canalization.name, date, Pollutant.name, 
                            control_gate_bc, pdk, knk
                            FROM Canalization JOIN Pollutant ON Canalization.id = Pollutant.canalization_id
					            JOIN Dates ON Pollutant.id = Dates.pollutant_id
					            JOIN ControlGate ON ControlGate.id = Canalization.control_gate_id
                            ORDER BY ControlGate.id""")
        return self.cur.fetchall()
    
    def get_task_five_data(self, company, date):
        self.cur.execute(f"""SELECT Pollutant.name as pollutant_name, control_gate_bc, canalization_bc, pdk, pds
                            FROM Pollutant JOIN Dates ON Pollutant.id = Dates.pollutant_id
                            WHERE date = '{date}' AND pollutant_name IN (
	                            SELECT name FROM Pollutant
                                WHERE canalization_id IN (
                                    SELECT id FROM Canalization
                                    WHERE company_id = (
                                        SELECT id FROM Company
                                        WHERE name = '{company}')
                                        )
                                    )""")
        return self.cur.fetchall()
    
    def get_dates(self):
        self.cur.execute("""SELECT DISTINCT date FROM Dates
                            ORDER BY date""")
        return self.cur.fetchall()
    
    def get_pollutant_name(self):
        self.cur.execute("""SELECT name FROM Pollutant
                            ORDER BY name""")
        return self.cur.fetchall()
        
    def get_pollutant_id(self, name):
        self.cur.execute(f"""SELECT id FROM Pollutant
                            WHERE name = '{name}'""")
        return self.cur.fetchone()

if __name__ == "__main__":
    m = Model()
    print(m.get_pollutant_name())