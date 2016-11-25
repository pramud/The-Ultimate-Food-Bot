import re
def isQuestionForPhNo(str):
	if "ph number" in str:
		return re.search("ph number (.*)",str).groups()[0].split()[1:]
	elif "phone number" in str:
		return re.search("phone number (.*)",str).groups()[0].split()[1:]
	elif "ph no" in str:
		return re.search("ph no (.*)",str).groups()[0].split()[1:]
	else:
		return False
def answerQuestion(str):
	op = isQuestionForPhNo(str)
	if(op):
		return  op
	else:
		return "UNKNOWN QUESTION"