# --------------------------------
# -- Flask => Create HTML Files --
# --------------------------------


from flask import Flask ,render_template



skills_app = Flask(__name__)

my_skills = [("Html",80),("CSS",76),("Js",70),("Java",90)]

@skills_app.route("/")
def homepage():
    return render_template("homepage.html", pagetitle="Homepage" , custom_css ="home")


@skills_app.route("/about")
def about():
    return render_template("aboutpage.html", 
                           pagetitle="About Us",
                          )




@skills_app.route("/skills")
def skills():
    return render_template("skills.html", pagetitle="My Skills",
                           pageHead="My Skills" ,
                           desc ="This Is My Skills Page",
                           skills=my_skills,
                           custom_css ="skills")






@skills_app.route("/add")
def add():
    return render_template("addpage.html",
                            pagetitle="Add Skill",
                            custom_css ="add")


if __name__ =="__main__":

    skills_app.run(debug=True,port=4000)