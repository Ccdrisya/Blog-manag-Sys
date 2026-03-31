
                        BLOG MANAGEMENT SYSTEM
                  A Python + MySQL CLI-Based Blog Platform
================================================================================

Blog Management System is a command-line based blog platform built with
Python and MySQL. It allows users to create posts, read and comment on
posts by category, and manage profiles. Admins get a separate panel to
manage users and categories with password-protected access.

--------------------------------------------------------------------------------
FEATURES
--------------------------------------------------------------------------------

  User Panel
    * Register a new account or log in as existing user
    * Create blog posts under a selected category
    * Browse posts by category (Maths, Physics, Chemistry, History, Computer)
    * Comment on any post by Post ID
    * View your profile (followers, following, owned posts)
    * Access the comment library

  Admin Panel (Password Protected)
    * View all user profiles in a table
    * Manage posts by category
    * Delete user profiles and their posts
    * 3-attempt login lockout for security

--------------------------------------------------------------------------------
TECH STACK
--------------------------------------------------------------------------------

  Language         : Python 3
  Database         : MySQL
  DB Connector     : mysql-connector-python
  Table Display    : PrettyTable

--------------------------------------------------------------------------------
DATABASE STRUCTURE
--------------------------------------------------------------------------------

  Database: blog

  Profiles Table
    id_profile    INT  AUTO_INCREMENT  PRIMARY KEY
    Username      VARCHAR(25)
    Email         VARCHAR(25)
    Followers     INT
    Following     INT
    Owned_Posts   INT
    Comments      INT

  qns Table (Posts)
    post_id       INT  AUTO_INCREMENT  PRIMARY KEY
    id_profile    INT  (Foreign Key -> Profiles)
    user_name     VARCHAR(20)
    Categories    VARCHAR(15)
    question      VARCHAR(300)

  comt Table (Comments)
    post_id       INT  (Foreign Key -> qns)
    id_profile    INT  (Foreign Key -> Profiles)
    question      VARCHAR(50)
    comment       VARCHAR(20)

  Categories supported: MATHS, PHYSICS, CHEMISTRY, HISTORY, COMPUTER

--------------------------------------------------------------------------------
PROJECT STRUCTURE
--------------------------------------------------------------------------------

  Blog-manag-Sys/
      blog.py           Main Python file (all logic in one script)
      README.md

--------------------------------------------------------------------------------
INSTALLATION & SETUP
--------------------------------------------------------------------------------

1. Clone Repository
   git clone https://github.com/Ccdrisya/Blog-manag-Sys.git
   cd Blog-manag-Sys

2. Install Dependencies
   pip install mysql-connector-python prettytable

3. Configure MySQL
   Make sure MySQL is running locally.
   Default credentials used in the project:

     Host     : localhost
     User     : root
     Password : root

   Update these in blog.py if your credentials are different.

4. Run the Program
   python blog.py

   The database and all tables are created automatically on first run.

--------------------------------------------------------------------------------
HOW TO USE
--------------------------------------------------------------------------------

  On launch, you will see the HOMEPAGE menu:

    1. Admin Panel  -->  Enter password (default: 1234) to access dashboard
    2. User         -->  Register or log in to start posting

  User Flow:
    a. Create a Post  -->  Enter username, category, and your question/post
    b. Read           -->  Browse by category, comment on posts
    c. Profile        -->  View your profile stats
    d. Exit

  Admin Flow:
    1. Profile Manager  -->  View all users, see their posts, delete accounts
    2. Category Manager -->  Browse posts filtered by category
    3. Exit

--------------------------------------------------------------------------------
AUTHORS
--------------------------------------------------------------------------------

  Drisya C C
  Devika P S
  Rinit Rolly
  Christeena Francis

================================================================================
