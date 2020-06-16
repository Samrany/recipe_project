import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os


def loop_print_list(ingredient_list):
	html_ingredients = " "
	for ingredient in ingredient_list:
		html_ingredients += f'<li><input type="checkbox" name="ingredient"><label> {ingredient} </label> </li><br>'
	return(html_ingredients)
		



def send_email(user_email, user_name, recipe_links, recipe_ingredients):
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

	Hi,
	Here are your recipe links:
	Here are your shopping ingredients:
	1
	2"""

	html = f"""\


	<html>
	  <body>
	    <p> Hi, {user_name} <br>
	       Here are your recipe links:<br>
	       <a href="http://www.realpython.com">Recipe 1</a> <br>
	       Here are your shopping ingredients:
	      <form action="/action_page.php" method="get"> {loop_print_list(recipe_ingredients)}


		  </form> 
		     
	    </p>
	  </body>
	</html>
	"""
	# <input type="checkbox"> <label> Oranges </label><br>

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


send_email("Shira.Amrany@gmail.com", "Shira", "recipe_link", ["orange", "apple"])