import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os


def return_html_checklist(shopping_list_dict):
	"""Takes a dictionary of ingredients with dictionary value containing "amount" and "metric"
	and returns html checklist items"""

	html_ingredients = " "

	# 'test' == ('te',
	# 		'st')

	for item in shopping_list_dict:
		amount = shopping_list_dict[item]['amount']
		metric = shopping_list_dict[item]['metric']
		if metric == None:
			html_ingredients += f'<input type="checkbox" name="ingredient"><label> {item.ingredient_name} {amount} </label> <br>'
		else:
			html_ingredients += f'<input type="checkbox" name="ingredient"><label> {item.ingredient_name} {amount} {metric} </label> <br>'
	
	return(html_ingredients)

def return_html_hyperlinks(recipes):
	"""Takes a list of recipe objects and returns html links"""
	hyperlinks =  " "
	for recipe in recipes:
		hyperlinks += f'<li> <a href="/{recipe.recipe_id}"> {recipe.recipe.recipe_name} </a> </li>'
	return(hyperlinks)

def send_email(user_email, user_name, recipes, recipe_ingredients):
	port = 465  # For SSL
	smtp_server = "smtp.gmail.com"
	sender_email = "cookmoreofwhatyoulove@gmail.com"
	# receiver_email = "shira.amrany@gmail.com"
	receiver_email = user_email
	password = os.environ.get("EMPASSWORD")
	message = MIMEMultipart("alternative")

	message["Subject"] = "Shopping List"
	message["From"] = sender_email
	message["To"] = receiver_email


	# The plain-text and HTML version of the message
	text = """\

	Your Email does not support html. Please refer to the webpage instead."""

	html = f"""\

	<html>
	  <body>
	    <p> Hi, {user_name} <br>

	       Here are your recipe links:
	       {return_html_hyperlinks(recipes)}
     
	      Here are your shopping ingredients:
	      <form action="/action_page.php" method="get"> {return_html_checklist(recipe_ingredients)}
		  </form> 
		     
	    </p>
	  </body>
	</html>
	"""

	# Turn these into plain/html MIMEText objects
	part1 = MIMEText(text, "plain")
	part2 = MIMEText(html, "html")

	# Add HTML/plain-text parts to MIMEMultipart message
	# The email client will try to render the last part first
	message.attach(part1)
	message.attach(part2)

	# Create secure connection with server and send email
	context = ssl.create_default_context()
	with smtplib.SMTP_SSL(smtp_server, port, context=context) as email_server:
	    email_server.login(sender_email, password)
	    email_server.sendmail(sender_email, receiver_email, message.as_string())


