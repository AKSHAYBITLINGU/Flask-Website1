from flask import Flask,render_template,jsonify

JOBS = [
  {
    'id':1,
    'title':'Data Analyst',
    'location':'Hyderabad, Telangana',
    'salary':'Rs. 1,20,000'
  },
  {
    'id':2,
    'title':'Data Scientist',
    'location':'Delhi, India',
    'salary':'Rs. 10,00,000'
  },
  {
    'id':3,
    'title':'Frontend Engineer',
    'location':'San Fransisco, USA',
    'salary':'Rs. 15,00,000'
  },
  {
    'id':4,
    'title':'Backend Engineer',
    'location':'Remote',
    'salary':'Rs. 12,00,000'
  }
]

app = Flask(__name__)

@app.route("/")
def hello_world():
  return render_template('home.html',jobs=JOBS,company_name='AN')

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__== "__main__":
  app.run(host='0.0.0.0',debug=True)

