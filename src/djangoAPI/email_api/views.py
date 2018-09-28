from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import re
from email.parser import Parser
parser = Parser()

@csrf_exempt 
def email_list(req):
	if req.method == "POST":
		body = req.body.decode('utf-8')
		email = parser.parsestr(body)
		emailFrom = email.get('From')
		if emailFrom[0] == '<':
			emailFrom = emailFrom[1:-1]
		emailTo = email.get('To')
		if emailTo[0] == '<':
			emailTo = emailTo[1:-1]
		emailDate = email.get('Date')
		emailSubject = email.get('Subject')
		emailMessageID = email.get('Message-ID')
		return JsonResponse({"from":emailFrom,"to":emailTo,"date":emailDate,"subject":emailSubject,"message-id":emailMessageID})