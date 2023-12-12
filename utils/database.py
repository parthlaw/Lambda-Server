from sqlalchemy import Column, MetaData, String, Table, create_engine
class DB:
    def __init__(self,cred):
        self.user=cred["username"]
        self.password=cred["password"]
        self.host=cred["host"]
        self.port=cred["port"]
        db_string=f"postgresql://{self.user}:{self.password}@{self.host}:{self.port}"
        print(db_string)
        self.db=create_engine(db_string)
        self.meta=MetaData(self.db)
        self.user_table = Table(
                'users',self.meta,
                Column('full_name',String),
                Column('mob_number',String),
                Column('pan_number',String,primary_key=True)
                )

