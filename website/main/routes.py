import os
from flask import *
from website.details import *
import requests

main = Blueprint("main", __name__)


@main.route("/favicon.ico")
def favicon():
    return send_from_directory(
        os.path.join(current_app.root_path, "../static"),
        "favicon.ico",
        mimetype="image/vnd.microsoft.icon",
    )


@main.route("/")
def home():
    response = requests.get("https://raw.githubusercontent.com/rrkas/MyWebsiteData/main/data/intro.html")
    if response.status_code == 200:
        intro_html = response.text
    else:
        intro_html = '<p style="color:indigo;">Error Loading intro!</p>'
    return render_template("home.html", intro_html=intro_html)


@main.route("/about")
def about():
    details_response = requests.get(
        "https://raw.githubusercontent.com/rrkas/MyWebsiteData/main/data/about_personal_details.json"
    )
    if details_response.status_code == 200:
        details = json.loads(details_response.text)
    else:
        details = {}
    education_df = pd.read_csv("https://raw.githubusercontent.com/rrkas/MyWebsiteData/main/data/about_education.csv")
    education_df.sort_values(by=["end_year"], inplace=True, ascending=False)
    education = [Education.from_df_row(education_df.iloc[row_idx]) for row_idx in range(len(education_df))]
    details["education"] = education
    return render_template("about.html", title="About", details=details)


@main.route("/cv")
def cv():
    details_response = requests.get(
        "https://raw.githubusercontent.com/rrkas/MyWebsiteData/main/data/about_personal_details.json"
    )
    if details_response.status_code == 200:
        file_id = json.loads(details_response.text)["cv_gdrive_file_id"]
        url = f'https://drive.google.com/file/d/{file_id}/preview?usp=drivesdk'
    else:
        url = None
    return render_template("cv.html", title="CV", url=url)


# ======================== error handlers ===========================


@main.app_errorhandler(404)
def error_404(error):
    return render_template("errors/404.html")


@main.app_errorhandler(403)
def error_403(error):
    return render_template("errors/403.html")
