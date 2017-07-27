import sqlite3


class MikiSQL:
    def __init__(self, filename='pymiki.db'):
        self.db = sqlite3.connect(filename)
        self.cursor = self.db.cursor()

    def close(self):
        self.db.commit()
        self.db.close()

    def close_no_save(self):
        self.db.close()


# accounts: (user_id text, user_name text, currency int, daily_reset text, command_uses int, xp int, marriage_slots int, marriages text, achievements text)
class AccountSQL(MikiSQL):
    def add_user_if_not_extant(self, user_id):
        self.cursor.execute("SELECT * FROM account WHERE user_id=?", (user_id,))
        if not (self.cursor.fetchone()):
            # ERROR
            return
        else:
            self.cursor.execute("INSERT INTO account VALUES(?,?,?,?,?,?,?)")

    def get_user_data(self, user_id, field='*'):
        return


class GuildSQL(MikiSQL):
    def get_guild_xp(self):
        return


# (pasta_tag text, pasta_text text, creator_id text, creation_date text, uses integer, likes integer, dislikes integer)
class PastaSQL(MikiSQL):
    def add(self, args: tuple):
        self.cursor.execute('''INSERT INTO pasta VALUES (?,?,?,?,?,?,?)''', args)
        self.db.commit()

    def exists(self, pasta_tag):
        self.cursor.execute("""SELECT * FROM pasta WHERE pasta_tag=?""", (pasta_tag,))
        if self.cursor.fetchone() is None:
            return False
        return True

    def pasta_owned(self, pasta_tag, user_id):
        self.cursor.execute("""SELECT * FROM pasta WHERE pasta_tag=? AND creator_id=?""", (pasta_tag, user_id))
        if self.cursor.fetchone() is None:
            return False
        return True

    def get(self, pasta_tag):
        self.cursor.execute("""SELECT pasta_text,uses FROM pasta WHERE pasta_tag=?""", (pasta_tag,))
        return self.cursor.fetchone()

        # HAH LMAO

    def get_owned(self, user_id):
        self.cursor.execute("""SELECT pasta_text,uses FROM pasta WHERE creator_id=?""", (user_id,))
        return self.cursor.fetchall()

    def get_info(self, pasta_tag):
        self.cursor.execute("""SELECT * FROM pasta WHERE pasta_tag=?""", (pasta_tag,))
        return self.cursor.fetchone()

    def delete(self, pasta_tag):
        self.cursor.execute("""DELETE FROM pasta WHERE pasta_tag=?""", (pasta_tag,))
        self.db.commit()

    def update_text(self, pasta_tag, pasta_text):
        self.cursor.execute('''UPDATE pasta SET pasta_text=? WHERE pasta_tag=?''', (pasta_text, pasta_tag))
        self.db.commit()

    def update_uses(self, uses, pasta_tag):
        self.cursor.execute('''UPDATE pasta SET uses=? WHERE pasta_tag=?''', (uses, pasta_tag))
        self.db.commit()

    def popular(self):
        self.cursor.execute('''SELECT pasta_tag,uses FROM pasta ORDER BY uses DESC LIMIT 12''')
        return self.cursor.fetchall()

    def top(self):
        return
