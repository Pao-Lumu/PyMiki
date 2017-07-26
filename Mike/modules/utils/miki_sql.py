import sqlite3


class MikiSQL:
    def __init__(self, filename : str)
        self.db = sqlite3.connect(filename)
        self.cursor = db.cursor()






    def commit(self):
        self.db.commit()

    def close(self):
        self.db.commit()
        self.db.close()

    def close_no_save(self)
        self.db.close()





class AccountSQL(MikiSQL):

    def __init__(self, filename='pymiki.db'):
        super().__init__(filename)

    def add_user_if_not_exists(self, userId):
        return

    def get_user_data(self, userId, field='*'):
        return

    def close(self):
       self.db.close()


class GuildSQL(MikiSQL):

    def __init__(self, filename='pymiki.db'):
        super().init(filename)

    def get_guild_xp()
