import requests

# make 200 requests to the server
output = open("output_response_after_rolling_update.txt", "a+")
old_code_response = "Hello World. <br/>This is Gopal Khatri Devops-nanodegree capstone project"
new_code_response = "Welcome to my Zone"
response_texts = []
for i in range(600):
    response = requests.get("http://Devops-173062868.us-east-1.elb.amazonaws.com")
    if response.text == old_code_response:
        response_texts.append("OUTDATED pod response: " + response.text)
    if response.text == new_code_response:
        response_texts.append("UPDATED pod response: " + response.text)
    response_texts.append("\n\n")
output.writelines(response_texts)
output.close()
