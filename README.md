# Spotify-MFA
A conceptual program for implementing 2-Factor Authentication into Spotify
Use this to explain the program when it is finalized
A chronological log of the stages of progress can be viewed in progress.md

***

**Feature log**

+ Explain how the program works/ what it has

**Notes**

+ Any disclaimers go here
+ Set up Twilio Account SID & Auth Token [Environment Variables](https://www.twilio.com/blog/2017/01/how-to-set-environment-variables.html)

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
- [ ] Implement registration system
- [ ] Have a code send to the number the user registered with on log in
- [ ] Separate registration/login/authentication page into three routes?
- [ ] Come up with a name for the project (Authify? :o)

+ Setup tables when database is loaded