from Util.DBconn import DBConnection
class DirectorService(DBConnection):
 
    def read_directors(self):
        try:
            self.cursor.execute("Select * from Directors")
            directors = self.cursor.fetchall()  # Get all data
            for director in directors:
                print(director)
        except Exception as e:
            print(e)