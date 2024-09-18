from flask import Flask, request
from flask_cors import CORS, cross_origin
import winsound, time

app = Flask(__name__)
CORS(app, support_credentials=True)

routesToBusNums = {
    "Channasandra to Tinfactory" : ["304K",
               "305P",
               "506A",
               "MF-1C",
               "MF-319E",
               "306"],
    "Channasandrs to whitefield" : ["328H","331","334E","KBS1K","V-333E","320A"],
    "Channasandra to ITPL" : ["304K","304VB","306","506A","MF-1C","335E","507B","V-335E"],
    "Channasandra to K R Market" : ["306","304V","V-333E"],
    "Majestic to Channsandra" : ["333E","KBS-1K","KBS-1I","SBS-1K","335E","334E"],
    "Tinfactory to Channsandra" : ["305P","304K","506A","MF-1C","MF-319E","306"]
}

busNumsToTimeSlots = {
    "304K" : ["5:30-6:00","6:30-7:00","7:30-8:00","8:30-9:00","12:30-13:00"],
    "328H" : ["5:30-6:00","6:30-7:00","7:30-8:00","8:30-9:00","12:30-13:00"],
    "304K" : ["5:30-6:00","6:30-7:00","7:30-8:00","8:30-9:00","12:30-13:00"],
    "306" : ["5:30-6:00","6:30-7:00","7:30-8:00","8:30-9:00","12:30-13:00"],
    "333E" : ["1:30-2:00","6:30-7:00","7:30-8:00","8:30-9:00","12:30-13:00"],
    "305P" : [],
}

@app.route("/getRoutes")
@cross_origin(supports_credentials=True)
def getRoutes():
    routes = ["Channasandra to Tinfactory",
              "Channasandrs to whitefield",
              "Channasandra to ITPL",
              "Channasandra to K R Market",
              "Majestic to Channsandra",
              "Tinfactory to Channsandra"]
    return routes

@app.route("/getBusNums")
@cross_origin(supports_credentials=True)
def getBusNums():
    args = request.args
    route = args.get("route")
    return routesToBusNums[route]

@app.route("/getTimeSlots")
@cross_origin(supports_credentials=True)
def getTimeSlots():
    args = request.args
    busNo = args.get("busNo")
    return busNumsToTimeSlots[busNo]

@app.route("/ring")
@cross_origin(supports_credentials=True)
def ring():
    duration = 2000 # milliseconds
    freq = 440 # Hz
    # time.sleep(2)
    winsound.Beep(freq, duration)
    return "The bus is here....."

if __name__ == "__main__":
    app.run()