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

[Back to Contents](#contents)

<h1 id="features">Features</h1> 

This program consists of 11 pages, each with distinct features and accessible through various routes.

- 4 main pages are always accessible via the fixed navigation bar, ensuring easy access from anywhere on the site.
- Drink and food menu pages are accessible exclusively via the main menu page.
- A booking management page allows users to edit their reservations, only accessible via the main booking page.
- 3 authentication pages enable users to create an account, log in, and log out.
- A 404 error page ensures users receive a helpful message when they enter an incorrect web address.

The program consists of the following features: 

### Template Features: 

- Header
    - The header remains fixed at the top of every page for easy navigation.
    - The restaurant name is bold and serves as a clickable link directing users to the homepage.
    - The header contains a navigation menu providing access to the site's main pages.
    ![Screenshot of the header when the user is logged out.][header-logged-out-screenshot]
- Responsive Navigation
    - On smaller devices (≤992px), the menu transforms into a slide-out navigation bar activated by a toggle menu icon, using Materialize CSS.
    - On larger screens, the navigation menu is displayed horizontally on the right side of the header.
    - A divider separates main navigation links from authentication links, adjusting based on screen size.
- User Authentication Visibility
    - If a user is logged in, only the log-out option is displayed.
    - If a user is not logged in, sign-up and log-in links are visible in the navigation menu.
- Hero Image
    - A high-definition hero image featuring a barista in the background and a coffee being made in the foreground is displayed at the top of each page, just below the header. This image provides visual consistency across the site while creating a clear separation between the header and the page content.
    - To ensure the image remains clear and visually appealing on all devices, media queries adjust its height and positioning dynamically, keeping the focus centered for an optimal viewing experience.
    ![Screenshot of the hero image of a barista in the background and a coffee being prepared at the machine in the foreground.][hero-screenshot]
- Login Status Message
    - When a user is logged in, a personalized greeting appears on the right side, below the hero image, displaying:
    "Hello, <username>"
    - If a user is not logged in, a message informs them:
    "You are not currently logged in."
    - This feature provides a clear and user-friendly acknowledgment of the user's authentication status.
    ![Screenshot of the screen display when a user has logged in. It displays feedback of successful action and a personalised message including the user's username.][authenticated-home-screenshot]
- Footer
    - The footer provides key business information and maintains a consistent yet inverted color scheme that complements the overall design. It includes:
        - Opening hours (left)
        - Copyright message (top right)
        - Social media icons (center bottom, evenly spaced)
    - Designed with responsive CSS styling, the footer maintains a clean, structured layout that is visually balanced, accessible across all devices, and ensures easy access to essential details while preserving a professional appearance.
    ![Screenshot of the footer.][footer-screenshot]


### Landing Page Features:

- Welcome Heading
    - Upon entering the website, users are greeted with a bold, centered welcome message on the landing page. This feature enhances user experience and engagement by:
        - Creating a Strong First Impression – The large, attention-grabbing heading immediately welcomes visitors and establishes the website’s tone.
        - Providing Clarity & Guidance – It helps orient users, confirming they’ve arrived at the right place.
        - Reinforcing Branding & Personality – The message reflects the brand’s voice and contributes to a warm, inviting atmosphere.
        - Enhancing Accessibility & Readability – The prominent, high-contrast text ensures the message is easy to read on all devices.
    - This simple yet effective design choice improves user engagement, navigation, and overall experience.
    ![Screenshot of the welcome message that appears on the landing page to welcome the user.][welcome-screenshot]
- About Us
    - The 'About Us' section introduces users to the restaurant owners and provides a brief overview of the café’s ethos.
        - This café is a community-focused space, welcoming both students and locals in an inclusive environment. They promote health-conscious living and actively support local artists, offering a space for them to perform and showcase their work.
        - The section also includes images of the owners, the café’s storefront, and their pup, helping visitors get a sense of the people behind the café and its overall vibe. This personal touch allows potential customers to decide whether the café aligns with their values and interests.
    ![Screenshot of the About Us section on the home page with images.][about-screenshot]
- Our Produce:
    - The Produce section highlights the café’s commitment to supporting local businesses by sourcing all ingredients locally. 
        - It reinforces their focus on fresh, organic, and healthy produce, while also catering to a variety of dietary requirements.
        - The café emphasizes the importance of nutritious food for students, linking it to brain nourishment and overall well-being, while maintaining competitive pricing to remain accessible.
        - Images of bakers, butchers, and a fresh vegetable stall add a personalized touch, showcasing the café’s ethical values and dedication to community support.
    ![Screenshot of the Produce section on the home page with images.][produce-screenshot]
- Visit us:
    - The final section of the Home Page highlights the events and activities available at the café, reinforcing its inclusive and welcoming atmosphere.
        - Visitors can enjoy a variety of social and creative experiences, including jam nights, board games, poetry nights, film screenings and more.
        - The café is a pet-friendly space, ensuring a relaxed and inviting environment for all. Student discounts are also available, making it an affordable and appealing spot for young people.
        - Images of individuals reading, groups playing board games, and live music performances help to sell the experience, giving users a visual glimpse of the vibrant and engaging atmosphere they can expect when visiting.
    ![Screenshot of the visit section on the hme page with images.][visit-screenshot]


### Menu Features:

- Menu Introdcution
    - This section provides general information about the café’s menus, including:
        - Food availability and serving times.
        - Where to access the individual menus.
        - A reminder to check regularly for updates, as the menus frequently change.
        - A prompt for customers to inform the café of any dietary requirements, allowing the team to adjust recipes accordingly.
    - This ensures that visitors are well-informed about their dining options while reinforcing the café’s flexibility and commitment to accommodating all dietary needs.
    ![Screenshot of the menu information displayed at the top of the menu page.][menu-intro-screenshot]
- Menu Links
    - Links to the Food and Drink menus are prominently displayed with CSS styling to ensure they stand out from the rest of the page.
    - To enhance usability and accessibility, responsive design has been implemented, allowing the links to adjust dynamically based on screen size. This ensures they are well-positioned and efficiently utilize available space across all devices.
    ![Screenshot of the links to the individual Food and Drink menus.][menu-links-screenshot]
- Menu Image
    - This page features an image of a mature couple enjoying breakfast at the café, smiling and sharing a pleasent moment together. The image serves to sell the experience by showcasing:
        - The stylish interior of the café
        - The healthy, high-quality food served
        - That the café is welcoming to all ages, not just students, despite much of the content being geared toward them
    - This visual representation helps reinforce the café’s inclusive and inviting atmosphere, appealing to a broader audience.
    ![Screenshot of the image located on the menu page.][menu-image-screenshot]
- Small Print
    - Beneath the image, a small print section provides important but non-prominent details, including:
        - Calorie information is approximate
        - Semi-skimmed milk is used unless otherwise specified
        - Plant-based milk alternatives are available
        - Customers are encouraged to inform staff of any dietary requirements
    - This space is reserved for useful but non-essential details, ensuring the information is available without distracting from the main content.
    ![Screenshot of the small print on the menuu page.][small-print-screenshot]
- Booking Page Link
    - At the bottom of the page, a bold, uppercase "BOOK A TABLE" link is prominently displayed, styled consistently with the menu links above.
    - This serves as a clear call to action, encouraging users to book a table after exploring the food and drink options, making it easier for them to plan their visit.
    ![Screenshot of the link to the booking page, located on the menu page.][booking-link-screenshot]


### Food/Drink menu Features:

- Menu Contents
    - Items are categorized by type, with each section headed by a bold title. Menu entries are displayed in the following format:
        - Food/drink item name
        - Estimated calories (in small font, enclosed in brackets)
        - Price (aligned to the right, with spacing for clarity)
        - Items are listed in ascending order of price for an intuitive browsing experience.
        - Each category includes a circular image representing the food or drink type, displayed below or alongside the menu list, depending on screen size.
- Responsive Design
    - The Food and Drink menus share a consistent CSS-styled layout for a cohesive look. They are fully responsive, adapting to different screen sizes:
        - On smaller devices, menu items are aligned vertically for better readability.
        - On larger screens, menu items are enclosed within a border, with images positioned to the right of the list.
    - Media queries ensure consistent spacing between content and the border, maintaining a balanced layout without the menu taking up excessive space.
    ![Screenshot of the Food menu on a large device with a border and the image alongside the food item lists.][food-menu-screenshot]


### Booking page Features:

- Unauthenticated Users 
    - If a user navigates to the Booking Page without being logged in, a notification box appears with clear instructions to either log in or create an account before booking a table.
    - The "Log In" and "Create an Account" links are highlighted in a different color to stand out as clickable actions.
    - This page is intentionally minimalistic, ensuring users are not distracted and are guided smoothly through the authentication process to complete their booking.
    - The simple design serves a business goal, encouraging users to sign in and proceed with their reservation efficiently.
    ![Screenshot of the page which is displayed when a user navigates to the booking page wihout being logged in.][unauthenticated-book-screenshot]
- Booking form:
    - If an authenticated user accesses the Booking Page, they are presented with a personalized greeting that addresses them by their username, instructing them to complete the booking form.
    - The form was built using Crispy Forms, providing a solid foundation for its structure and functionality. To ensure visual consistency across the website, custom CSS styling was applied to:
        - The form itself, with the same border and backgrund colour as other sections within the website.
        - Input field labels, including font and color.
        - The submit button.
    - The form includes the following fields:
        - Party Size*
            - Users must enter a whole number between 1 and 10.
            - If an invalid input is entered, they receive real-time feedback prompting them to enter a valid number.
        - Date*
            - The field initially displays the date format as a guide.
            - Users can manually enter a date or click the calendar icon to select a date from the calendar picker.
            - Feedback is provided if the date format is incorrect or if the selected date is in the past.
        - Time*
            - A dropdown menu allows users to select a time in 30-minute increments during the café’s opening hours.
            - If a user attempts to book a time that has already passed, they receive an error message prompting them to select a valid time.
        - Special Requests (Optional)
            - Users can add special requests or dietary requirements before their booking.
            - This field is optional, meaning the form can be submitted without completing it.
        - Any field marked with an asterisk (*) is required, and users will receive feedback prompting them to complete any missing fields before they can submit the form.
    ![Screenshot of the booking form with the heading and intro above.][booking-form-screenshot]
    - When a user submits a booking request, they receive immediate feedback based on availability:
        - Successful Booking:
            - If there is availability, the user is notified of their successful reservation.
            - Their booking is then added to the 'Your Current Bookings' section below the form for easy reference.
    ![Screenshot of confirmation message which is displayed when a booking has been made successfully.][bookng-confirmation-screenshot]
        - No Availability:
            - If the requested date, time, or party size is unavailable, an error message informs the user.
            - They are then prompted to resubmit the form with an alternative booking option.
    ![Screenshot of message that is displayed to user when there is no availability for their request.][booking-declined-screenshot]
        - This ensures clear communication and a seamless booking experience, allowing users to quickly adjust their reservations when needed.
- User Bookings Display
    - If a logged-in user has any approved future bookings, they will be displayed below the booking form for easy reference and management.
        - Booking List Display:
            - Heading: "Your Current Bookings:" appears above the list.
            - Sorting: Bookings are displayed in chronological order, with the nearest date first.
        - Layout:
            - Each booking is shown in a vertical list, centered on the page.
            - Each entry is enclosed within a bordered container for clear separation.
            - The booking details include date, time, and party size.
        -  Management Options:
            - Below each booking, users have access to "Edit" and "Cancel" buttons, allowing them to modify or remove their reservations if needed.
    - This feature ensures users can quickly view, manage, and update their bookings in a structured and intuitive way.
    ![Screenshot of the list which displays any current booking that the user has.][bookings-display-screenshot]


### Edit Booking Page Features:

When a user clicks the "Edit" button on one of their listed bookings, they are directed to a separate page containing a form titled "Edit Booking".
- Editing Process
    - The form is pre-populated with the party size and date of the existing booking.
    - Users can modify their booking details and submit an update request.
- Feedback & User Flow
    - If availability exists, the booking is updated, and the user is redirected to the main Booking Page, where the updated booking will be displayed in the ‘Your Current Bookings’ section.
    - If the requested date, time, or party size is unavailable, an error message informs the user.
    - They remain on the Edit Booking Page and are prompted to select an alternative option.
- This ensures a smooth user experience, allowing for seamless modifications while maintaining clarity through real-time feedback.
    ![Screenshot of the edit booking page which host a form for users to complete with ammended booking details.][edit-booking-screenshot]


### Delete Booking Model:

When a user clicks the "Cancel" button next to one of their current bookings, a confirmation modal appears at the center of the screen, overlaying the current page.
- Modal Functionality
    - The modal prompts the user to confirm their cancellation and reminds them that this action cannot be undone.
    - The user must select either:
        - "Yes" – to confirm the cancellation.
        - "No" – to close the modal and return to the previous page without making changes.
- Feedback & User Flow
    - If "Yes" is clicked:
        - The user receives confirmation that their booking has been successfully canceled.
        - They are redirected to the main Booking Page, where their updated list of current bookings is displayed.
    - If "No" is clicked:
        - The modal closes, and the user remains on the current page, with no changes made.
This confirmation step ensures that users do not accidentally delete their reservations, providing a smooth and secure experience.
    ![Screenshot of the cancellation model that is displayed once the user clicks the 'cancel' button next to their current booking.][delete-modal-screenshot]


### Contact Page Features: 

At the top of the Contact Page, a heading encourages users to visit the restaurant, setting a welcoming tone. The page is structured with clear headings labeling each section:
- Location:
    - The restaurant’s address is displayed prominently at the top center of the page.
    - Below the address, an interactive Google Maps widget features a marker pinpointing the restaurant's location.
        - The map was created using the Google Maps API, allowing users to click the link and open Google Maps for personalized directions from their current location.
    ![Screenshot of the location section of the cntact page, which includes the address of the restaurant and an interactive Google map.][location-screenshot]
- Opening Times:
    - A full list of the restaurant’s operating hours.
- Get in Touch: 
    - Contact details, including telephone number and email address.
- Add Us:
    - Social media links with their associated icons encouraging users to connect.
    ![Screenshot of the contact details associated with the restaurant, including their phone number, email address, opening times and links to their social media pages.][contact-details-screenshot]
- Responsive Design
    - On mobile devices, all sections are displayed vertically for easy readability.
    - On larger screens, Flexbox styling is used to align the last three sections (Opening Times, Contact Info, and Social Media Links) horizontally at the bottom, improving symmetry and visual balance.
    - This layout ensures ease of access to key contact details, enhancing the user experience while keeping the design clean and intuitive.


### Sign Up Page Features:

The Sign-Up Page provides a clear and welcoming experience for new users, ensuring a smooth registration process.
- Page Structure & User Guidance
    - A large heading welcomes users, followed by a brief introductory message.
    - A line divider separates the form from a prompt for returning users, asking if they already have an account.
    - A highlighted link directs existing users to the Login Page for easy access.
- Sign-Up Form Features
    - The form was built using Crispy Forms, ensuring a clean and structured layout.
    - Custom CSS styling maintains visual consistency with other forms on the website, enhancing its professional appearance.
    - The form includes four fields:
        - Username (required)
        - Email (optional)
        - Password (required)
        - Confirm Password (required)
- User Feedback & Validation
    - If any required fields are left blank, the user receives real-time feedback prompting them to complete them.
    - A small print section outlines password requirements.
    - If the password does not meet the minimum security criteria, an error message informs the user why and guides them to correct it.
- Form Submission
    - Once the form is completed correctly, users can click the submit button to proceed with registration.
- This setup ensures an intuitive, user-friendly registration process while maintaining professional design consistency across the website.
    ![Screenshot of the Sign up page including the heading, introduction, link to login page and the sign up form itself.][signup-screenshot]


### Login Page Features:

The Login Page provides a clear and structured experience, guiding users through the authentication process.
- Page Structure & User Guidance
    - A prominent heading welcomes users, followed by a message informing them that they must log in to create or amend a reservation.
    - A line divider separates the login form from a prompt for new users.
    - If a user does not have an account, they are instructed to sign up first, with a highlighted link directing them to the Sign-Up Page.
- Login Form Features
    - The form is styled consistently with the rest of the website’s forms for a professional and cohesive look.
    - It contains two input fields:
        - Username
        - Password
    - A "Remember Me" checkbox allows users to stay signed in for future visits.
    - A "Sign In" button submits the form.
- User Feedback & Authentication
    - If a user enters incorrect credentials, an error message appears at the top of the page, prompting them to try again.
    - If login is successful, a confirmation message is displayed, and the user is redirected to the Home Page.
- This layout ensures a smooth, user-friendly login process, reducing friction while maintaining clarity and accessibility.
    ![Screenshot of the Login page including the heading, introduction, link to sign up page and the login form itself.][login-screenshot]

### Logout Page Features:

The Logout Page is intentionally simple, ensuring a clear and seamless sign-out process.
- Page Structure & Functionality
    - A bold heading informs the user that they are about to log out.
    - A confirmation message is displayed inside a styled box, asking the user to confirm their decision.
    - A "Sign Out" button allows them to proceed.
- User Feedback & Redirect
    - Upon clicking the Sign Out button, users receive feedback confirming they have been logged out.
    - They are then automatically redirected to the Home Page.
- This design keeps the process quick, intuitive, and distraction-free, ensuring users can log out efficiently when needed.
    ![Screenshot of the Log out page.][logout-screenshot]


### 404 Error Page

If a user enters an incorrect URL, they are directed to a custom-styled 404 error page, ensuring a clear and user-friendly experience.
- Page Structure & Features
    - A bold, clear title indicating that the page cannot be found.
    - A large "No Entry" icon, visually reinforcing the error.
    - A brief message explaining that the requested page does not exist and prompting users to:
        - Check the URL and try again.
        - Click a highlighted link to return to the Home Page.
- Navigation & Styling
    - The Home Page link stands out with contrasting colors, making it easy to find.
    - If clicked, the user is redirected back to the Home Page for a seamless experience.
The page is styled consistently with the rest of the website, maintaining a professional and cohesive design.
This ensures that users encountering a broken or incorrect link are guided smoothly back to the main site without frustration.
    ![Screenshot of the custom styled 404 error page.][404-error-screenshot]


<h2 id="features-to-implement">Features Left To Implement</h2> 

### Events Calendar
Feature: A dedicated events calendar displaying upcoming events at the restaurant, such as live music, themed nights, book readings, or special promotions.
- Why This Would Add Value:
    - Helps customers plan their visits around events that interest them.
    - Encourages more foot traffic on event days by promoting engaging activities.
    - Enhances the sense of community, reinforcing the café’s ethos of being an inclusive and welcoming space.

### Contact Form with a Comments Box
Feature: A comments box within the contact section for authenticated users to send questions, queries, or suggestions directly to the restaurant.
- Why This Would Add Value:
    - Provides a direct and easy communication channel between customers and the restaurant.
    - Encourages customer engagement by making it simple to ask about menu items, dietary accommodations, or upcoming events.
    - Helps gather valuable feedback, allowing the restaurant to improve based on user suggestions.

### Clickable Menu Item Links for More Product Information 
Feature: Each menu item would be clickable, leading to a dedicated page with details such as nutritional information, dietary alternatives, ingredients, and pairing recommendations.
- Why This Would Add Value:
    - Offers more transparency about menu items, catering to health-conscious customers or those with dietary restrictions.
    - Allows users to see available alternatives (e.g., plant-based options, gluten-free substitutes).
    - Enhances customer decision-making, making it easier to choose suitable dishes before visiting.
- When designing the Food and Drink models, I anticipated the need for detailed product pages. To support this functionality, I included the following fields:
    - Slug – Enables clean and SEO-friendly URLs for individual item pages.
    - Description – Provides space for a detailed explanation of each item, including ingredients and flavors.
    - Food Image – Allows for visual representation, enhancing presentation and user appeal.
    - Boolean Fields (Vegan, Vegetarian, Gluten-Free) – These classifications help users quickly identify menu items that align with their dietary preferences.
- By incorporating these fields early in development, the foundation is already in place for future enhancements, such as dedicated product pages with more tailored information, filtering options, and personalized recommendations.

### Reviews & Ratings System
Feature: A user-generated review and rating system allowing customers to rate menu items or leave feedback on their overall dining experience.
- Why This Would Add Value:
    - Authentic customer reviews help new visitors make informed decisions when choosing menu items.
    - Allows customers to share their experiences, fostering community interaction and a sense of connection with the restaurant.
    - Helps the restaurant identify popular dishes, make improvements, and respond to customer concerns.
    - Customers with dietary preferences or allergies can benefit from insights shared by others who have similar needs.
    - Positive reviews can reinforce customer loyalty, making them more likely to return.

[Back to Contents](#contents)

<h1 id="technology-used">Technology Used</h1> 

### Languages & Frameworks
- HTML
    - The structural foundation of the website, used to create the page layout and content elements.
- CSS
    - Responsible for styling and layout, ensuring consistency, responsiveness, and a visually appealing design.
- Python
    - Was the main language used for backend development in Django, handling data processing, authentication, and business logic.
- Django
    - A Python-based web framework that handles database management, authentication, and server-side logic.
- JavaScript
    - Added interactivity to the site, enabling dynamic features like event handling, form validation, and animations.
### Development, Version Control & Deployment
- GitHub
    - Used for agile development, version control, storing the project repository, tracking changes, and enabling collaboration.
- Gitpod/VS Code
    - The Integrated Development Environments (IDEs) used for writing, debugging, and managing the project’s code efficiently.
    - Initially I started by using Gitpod but have migrated my project over to VS Code mid project.
- Heroku
    - A cloud platform used to deploy and host the live website, making it accessible to users online.
### Django Extensions & Libraries
- Django AllAuth
    - Handles user authentication, account registration and login/logout.
- Crispy Forms
    - Provides enhanced form rendering, ensuring a clean, professional, and styled user interface.
- Django Template Language (DTL)
    - Used for dynamic content rendering, allowing flexible data presentation within templates.
- Summernote
    - A rich-text editor integrated via Django-Summernote, allowing formatted content editing within the Django admin panel.
### Design & Planning Tools
- Figma 
    - A UI/UX design tool used for wireframing and prototyping the website layout before development, as well as creating a process flowchart to visualize the user journey and system interactions.
- Lucidchart 
    - A diagramming tool used to create the Entity Relationship Diagram (ERD) for database schemas and architectural diagrams to plan the project structure and data flow.
### Media & Storage Services
- Cloudinary 
    - A media storage and management platform used for storing and serving images dynamically, ensuring fast and efficient image delivery.
- Google Cloud 
    - Used to support API integration and enable the seamless use of the Google Maps API within the project.
- PostgreSQL 
    - A robust relational database system used in the production environment for handling and storing structured data efficiently.
### Third-Party APIs & Libraries
- Google Maps API
    - Google Maps API was implemented in the Contact Page, allowing users to view the restaurant’s location, interact with the map, and get personalized directions.
- Materialize CSS 
    - A CSS framework used for modern UI components, including a responsive sliding navigation bar on smaller devices.
- Bootstrap
    - Used for layout styling, grid-based responsiveness, and UI components to maintain consistency.
### Additional Tools & Libraries
- ChatGPT
    - Used to generate images for the website, ensuring a consistent and visually appealing design.
    - Assisted in debugging issues, providing explanations and solutions for resolving code errors and logic problems throughout development.
- Google Fonts
    - Used to import and apply custom fonts and icons, ensuring a consistent, aesthetically pleasing, and readable typography across the website.
    - Helps maintain brand identity and enhances the overall user experience.
### Validation & Code Quality Tools
These tools ensured code quality, accessibility, and performance across the project:
- W3C Validator
    - Checked HTML validity.
- Jigsaw 
    - Verified CSS correctness.
- CI Linter 
    - Ensured clean, structured Python and Django code.
- JSHint 
    - Analyzed JavaScript for potential errors.

[Back to Contents](#contents) 

[flow-chart]: static/images/flow-chart.png
[erd]: static/images/erd.png
[wireframes]: static/images/wireframes.png
[header-logged-in-screenshot]: static/images/header-logged-in.png
[hero-screenshot]: static/images/hero.png
[header-logged-out-screenshot]: static/images/header-logged-out.png
[authenticated-home-screenshot]: static/images/authenticated-home.png
[footer-screenshot]: static/images/footer.png
[welcome-screenshot]: static/images/welcome.png
[about-screenshot]: static/images/about.png
[produce-screenshot]: static/images/produce.png
[visit-screenshot]: static/images/visit.png
[menu-intro-screenshot]: static/images/menu-intro.png
[menu-links-screenshot]: static/images/menu-links.png
[menu-image-screenshot]: static/images/menu-image.png
[small-print-screenshot]: static/images/menu-small-print.png
[booking-link-screenshot]: static/images/booking-link.png
[food-menu-screenshot]: static/images/food-menu.png
[unauthenticated-book-screenshot]: static/images/unauthenticated-book.png
[booking-form-screenshot]: static/images/booking-form.png
[bookng-confirmation-screenshot]: static/images/booking-confirmed.png
[booking-declined-screenshot]: static/images/booking-declined.png
[bookings-display-screenshot]: static/images/bookings-display.png
[edit-booking-screenshot]: static/images/edit-booking.png
[delete-modal-screenshot]: static/images/delete-modal.png
[location-screenshot]: static/images/location.png
[contact-details-screenshot]: static/images/contact-details.png
[login-screenshot]: static/images/login.png
[logout-screenshot]: static/images/logout.png
[404-error-screenshot]: static/images/404-error.png
[signup-screenshot]: static/images/signup.png
