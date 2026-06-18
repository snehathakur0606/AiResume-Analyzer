`from flask import Flask
app = Flask(_name_)
@app.route('/')
def home():
  return"AI Resume Analyzer"
  if __name__ == '__main__':
    app.run(debug=True)
