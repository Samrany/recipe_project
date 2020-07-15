# Fresh&Whole

### What's it all about?
Fresh&Whole is a curated recipe site, featuring content from health-focused bloggers and chefs. Users can create a profile, search recipes by ingredient, save favorites, and choose how many recipes they want to cook, subsequently generating the corresponding shopping list of ingredients needed which is sent to that user's e-mail.  Users can also follow the link to the originator's website checking out the full-fledge recipe blog post. No longer do you have to put off trying those new recipes because you don’t have the ingredients – get your shopping list and get cooking.

### Features

The homepage allows users to create an account or login, both routes redirect to the homepage with unlocked features once a user is logged in.

![image](https://user-images.githubusercontent.com/64447015/87495941-66345d80-c607-11ea-81d1-13a6a62e976d.png)

![image](https://user-images.githubusercontent.com/64447015/87496188-f1155800-c607-11ea-8e13-24503e58f7b7.png)

Once logged in, a user can search by ingredient, save favorites, and go to their favorites page.
![image](https://user-images.githubusercontent.com/64447015/87496262-11451700-c608-11ea-942a-1f57ad1275a3.png)

On a user's favorites page, he/she can choose to create a shopping list of ingredients from a certain number of random recipes. (version 2.0 will allow users to choose which recipes to export)

![image](https://user-images.githubusercontent.com/64447015/87496555-a9db9700-c608-11ea-9014-a2527eb8861f.png)

This shopping list is also sent to his/her e-mail.

![image](https://user-images.githubusercontent.com/64447015/87496688-f0c98c80-c608-11ea-98a2-2a624d933e66.png)

### About Me
This was my first full-stack app but the seeds for my interest in coding were planted long ago. I originally studied business in the hospitality industry at Cornell University where I TA’d Information Systems and thoroughly enjoyed the few cs related classes in my curriculum. I even chose to take VBA as an elective (which I unfortunately forgot soon thereafter).

I started my career as an analyst and progressed in various business-centered roles over the past 10 years. In my last role, I worked cross-collaboratively to solve various business problems and designed, built, and implemented numerous (excel or process related) tools to help the business make more informed decisions and scale. I knew there was further I could take things but didn’t have the technical knowledge, skills, or resources to do so. I had explored the idea of SWE for the last few years and decide to make the jump and join Hackbright’s SWE program when Covid opened up a window of opportunity. I’ve been enjoying the journey since. After all, growing up with an Engineer father, I was programmed to enjoy logic and problem-solving.

### Deployment 
www.freshandwhole.com

### Tech

**Tech Stack**: PostgreSQL, SQLAlchemy, Python, Flask, Flask tests, Jinja, Javascript, JQuery,  Ajax, Bootstrap

**Apis**: Spoonacular,  Python SMTP library

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
