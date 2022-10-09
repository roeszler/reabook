<!-- ![Reabook.net](https://res.cloudinary.com/yodakode/image/upload/v1661790281/ReaBook/ReaBook_Icon_00402B_gray_szgzia.ico) -->
# ReaBook Booking System

> **ReaBook** - attracts and drives initial bookings to view real estate for sale, rent or lease.

## Full Stack Toolkit with Django - [Code Institute](https://codeinstitute.net/)

### Applying: HTML, CSS, JavaScript, Python+Django, Relational Databases (PostgreSQL), c

* Repository link : https://github.com/roeszler/reabook
* Terminal : https://reabook.herokuapp.com/
* User Stories : https://github.com/users/roeszler/projects/4
<!-- * GitPod Admin Panel : [GP Admin Log In](https://8000-roeszler-reabook-nqaw4dtiyn0.ws-eu62.gitpod.io/admin/login/) -->
<!-- * Heroku Admin Panel : [HK Admin Log In](https://reabook.herokuapp.com/admin/) -->
---

<details>
<summary style="font-size: 1.5rem;">Table of Contents (dropdown list)</summary>

1. [Project Purpose](#1-project-purpose)
2. [Agile Development Process](#2-agile-development-process)
    * [Requirements Engineering](#21-understanding-requirements)
        * [User Centered Design](#22-implementation)
        * [Defining Requirements](#defining-the-requirements)

2. [User Experience Design](#2-user-experience-design)
    * [User Stories](#user-stories)
        * [First Time Visitor Goals](#first-time-visitors)
        * [Returning Visitor Goals](#returning-visitors)
        * [Coding Colleagues](#coding-colleagues)
    * [Design](#design)
        * [Imagery](#imagery)
        * [Fonts](#fonts)
        * [Color Scheme](#color-scheme)
        * [Site Mockup & Wireframe](#site-mockup--wireframe)
3. [Features](#3-features)
    * [Existing Features](#existing-features)
        * [Splash Screen (Gameplay & Rules)](#splash-screen--rules)
        * [Game Area](#game-area)
        * [Bet Amount Area](#bet-amount-area)
        * [Bet Type Area](#bet-type-area)
        * [Spin Button](#spin-button)
        * [Score Area](#score--bank-balance-area)
        * [Footer](#footer)
        * [PopUps](#popups-modals)
        * [Record User Choices](#choice-html)
    * [Future Features](#possible-future-features)
4. [Technologies](#4-technologies)
    * [Tools](#tools)
    * [Browsers](#supported-screens-and-browsers)
5. [Testing](#5-testing)
    * [Issues and Resolutions](#issues--resolutions)
    * [Validator Testing](#validator-testing)
6. [Deployment](#6-deployment)
    * [Display Environment](#display-environment-github--gitlab--bitbucket)
    * [Development Environment](#development-environment-gitpod)
7. [Credits](#7-credits)
    * [Content](#content)
    * [Media](#media)
</details>

---

## 1. Project Purpose

ReaBook (the Site) is the skeleton of a real estate advertising site used to present the deployment of an appointment booking system (the App) using a Full Stack Framework.

### Database Functionality

At the time of release, the site is deployed via the [Heroku](https://www.heroku.com/platform) platform at https://reabook.herokuapp.com/. Here users can:
* Select and submit requests to attend store owner users arranged viewing times for properties listed for sale or rent.
    > Main nav > Book > (login) > Reabook Viewings

* Create, retrieve and navigate through orders to update information, check production status and/or re-book properties.
    > Create = Book Viewings button

    > Retrieve = View / Edit link

    > Navigate = Quick Links / My ReaBook menus

* Agent / Member / Admin users can list, edit and advertise times for potential customers to view properties currently for sale or rent in their business portfolio.
    > Property List = Manage Properties > Add Property

    > Property Edit = Manage Properties > Edit / Delete

### Note:

The ReaBook business premise is to collate and drive leads into existing appointment management systems, **not** provide appointment management service.

It is acknowledged that most all real estate services will already have well developed appointment management processes. The ReaBook app is focused to enhance the lead generation into these systems and provide advertising of properties to future clients across all agents. More akin to a cross-agency site to dive leads for properties available for sale, rent, or spaces to lease.

<div align="right">

[Back to Top :arrow_up:](#table-of-contents)

</div>

## 2. Agile Development Process

This project (ReaBook) has been developed following an Agile methodology. As part of the assessment process at the [Code Institutes](https://codeinstitute.net/) - [Full Stack development program](https://codeinstitute.net/se/full-stack-software-development-diploma/). 

Created by student developer; [Stuart Roeszler](https://www.linkedin.com/in/stuartroeszler/). In light of this, some of the project management processes such as [team velocity](#team-velocity) and [information radiators](#information-radiators) are outlined only, however would form a crucial part of a live, team based project.
### 2.1 Requirements Engineering
#### User Centered Design (UCD) Process:
* Planning followed a User Centered Design (UCD) Process to identify and structure the development process.
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

---

### Defining the Requirements
Project requirements for a project such as ReaBook would be sourced from activities undertaken in the UCD [strategy](static/documentation/ucd/1-strategy.md) and [scope](static/documentation/ucd/2-scope.md) panes.

### Requirements Analysis
Important that the requirements defined are actually understood. Important to check and record each requirement is:    
* Clear
* Non-conflicting
* Has passed a trade-off process between owner and developer: Importance vs Feasible 

Consideration and documentation at this point as to:
* How will each requirement be implemented?
* How will each requirement be Tested?
* What is the process to evaluate each requirement? (to meet initial requirements)

<details>
<summary style="font-size: 1rem;">
Sample format of a user story with acceptance criteria for the ReaBook project
</summary>


</details>

### 2.2 Implementation
#### Theme
#### Epics

<details>
<summary style="font-size: 1rem;">
Epics
</summary>
        
- Epics
    - [User Experience]()
    - [Site Framework]()
    - [Dataset Design]()
    - [Read Dataset]()
    - [Display Properties / Products]()
    - User Profile
        - [Admin User]()
        - [Agent Member]() User (staff)
        - [Customer User]()
    - [Sign In]()
    - [Register]()
    - [Create Property Listing]() (staff)
    - [Edit Property Listing]() (staff)
    - [Delete Property Listing]() (staff)
    - [Book Viewing]()
    - [Edit Viewing]()
    - [Delete Viewing]()
</details>

<details>
    <summary style="font-size: 1rem;">
    User Persona (sample)
    </summary>
        
![user_persona](static/documentation/wireframes/Bookings_Page.png)

</details>

<details>

#### User Stories
- Cards: https://github.com/users/roeszler/projects/4/views/1
- Acceptance Criteria
- Tasks
- Story Point Value
- 

<summary style="font-size: 1rem;">
User Stories
</summary>

- [Customer User](https://github.com/roeszler/reabook/labels/User%20%28Customer%29)
- [Agent / Member User](https://github.com/roeszler/reabook/labels/User%20%28Member%29)
- [Admin User](https://github.com/roeszler/reabook/labels/User%20%28Admin%29)

</details>

### 2.3 Project Management
Continuing to promote the Agile framework of software development, where possible I implemented the following during completion of each [user story](https://github.com/roeszler/reabook/issues):  
### Story Point Estimation
Difficult to estimate with current level of experience, focused on the amount of work done posthumously in most cases. This was primarily due to the errors that came with each development iteration and the relative simple or solutions to solve the problem. 

One such instance was the inclusion of a django dropdown as part of the booking process. This was aimed to sequentially lead the user booking a viewing appointment to the next step. The combined front end JavaScrip and backend Python solution to achieve the sequential update and display of the data entered became too large for the story points I had assigned to the task. 

In this way I refactored the code to provide a more basic, consistent user experience that was achievable in the timeframe. 

### Team Velocity
Considers an average amount of story points the development 'team' can manage to finish in one iteration of a particular length.

In the development of the ReaBook project, focus was placed on gathering experience and testing hypotheses in my journey as a student. In light of the additional time this takes and value to the overall project or future projects at this point in time, Team Velocity has not been calculated for a single student developer.


### MoSCow Prioritization
This technique was invaluable to each stage of the development process. The looping approach of Agile development and continuous revision throughout each sprint, I employed MoSCow with great effect. Each task was reviewed and re-reviewed considering where it's importance lies:
* Must Have - non negotiable (core, legal, security)
* Should Have - if work around available, not vital. Add significant value. (Performance improvements, minor defects fixes, new functionality).
* Could Have - delivered in their entirety in a best-case scenario. When a problem occurs and the deadline is at risk, one or more “could-have” items are dropped.
* Won’t Have - Agile team has agreed that the PBI wouldn’t be delivered. Possible reschedule to later iterations? Recorded to manage expectations always.

The culmination of the MoSCow prioritization process can be seen in those with an [on hold](https://github.com/roeszler/reabook/labels/on%20hold), [wontfix](https://github.com/roeszler/reabook/labels/wontfix) or [future release](https://github.com/roeszler/reabook/labels/future%20release) tag respectively.

### Information Radiator(s)
As real-time, informative and straightforward work status display, a magnetic whiteboard with post-it notes was used to clarify current tasks and manage development time. 

Common contents included:
* Remaining user stories,
* User stories’ status in the current iteration,
* The progress toward the next sprint,  
* Total numbers of open defects
* Further research / assistance required

### Sprints
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

## 3. Wireframes

<details>
    <summary style="font-size: 1rem;">
    Initial Concept - Booking App Wireframe
    </summary>
        
![Booking App Page Wireframe](static/documentation/wireframes/Bookings_Page.png)
</details>

<details>
    <summary style="font-size: 1rem;">
    Initial Concept - Landing Page Wireframe
</summary>

![Booking App Page Wireframe](static/documentation/wireframes/ReaBook_Index_v1.0.png)
</details>

## 4. 

<!-- ## X. Assets
- **Cloudinary**:
  The video files itself are not stored in the Focus database, they are linked with a url from a video hosting server. Focus fitness uses [Cloudinary](https://cloudinary.com/).

<details>
<summary>How To add an image to Cloudinary and add to ReaBook.</summary>

1. Make a Cloudinary account.
2. Login and make a file to keep you videos in.
3. Upload the image, when if has finished it will show you the Url.
4. Copy the Url.
5. In the ReaBook admin section click on properties tab in the app_properties section.
6. Click ‘Add Property'.
7. Fill out all the fields in the form.
8. Where it says 'Image url' paste in the videos url.
9. Press 'Save'.

</details> -->