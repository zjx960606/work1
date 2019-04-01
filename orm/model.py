class Book():

    def __init__(self, id,name,zuo_zhe,price):
        self.id=id
        self.name=name
        self.zuo_zhe=zuo_zhe
        self.price=price

    def __str__(self):
        return 'id: %s name: %s price: %s zuo_zhe %s',(self.id,self.name, self.zuo_zhe,self.price)


from sqlalchemy import create_engine

engine = create_engine("mysql+mysqlconnector://root:123456@localhost/flaskdb",
                                    encoding='utf8', echo=True)

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String,ForeignKey
Base = declarative_base(bind=engine)


class User(Base):
    __tablename__='user'
    id=Column(Integer,primary_key=True,autoincrement=True,nullable=False)
    username = Column(String(50),nullable=False)
    password = Column(String(50),nullable=False)


class User_list(Base):
    __tablename__='user_list'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name=Column(String(20),nullable=False)
    author=Column(String(20),nullable=False)
    price=Column(Integer,nullable=False)
    user_id=Column(Integer,ForeignKey(User.id),nullable=False)


if __name__=='__main__':
    # 创建表
    Base.metadata.create_all(bind=engine)
