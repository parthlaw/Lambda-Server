from sqlalchemy import Column, MetaData, String, Table, create_engine, select, update
from sqlalchemy.dialects.postgresql import UUID
import uuid
import psycopg2

from schemas.validation_resp import ValidationResp
class DB:
    def __init__(self,cred):
        self.user=cred["username"]
        self.password=cred["password"]
        self.host=cred["host"]
        self.port=cred["port"]
        db_string=f"postgresql://{self.user}:{self.password}@{self.host}:{self.port}"
        print(db_string)
        self.db=create_engine(db_string,connect_args={"sslmode": "require"})
        self.meta=MetaData(schema=None)
        self.user_table = Table(
                'users',self.meta,
                Column('id',UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
                Column('full_name',String),
                Column('mob_number',String),
                Column('pan_number',String,primary_key=True)
                )
    def _validate_phone(self,phone:str):
        if len(phone)!=10:
            return False
        return True
    def _validate_pan(self,pan:str):
        return True
    def _validate_name(self,name:str):
        if len(name)==0:
            return False
        return True
    def _validate_user(self,user:dict):
        validation_errors=[]
        if "mob_number" in user:
            if not self._validate_phone(user["mob_number"]):
                validation_errors.append(ValidationResp.Wrong_Phone)
        if "full_name" in user:
            if not self._validate_name(user["full_name"]):
                validation_errors.append(ValidationResp.EMPTY_NAME)

        if "pan_number" in user:
            if not self._validate_pan(user["pan_number"]):
                validation_errors.append(ValidationResp.Wrong_PAN)
        return validation_errors
    def create_user(self,user):
        try:
            connection = psycopg2.connect(user=self.user,password=self.password,host=self.host,database="postgres")
            cursor = connection.cursor()
            validation_errors = self._validate_user(user)
            if len(validation_errors)!=0:
                return validation_errors
            # with self.db.connect() as conn:
            # insert_statement = self.user_table.insert().values(
            #         full_name=user["full_name"],
            #         mob_number=user["mob_number"],
            #         pan_number=user["pan_number"]
            #         )
            id = uuid.uuid4()
            full_name=user["full_name"]
            mob_number=user["mob_number"]
            pan_number=user["pan_number"]
            insert_statement=f"INSERT INTO users (id,full_name,mob_number,pan_number) VALUES ('{str(id)}','{full_name}','{mob_number}','{pan_number}')"
            print("INSERT",insert_statement)
            cursor.execute(insert_statement)
            cursor.close()
            connection.commit()
            return user
        except Exception as e:
            print("ERROR",e)
            raise e
    def get_users(self):
        with self.db.connect() as conn:
            list_users_query = select([self.user_table])
            rows=conn.execute(list_users_query).all()
            if rows is None:
                return []
            return rows
    def delete_user(self,user_id):
        select_query=select([self.user_table]).where(self.user_table.c.id==user_id)
        with self.db.connect() as conn:
            result = conn.execute(select_query).first()
        if result is None:
            return False
        delete_query = self.user_table.delete().where(self.user_table.c.id==user_id)
        with self.db.connect() as conn:
            conn.execute(delete_query)
        return True
    def update_user(self,user_id,update_data:dict):
        validation_errors = self._validate_user(update_data)
        if len(validation_errors)!=0:
            return validation_errors
        select_query=select([self.user_table]).where(self.user_table.c.id==user_id)
        with self.db.connect() as conn:
            result = conn.execute(select_query).first()
        if result is None:
            return None
        for key,value in update_data.items():
            result[key]=value
        update_query = update(self.user_table).where(self.user_table.c.id==user_id).values(
                full_name=result["full_name"],
                mob_number=result["mob_number"],
                pan_number=result["pan_number"]
                )
        with self.db.connect() as conn:
            result= conn.execute(update_query)
        return result

