# Introduction to APIs

**I made changes to the notes from the github link below to make my own notes**

API beginner course by FreeCodeCamp: [Youtube Video](https://www.youtube.com/watch?v=GZvSYJDk-us)
GitHub [link](https://github.com/craigsdennis/intro-to-apis-course).

Tip: For signups, you can have infinite mail id’s by using name+site@gmail.com

## Unit 1 - What is an API

In this unit we'll define what an API(Application Programming Interface) is and why you should use them.

### Video 1 - Welcome

👋 Hello and welcome to the course and your notes! Make sure you check this area out often!

#### 👀 - Beginner content

* [freeCodeCamp.org](https://www.freecodecamp.org/) is a great place to get started and I recommend jumping [right in](https://www.freecodecamp.org/learn/responsive-web-design/basic-html-and-html5/say-hello-to-html-elements).
* [freeCodeCamp on YouTube](https://www.youtube.com/freecodecamp) provides a wonderful collection of beginning programming courses. I recommend the [🎥 JavaScript](https://www.youtube.com/watch?v=PkZNo7MFNFg) and [🎥 Python](https://www.youtube.com/watch?v=rfscVS0vtbw) tutorials.

#### 📚 - Designing API Content

* [ProgrammableWeb 101 - What exactly is an API](https://www.youtube.com/watch?v=cpRcK4GS068&list=PLcgRuP1JhcBP8Kh0MC53GH_pxqfOhTVLa)
* [moseif - API Guide](https://www.moesif.com/blog/api-guide/)

### Video 2 - Defining Interface

**Interface**
Interface is the thing that you interact with and control the way a device works. The process happening inside a device is abstracted by the interface. They are also used in GUIs. Like a play button in a music player. Interfaces abstract the implementation of the process. 

#### 📚 - Learn more

##### Media Player APIs

Don't worry about understanding it, just appreciate their complexity

* [Android MediaPlayer API documentation](https://developer.android.com/reference/android/media/MediaPlayer)
* [iOS Media Player API documentation](https://developer.apple.com/documentation/mediaplayer)
* [Web Audio API](https://developer.mozilla.org/en-US/docs/Web/API/Web_Audio_API)

### Video 3 - Defining API

In the context of APIs, the word Application refers to any software with a distinct function. Interface can be thought of as a contract of service between two applications. This contract defines how the two communicate with each other using requests and responses.

Like the UI is made for the user, the API is made for the application programmer.

#### 📚 - Learn more

* [mdn - Web APIs](https://developer.mozilla.org/en-US/docs/Web/API)
* [Google vs. Oracle on the rights to the Java API](https://www.theverge.com/2019/11/15/20946398/oracle-google-java-copyright-lawsuit-trial-supreme-court-request)

### Video 4 - Remote APIs

Using API’s gives us many advantages. One of them is computational power. Doing some of the tasks a remote API does, like, searching for a song playing in real time, using google translate to translate something in real time using a camera. To do these things, you will need to have a database of all the songs or words on your device. But, with a remote API, you don’t need to.

* [Wikipedia - SOAP](https://en.wikipedia.org/wiki/SOAP)
* [Wikipedia - Remote Procedure Call (RPC)](https://en.wikipedia.org/wiki/Remote_procedure_call)
* [SOAP and REST at Odds](https://thehistoryoftheweb.com/soap-rest-odds/)
* [SOAP vs. REST](https://stackify.com/soap-vs-rest/)
* [REST vs. RPC](https://cloud.google.com/blog/products/application-development/rest-vs-rpc-what-problems-are-you-trying-to-solve-with-your-apis)

### Video 5 - How the web works

URL – Universal Resource Locator, URI is a super set of URLs, I in URI is Identifier. 

When clicking a link on your browser, the browser which acts as a client to the server, will send a HTTP URI GET request to the server, for this request, the server will send a response, whose body will be in HTTP(Hyper Text Transfer Protocol).

Resource in URL can be used to describe anything. In an example of a bookstore website, a book shows information like its author, which is also a resource. If you click on the author, it will show a collection of books by that author. You may also see a group of reviews from fans, which is also a resource. If you click on a fan, you will see a collection of books and authors they like.

* [Wikipedia - HTTP](https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol)
* [mdn - How the web works](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/How_the_Web_works)
* [Space Jam Website](http://www.spacejam.com)

### Video 6 - RESTful API Constraint Scavenger Hunt

* [Wikipedia - Representational State Transfer](https://en.wikipedia.org/wiki/Representational_state_transfer)

## Unit 2 - Exploring APIs

REST – Representational State Transfer. 
This type of remote API is one of the many used but, it is the most used one. This course focuses on REST API’s. 
For an API to be RESTful, these constraints should be followed:
1. Client-Server Architecture
2. Statelessness
3. Layered System
4. Cacheability
5. Uniform Design
6. Code on Demand

An API's definition is simply a contract which defines how two applications should communicate. This communication happens between client and server, so it is **client-server** communication.

**Stateless** means it doesn’t remember anything happening in a session, so if you want to maintain state like login in a session, you must do it in every session individually using headers.

A **layered system** is when an API calls another API. This is done to make the API more efficient. Like, if you want to get the weather of a city, you can use an API which calls another API to get the weather of that city.

A RESTful API should support **caching**. If you have any file which is consuming more storage, you should be careful to conserve resources by not calling that file again and again. So, you can just store the file and check if it is modified. If it is, we should call for that file, if it isn’t, we can just call the stored file.

(The information on uniform design is taken from [here](https://medium.com/extend/what-is-rest-a-simple-explanation-for-beginners-part-2-rest-constraints-129a4b69a582).)
The result of the **uniform design** is that requests from different clients look the same. Different clients means chrome browser, android app, linux server, python script or anything else.
Uniform design has four more constraints in it. They are:
1. The request to the server has to include resource identifier.
2. The response the server returns include enough information so the client can modify the resource.
3. Each request to API has all info server need to perform the request, and each response server returns has all info client needs to understand it.
4. Something about Hypermedia as the engine of application state, which I quite didn't understand. You can watch a [video](https://www.youtube.com/watch?v=6UXc71O7htc) on it here. 

The **code on demand** constraint is optional. An API can be RESTful even without this. The client can request code from the server, and then the response from the server will contain some code, usually in the form of a script, when the respnse is in HTML. The client can then execute that code.

The body of the reply you get when you send a http request is in JSON, which is JavaScript Object Notation. It provides a way to structure and nest your data. Every programming language will have ways to turn a JSON string into a native object. You can also specify a Content Type in your request.

HTTP Verbs used in REST APIs:			CRUD
GET						                       Read
POST						                      Create
PUT						                       Update
PATCH                           Update
DELETE						                    Delete

### Video 1 - Exploring an API online

This course uses Spotify and Twilio APIs. Using a Twilio API, you can send a text message from a number to your registered phone number (one of many things it can do).

* [Spotify for Developers](https://developer.spotify.com/)
* [Spotify - Search API {BETA}](https://developer.spotify.com/documentation/web-api/reference-beta/#category-search)
* [Lizzo's Spotify Page](https://open.spotify.com/artist/56oDRnqbIiwx4mymNEv7dS)
* Lizzo's Spotify ID: `56oDRnqbIiwx4mymNEv7dS`

#### 👀 - Explore

ProgrammableWeb provides [a categorized directory of APIs](https://www.programmableweb.com/category-api). API List provides [categories and a powerful search feature](https://apilist.fun/).

### Video 2 - Using an API from the command line

* [Twilio](https://www.twilio.com/referral/d4X15O)
* [Twilio Console](https://twilio.com/console?utm_source=gh-link&utm_medium=referral&utm_campaign=intro-to-apis)
* [SMS Getting Started](https://www.twilio.com/console/sms/getting-started/build?utm_source=gh-link&utm_medium=referral&utm_campaign=intro-to-apis)
* Check out the [jq tutorial](https://stedolan.github.io/jq/tutorial/) for parsing JSON on the command line

#### cURL

##### Mac OS

###### Using Homebrew

```bash
brew install curl
```

###### Download

[⬇️ - Download cURL for MacOSX](https://curl.haxx.se/dlwiz/?type=bin&os=Mac+OS+X)

##### Windows

[⬇️ - Download cURL for Windows](https://curl.haxx.se/windows/)

NOTE: If you are running PowerShell, delete the `curl` alias for `Invoke-WebRequest` by adding the following command to your profile (`C:\Users\<username>\Documents\WindowsPowerShell\Microsoft.PowerShell_profile.ps1)`:

```bash
Remove-Item alias:curl
```

#### 📚 - Learn More

* [cURL manpage](https://curl.haxx.se/docs/manpage.html)
* [Wikipedia - POST (HTTP)](https://en.wikipedia.org/wiki/POST_(HTTP)) (For info on `form-urlencoded` search for "Use for submitting web forms)

### Video 3 - Using Postman to explore APIs

This course is also using Postman, which will also be useful for the APISEC course also. 

Now, you can create a folder to save your API requests, you should get the request URL from the CURL, or from the API. Then for the authentication part, create variables for the username and password and use them to avoid sharing sensitive information with your team.

⬇️ - Download [Postman](https://postman.com/downloads)

The Twilio Messages API URL is:

```bash
https://api.twilio.com/2010-04-01/Accounts/<Your Account SID Here>/Messages.json
```

Make sure to replace that `SID` with your Account SID which can be found in the [Twilio console](https://twilio.com/console)

### Video 4 - Please please Mr. Postman

⬇️ - Many wonderful API Collections can be downloaded for exploration in the [Postman API Network](https://explore.postman.com/)

#### 📚 - Learn more

* [How Collaboration Works in Postman](https://www.getpostman.com/how-api-collaboration-works)
* [Official Postman Tutorials](https://www.getpostman.com/resources/videos-tutorials/)

The next part is about using JavaScript and Python to write a code which can print the latest message sent or send a new message. This is done by downloading helper libraries of an API in your preferred language. These helper libraries are also called as SDKs(Software Development Kit).

### Video 5 - Using Helper Libraries (JavaScript)


* [Install Node.js](https://nodejs.org/en/download/)
* [Install Python 3](https://www.python.org/downloads/)
* [Install Visual Studio Code](https://code.visualstudio.com/download)
  * [macOS](https://code.visualstudio.com/docs/setup/mac)
  * [Windows](https://code.visualstudio.com/docs/setup/windows)
  * [Linux](https://code.visualstudio.com/docs/setup/linux)

To use the [Twilio Node Helper Library](https://www.twilio.com/docs/libraries/node#installation)

```bash
npm install twilio
```

#### 📚 - Learn More

* [Wikipedia - Boilerplate code](https://en.wikipedia.org/wiki/Boilerplate_code)

### Video 6 - Using Helper Libraries (Python)

* [Install Python 3](https://www.python.org/downloads/)

To use the [Twilio Python Helper Library](https://www.twilio.com/docs/libraries/python)

```bash
pip install twilio
```

## Unit 3 - Using APIs

### Video 1 - Introducing the project

* [Glitch](https://glitch.com)

#### 📚 - Learn more

* [Slack API](https://api.slack.com/)
* [Sportsball APIs](https://rapidapi.com/blog/best-sports-apis-ranked/)
* [Philips Hue API](https://developers.meethue.com/)
* [🎥 Furby Hacking 101 w/ Chloe Condon](https://www.youtube.com/watch?v=dWpqoMObX54)

### Video 2 - Flask app

⚠️ Several students have reported that cloning sets up a default Glitch application. If this happens to you, in the Glitch app that is created choose "Tools >> Extras >> Git Import and Export >> Import from GitHub" when prompted enter "craigsdennis/intro-to-apis-node" or "craigsdennis/intro-to-apis-flask"

[Complimentr Flask GitHub repository](https://github.com/craigsdennis/intro-to-apis-flask) is located at `https://github.com/craigsdennis/intro-to-apis-flask.git`

* [Twilio docs - Create a Message with Python](https://www.twilio.com/docs/sms/api/message-resource?code-sample=code-create-a-message&code-language=Python&utm_source=gh-link&utm_medium=referral&utm_campaign=intro-to-apis)
* [Twilio docs - List all Messages with Python](https://www.twilio.com/docs/sms/api/message-resource?utm_source=gh-link&utm_medium=referral&utm_campaign=intro-to-apis&code-sample=code-read-list-all-messages&code-language=Python)

#### 📚 - Learn more

* [Flask documentation](https://flask.palletsprojects.com/)
* [Environment Variables](https://www.twilio.com/docs/usage/secure-credentials)

### Video 3 - Dealing with API Limits

#### 📚 - Learn more

* [Nordic APIs - Everything You Need To Know About API Rate Limiting](https://nordicapis.com/everything-you-need-to-know-about-api-rate-limiting/)

### Video 4 - JavaScript Single Page Application

⚠️ Several students have reported that cloning sets up a default Glitch application. If this happens to you, in the Glitch app that is created choose "Tools >> Extras >> Git Import and Export >> Import from GitHub" when prompted enter "craigsdennis/intro-to-apis-node" or "craigsdennis/intro-to-apis-flask"

[Complimentr Node.js GitHub repository](https://github.com/craigsdennis/intro-to-apis-node) is located at `https://github.com/craigsdennis/intro-to-apis-node.git`

* [Twilio docs - Create a Message with Node.js](https://www.twilio.com/docs/sms/api/message-resource?code-sample=code-create-a-message&code-language=Node.js&utm_source=gh-link&utm_medium=referral&utm_campaign=intro-to-apis)
* [Twilio docs - List all Messages with Node.js](https://www.twilio.com/docs/sms/api/message-resource?utm_source=gh-link&utm_medium=referral&utm_campaign=intro-to-apis&code-sample=code-read-list-all-messages&code-language=Node.js)

#### 📚 - Learn more

* [mdn - Async / Await](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Asynchronous/Async_await)
* [Vue.js - Getting Started](https://vuejs.org/v2/guide/)
* [Node.js - Getting Started](https://nodejs.org/en/docs/guides/getting-started-guide/)

### Video 5 - Moar JavaScript and Recap

* [Wikipedia - REST Architectural Constraints](https://en.wikipedia.org/wiki/Representational_state_transfer#Architectural_constraints)

### Video 6 - Review

I built a little Twilio application using [Studio](https://www.twilio.com/docs/studio?utm_source=gh-link&utm_medium=referral&utm_campaign=intro-to-apis) and some APIs to gather your feedback.

Please text `FEEDBACK` to me at [(503) 461-5537](tel:+15034615537) and let me know what you thought about this course! (You can also call if that's your jam)

👋 Thanks for hanging out! 🙏 Keep me updated on your journey 💪🚀!

[@craigsdennis](https://twitter.com/craigsdennis)

PS. If you want to keep on learning for free, I can't recommend [the video game TwilioQuest 🎮](https://twilio.com/quest?utm_source=gh-link&utm_medium=referral&utm_campaign=intro-to-apis) enough.

#### 📚 - Learn more

* [📹 Understanding Webhooks on freeCodeCamp](https://www.youtube.com/watch?v=41NOoEz3Tzc) is a course I made about reverse APIs, APIs that call you instead of you calling them. Come hang out some more!
