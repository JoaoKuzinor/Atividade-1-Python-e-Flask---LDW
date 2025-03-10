from flask import render_template, request, redirect, url_for
import urllib
import json

players = []
teamlist = [{"name": "Santos", "year": 1912, "description": "Santos Futebol Clube"}]


def init_app(app):

    @app.route("/")
    def home():
        return render_template("index.html")

    @app.route("/teams", methods=["GET", "POST"])
    def teams():
        team = teamlist[0]
        if request.method == "POST":
            if request.form.get("player"):
                players.append(request.form.get("player"))
        return render_template("teams.html", team=team, players=players)

    @app.route("/cadteams", methods=["GET", "POST"])
    def cadteams():
        if request.method == "POST":
            if (
                request.form.get("name")
                and request.form.get("year")
                and request.form.get("description")
            ):
                teamlist.append(
                    {
                        "name": request.form.get("name"),
                        "year": request.form.get("year"),
                        "description": request.form.get("description"),
                    }
                )
        return render_template("cadteams.html", teamlist=teamlist)

    @app.route("/apiteams", methods=["GET", "POST"])
    @app.route("/apiteams/<int:idTeam>", methods=["GET", "POST"])
    def apiteams(id=None):
        url = "https://www.thesportsdb.com/api/v1/json/3/search_all_teams.php?s=Soccer&c=Switzerland"
        res = urllib.request.urlopen(url)
        data = res.read()
        teamsjson = json.loads(data)
        if id:
            tinfo = []
            for t in teamsjson["teams"]:
                if t["idTeam"] == id:
                    tinfo = t
                    break
            if tinfo:
                return render_template("teaminfo.html", tinfo=tinfo)
            else:
                return f"Time com a ID {id} não foi encontrado."
        else:
            return render_template("apiteams.html", teamsjson=teamsjson["teams"])
