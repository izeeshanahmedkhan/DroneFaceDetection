import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text  import MIMEText
from email.mime.image import MIMEImage
import os
import requests
import json
from datetime import datetime

fromEmail = 'dronebatwing@gmail.com'
fromEmailPassword = 'batwing1'
toEmail = 'nashah333@gmail.com'
now = datetime.now()

def sendEmail(ID):
    a = os.popen('wget -qO- https://ipecho.net/plain').read()
    ip = a
    send_url = "http://api.ipstack.com/{}?access_key=7f5640a84bedef56c96ceb3e6d1ddb51".format(ip)
    geo_req = requests.get(send_url)
    geo_json = json.loads(geo_req.text)
    
    latitude = "Lattitude: " + str(geo_json['latitude'])
    longitude = "Longitude: " + str(geo_json['longitude'])
    city = "City: " + geo_json['city']
    country = "Country: " + geo_json['country_name']
    state = "State: " + geo_json['region_name']
    dt_string = now.strftime("%B %d, %Y %H:%M:%S")

    msgRoot = MIMEMultipart('related')
    msgRoot['Subject'] = 'Security Update'
    msgRoot['From'] = fromEmail
    msgRoot['To'] = toEmail
    msgRoot.preamble = 'Batwing Drone Security Camera Update'

    msgAlternative = MIMEMultipart('alternative')
    msgRoot.attach(msgAlternative)
    msgText = MIMEText('Batwing Drone cam found ' + str(ID))
    msgAlternative.attach(msgText)
    
    msgText = MIMEText('<br><h1>Batwing - Drone Cam Found ' + str(ID) + ' <h1><br> ' + latitude + '<br> ' + longitude + '<br> ' + country +'<br> ' + state + '<br> ' + city + '<br> ' + dt_string + '<br><br><img src="cid:image1">', 'html')
    msgAlternative.attach(msgText)

    fp = open('test.jpg', 'rb')
    msgImage = MIMEImage(fp.read())
    fp.close()

    msgImage.add_header('Content-ID', '<image1>')
    msgRoot.attach(msgImage)

    smtp = smtplib.SMTP('smtp.gmail.com', 587)
    smtp.starttls()
    smtp.login(fromEmail, fromEmailPassword)
    smtp.sendmail(fromEmail, toEmail, msgRoot.as_string())
    smtp.quit()
