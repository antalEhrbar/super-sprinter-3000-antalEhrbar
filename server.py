from flask import Flask, render_template, redirect, request, session

app = Flask(__name__)


def get_file_name():
    return "./templates/datas.csv"


def read_story_from_file():
    file_name = get_file_name()
    with open(file_name, "r") as file:
        lines = file.readlines()
    table = [element.replace("\n", "").split(";") for element in lines]
    return table


def add(new_story):
    stories = read_story_from_file()
    maxi = 0
    for line in stories:
        if int(line[0]) > maxi:
            maxi = int(line[0])
    new_story.insert(0, str(maxi))
    stories.append(new_story)
    write_story_to_file(stories)


def delete(id_):
    all_story = read_story_from_file()
    for index, sub_list in enumerate(all_story):
            if sub_list[0] == str(id_):
                all_story.pop(index)
    write_story_to_file(all_story)


def write_story_to_file(all_story):
    file_name = get_file_name()
    with open(file_name, "w") as file:
        for record in all_story:
            row = ';'.join(record)
            file.write(row + "\n")

@app.route("/")
@app.route("/list")
def route_list():
    all_story = read_story_from_file()
    return render_template("list.html", all_story=all_story)


@app.route("/story", methods=["GET"])
def story_making():
    return render_template("form.html")


@app.route("/save-story", methods=["POST"])
def save_new_stories_to_file():
    story_title = request.form["story_title"]
    user_story = request.form["user_story"]
    acceptance_critera = request.form["acceptance_critera"]
    business_value = request.form["business_value"]
    estimation = request.form["estimation"]
    status = request.form["status"]
    new_story = [story_title, user_story, acceptance_critera, business_value, estimation, status]
    add(new_story)
    return redirect("/")


@app.route("/delete-story/<int:id_>", methods=["POST"])
def delete_story(id_):
    delete(id_)
    return redirect("/")

if __name__ == "__main__":
  app.secret_key = 'lolitsmeagain1896'
  app.run(
      debug=True,
      port=5000
  )

