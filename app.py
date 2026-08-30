from flask import Flask, request
import subprocess
app = Flask(  name  )
@app.route("/run") 
def run_command():

command = request.args.get("command")
result = subprocess.check_output(command, shell=True) 
return result

if  name	== " main ": 
  app.run()

