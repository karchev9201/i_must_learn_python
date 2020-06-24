from flask import Flask, render_template, request, send_file
from scrapper import jobs as find_jobs
from exporter import save_to_csv

app = Flask("Scrapper")

data_for_test = {}

@app.route("/")
def home():
  return render_template("scrapper.html")

@app.route("/report")
def report():
  question_keyword = request.args.get('q')
  if question_keyword:
    question_keyword = question_keyword.lower()
    data = data_for_test.get(question_keyword)
    if data:
      jobs = data
    else:
      jobs = find_jobs(question_keyword)
      data_for_test[question_keyword] = jobs
    print(jobs)
  else:
    return home()
  return render_template("report.html", 
  searchingBy=question_keyword,
  resultNumber=len(jobs),
  jobs=jobs)

@app.route("/export")
def export():
  try:
    question_keyword = request.args.get('q')
    if not question_keyword:
      raise Exception()
    question_keyword = question_keyword.lower()
    jobs = data_for_test.get(question_keyword)
    if not jobs:
      raise Exception()
    save_to_csv(jobs,"jobs")
    return send_file("jobs.csv")
  except:
    return home()
  
    

app.run(host="0.0.0.0")
