# Accounting Web Application

This is an accounting web application designed to help users manage their financial transactions, track their profit and loss, and generate balance sheets and cash flow statements.


[![Python Badge](https://img.shields.io/badge/Python-YourColor?style=for-the-badge&logo=Python&logoColor=yellow)](https://www.python.org/) [![Django Badge](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=blue)](https://docs.djangoproject.com/en/4.2/) 
[![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)](https://www.sqlite.org/docs.html)
[![Bootstrap Badge](https://img.shields.io/badge/bootstrap-%23563D7C.svg?style=for-the-badge&logo=bootstrap&logoColor=white)](https://getbootstrap.com/)
[![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)](https://www.django-rest-framework.org/) [![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)](https://www.geeksforgeeks.org/html5-introduction/) [![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)](https://www.w3.org/Style/CSS/Overview.en.html)
[![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)](https://www.w3schools.com/js/)


## Features

1. **User Authorization: **
   - Secure user registration with email confirmation.
   - Login functionality with authentication checks.
   - Logout feature for user sessions.
   - Customized password reset functionality for enhanced security.
  
2. **Transaction Management**:
    - Add, edit, and delete financial transactions.

3. **Profit and Loss Tracking**:
   - Effortlessly Monitor your sales, expenses, and track overall profit/loss.

4. **Balance Sheet**:
   - Gain insights into your financial health by viewing assets, liabilities, and equity.

5. **Cash Flow Analysis**: Analyze cash inflow and outflow for better financial planning.
   - Analyze cash inflow and outflow for better financial planning.

## Getting Started

### Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.x installed
- Django installed
- A modern web browser

### Installation

1. Clone the repository:

        git clone https://github.com/vivekmogalla/AccountingWebsite.git

2. Navigate to the Project directory
 
        cd AccountingWorld

3. Install python virtual environment using pip command
 
       pip install virtualenv (same for linux and windows)

4. Create a Python virtual environment
 
       virtualenv env (same for linux and windows)

5. Activate the virtual environment
 
       cd env/scripts/.activate (windows)
       source env/bin/activate (Linux)

6. Install the required Python packages

        pip install -r requirements.txt

7. Run database migrations

        python manage.py migrate

8. Create a superuser accont (for admin access)

        python manage.py createsuperuser

9. Start the development server:

        python manage.py runserver

## Usage
### User Authentication
#### Signup
1. Navigate to the signup page.

   <img width="960" alt="image" src="https://github.com/vivekmogalla/AccountingIsland/assets/131423732/7bd6f564-ff36-406d-96bc-1dc66499254e">

2. Fill out the required fields, including your email and password.

   <img width="958" alt="image" src="https://github.com/vivekmogalla/AccountingIsland/assets/131423732/e99e22bd-4592-4999-9333-346559524f9b">

3. Submit the form.

   <img width="960" alt="image" src="https://github.com/vivekmogalla/AccountingIsland/assets/131423732/aba4ae35-fdc0-4bb2-b5df-f976999923fb">

4. Check your registered email for an activation link.

   <img width="960" alt="image" src="https://github.com/vivekmogalla/AccountingIsland/assets/131423732/d8a0c0bf-a02d-4511-96bf-cf3c5c8f67e3">

5. Click on the activation link to activate your account.

   <img width="960" alt="image" src="https://github.com/vivekmogalla/AccountingIsland/assets/131423732/87f60abd-ef51-464e-a09e-2ffe7b1018ce">




#### Login
1. Visit the login page.
2. Enter your username and password.

   <img width="959" alt="image" src="https://github.com/vivekmogalla/AccountingIsland/assets/131423732/186a115f-b039-47d3-b7f8-3253c0bdcf30">

3. Click the login button.
4. If your account is activated, you will be redirected to the dashboard.

   <img width="960" alt="image" src="https://github.com/vivekmogalla/AccountingIsland/assets/131423732/6762f70a-fc5a-40ef-a821-3ad41e8a2110">


#### Logout
1. To logout, click on the logout option in the dashboard or visit the logout page.
2. You will be logged out, and redirected to the login page.

#### Password Reset
1. If you forget your password, click on the "Forgot Password" link on the login page.

   <img width="960" alt="image" src="https://github.com/vivekmogalla/AccountingIsland/assets/131423732/19ba4a95-4190-4daf-a569-1954a774dd8b">

2. Enter your email address.
3. Check your email for a password reset link.

   <img width="958" alt="image" src="https://github.com/vivekmogalla/AccountingIsland/assets/131423732/ee228493-3675-470e-b963-e868b584bf2f">

4. Click on the link to reset your password.
   
   <img width="960" alt="image" src="https://github.com/vivekmogalla/AccountingIsland/assets/131423732/4d1e326e-4715-4afd-be2f-3b1419d6fcc6">



Note: Ensure that your account is activated before logging in. Activation links are sent to your registered email during the signup process.

### Financial Management

#### Adding Transactions

1. Go to the 'Add Transactions' page.

   <img width="313" alt="image" src="https://github.com/vivekmogalla/AccountingIsland/assets/131423732/e0496749-8370-44ca-abe7-f23a66403bbf">

2. Fill in the type, date, and amount for the new transaction.

   <img width="342" alt="image" src="https://github.com/vivekmogalla/AccountingIsland/assets/131423732/09fba1fa-dafa-46c8-ab8c-1da888c832e0">

3. Submit the form to save the transaction.

#### Viewing Transactions

1. Visit the 'Transaction List' page from the dashboard, and navigate through the list using the pagination feature.

   <img width="960" alt="image" src="https://github.com/vivekmogalla/AccountingIsland/assets/131423732/68254013-350b-4dad-b0f8-5438106963b3">

3. Browse and filter transactions based on the selected account.

   <img width="960" alt="image" src="https://github.com/vivekmogalla/AccountingIsland/assets/131423732/88ed05a6-7caa-4d1a-ab6b-6aa2bfce8cbf">


#### Resetting Transactions

1. Use the 'Reset Transactions' feature to clear all transactions

   <img width="960" alt="image" src="https://github.com/vivekmogalla/AccountingIsland/assets/131423732/1909c72b-260b-4cbb-8625-58d7dcc76f30">


#### Viewing Financial Summary

1. Check the 'Balance Sheet' for insights into bank balance, debtors, VAT, etc.
2. Analyze 'Cash Flow' to understand cash inflow and outflow.
3. Calculate profit/loss with the 'Calculate Profit/Loss' function.
4. All the above 3 options are displayed in the Dashboard page as shown below.

   <img width="960" alt="image" src="https://github.com/vivekmogalla/AccountingIsland/assets/131423732/3bf4eb43-0309-430e-b4c5-4ba6e9692d6e">


Note: Make sure you are logged in to access these features. Some actions may require specific permissions based on user roles.
