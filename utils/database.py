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
    def _get_conn(self):
        return psycopg2.connect(user=self.user,password=self.password,host=self.host,database="postgres")

    def _convert_row(self,rows):
        resp=[]
        for row in rows:
            obj={}
            i=0
            for column in self.user_table.columns:
                obj[column.name]=row[i]
                i+=1
            resp.append(obj)
        return resp


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
            connection = self._get_conn()
            cursor = connection.cursor()
            validation_errors = self._validate_user(user)
            if len(validation_errors)!=0:
                return validation_errors
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
        # with self.db.connect() as conn:
        connection = self._get_conn()
        cursor = connection.cursor()
        list_users_query = f"SELECT * FROM {str(self.user_table.name)}"
        cursor.execute(list_users_query)
        rows = cursor.fetchall()
        cursor.close()
        connection.commit()
        print(rows)
        resp=self._convert_row(rows)
        print(resp)
        if rows is None:
            return []
        return resp
    def delete_user(self,user_id):
        select_query=f"SELECT * FROM {str(self.user_table.name)} WHERE id='{user_id}'"
        connection=self._get_conn()
        cursor=connection.cursor()
        cursor.execute(select_query)
        result=cursor.fetchall()
        if result is None or len(result)==0:
            cursor.close()
            connection.commit()
            return False
        delete_query = f"DELETE FROM {str(self.user_table.name)} WHERE id='{user_id}'"
        cursor.execute(delete_query)
        cursor.close()
        connection.commit()
        return True
    def update_user(self,user_id,update_data:dict):
        validation_errors = self._validate_user(update_data)
        if len(validation_errors)!=0:
            return validation_errors
        print(user_id)
        select_query=f"SELECT * FROM {str(self.user_table.name)} WHERE id='{user_id}'"
        connection=self._get_conn()
        cursor=connection.cursor()
        cursor.execute(select_query)
        result = cursor.fetchall()
        if result is None or len(result)==0:
            cursor.close()
            connection.commit()
            return None
        result = self._convert_row(result)[0]
        for key,value in update_data.items():
            result[key]=value

        update_columns=""
        i=0
        for column in self.user_table.columns:
            if(column.name=="id"):
                continue
            if i!=0:
                update_columns+=","
            update_columns+=f"{column.name}='{result[column.name]}'"
            i+=1
        update_query =f"""UPDATE {str(self.user_table.name)}
                        SET {update_columns}
                        WHERE id='{user_id}'"""        
        cursor.execute(update_query)
        cursor.close()
        connection.commit()
        return result

