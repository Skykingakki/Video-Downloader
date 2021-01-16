from flask import Flask, render_template, request, redirect
import youtube_dl
app = Flask(__name__)

@app.route('/')
def home():
   return render_template('index.html')
@app.route('/download', methods =["POST" , "GET"])
def download():
   urll = request.form["urll"]
   with youtube_dl.YoutubeDL() as ydl:
      url = ydl.extract_info(urll, download = False)
      dlink = url["formats"][-1]["url"]
      return redirect(dlink+"&dl=True")

if __name__ == '__main__':
   app.run(port = 80)