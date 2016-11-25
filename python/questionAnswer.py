import re
def isQuestionForPhNo(str):
	if "ph number" in str:
		return re.search("ph number (.*)",str).groups()[0].split()[1]
	elif "phone number":
		return re.search("phone number (.*)",str).groups()[0].split()[1]
	elif "ph no":
		return re.search("ph no (.*)",str).groups()[0].split()[1]
	else:
		return False
def answerQuestion(str):
	if(isQuestionForPhNo(str)):
		return  isQuestionForPhNo(str)
	else:
		return "UNKNOWN QUESTION"