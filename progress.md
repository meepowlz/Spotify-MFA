# Project Progress Documentation

***

## December 2021

+ GitHub repository created
+ Various authentication methods brainstormed for project purpose
+ SMS-based authentication chosen
+ Basic Flask webpage & HTML templates began

***

## Week of 01/03/2022

+ Stages of project outlined for the month of January
+ Twilio and Authy SMS (or PyOTP) decided on for use in the authentication process
+ Twilio account & phone number set up

***

## Week of 01/10/2022

+ Twilio used to send text messages successfully
+ Authentication page set up
+ Twilio used to send dynamic authentication codes
+ Twilio used to verify authentication codes
+ Unsuccessful authentication attempts prompts error message 

***

## Week of 01/17/2022

+ Began implementing Flask Sessions to store user login information
+ Decorators were attempted

***

## Week of 01/24/2022

+ Decorator successfully functioning for redirecting user if they are not logged in
+ Country code phone number dropdown added
+ Phone number verification implemented
+ Username/password/mobile number phone submission changed

***

## Week of 01/31/2022

***

# Method Procedure

### The scientific method procedure to be followed in the development, testing, and analysis of the MFA program

***

**Pre-Development**

- [x] Brainstorm & discuss the potential methods of authentication
- [x] Select a method of authentication for use
  + Selected: SMS Authentication
- [x] Create GitHub repository for the project
- [x] Determine resources needed for project
- [x] Outline project goals 
- [ ] Outline preliminary test cases to guide the project

**Development**

- [x] Set up a basic web server to host the project on
- [x] Set up Twilio & have it successfully send a message
- [x] Have Twilio send an authentication code
- [ ] Fix so other phone numbers can work? [Read here](https://www.twilio.com/blog/international-phone-number-input-html-javascript)
- [ ] Ensure the session gets reset on application load?
- [ ] Work on secret keys, cookies, and storing user data