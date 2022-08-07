from flask import Flask, render_template
from flask import request, redirect
from flask_sqlalchemy import SQLAlchemy
from  datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///friends.db'
#Intialize database
db = SQLAlchemy(app)


#Create db model 

class Friends(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime,default=datetime.utcnow)

    #Create functon to return string when we add something 
    def __repr__(self):
        return 'Name %r' % self.id








########

subscribers = []

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/about')
def about():
    names = ["John","Mary","Wes","Sally"]
    return render_template("about.html", names=names)

@app.route('/subscribe')
def subscribe():
    title = "Subscribe to my email newsletter"
    return render_template("subscribe.html", title=title)

@app.route('/form', methods = ["POST"])
def form():
    first_name = request.form.get("first_name")
    last_name = request.form.get("last_name")
    email =  request.form.get("email")

    #Emailing the user  #refer to codemy video #
    # message = "You have been subscribed to my email newsletter"
    # server = smtplib.SMTP("smtp.gmail.com", 587)
    # server.starttls()
    # server.login("alex.a.ibrahim@gmail.com","password")
    # server.sendmail("alex.a.ibrahim@gmail.com", email, message)
    

    #Ensure forms are filled out 
    if not first_name or not last_name or not email:
        error_statement = "All Form Fields Required..."
        return render_template(
            "subscribe.html", 
            first_name = first_name, 
            last_name=last_name, 
            email = email , 
            error_statement=error_statement)

    
    subscribers.append(f"{first_name} + {last_name} + {email}")

    title = "Thank You"
    return render_template("form.html", subscribers = subscribers)


@app.route('/friends', methods=['POST','GET'])
def friends():
    title = "My friend list"

    if request.method == "POST":
        friend_name = request.form['name']
        random_string = "sksksksk"
        new_friend = Friends(name=friend_name)

        try:
            db.session.add(new_friend)
            db.session.commit()
            return redirect('/friends')
        
        except:
            return "There was an error addding your friend"

    else:
        friends = Friends.query.order_by(Friends.date_created)
        return render_template("friends.html", title=title, friends=friends)

@app.route('/update/<int:id>', methods=['POST','GET'])
def update(id):
        friend_to_update = Friends.query.get_or_404(id)

        if request.method == "POST":
            friend_to_update.name = request.form['name']

            try:
                db.session.commit()
                return redirect('/friends')

            except:
                return "There was a problem updating that friend"
        
        else:
            return render_template('update.html', friend_to_update=friend_to_update)
