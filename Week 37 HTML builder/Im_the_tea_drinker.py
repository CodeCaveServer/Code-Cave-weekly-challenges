import os
import sys

file = open("input.txt", "r")
file = file.readlines()
bulletpointline = ""
numberpointline = ""
for line in file:
    if line.startswith("BULLET POINTS:"):
        bulletpointline += line
    elif line.startswith("NUMBER LIST:"):
        numberpointline += line

bulletpointline = bulletpointline.replace("BULLET POINTS:", "")
numberpointline = numberpointline.replace("NUMBER LIST:", "")
bulletpoints = bulletpointline.split(", ")
numberpoints = numberpointline.split(", ")

html = open("output.html", "w")
html.write("<html><head><title>My HTML</title></head><body>")
html.write("<body>")

if bulletpoints != ['']:
    html.write("<ul>")
    for point in bulletpoints:
        html.write("<li>" + point + "</li>")
    html.write("</ul>")
if numberpoints != ['']:
    html.write("<ol>")
    for point in numberpoints:
        html.write("<li>" + point + "</li>")
    html.write("</ol>")

html.write("</body></html>")
html.close()
print("HTML file created")

