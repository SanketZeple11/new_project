from Userapp import app
from Userapp.master.views import refreshtoken, login, logout, register
from Userapp.user.views import getAllUser, getUser
from Userapp.role.views import udtpassword

app.register_blueprint(refreshtoken)
app.register_blueprint(logout)
app.register_blueprint(register)
app.register_blueprint(login)
app.register_blueprint(getAllUser)
app.register_blueprint(getUser)
app.register_blueprint(udtpassword)

if __name__ == "__main__":
    app.run()
