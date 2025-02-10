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

This website has been designed and developed using built-in Django features such as template language tags, Django Allauth for authentication, and Crispy Forms for enhanced form styling. Additionally, CSS styling and media queries have been implemented to ensure responsiveness for devices with a minimum width of 320px.

### Process Flow Chart

The Process Flow Chart visually represents the structure of the website and the possible user navigation paths, helping to illustrate the user journey and overall functionality.

![This is a flow chart demonstrating the structure of this website and the process to navigate around it.][flow-chart]

- When users enter the website, they are directed to the home page, which provides navigation to all other pages.
- A persistent header, present on every page, allows seamless navigation throughout the site. Logged-in users will see a logout option, while those who are not logged in will have access to the sign-up and login pages.
- Upon logging in or out, users receive confirmation feedback and are redirected to the home page.
- When a user creates or modifies a booking, they receive appropriate feedback and are redirected to the booking page, where their current bookings are listed.
- The website is designed to provide clear and consistent feedback, ensuring a smooth user experience and making navigation intuitive.

### ERD

The ERD below illustrates the different models used within the database and the relationships between them.

![This is the ERD which was created to show the database structure and the relationships held between the different models][erd]

- In hindsight, I believe the design could have been more concise and efficient. As this was my first time creating a database model, I learned a lot throughout the process. I had to add models and modify fields along the way, which led to challenges when populating existing fields. This experience underscored the importance of thorough planning, as having a well-structured design from the outset would have made the process much smoother.
- Looking back, I could have structured the models more effectively by linking the main pages to the restaurant model and attaching subsections to the relevant pages, rather than connecting everything directly to the restaurant model.
- Additionally, I now realize that placing the address and contact details within the main restaurant model was not the best approach. Instead, these details would have been more appropriately stored in separate models where they are specific and relevant to their context.

### Wireframes

Below are the original wireframe images created during the design thinking process for this website. While the final outcome has evolved, the core page structure remains intact. Creating wireframes was a valuable tool, providing a foundation to build upon and refine as development progressed.

![These are basic images outlining the initial website structure designed during the planning phase.][wireframes]

- The pages follow a consistent structure, implemented using a base.html template. This template includes common elements such as the logo, navigation bar, general styling, and footer.
- The main **landing page** content has remained the same, however, the layout has been adjusted during development:
    - On mobile devices, multiple images are used on the home page to engage users and enhance aesthetics.
    - On tablets and larger screens, images transition from a vertical to a horizontal layout, which I believe works well visually.
- A main **menu page** was introduced to provide an overview of the available menus, with links to separate food and drink menus and a booking page.
    - The food and drink menus consist of item lists, including prices and calorie details, accompanied by representative images.
- I initially designed an **events page**, which I would have liked to implement, but it was not prioritized to ensure the website met its primary goal—encouraging users to visit the restaurant. However, I plan to add this feature in the future as it would add value to the site.
- The **booking page** remains largely the same; however, I have added a section at the bottom that displays the user's current bookings, allowing them to edit or delete bookings with the click of a button.
- The **contact page** hosts the address and an interactive map feature at the top of the page and when in a tyablet or larger device, the remaining details are listed below in a horizontal line using flex, instead of having the stagered appearance that it displayed within the wireframe modals. The order has been manipulated for aesthetics when on larger devices due to the size and importance of the sections involved.
    - I wanted to include a contact page feature allowing users to leave comments or send messages to the restaurant. However, this was set aside in favor of implementing more essential features first.

<h1 id="surface">Surface</h1>

### Colours

The following colors have been used throughout the website to ensure consistency and a professional appearance. They comply with contrast recommendations for accessibility.

#### Header

- Background color: `#FCF4D9` (*Vanilla Beige*)
- Font and Navigation links: `#0B5509` (*Deep Forest Green*)

#### Main Body

- Background color: `#FCF4D9` (*Vanilla Beige*)
- Headings: `#0B5509` (*Deep Forest Green*)
- Text: `#5E625E` (*Soft Graphite*)
- Links: `#C64A03` (*Deep Rust*)
- Inside borders: `#F9F6EE` (*Warm Ivory*)

#### Footer

- Background color: `#0B5509` (*Deep Forest Green*)
- Font and Navigation links: `#FCF4D9` (*Vanilla Beige*)

These colors provide high contrast for readability while maintaining a neutral, earthy palette. The light background creates a warm, inviting, and natural aesthetic, while the deep green, rust, and graphite tones reinforce the restaurant’s eco-friendly ethos. 

To enhance visibility and clarity, lighter borders are used around forms and buttons, adding contrast and contributing to a refined, accessible user experience.

### Fonts

A combination of carefully selected fonts has been used throughout the website to create visual contrast, readability, and a refined aesthetic. These fonts contribute to the website's professional yet inviting feel.

#### Headings & Links

- Primary Font: `'Vidaloka'` (Serif)  
- Fallback Font: `'Serif'`  
- This elegant serif font is used for headings, links, and the contact section, providing a classic and sophisticated feel. Its high contrast and sharp details make it ideal for drawing attention to key elements.  
- These fonts have been sourced from Google Fonts and imported into `style.css`, which is linked to the `base.html` template to ensure consistency across all pages.

#### Main Text

- Primary Font: `'Helvetica Neue'` (Sans-serif)  
- A clean, modern sans-serif font used for large areas of text, including the home page and main menu page. Its neutral and legible design enhances readability, making long passages of text easy to consume.  
- This font has been implemented via the Django Summernote admin panel to maintain consistency in content management.

#### Buttons

- The buttons inherit their styling from Crispy Forms built-in font, ensuring compatibility with form elements and maintaining a clean, user-friendly appearance.

The pairing of Vidaloka for headings and Helvetica Neue for body text creates a visually appealing contrast that improves readability and user experience. The serif font conveys elegance and tradition, while the sans-serif font brings modernity and clarity, aligning with the website’s professional yet warm and welcoming theme.  

### Images

All images used on the website were generated using the ChatGPT AI image tool. These images maintain a consistent style and size, ensuring a cohesive visual experience across the site.  

To enhance responsiveness, media queries have been implemented to dynamically adjust the layout of images across different screen sizes, improving the overall user experience on various devices.

Images are stored using Cloudinary, a third-party media hosting platform, for efficient loading times and scalability. Additionally, all images are backed up locally within the static files in the IDE. This redundancy ensures that if Cloudinary becomes unavailable, the images can still be retrieved and displayed from local storage.
 
Every image includes descriptive alt text, improving accessibility for visually impaired users and enhancing SEO.


[flow-chart]: static/images/flow-chart.png
[erd]: static/images/erd.png
[wireframes]: static/images/wireframes.png
