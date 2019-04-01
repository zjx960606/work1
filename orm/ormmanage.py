from orm import model
from sqlalchemy import create_engine
engine = create_engine("mysql+mysqlconnector://root:123456@localhost/flaskdb",
                                    encoding='utf8', echo=True)
from sqlalchemy.orm import sessionmaker
session=sessionmaker()()

# 添加注册用户
def insertUser(username,password):
    result=session.add(model.User(username=username,password=password))
    session.commit()
    session.close()
# 登录
def checkUser(username,password):
    result=session.query(model.User).filter(model.User.username==username).filter(model.User.password==password).first()
    if result:
        return True
    else:
        return False


def checkUser_id(username):
    result=session.query(model.User).filter(model.User.username==username).first().id
    if result:
        return result
    else:
        return -1
# 商品
def userList(user_id):
    result=session.query(model.User_list.id,model.User_list.name,model.User_list.author,model.User_list.price,
                         model.User_list.user_id).filter(model.User_list.user_id==user_id).all()

    return result

# 增加

def add(name,author,price,user_id):
    session.add(model.User_list(name=name,author=author,price=price, user_id=user_id))
    session.commit()
    session.close()

# 删除
def delete(book_id):
    session.query(model.User_list).filter(model.User_list.id==book_id).delete()
    session.commit()
    session.close()
# 修改

def update(id,name,author,price):
    session.query(model.User_list).filter(model.User_list.id==id).update({model.User_list.name:name,
                                    model.User_list.author:author,model.User_list.price:price})
    session.commit()
    session.close()
