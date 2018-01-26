from server.app import DB


class BaseModel:
    def save(self):
        """Save data to database"""
        DB.session.add(self)
        DB.session.commit()
