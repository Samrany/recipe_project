# Fresh&Whole

### What's it all about?
Fresh&Whole is a curated recipe site, featuring content from health-focused bloggers and chefs. Users can create a profile, search recipes by ingredient, save favorites, and choose how many recipes they want to cook, subsequently generating the corresponding shopping list of ingredients needed which is sent to that user's e-mail.  Users can also follow the link to the originator's website checking out the full-fledge recipe blog post. No longer do you have to put off trying those new recipes because you don’t have the ingredients – get your shopping list and get cooking.

### Deployment 
www.freshandwhole.com

### Tech

**Tech Stack**: PostgreSQL, SQLAlchemy, Python, Flask, Flask tests, Jinja, Javascript, JQuery,  Ajax, Bootstrap

**Apis**: Spoonacular,  Python SMTP library

### Features
The homepage allows users to create an account or login, both routes redirect to the homepage with unlocked features once a user is logged in.

<img src="https://user-images.githubusercontent.com/64447015/87886103-33a3af80-c9cf-11ea-9b47-2db43d3dc525.png" width = "500" />

Once logged in, a user can search by ingredient, save favorites, and go to their favorites page.

<img src= "https://user-images.githubusercontent.com/64447015/87886123-5e8e0380-c9cf-11ea-92d8-218944212cfb.png" width = "500" />

Each recipe card features the ingredients front and center for quick browsing:

<img src = "https://user-images.githubusercontent.com/64447015/87886176-b4fb4200-c9cf-11ea-8a82-b52d701466d6.png" width = "200" />

On a user's favorites page, he/she can choose to create a shopping list of ingredients from a certain number of random recipes. (version 2.0 will allow users to choose which recipes to export)

<img src = "https://user-images.githubusercontent.com/64447015/87886284-9184c700-c9d0-11ea-89ea-bb802d68da43.png" width = "500" />

A shopping list of unique ingredients is created using metric conversion in the background via Spoonacular API.

<img src = "https://user-images.githubusercontent.com/64447015/87886391-53d46e00-c9d1-11ea-995c-416f6d8da84a.png" width = "400" />

This shopping list is also sent to his/her e-mail.

<img src = "https://user-images.githubusercontent.com/64447015/87886308-bc6f1b00-c9d0-11ea-84c8-a4c888e58f30.png" width = "400" />

If a user wants to find out more about a recipe card, he/she can click on it to get more information and follow the link to the original blogger's website.

<img src = "https://user-images.githubusercontent.com/64447015/87886329-df99ca80-c9d0-11ea-89ec-41dfd9f413e2.png" width = "500" />

### Installation

Install PostgresQL and Python
Clone or fork this repo
Create and activate a virtual environment inside your directory:
```sh
$ Virtualenv env
$ Source env/bin/activate
```

Install dependencies
```sh
pip install -r requirements.txt
```
Create a gmail account from which to send emails
Change sender email in send_email.py file to your new gmail account.

Save your API keys in a file called "secrets.sh" using this format:
```sh
export EMPASSWORD="YOUR PASSWORD HERE”
export SPOONACULAR="YOUR API KEY HERE"
```

Source your keys from your secrets.sh file into your virtual environment
```sh
source secrets.sh
```
Set up the database by running the seed_database.py file
Run the app ("server.py")

You can now navigate to ‘localhost:5000/’ to access Fresh&Whole!

### About Me
This was my first full-stack app but the seeds for my interest in coding were planted long ago. I originally studied business in the hospitality industry at Cornell  where I TA’d Information Systems and thoroughly enjoyed the few cs related classes in my curriculum. I even chose to take VBA as an elective (which I unfortunately forgot soon thereafter).

I started my career as an analyst and progressed in various business-centered roles over the past 10 years. In my last role, I worked cross-collaboratively to solve various business problems and designed, built, and implemented numerous (excel or process related) tools to help the business make more informed decisions and scale. I knew there was further I could take things but didn’t have the technical knowledge, skills, or resources to do so. I had explored the idea of SWE for the last few years and decide to make the jump and join Hackbright’s SWE program when Covid opened up a window of opportunity. I’ve been enjoying the journey since. After all, growing up with an Engineer father, I was programmed to enjoy logic and problem-solving.
