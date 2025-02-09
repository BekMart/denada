# DE NADA

## Full Stack Project - Portfolio Project 4

This website has been designed and built to adevrtise a restuarant and take bookings for customers to come and visit, taking into consideration the date, time and number of guests to ensure that there is availability. Users are able to create, read, edit and cancel their own bookings from the database, if they are authenticated by successfully logging into their account.

This project is for educational purposes. The main aim is to build a functional and responsive Full Stack website using HTML, CSS, Python, Django, JavaScript and Postgres as a relational database.

## [Live Link to Program here.](https://denada-2b03b2e8c951.herokuapp.com/)

<h1 id="contents">Table of Contents</h1> 

- [UX](#UX)
    - [User-Centered Problem Statement](#user-centered-problem-statement)
    - [Website Owner Business Goals](#website-owner-goals)
    - [User Goals](#user-goals) 
    - [User Stories](#user-stories) 
    - [Structure](#structure) 
    - [Surface](#surface)
- [Features](#features) 
    - [Features Left To Implement](#features-to-implement) 
- [Technology Used](#technology-used) 
- [Testing](#testing) 
    - [Functionality Testing](#functionality) 
    - [Compatibility Testing](#compatibility)
    - [User Stories Testing](#story-testing)
    - [Issues Found](#issues) 
    - [Performance Testing](#performance)
    - [Code Validation](#validation) 
- [Deployment](#deployment)
- [Credits](#credits)

<h1 id="UX">UX</h1>

<h2 id="user-centered-problem-statement">User-Centered Problem Statement</h2>

*"As a student looking for an affordable and vibrant place to socialize, I struggle to find a venue that truly matches my personality and interests. Most places feel generic, uninspired, and lack cultural depth, offering nothing beyond the usual mainstream experience. The absence of good music, creative ambiance, and like-minded people makes social outings feel unappealing, leaving me frustrated and often choosing to stay home instead."*

*"I also care about my health and well-being and want to enjoy a space where I can connect with cultured, artistic individuals in a pleasant, welcoming environment that feels fresh and inspiring."*

<h2 id="website-owner-goals">Website Owner Business Goals</h2> 

- Develop an attractive, intuitive, and responsive website that provides a secure and seamless booking experience, encouraging users to reserve a table at the restaurant.
- Implement a relational database model to support an efficient and fully functional booking system.
- Provide authenticated users with access to exclusive content and personalized booking management.
- Enable users to create, view, modify, and cancel their reservations through an easy-to-use interface, ensuring flexibility and control over their bookings.

<h2 id="user-goals">User Goals</h2> 

### New Users 

- Discover a unique and culturally rich social space.
- Easily navigate the website and explore the available menus/events
- Create an account for personalised bookings.
- Make a booking with no hassle.

### Returning Users 

- Quickly log in to create or manage any bookings.
- Engage with the community and social scene.
- Access exclusive perks and loyalty rewards.

<h2 id="user-stories">User Stories</h2> 

### As a web designer... 

- I want to create an engaging and visually appealing website, so that users feel inspired to book a table and visit the restaurant.
- I want to implement a secure and user-friendly online booking system, so that users can easily make, manage, and cancel reservations without confusion.
- I want to develop a relational database model, so that all booking, user, and event data is efficiently stored and managed.
- I want to offer authenticated users access to exclusive content, so that they feel valued and engaged with the restaurant’s events and promotions.
- I want to track and manage user reservations and preferences, so that I can offer personalized recommendations and loyalty perks to returning customers.

### As a new user...

- I want to discover what makes this restaurant unique, so that I can decide if it matches my personality and interests.
- I want to easily browse the menu, upcoming events, and ambiance details, so that I can decide if this is a place I’d like to visit.
- I want to create an account quickly, so that I can save my preferences and easily book a table.
- I want to make a hassle-free booking, so that I can secure a table without unnecessary steps or confusion.

### As a returning customer...

- I want to log in quickly and access my bookings, so that I can modify or cancel them if necessary.
- I want to receive personalized recommendations for events or menu items, so that I feel more connected to the restaurant’s cultural scene.
- I want to engage with the community through exclusive events and discussions, so that I can meet like-minded people in a culturally rich environment.
- I want to earn rewards or loyalty perks for repeat visits, so that I feel valued and encouraged to keep coming back.

<h1 id="structure">Structure</h1>

### Process Flow Chart

![This is a flow chart demonstrating the structure of this website and the process to navigate around it.][flow-chart]

- When users enter the website, they are directed to the home page, which provides navigation to all other pages.
- A persistent header, present on every page, allows seamless navigation throughout the site. Logged-in users will see a logout option, while those who are not logged in will have access to the sign-up and login pages.
- Upon logging in or out, users receive confirmation feedback and are redirected to the home page.
- When a user creates or modifies a booking, they receive appropriate feedback and are redirected to the booking page, where their current bookings are listed.
- The website is designed to provide clear and consistent feedback, ensuring a smooth user experience and making navigation intuitive.

[flow-chart]: static/images/flow-chart.png