from flask import request, render_template, redirect
from app import app
import sys
import os

try:
   pyWrskpLoc = os.environ["PYWRKSP"]
   
except KeyError:
   pyWrkspLoc = input('Enter the pwd for the pyWrskp repo') # change this to the loc of the pyWrskp repo (include the pyWrskp part)

User = ''

blogPosts_list = [
    {
        'creator':{'username':'Jonah', 'user':'Jonah'},
        'content':'Why this website is better then the other',
        'info':'It is home made by me! It also has many pages, unlike the first website I made!',
        'link':'/post/Jonah'
    },
    {
        'creator':{'username':"Mr. Payne's 4/5 class 2020-21", 'user':"Mr.Payne's+45+class+2020-21"},
        'content':'Why in-person school is better then the online version',
        'info':"In-person school is sooooooooooo much better than online school becuase when we are in person we can chat, and eat together (note this was not written by Mr.Payne's class, it was written by Jonah)",
        'link':"/post/Mr.Payne's+45+class"
        },
    {
        'creator':{'username':'Jonah', 'user':'Jonah1'},
        'content':'What does www stand for?',
        'info':'What does www (like https://www...) mean? www means World Wide Web!',
        'link':'/post/Jonah1'
        },
    {
        'creator':{'username':'Jonah', 'user':'Jonah2'},
        'content':'How to show the CEO info',
        'info':'in your web address bar, remove "/link/Jonah2", and put "/ceo+info" instead, then press enter, and bingo, you got the CEO info!',
        'link':'/post/Jonah2'
        }]

CEO = {'name':'Jonah Makowski',
       'emails':{
        '1':'jonah.kmjn@gmail.com',
        '2':'jonah@makowski.ca',
        '3':'jonah@makowski.at'},
       'link':'https://www.youtube.com/channel/UC1ti62i-uMnBVAh9b_Pp3UA/'}

@app.route('/', methods=['POST', 'GET'])
@app.route('/welcome', methods=['POST', 'GET'])
def Welcome():
    return render_template('index.html', title='Welcome', User = User)

@app.route('/home', methods=['POST', 'GET'])
def home():
    return render_template('home.html', title='Home', User = User)

@app.route('/home/blogposts', methods=['POST', 'GET'])
@app.route('/home/blogposts/', methods=['POST', 'GET'])
@app.route('/blogposts', methods=['POST', 'GET'])
def blog_posts():
    return render_template('posts.html', title='blog posts', posts=blogPosts_list)

@app.route('/post/<creator>', methods=['POST', 'GET'])
def post(creator):
    usr = False
    for post in blogPosts_list:
        if post['creator']['user'] == creator:
            usr = True
            break
    if usr == False:
        error_code = '404'
        error='{} error'.format(str(error_code))
        title = error
        return render_template('error.html', title=title, error=error)
    else:
        return render_template('Blog_outline.html', title=post['creator']['username'] + "'s blog post", post=post)

@app.route('/home/blogposts/small', methods=['POST', 'GET'])
@app.route('/home/blogposts/small/', methods=['POST', 'GET'])
@app.route('/blogposts/small', methods=['POST', 'GET'])
@app.route('/blogposts+small', methods=['POST', 'GET'])
@app.route('/home/blogposts+small', methods=['POST', 'GET'])
def blog_post_small():
    return render_template('posts_small.html', title='blog posts', posts=blogPosts_list)

@app.route('/music', methods=['POST', 'GET'])
def music():
    return render_template('music.html', title='Music')

@app.route('/calendar', methods=['POST', 'GET'])
def calendar():
    return render_template('calendar.html', title='calendar')

@app.route('/ceo+info', methods=['POST', 'GET'])
def ceo_info():
    if request.method == "POST":
        return redirect(CEO['link'])
    name = 'Name:         ' + CEO ['name']
    email = 'Emails:       {}, {}, {}'.format(CEO['emails']['1'], CEO['emails']['2'], CEO['emails']['3'])
    link = 'Youtube channel: ' + CEO['link']
    print(name + '\n' + email + '\n' + link)
    return render_template('CEO_info.html', title='CEO info', name = name, email=email, link=link)

@app.route('/youtube', methods=['POST', 'GET'])
def youtube():
    return render_template('youtube.html', title='youtube')

@app.route('/page', methods=['POST', 'GET'])
def page():
    return render_template('page.html', title='List of Pages | This is a list of pages on this website')

@app.route('/cac', methods=['POST', 'GET'])
def caculator_sender():
    if request.method == "POST":
        global pyWrkspLoc
        try:
            num2 = int(request.form.get("num2"))
        except:
            num2 = None
        import sys
        sys.path.append(pyWrkspLoc + '/src/other/home')

        from caculator import use
        
        q, a = use(int(request.form.get("num1")),
                   num2,
                   request.form.get("type"))
        return render_template('caculator.html', title='Caculator', a = a, q = q)
    return render_template('caculator_redirect.html', title='Caculator Sender')

@app.route('/passwords', methods=['GET', 'POST'])
def passwords():
    if request.method == "POST":
        global pyWrkspLoc
        from random import randint
        
        sys.path.append(pyWrkspLoc + '/src/password_maker')

        from Creater import create
        
        password = create(request.form.get("letters"),
                        request.form.get("numbers"),
                        request.form.get("sc"),
                        request.form.get("super_c"),
                        int(request.form.get("length")),
                        'n',
                        False)
        return render_template('password_show.html', title='Passwords', password=password)
    return render_template('passwords.html', title='Passwords')

@app.route('/login', methods=['GET', 'POST'])
def login():
    global User
    if request.method == "POST":
        global pyWrkspLoc
        password = request.form.get("password")
        User = request.form.get("username")
        if User == 'WhiteSwine' and password == 'LOLA IS THE BEST':
            return render_template('logged_in.html', title = 'logged in!', user = User)
        else:
            return '<h1>INCORRECT</h1>'
        
    return render_template('login.html', title='login')

@app.route('/turtle', methods=['GET', 'POST'])
def turtle():
    if request.method == "POST":
        global pyWrkspLoc
        
        sys.path.append(pyWrkspLoc + '/src/other/home')
        
        try:
            from noah_and_me_turtle import run
            run()
        except:
            return redirect('/')
        return '<h1>Done</h1> <p>if nothing is happening, you have an error</p> <a href="/">return to home page</a>'
    return render_template('turtle.html', title='Noah and me turtle')

@app.route('/pygame/draw', methods=['GET', 'POST'])
def draw():
    if request.method == "POST":
        global pyWrkspLoc
        sys.path.append(pyWrkspLoc + '/src/other/classes')
        
        from Class_one import draw
        
        draw()
        return '<h1>Done</h1> <p>if nothing is happening, you have an error</p> <a href="/">return to home page</a>'
    return render_template('pygame_draw.html', title='DRAW!')

@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    return render_template('feedback.html', title='Feedback')

@app.route('/fire', methods=['GET', 'POST'])
def fire():
    return render_template('fire.html', title='Fire')

@app.route('/alarm', methods=['GET', 'POST'])
def alarm():
    if request.method == 'POST':
        global pyWrkspLoc
        sys.path.append(pyWrkspLoc + '/src/alarm')
        
        from time_only import work
        
        work(request.form.get('hour'), request.form.get('min'), print_info=False)
        
        return '<h1>DING-DONG</h1> <a href="/">return to home page</a>'
    return render_template('alarm.html', title='Alarm clock!')

@app.route('/lola', methods=['GET', 'POST'])
def lola():
    return render_template('lola.html', title='Lola Image')

@app.route('/code', methods=['GET', 'POST'])
def code():
    if request.method == 'POST':
        global pyWrkspLoc
        sys.path.append(pyWrkspLoc + '/src/coder-decoder')
        
        from coder import coderDecoder
        
        key = request.form.get('key')
        coder_decoder = request.form.get('type')
        
        coder = coderDecoder(message=request.form.get('message'), key=key, print_info=False)
        if coder_decoder == 'code':
            message = coder.code()
        elif coder_decoder == 'decode':
            message = coder.decode()
        return render_template('coder_show.html', title='coder decoder show', message=message, key=key)
    return render_template('coder.html', title='coder decoder')