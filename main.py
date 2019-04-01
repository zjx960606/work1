from flask import Flask,render_template,request,redirect,make_response

from orm import ormmanage as manage
import datetime

app = Flask(__name__)
app.send_file_max_age_default=datetime.timedelta(seconds=1)
app.debug=True



#将http://127.0.0.1:5000/ 和视图绑定
@app.route('/')
def index():
    if request.method == 'GET':
        # # 获取凭证cookie
        user=request.cookies.get('name')
        return render_template('index.html',userinfo=user)
    elif request.method == 'POST':
        # username = request.form['username']
        # password = request.form['password']
        # print(username, password)
        # print('收到post请求，提交表单参数')

        return redirect('/list')


@app.route('/list')
def list():
    # b1 = model.Book(1,'倚天屠龙记','李世民',10)
    # b2 = model.Book(2, '倚天屠龙记', '百里',30)


    try:
        username=request.cookies.get('name')
        userid=manage.checkUser_id(username)
        result = manage.userList(user_id=userid)
        #  获取凭证cookie
        # user = request.cookies.get('name')
        print(result)
        return render_template('list.html',rega=result,userinfo=username)
    except:
        return render_template('list.html')


@app.route('/regist',methods=['POST','GET'])
def regist():
    if request.method=='GET':
        args=request.args
        name=args.get('name')
        valuel=args.get('valuel')
        print(name,valuel)
        print('收到get请求，返回注册界面')
        return render_template('regist.html')
    elif request.method=='POST':
        username=request.form['username']
        password=request.form['password']
        print(username,password)
        print('收到post请求，提交表单参数')

        try:
            manage.insertUser(username,password)
            return redirect('/login')

        except:
           redirect('/regist')




@app.route('/login',methods=['POST','GET'])
def login():
    if request.method=='GET':
        return render_template('login.html')
    elif request.method=='POST':
        username = request.form['username']
        password = request.form['password']
        print(username, password)
        print('收到post请求，提交表单参数')

        # 判断账户密码与数据库中是否一致
        try:
            result=manage.checkUser(username,password)
            if result==True:
                print(result)
                res = make_response(redirect('/'))
                res.set_cookie('name', username, expires=datetime.datetime.now() + datetime.timedelta(days=7))
                return res
            else:
                print('用户名或密码错误')
                return redirect('/login')
        except:
           return redirect('/login')

# 增加
@app.route('/add',methods=['GET','POST'])
def add():
    #  # 获取凭证cookie
    username = request.cookies.get('name')
    userid = manage.checkUser_id(username)
    if request.method=='GET':
        return render_template('add.html',userinfo=username)
    elif request.method=='POST':
        bookname=request.form['name']
        author=request.form['author']
        price=request.form['price']

        try:

            manage.add(bookname,author,price,userid)
            print(1111)
            return redirect('/list')
        except:
            pass


@app.route('/list/<id>',methods=['GET','POST'])
def delete(id):
    manage.delete(id)
    return redirect('/list')


@app.route('/update/<id>',methods=['GET','POST'])
def update(id):
    #  # 获取凭证cookie
    username = request.cookies.get('name')

    if request.method=='GET':
        return render_template('update.html',id=id,userinfo=username)
    elif request.method=='POST':
        bookname=request.form['name']
        author=request.form['author']
        price=request.form['price']

        try:

            manage.update(id,bookname,author,price)
            print(1111)
            return redirect('/list')
        except:
            pass


@app.route('/quit')
def quit():
    res = make_response(redirect('/'))
    res.delete_cookie('name')
    return res






if __name__=="__main__":
    app.run()


