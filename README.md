# Spotify-MFA
A conceptual program for implementing Multi-Factor Authentication into Spotify

Uses SMS code verification in conjunction with standard username/password procedures

***

**Feature log**

+ Allows for registration of users locally
+ Unique username and mobile number constraints
+ Mobile number verification system used to prevent fake numbers
+ Country code dropdown for ease of use
+ Password hashing to secure data
+ Fetch API and JSON data used to more securely transmit data
+ 6-Digit code verification used to authenticate users
+ Powered by Twilio, Flask, and SQLite3

**Setup Notes**

+ Install packages from 'requirements.txt' file
+ Set up Twilio Account SID & Auth Token [Environment Variables](https://www.twilio.com/blog/2017/01/how-to-set-environment-variables.html)
