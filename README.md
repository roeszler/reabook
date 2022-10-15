<!-- ![Reabook.net](https://res.cloudinary.com/yodakode/image/upload/v1661790281/ReaBook/ReaBook_Icon_00402B_gray_szgzia.ico) -->
# ReaBook Booking System

> **ReaBook** - attracts and drives initial bookings to view real estate for sale, rent or lease.

## Full Stack Toolkit with Django - [Code Institute](https://codeinstitute.net/)

### Applying: HTML, CSS, JavaScript, Python+Django, Relational Databases (PostgreSQL), c

* Repository link : [github.com/roeszler/reabook](https://github.com/roeszler/reabook)
* Terminal : [reabook.herokuapp.com](https://reabook.herokuapp.com/)
* User Stories : [github.com/users/roeszler](https://github.com/users/roeszler/projects/4)

---

<details>
<summary style="font-size: 1.5rem;">Table of Contents (dropdown list)</summary>

1. [Project Purpose](#1-project-purpose)
    * [Database Functionality](#database-functionality)
    * [Considerations](#important-consideration)
2. [Agile Development Process](#2-agile-development-process)
    * [Requirements Engineering](#21-understanding-requirements)
        * [User Centered Design](#22-implementation)
        * [Defining Requirements](#defining-the-requirements)
        * [User Personas](#user-personas)
        * [Requirements Analysis](#requirements-analysis)
3. [Concept Development](#3-concept-development)
    * [Themes](#31-themes)
    * [Epics](#32-epics)
    * [User Story Framework](#33-user-stories)
        * [Integrating User Stories](#user-story-integration-github)
4. [Project Management](#4-project-management)
    * [Story Point Estimation](#41-story-point-estimation)
    * [Team Velocity](#42-team-velocity)
    * [MoSCow Prioritization](#43-moscow-prioritization)
    * [Information Radiators](#44-information-radiators)
    * [Sprints](#45-sprints)
5. [User Experience Design](#5-ux-design)
    * [Structure](#51-structure)
    * [Mockup & Wireframes](#52-application-mockup--wireframes)
        * [UX Flowcharts](#ux-flowcharts-mockups)
            * Customer
            * Admin / Member
        * [Database](#the-database-model)
        * [Wireframes](#ux-wireframes)
6. [Features](#6-features)
    * [Existing Features](#61-existing-features)
        * [Login / Registration](#registration-and-login)
        * [Main Navigation Bar](#main-navigation-bar)
        * [Sub Navigation Bar](#sub-navigation-bar)
        * [Main Page](#main-landing-page-indexhtml)
        * [View Properties / Search Results](#search-results--view-properties)
        * [Bookings](#request-booking-page)
        * [User Diary](#user-diary-page)
        * [View / Update / Edit Booking](#view--update--edit-a-booking-request)
        * [As Agent / Member User](#as-a-member--agent)
            * [Manage Properties](#property-management-landing-page)
            * [Create a Property](#list-a-property)
            * [Edit a Property](#edit--update-a-property-listing)
        * [Successful Submission](#successful-submission)
    * [Future Features](#62-future-features)
7. [Technologies](#7-technologies)
    * [Tools](#tools)
    * [Supported Browsers](#supported-screens-and-browsers)
8. [Testing](#8-testing)
    * [MVC Testing](#mvc-testing)
        * [Python](#automated-python-testing)
        * [JavaScript](#automated-javascript-testing)
        * [Manual](#manual-testing)
    * [Debugging](#bugs--debugging)
    * [Validation](#validator-testing-of-custom-code)
9. [Deployment](#9-deployment)
10. [Credits](#10-credits)
    * [Content](#content)
    * [Media](#media)
</details>

---

## 1. Project Purpose
ReaBook (the Site) is a framework for a real estate advertising site used to present the deployment of an appointment booking system (the App) using the [Django](https://www.djangoproject.com/) Full Stack Framework.

### Professional Development
A primary focus of this project has been to practice, test theories and increase the depth of my experience in planning, design and implementation of full stack solutions. As a student developer, I decided to take the opportunity to extend myself into a scope larger than was required for the [Code Institutes](https://codeinstitute.net/) portfolio project 4. 

From this process, I am more fluent and comfortable with the implementation of the agile processes, database design and management, debugging and deployment. I am pleased to include the Reabook project to form part of my larger professional portfolio.

### Database Functionality
At the time of release, the site is deployed via the [Heroku](https://www.heroku.com/platform) platform at [reabook.herokuapp.com](https://reabook.herokuapp.com/). Here users can:
* Select and submit requests to attend store owner users arranged viewing times for properties listed for sale or rent.
    > Main nav > Book > (login) > Reabook Viewings

* Create, retrieve and navigate through orders to update information, check production status and/or re-book properties.
    > Create = Book Viewings button

    > Retrieve = View / Edit link

    > Navigate = Quick Links / My ReaBook menus

* Agent / Member / Admin users can list, edit and advertise times for potential customers to view properties currently for sale or rent in their business portfolio.
    > Property List = Manage Properties > Add Property

    > Property Edit = Manage Properties > Edit / Delete

### Important Consideration:
The ReaBook business premise is to collate and drive leads into existing appointment management systems. Specifically, it **is not to provide appointment management service**. Most all real estate agencies will already have well developed appointment management systems, so the ReaBook app is focused on enhancing the lead generation into these systems and provide advertising across all agents. 

## 2. Agile Development Process

Created by student developer; [Stuart Roeszler](https://www.linkedin.com/in/stuartroeszler/), the Reabook project has been developed following an Agile methodology as part of the assessment process at the [Code Institutes](https://codeinstitute.net/) - [Full Stack development program](https://codeinstitute.net/se/full-stack-software-development-diploma/). 

Some of the Agile [Project management](#4-project-management) processes (like [team velocity](#42-team-velocity)) do not easily translate into a single person development team. They would however form a crucial part of a live, team based project and have been outlined accordingly.

### 2.1 Requirements Engineering
#### User Centered Design (UCD) Process:
* User Centered Design (UCD) Process was used to identify key goals and structure the development process.
    <details>
    <summary style="font-size: 1rem;">
    For a more detailed look at the ReaBook UCD Process (dropdown list)
    </summary>
        
    - [Strategy](static/documentation/ucd/1-strategy.md)
    - [Scope](static/documentation/ucd/2-scope.md)
    - [Structure](static/documentation/ucd/3-structure.md)
    - [Skeleton](static/documentation/ucd/4-skeleton.md)
    - [Surface](static/documentation/ucd/5-surface.md)

    </details>

#### Defining the Requirements
Seen from activities undertaken in the User Centered Design (UCD) [strategy](static/documentation/ucd/1-strategy.md) and [scope](static/documentation/ucd/2-scope.md) panes, the requirements for the ReaBook project are: 

To make an online community looking for one-stop access to real estate available in an area.

> ReaBook: A single cross-agency site where users can interact to find and visit their next property solution. Users would be able to seek to properties in their region and be able to make bookings direct to member agents from our bookings store. Member Agent users will be able to list properties for sale, rent or lease and receive a customer stream into their businesses.

#### User Personas
Three primary user personas were defined from the above requirements engineering process:

<details>
    <summary>1. Customer User</summary>

- **Who are they?**
    - 18 to 45 years old, fully employed, professional couple &/or early stage family, further educated, non-local.
- **What is their main goal?**
    - Find rental accommodation, property purchase and/or lease of new business spaces in a variety of city and rural locations.
- **What is the main barrier to achieving their goal?**
    - Spread of multiple properties across multiple real-estate businesses makes search and access difficult.

- **Persona Card**:
    ![user_persona](static/documentation/wireframes/Home-seeker-Persona-ReaBook.png)
</details>

<details>
    <summary>2. Agent / Member User</summary>

- **Who are they?**
    - Early to established real-estate business with expertise in local region.
- **What is their main goal?**
    - Constantly feed new sales to maintain business growth and position. 
- **What is their main barrier to achieving their goal?**
    - Access to new customers wishing to engage their real-estate services.
- **Persona Card**:
    ![user_persona](static/documentation/wireframes/Owner-Agent-Persona-ReaBook.png)
</details>

<details>
    <summary>3. Admin User</summary>

- **Who are they?**
    - New to intermediate, IT literate professionals looking for platform to manage B2C connections 
- **What is their main goal?**
    - Add value to businesses in the real-estate fields internationally.
- **What is their main barrier to achieving their goal?**
    - Access to cross platform sales funnel into existing management systems
- **Persona Card**:
    ![user_persona](static/documentation/wireframes/IT-Admin-Persona-ReaBook.png)
    </details>


### Requirements Analysis
Used to confirm understanding and documented check that each requirement is:    
* Clear
* Non-conflicting
* Has successfully completed a trade-off process between owner and development team as to what is important and what is feasible.

Consideration and documentation at this point as to:
* How will each requirement be implemented?
* How will each requirement be Tested?
    * [Automated Testing](#automated-python-testing)
    * [Manual testing tree](#manual-testing)
* What is the agreed [process](#33-user-stories) and outcomes to evaluate each requirement? (to meet initial requirements)

<details>
<summary style="font-size: 1rem;">
Sample user story with acceptance criteria for the ReaBook project
</summary>
<br>
User Story: 
* As a **user**, I can **select the time I would like to visit a property** so that **I can arrange my day efficiently with little difficulty**.

**Acceptance Criteria**:

* [x] Booking details must include the time and date of intended appointment, the subject property address, the name, email and phone number of the person requesting the booking. 

* [x] The agent / employee is able to select the time of the booking details from 3 sessions during the the day (Morning, Afternoon and Evening).

* [x] The font size used in the conformation email is 12 point.

**Tasks**:

* [x] Design a “submit” button and add it to the booking details page.

* [x] Create the HTML and CSS for the dropdown menu including the booking times. 

* [x] Create the HTML, CSS and copy for the successful submission email.

* [x] Create the code for the model, viewer and controller.

* [x] Test the completed functionality that includes email submission.

[Live sample of a user story card with acceptance criteria (GitHub)](https://github.com/roeszler/reabook/issues/48).

</details>

## 3. Concept Development
### 3.1 Themes
Collect related epics that have something in common. In the project, this can be seen as:

<details>
<summary>User Experience (Theme)</summary>

* Account Registration journey (Epic)
* Add Property journey (Epic)
* Bookings journey (Epic)
* Sign in/out journey (Epic)
</details>

<details>
<summary>Account Management (Theme)</summary>

* Sign-in feature (Epic)
* User profile feature (Epic)
* Sign-up feature (Epic)
</details>

<details>
<summary>Property Management (Theme)</summary>

* Display multiple properties feature (Epic)
* Display single property feature (Epic)
* Add single property feature (Epic)
* Edit single property feature (Epic)
</details>

<details>
<summary>Booking Management (Theme)</summary>

* Display booking feature (Epic)
* Create booking feature (Epic)
* Update booking feature (Epic)
* Display multiple bookings feature (Epic)
</details>

### 3.2 Epics
Epics are larger multiple iteration that can be broken into user stories.
<details>
<summary style="font-size: 1rem;">
List if Reabook Epics.
</summary>
        
- Reabook Epics
    1. Dataset Design (see: [Design Section](#5-design))
    2. [Site Framework](https://github.com/roeszler/reabook/milestone/1)
        - User Profile Framework
            - Admin User (see [Admin Persona](#user-personas))
            - Agent Member User (see [Staff Persona](#user-personas)) 
            - Customer User (see [User Persona](#user-personas)) 
        - [Site Pages](#61-existing-features)
            - Login
            - Register
            - Profile
            - Index
            - Properties
            - Bookings Diary
                - Make Booking
                - Edit / Delete Booking
            - Manage Properties
                - Add Properties
                - Edit / Delete Properties
    3. [User Experience](#5-ux-design)
        - [View & Search Properties](https://github.com/roeszler/reabook/milestone/6)
            - Read Dataset
            - Display Properties
        - [Make & Manage Bookings](https://github.com/roeszler/reabook/milestone/7)
            - Book Viewing
            - Edit Viewing
            - Delete Viewing
        - [Create Property Listing](https://github.com/roeszler/reabook/milestone/11) (staff)
            - Edit Property Listing (staff)
            - Delete Property Listing (staff)
        - [Account Administration](https://github.com/roeszler/reabook/milestone/8) (staff)
</details>

### 3.3 User Stories
Reabook user stories have been produced in a brief format for simplicity. In a team environment, a [User Story Card](https://github.com/roeszler/reabook/issues/48) would be used. Each card would contain:

- Acceptance Criteria
    - Subjectively confirms that the work on a particular user story is completed
- Tasks
    - Are the various individual activities carried out by the development team to implement each User Story as a “Task”
    - Each development team is responsible for
        - Identifying, assigning, and tracking tasks’ progress
        - Taking technical decisions required to deliver the user story
- Story Point Value
    - Are relative estimations focused on the amount of work needed to be done to complete the story
    - Are relative estimations compared to the other stories in the project

- [Sample Story Card with acceptance criteria (GitHub)](https://github.com/roeszler/reabook/issues/48).

### User Story Integration (GitHub)
Key to Agile process is the looping process of define, design, develop and test over short, well defined periods (sprints). The integration of this process into the day to day operation of the development team requires a shared repository that displays live information on where the project is at any given time. 

For the purposes of this project, the GitHub issues management feature has been used to coordinate development, albeit with a single student developer.

By coordinating user stories in this way, each added to the formation of an overall [project feature](#61-existing-features) and deliver the value users gain by using the ReaBook app.

Users & their stories:
- [Customer User](https://github.com/roeszler/reabook/labels/User%20%28Customer%29)
- [Agent / Member User](https://github.com/roeszler/reabook/labels/User%20%28Member%29)
- [Admin User](https://github.com/roeszler/reabook/labels/User%20%28Admin%29)

For a full description, jump ahead to: [Section 6. Features](#61-existing-features).
## 4. Project Management
Adhering to the Agile framework, where possible the following processes were completed during each user story:  
### 4.1 Story Point Estimation
Difficult to estimate with current level of experience, focused on the amount of work done posthumously in most cases. This was primarily due to the errors that came with each development iteration and the relative simple or solutions to solve the problem. 

One such instance was the inclusion of a bootstrap dropdown as part of the booking process. This was aimed to sequentially lead the user booking a viewing appointment to the next step. 

The combined front end JavaScrip and backend Python solution to achieve the sequential update and display of the data entered became out of scope for the project and story points I had allocated to the task. 

As part of the [agile manifesto](https://agilemanifesto.org/) approach (responding to change over following a plan) the code was refactored to provide a more basic, consistent user experience that was achievable in the time-frame. 

### 4.2 Team Velocity
Considers an average amount of story points the development 'team' can manage to finish in one iteration of a particular length. 

As this is an average measure, and focus the ReaBook project was placed on gathering experience and testing hypotheses in my journey as a student, Team Velocity has not been calculated for a single student developer.

### 4.3 MoSCow Prioritization
This technique was invaluable to each stage of the development process with the looping approach of Agile development and continuous revision throughout each sprint. 

Each task was reviewed and re-reviewed considering where it's importance lies:
* Must Have - non negotiable (core, legal, security)
* Should Have - if work around available, not vital. Add significant value. (Performance improvements, minor defects fixes, new functionality).
* Could Have - delivered in their entirety in a best-case scenario. When a problem occurs and the deadline is at risk, one or more “could-have” items are dropped.
* Won’t Have - Agile team has agreed that the PBI wouldn’t be delivered. Possible reschedule to later iterations? Recorded to manage expectations always.

The culmination of the MoSCow prioritization process can be seen in those with an [on hold](https://github.com/roeszler/reabook/labels/on%20hold), [wontfix](https://github.com/roeszler/reabook/labels/wontfix) or [future release](https://github.com/roeszler/reabook/labels/future%20release) tags respectively.

### 4.4 Information Radiator(s)
As real-time, informative and straightforward work status display, a magnetic whiteboard with post-it notes was used to clarify current tasks and manage development time. 

Common contents included:
* Remaining user stories,
* User stories’ status in the current iteration,
* The progress toward the next sprint,  
* Total numbers of open defects
* Further research / assistance required

### 4.5 Sprints
Once the basic management processes of the project was devised, the software development proceeded in incremental cycles. Each activity was done in small loops (Sprints).

These reflect the iterative Agile approach, where development focus is on autonomy, collaboration and early, continuous delivery. This proved to make the project both adaptive and evolve as it progressed.  

<details>
    <summary style="font-size: 1rem;">
    For a more detailed look at the ReaBook development sprints (dropdown list)
    </summary>

- [Sprint 1 - Site Framework](https://github.com/roeszler/reabook/milestone/1)
- [Sprint 2 - View & Search Property](https://github.com/roeszler/reabook/milestone/6)
- [Sprint 3 - Make & Manage Bookings](https://github.com/roeszler/reabook/milestone/7)
- [Sprint 4 - Create Properties](https://github.com/roeszler/reabook/milestone/11)
- [Sprint 5 - Account Administration](https://github.com/roeszler/reabook/milestone/8)
- [Sprint 6 - Refactor Dependencies](https://github.com/roeszler/reabook/milestone/9)
- [Sprint 7 - Bugs, General Refactoring and Documentation](https://github.com/roeszler/reabook/milestone/10)

</details>

## 5. UX Design
### 5.1 Structure
The application is intended to allow users to easily navigate through an appointment request process. Users journey through finding and selecting property, choosing booking, booking conformation and summaries and tables to confirm their booking request have been sent.

### 5.2 Application Mockup & Wireframes
Graphics of the application have been designed to show member users and users early concepts of user journeys before any coding started. They provided an indication of:

* The variety of functions required
* The critical pathways of functions needed to reach each user outcome
* The relationships between each function
* The logical approach to code creation, promoting readability and aiding future fault-finding processes
* The experience as users navigate through the booking application processes

### UX Flowcharts Mockups:

<!-- <details>
    <summary>
    Site Map
    </summary>
        
![Site Map]()
</details> -->


<details>
    <summary>
    Customer User C.R.U.D. Flowcharts
    </summary>

Flowchart 1 - CREATE & READ
![Customer User C.R.U.D. Flowchart 1](static/documentation/img/Flowchart-1-Customer-User-ReaBook.png)

Flowchart 2 - UPDATE & DELETE
![Customer User C.R.U.D. Flowchart 2](static/documentation/img/Flowchart-2-Customer-User-ReaBook.png)
</details>

<details>
    <summary>
    Admin / Member User C.R.U.D. Flowcharts
    </summary>

Flowchart 3 - CREATE & READ
![Admin / Member User C.R.U.D. Flowchart 3](static/documentation/img/Flowchart-3-Member-User-ReaBook.png)

Flowchart 4 - UPDATE & DELETE
![Admin / Member User C.R.U.D. Flowchart 4](static/documentation/img/Flowchart-4-Member-User-ReaBook.png)
</details>

### The Database Model:
The model is fairly simple, however of note is:

* The central part of the model is the Property table. This stores all the details about Member / Agent listed properties. 
* Two tables Category and Sector act as dictionaries to the Property table. 
* The employee and schedule tables are our administrative tables. 
* The other four tables deal with clients, client contacts, and the services provided.
* Note: that the name 'Property' is a [python attribute](https://docs.python.org/3.8/library/functions.html#property), so coding entailed the use of 'prop' or ''properties' or 'property_id' to avoid conflicts.

<details>
    <summary>
    Database Model
    </summary>
        
![Database Model](static/documentation/img/reaboo-db-models.png)
</details>


### UX Wireframes
Early representation of the look, feel and HTML structure of the project. Aids concept development and communication of ideas to stakeholders:

<details>
    <summary>
    Initial Concept - Landing Page Wireframe
</summary>

![Booking App Page Wireframe](static/documentation/wireframes/ReaBook_Index_v1.0.png)
</details>

<details>
    <summary>
    Initial Concept - Booking App Wireframe
    </summary>
        
![Booking App Page Wireframe](static/documentation/wireframes/Bookings_Page.png)
</details>

## 6. Features
### 6.1 Existing Features

<!-- ### [Sprint 1 - Site Framework](https://github.com/roeszler/reabook/milestone/1) -->
### Registration and Login
The [allauth](https://django-allauth.readthedocs.io/en/latest/) third party package has been installed into the framework to handle the logic of user login, logout and registrations.

![Login Mobile](static/documentation/img/reabook-login-mobile.png) ![Register Mobile](static/documentation/img/reabook-register-mobile.png)

### Main Navigation Bar
![Navbar](static/documentation/img/reabook-navbar.png)
Mobile:
![Navbar Mobile](static/documentation/img/reabook-navbar-mobile.png)
* Site-wide navbar and search functionality
* My account dropdown menu that alters depending on user:
    * Non-Authenticated Site Visitor
    
        ![visitor-menu](static/documentation/img/visitor-menu.png)
    
    <details>
    <summary>Admin</summary>

    ![Admin-menu](static/documentation/img/admin-menu.png)
    </details>
    <details><summary>Agent / Member Menu</summary>
    
    ![member-menu](static/documentation/img/member-user.png)
    </details>
    <details><summary>User Menu</summary>
    
    ![user-menu](static/documentation/img/user-menu.png)
    </details>

* Bookings tally displays the number of bookings is indicated for authenticated users. This links to the [users diary](#existing-bookings-page) and indicated the total number of current bookings.
![bookings tally](static/documentation/img/reabook-bookings-tally.png)

### Sub Navigation Bar
This feature has been added to include quick access to common classes and sectors that the ReaBook database models allows.

![subnavbar](static/documentation/img/reabook-subnav.png)

Key Features:
* JavaScript / JQuery event handler monitors the mouseover, dropdown and fade on scroll functions for this and the main navigation bar to a lesser extent.
![scrollfade](static/documentation/img/reabook-scrollfade.png)
* SubNav not present on mobile browsers

### Main Landing Page (index.html)
* The landing page is intended to ground the user into the primary purpose of the application, options to explore and key branding and iconography throughout the site.

<details>
    <summary>
    ReaBook Landing Page Image
    </summary>
        
![ReaBook Landing Page](static/documentation/img/ReaBook_index.png)
</details>

Key Features:
* Landing page panels will automatically be updated with the newest properties first.

    ![order-by](static/documentation/img/order_by-function.png)

    ![order-by](static/documentation/img/order_by-function-2.png)

### Search Results / View Properties
* The main view properties / search results page is intended to provide the user with a familiar format and function to searching properties as they would do with selecting a product on many popular e-commerce sites.

<details>
    <summary>
    ReaBook Properties View Page
    </summary>
        
![ReaBook Properties View Page](static/documentation/img/ReaBook_view.png)
</details>

Key Features:
* Responsive layout from mobile first design principles to increased options for desktop users.
* If statements to automate the summary information displayed for each card
* Fallback image for properties without specific images supplied by user. 

### Request Booking Page
* Takes the user through the process of submitting a request to the property agent for an appointment to view the property: 
<details>
    <summary>
    1. Choose Property
    </summary>
        
![Choose Property](static/documentation/img/reabook-choose-prop.png)
</details>

<details>
    <summary>
    2. Choose date and time
    </summary>
        
![Choose date and time](static/documentation/img/reabook-choose-time.png)
</details>

<details>
    <summary>
    3. Enter Details & Submit
    </summary>
        
![Enter Details](static/documentation/img/reabook-enter-details.png)
</details>

<details>
    <summary>
    4. Receive Conformation Email & Next Steps.
    </summary>
        
![Conformation Email](static/documentation/img/reabook-conformation-booking.png)
</details>

Key Features: 
* Create database entry function
* Local search function included should user land directly to bookings page
* Only displays properties checked as 'for viewing' by member agent user
* JavaScript function to manage time and date UI
* User delete as part of agents external booking system(s)
* Request appears in user specific right sidebar 'Quick Links'

### User Diary Page
This is intended to be the main pivot point for users that have made a booking. Properties will appear in table format in the main section of this page, with navigation options through the site on the left and shortcuts to existing bookings on the right.
<details>
    <summary>
    User Diary Page
    </summary>
        
![User Diary Page](static/documentation/img/reabook-diary.png)
</details>

### View / Update / Edit a Booking Request
* Provides option to update booking request details

<details>
    <summary>
    View / Update / Edit Booking Page
    </summary>
        
![View Booking Page](static/documentation/img/reabook-update-booking.png)
</details>

Key Features: 
* READ and UPDATE existing database entry function
* Nested property specific information
* Email sent to agent to confirm changes

### Forms
Django [forms](https://docs.djangoproject.com/en/4.1/topics/forms/) have been used to integrate the submitted data into the app. They are represented to the user in the add, edit and update both properties and bookings
### As a Member / Agent: 

### Property Management Landing Page
* Provides admin / member users a brief summary table of their current properties.
* This is intended to be the main pivot point for agent / member users that have created a property. Properties will appear in table format in the main section of this page, with navigation options through the site on the left.

<details>
    <summary>
    Property Management Landing Page
    </summary>
        
![Property Management Landing Page](static/documentation/img/reabook-manager.png)
</details>

Key Features: 
* CREATE, READ and UPDATE existing database entry function
* Nested property specific information
* Summary address information only on mobiles

### List a Property
* Enables Member / Agent as staff user to CREATE a new property listing as an entry in the database

<details>
    <summary>
    List Property Page
    </summary>
        
![List a Property Page](static/documentation/img/reabook-add-property.png)
</details>

Key Features: 
* POST to database function
* request.FILES command included in CREATE function
* Required fields key for display view and data analytics longer term

### Edit / Update a Property Listing
* Enables Member / Agent as staff user to UPDATE the details of an existing property listing in the database

<details>
    <summary>
    Edit / Update a Property Page
    </summary>
        
![Edit / Update / Delete a Property Page](static/documentation/img/reabook-edit.png)
</details>

Key Features: 
* POST to database function
* request.FILES command included in UPDATE function
* Python code ```.delete()``` delivers DELETE function 
### Successful Submission
* System message indicating the the submission to CREATE, UPDATE or DELETE was successful providing the user with confidence that the process has completed.

![Success Message](static/documentation/img/reabook-success.png)

### 6.2 Future Features
* Edit User Profile & Passwords
* Extend account management functions 
* Member subscription model
* Refinement of style and feel. Current focus to have working C.R.U.D. functions
* Age depreciation of bookings / property listings according to days active
* ...

## 7. Technologies
### Tools
The skill-sets used in the creation and review of this project are based around a working knowledge of a full stack development approach using Agile methodologies with HTML, CSS, JavaScript (JQuery), Python, the Django framework, Bootstrap and Relational Database Design (SQLite and PostgreSQL). The tools and the benefit of using each in the application development are : 

* [GitHub](https://github.com/)
  * Allows a variety of benefits to create, document, store, showcase and share a project in development.
* [GitPod](https://www.gitpod.io/)
  * Provides a relatively secure workspace to code and develop software projects in a remotely accessible cloud based platform.
* [Heroku Platform](https://www.heroku.com/platform)
  * Provides a platform for deploying and running python based apps.
* The [Django Framework](https://www.djangoproject.com/) with embedded technologies as at version 3.2.15 and additional installations of:
  * [Allauth](https://django-allauth.readthedocs.io/en/latest/) to manage user authentication and management.
  * [Cloudinary](https://cloudinary.com/) Image and Video Upload, Storage, Optimization and Content Display Network.
  * [dj-database-url](https://pypi.org/project/dj-database-url/) to return a Django database connection dictionary, populated with data specified from the reabook URL.
  * [Gunicorn](https://gunicorn.org/) a Python Web Server Gateway Interface (WSGI) HTTP server.
  * [Pillow](https://pypi.org/project/Pillow/) part of the Python Imaging Library (PIL) adding image processing capabilities to the Python interpreter.
  * [django-countries](https://pypi.org/project/django-countries/) provides country choices for use with forms.
  * [django-crispy-forms](https://pypi.org/project/django-crispy-forms/) reusable layouts out of form components to avoid repetitive tasks (DRY).
* [Convertio Image Optimiser](https://convertio.co/)
  * Able to reduce the file size and format of images ready for rapid access, improving device performance, accessibility and user experience.
* [Lucidchart Flowchart Diagrams](https://www.lucidchart.com/pages/)
  * A diagramming application that allows the mapping and creation of flowcharts to visualise design workflows.
* [Balsamiq Wireframes](https://balsamiq.com/wireframes/)
  * A computer based low-fidelity UI wireframing tool to sketch up simple visuals assisting the concept development and planning stages.


### Supported Screens and Browsers
The live application ([ReaBook](https://reabook.herokuapp.com/)) has been tested on each of the following popular browsers to check for maintained function and interactivity :
- [Google Chrome](https://www.google.com/chrome/)
- [Microsoft Edge](https://www.microsoft.com/en-us/edge) 
- [Apple Safari](https://www.apple.com/safari/)
- [Mozilla Firefox](https://www.mozilla.org/en-US/firefox/new/)

## 8. Testing
A primarily manual testing of code  was followed. Automated testing was applied using a Model, View and Controller (MVC) framework built-in to the Python standard library of [Django](https://docs.djangoproject.com/en/4.1/topics/testing/) called [unittest](https://docs.python.org/3/library/unittest.html#module-unittest).

### MVC Testing
Model, View and Controller (MVC) testing with [unittest](https://docs.python.org/3/library/unittest.html).[TestCase](https://pypi.org/project/testcase/)

#### 3 Phases of a test:
1. Arrange: Creating the conditions for the unit-test to run within like an instance object
2. Act: Giving the object some sort of input / data
3. Assert: Checking wether the output data turned out as expected

**F** Fast to complete
**I** Independent of other tests
**R** Repeatable
**S** Self validating
**T** Timely (right place and time)

### Automated Python Testing

A variety unittest.TestCase [methods](https://docs.python.org/3/library/unittest.html#deprecated-aliases) can be used to create a test case. For the purposes of this project a sample test case was created to test the `integer_type_check` function that requires only an integer is entered into a field.

Important to note that during testing, the development environment settings were set to:

```
DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
```

The test is located at:
`app-bookings > test_views > TestTypeInteger`

The early form of the test was defined with `assertIsInstance()` method with an `integer` input value of `233`. This expects the `integer_type_check` function to have an input of an integer (`int`) to pass:

```
def test_entry_is_integer(self):
    """ To test that input is an integer """
    self.assertIsInstance(integer_type_check(233), int)
```

<details>
    <summary>
    This is sequentially repeated with a variety of related values...
    </summary>

```
class TestTypeInteger(TestCase):
    """ To test the integer_type_check function in working """
    
    def test_entry_is_integer(self):
        """ To test that input is an integer """
        self.assertIsInstance(integer_type_check(233), int)
    
    def test_entry_is_integer(self):
        """ To test that input is exactly equal to 10 """
        self.assertEqual(integer_type_check(10), True)
    
    def test_entry_is_integer(self):
        """ To test that input is not a string """
        self.assertIsInstance(integer_type_check('233'), int)
    
    def test_entry_is_integer(self):
        """ To test that input is not a float """
        self.assertIsInstance(integer_type_check(233.3), int)
    
    def test_entry_is_integer(self):
        """ No more than one input required """
        self.assertIsInstance(integer_type_check(21, 22), int)
```
</details>

### Test Driven Development

Following a Red-Green-Refactor approach to Test-driven development (TDD), the `integer_type_check` function was altered to produce firstly a failing test, then a passing test, and finally a passing test with refactored code:

<details>
    <summary>
    Failing Test (red)...
    </summary>

```
def integer_type_check(request):
    """ To ensure that only an integer is entered into a field """
    if isinstance(request, int):
        if request == 1.4:
            return True
        else:
            raise TypeError('An integer was not passed into the field')
    
    if __name__ == '__main__':
        print(integer_type_check(1.4))
```
CLI output:
```
(main) $ python3 manage.py test

Creating test database for alias 'default'...
System check identified no issues (0 silenced).
E
======================================================================
ERROR: test_entry_is_integer (app_bookings.test_views.TestTypeInteger)
To test that input is an integer
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/workspace/reabook/app_bookings/test_views.py", line 16, in test_entry_is_integer
    self.assertEqual(integer_type_check(1), True)
  File "/workspace/reabook/app_bookings/views.py", line 285, in integer_type_check
    raise TypeError('An integer was not passed into the field')
TypeError: An integer was not passed into the field

----------------------------------------------------------------------
Ran 1 test in 0.001s

FAILED (errors=1)
Destroying test database for alias 'default'...
```
</details>

<details>
    <summary>
    Passing Test (green)...
    </summary>

```
def integer_type_check(request):
    """ To ensure that only an integer is entered into a field """
    if isinstance(request, int):
        if request == 10:
            return True
        else:
            raise TypeError('An integer was not passed into the field')
    
    if __name__ == '__main__':
        print(integer_type_check(10))
```
CLI output:
```
(main) $ python3 manage.py test

Creating test database for alias 'default'...
System check identified no issues (0 silenced).
.
----------------------------------------------------------------------
Ran 1 test in 0.001s

OK
Destroying test database for alias 'default'...
```
</details>

<details>
    <summary>
    Refactored Code...
    </summary>

```
def integer_type_check(request):
    """ To ensure that only an integer is entered into a field """
    if isinstance(request, int):
        return True
    else:
        raise TypeError('An integer was not passed into the field')
    
    if __name__ == '__main__':
        print(integer_type_check(10))
```
CLI output:
```
(main) $ python3 manage.py test

Creating test database for alias 'default'...
System check identified no issues (0 silenced).
.
----------------------------------------------------------------------
Ran 1 test in 0.001s

OK
Destroying test database for alias 'default'...
```
        
</details>

Further testing was carried out to create a platform of test folders across the whole project and practice the above process by testing:

<details>
    <summary>
    TestHomeViews(TestCase)...
    </summary>

```
""" Tests the home index.html view """
from django.test import TestCase
from app_properties.models import Property, Category


class TestHomeViews(TestCase):
    """ Tests the home app views """
    def setUp(self):
        self.category = Category.objects.create(
            name='test',
            friendly_name='Test Category'
        )

        self.page = Property.objects.create(
            category=self.category,
            name='Test Property',
            ribbon_feature='This is a test page',
            description='This is test New Property Entry',
            house_no=22,
            bedrooms=3,
            bathrooms=1,
            carports=1,
            air_conditioning=1
        )
        self.category.title_page = self.page
        self.category.save()


    def test_landing_page(self):
        """ Tests loading the landing page """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')

```

CLI Output:
```
(main) $ python3 manage.py test
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
........
----------------------------------------------------------------------
Ran 8 tests in 0.070s

OK
Destroying test database for alias 'default'...
```
</details>

### Automated JavaSCript Testing
[Jest](https://jestjs.io/) is a popular JavaScript Testing Framework that can be applied to the JavaScript functions contained in this project. It follows the same [MVC testing](#mvc-testing) and [Test Driven Development](#test-driven-development) approach as detailed in the Pythonic testing seen above. 

Jest uses [Node.JS](https://nodejs.org/en/) JavaScript runtime environment via the node package manager (NPM) utility.

Due to the reliance on pythonic code and the relatively simple nature of the javascript components contained in the project, testing was done manually for each JS component at the time.

The custom JavaScript code is located in the `scrollfade.js` file, and line 54 of the `main.js` file, both located in the project static folders:

<details>
    <summary>
    Calendar radio buttons converted into fields ...
    </summary>

```
 var curr_date = $("<td class='table-date'><label for='"+day+"' class='mb-0'>"+day+"</label><input class='sr-only' type='radio' name='date_of_viewing' id='"+day+"' value='"+year+"-"+month+"-"+day+"'/></td>");
```
</details>

<details>
    <summary>
    Fade navigation bars on scroll (at different rates)...
    </summary>

```
$(window).scroll(function(){
    $("#sub-nav").css("opacity", 1 - $(window).scrollTop() / ($('#sub-nav').height() / 2));
    $("#topnav").css("opacity", 1 - $(window).scrollTop() / ($('#topnav').height() / 0.01));
});
```
</details>

<details>
    <summary>
    Sub Nav dropdown list display on hover...
    </summary>

```
$('.dropdown').hover(function(){
    $('.auto-dropdown', this).trigger('click');
});
```
</details>

<details>
    <summary>
    To control the click on "Select Viewing Time" radio inputs...
    </summary>

```
$('.radio-wrapper').on('click','.time-slot',function () {
    $('.time-slot').removeClass('selected');
    $(this).addClass('selected');
});
```
</details>

</details>

<details>
    <summary>
    A handy "Go back one page" function seen as the '< previous' buttons...
    </summary>

```
$(document).ready(function(){
$('.btn-back').click(function(){
    parent.history.back();
    return false;
});
```
</details>

### Manual Testing

A [Critical Pathway Method](https://asana.com/resources/critical-path-method) (CPM) using a [testing tree](https://www.optimalworkshop.com/learn/101s/tree-testing/) process has been used to documented the manual testing process. This has been integrated with the [GitHub issues management utility](https://github.com/roeszler/reabook/issues) to collect and coordinate testing within each defined User Story for the project. 

In the CPM, users/testers complete tasks by clicking through the app in a sequential way. In a live version the results of the task would indicate:
* How many users got it right?
* How many users got it wrong?
* The paths users took before they selected an answer.
* How long it took users to complete the task?

For the purposes of this project, manual feature testing was performed within each sprint cycle of the development process. These sprints (or [milestones](https://github.com/roeszler/reabook/labels/test)) were managed in the GitHub repository. Testing was tracked using the "[test](https://github.com/roeszler/reabook/labels/test)" label, that was defined to work across the whole project. 

Transposed over this process was a testing tree, used as an information radiator and keep the progress of the testing at one visual location.
<details>
    <summary>
    Reabook and testing tree...
    </summary>

* Sample Only:

![critical pathway and testing tree](static/documentation/img/reabook-test-tree.png).
</details>

### Bugs & Debugging
At the point of deployment, the site appears to be free of errors and bugs. The coordination and management of a systematic debugging process can be seen at:
- [Sample Template to Notifying Team of a Bug](https://github.com/roeszler/reabook/issues/50)
- [Summary of Bugs](https://github.com/roeszler/reabook/issues?q=is%3Aissue+is%3Aopen+label%3Abug)

### Validator Testing of Custom Code
The manipulation of `.html` documents throughout the project highlights limitations the generic W3 html Validator. The use of things like 'includes templates' and `{{  }}` or `{%  %}` consistently throws errors in the validator. Outside of these errors, that code has been thoroughly checked and no other errors were found when passing each `.html` document through the [W3 Markup Validator](https://validator.w3.org/);
    * Results : [All right.](https://validator.w3.org/nu/?doc=https%3A%2F%2Freabook.herokuapp.com%2F)

        <details>
        <summary>
        Results Image...
        </summary>

        ![CSS Passed](static/documentation/img/W3-Html-Validation.png)
        </details>

* [W3 CSS Validator](https://jigsaw.w3.org/css-validator/)
    * No errors were found when passing through the W3 CSS validator
    * Results URL : [No Error Found.](https://jigsaw.w3.org/css-validator/validator)
    
        <details>
        <summary>
        Results Image...
        </summary>

        ![CSS Passed](static/documentation/img/WC3-css.png)
        </details>

    
* [PEP8 Python Validator](https://pypi.org/project/pep8/)
    * No errors were found when passing through the PEP8 validator
    * Results : [All right]()

## 9. Deployment
This project was deployed using the Django Framework into Heroku. The steps to deploy are as follows:

* Fork or clone the [Code-Institute-Org: python-essentials-template](https://github.com/Code-Institute-Org/python-essentials-template)
* Click the Use this template to create a clone in GitHub
* Follow Display environment settings below:
### Display Environment (GitHub / GitLab / BitBucket)

The application has been deployed to GitHub pages. 

<details>
<summary>
The steps to deploy a clone of the GitHub repository...
</summary>

* Create / open an existing repository for the project with the name of your choice on your GitHub, GitLab or Bitbucket account page.
* Navigate within the GitHub repository you chose, and then navigate to the "settings" tab, which displays the general title.
* On the left hand navigation menu, I selected the "pages" option midway down the menu.
* At the top of the pages tab, the source section drop-down menu changed to select the branch: "main" with the folder selected as `"/(root)"`
* Committed to the save and waited a few moments for the settings to coordinate with the server. 
* On refresh of the browser, the dedicated ribbon changed to the selected web address, indicating a successful deployment.

> The live application link can be found here - https://reabook.herokuapp.com/

> The accessible GitHub repository for this application is https://github.com/roeszler/reabook
</details>

### Development Environment (GitPod)
The application has been deployed to GitPod pages during development. 

<details>
<summary >
The steps to deploy the project from GitHub to GitPod... 
</summary>

* In the GitHub, GitLab or Bitbucket account page where you created a repository for the project, navigate to the tab titled `'<> Code'`
* From here, navigate to the button on the top right of the repository navigation pane titled 'Gitpod'.
* If you press this it will create a new GitPod development environment each time.
</details>

<details>
<summary >
Alternatively, if you have already created the GitPod environment for your project...
</summary>

* In the browser’s address bar, prefix the entire URL with [gitpod.io/#](https://gitpod.io/#) or [gitpod.io/workspaces](https://gitpod.io/workspaces) and press Enter. This will take you to a list of workspaces that have been active within the past 14 days.
* Search for the workspace you wish to work on and access the link to it that lies within the pathway `https://gitpod.io/`.
* Sign in to the workspace each time with [gitpod.io/#](https://gitpod.io/#) using one of the listed providers (GitHub / GitLab / BitBucket) and let the workspace start up.
* On navigating to the workspace for the first time, it may take a little while longer than normal to initially install all it needs. Be patient.
* It is recommend that you install the GitPod browser extension to make this a one-click operation into the future.
</details>

### Full Stack Development Framework Environment (Django+Python)
A variety of frameworks are available for software development to provide generic functionality quickly. For the purposes of this project, the Django framework was used. A comprehensive tutorial of this process can be found at: [Django app Tutorial](https://docs.djangoproject.com/en/4.1/intro/tutorial01/).

<details>
<summary >
The basic CLI installation steps to install Django and dependencies...
</summary>

* pip3 install 'django<4'
* pip3 install gunicorn
* pip3 install dj_database_url
* pip3 install psycopg2
* pip3 install dj3-cloudinary-storage
* pip3 install django-allauth
* pip3 install pillow
* pip3 install django-countries
* pip install django-crispy-forms
* pip3 freeze --local > requirements.txt
* django-admin startproject proj_reabook .
* python3 manage.py startapp app_properties
* python3 manage.py startapp app_home
* python3 manage.py startapp app_bookings
* python3 manage.py startapp app_diary
</details>

<details>
<summary >
Once database models are configured...
</summary>

* python3 manage.py makemigrations --dry-run
* python3 manage.py makemigrations
* python3 manage.py migrate --plan
* python3 manage.py migrate
* python3 manage.py loaddata 'model_name'
</details>


### Deployment Environment (Heroku)
<details>
<summary >
The steps to create a server side Database and deploy to Heroku...
</summary>

* Login Heroku and create new Heroku app
* In 'settings' tab: set the buildpacks to `heroku/python`.
* In 'resources' tab: search and set the add-on to `heroku-postgresql` under a `hobby-dev` plan.
* In 'settings' tab: Reveal config vars, add and save KEY : VALUE variables in this order :
  * CREDS : Copy and paste entire contents of 'your' creds.json file
  * PORT : 8000
  * DATABASE_URL : Ensure a copy of the DATABASE_URL indicates something starting with `postgres://`.
  * SECRET_KEY : generate a unique key your self or somewhere like [netlify](https://django-secret-key-generator.netlify.app/)
* Within 'deploy' tab: choose GitHub as deployment method and link app to the repository
* Choose 'Deploy Branch' option you prefer.
* Optionally create and maintain a `env.py` file in you development environment using `.gitignore` functionality.

</details>

## 10. Credits
### Content

* Hosted at [Heroku](https://www.heroku.com/platform).
* Repository and issue management features provided at [GitHub](https://github.com/roeszler/reabook).
* Developed using the [GitPod Development Environment](https://www.gitpod.io/).
* Primary and additional Python coding was studied and reworked from modules provided through the Code Institute's [Diploma in Full Stack Software Development](https://codeinstitute.net/se/full-stack-software-development-diploma/), [W3 Schools](https://www.w3schools.com/), [Stack overflow](https://stackoverflow.com/), [mozilla.org](https://developer.mozilla.org/en-US/docs/Web/JavaScript) and [Django Project](https://www.djangoproject.com/).
* Testing tree process sourced from [Optimal Workshop](https://www.optimalworkshop.com/learn/101s/tree-testing/).
* Images were altered from original layout using [pixlr](https://pixlr.com/).
* Images have been stored for delivery using the [cloudinary](https://cloudinary.com/) content delivery network.
* Test Case scenarios researched from [softwaretestingo.com](https://www.softwaretestingo.com/), [Software Testing Help](https://www.softwaretestinghelp.com/test-execution-software-testing-qa-training-on-a-live-project-day-5/) and [QA Test Lab](https://qatestlab.com/).
* Code styling and error detection by systematic code refactoring following a run of the `python3 -m flake8` command to evoke the [flake8](https://flake8.pycqa.org/en/latest/) style enforcement tool.

### Media
- The photos, videos and vector graphics used on the home and each for property were sourced and/or researched from [Pexels](https://www.pexels.com/collections/aparments-9aglwiv/), [pixbay.com](https://pixabay.com/users/openclipart-vectors-30363/) and [freepik.com](https://www.freepik.com/home).
  * All property images - sourced from users seen in curated pexels collection [apartments](https://www.pexels.com/collections/aparments-9aglwiv/).
  * 404 imagery sourced from user [storyset](https://www.freepik.com/author/stories) on [freepik.com](https://www.freepik.com/home).
  * No Image picture sourced from user [Code Institute](https://github.com/Code-Institute-Solutions) walkthrough project [boutique_ado_v1](https://github.com/Code-Institute-Solutions/boutique_ado_v1/blob/250e2c2b8e43cccb56b4721cd8a8bd4de6686546/media/noimage.png).
  * All icons sourced and edited from [Font Awesome](https://fontawesome.com/).

---
__COPYRIGHT NOTICE__ :

 *The ReaBook site is a functional program intended for educational purposes at the time of coding. Notwithstanding, it has been written as a proof of concept and invitation to treat for a business [reabook.net](https://reabook.net/) and possible stakeholders into the future. Copyrights for code, ideas, concepts and materials strictly lies with Stuart Roeszler © 2022. All rights reserved.*