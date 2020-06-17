from flask import Flask, render_template, request, send_file
from github import Github, UnknownObjectException
import os
import pandas
import config
import markdown2

from database import DataBase

def get_github_repos():
    repos = []
    for repo in github.get_user().get_repos(visibility="public"):
        try:
            contents = repo.get_contents("README.md")
            repos.append(dict({"repo_name": repo.name, "readme": contents.decoded_content.decode("utf-8"),
                               "repo_url": repo.url}))
        except UnknownObjectException as e:
            print(e)
    return repos

github = Github(os.environ["GITHUB_TOKEN"])
app = Flask(__name__)
app.config.from_object(config)
github_projects = get_github_repos()
db_client = DataBase(database="projects", projects=github_projects)


@app.route('/')
def index():
    print("print projects")
    for i in range(len(github_projects)):
        github_projects[i]['readme'] = markdown2.markdown(github_projects[i]['readme'])
    return render_template('index.html', github_projects=github_projects)

@app.route("/project/<repo_name>")
def project(repo_name):
    project_info = db_client.get_project(repo_name)
    readme = markdown2.markdown(project_info['readme'])

    return render_template("project.html", repo_name=project_info['repo_name'],
                           readme=readme, repo_url=project_info['repo_url'])

@app.route("/project/images/<image_name>")
def image(image_name):
    if os.path.exists("static/{0}".format(image_name)):
        return send_file("static/{0}".format(image_name))
    else:
        return False

@app.route('/subnets')
def subnet():
    df = pandas.read_csv('C:\\Users\\alex\\subnet.csv')
    return render_template('table.html', csv=df)

@app.route('/vlans')
def vlans():
    df = pandas.read_csv('/Users/alexmarriott/Documents/vlans.csv')
    return render_template('vlans.html', csv=df)

if __name__ == '__main__':
    app.run(host=os.environ['FLASK_RUN_HOST'], port="80")