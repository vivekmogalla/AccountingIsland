# Accounting Web Application

This is an accounting web application designed to help users manage their financial transactions, track their profit and loss, and generate balance sheets and cash flow statements.


[![Python Badge](https://img.shields.io/badge/Python-YourColor?style=for-the-badge&logo=Python&logoColor=yellow)](https://www.python.org/) [![Django Badge](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=blue)](https://docs.djangoproject.com/en/4.2/) 
[![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)](https://www.sqlite.org/docs.html)
[![Bootstrap Badge](https://img.shields.io/badge/bootstrap-%23563D7C.svg?style=for-the-badge&logo=bootstrap&logoColor=white)](https://getbootstrap.com/)
[![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)](https://www.django-rest-framework.org/) [![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)](https://www.geeksforgeeks.org/html5-introduction/) [![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)](https://www.w3.org/Style/CSS/Overview.en.html)
[![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)](https://www.w3schools.com/js/)


## Features
- **Transaction Management**: Add, edit, and delete financial transactions.


- **Profit and Loss Tracking**: Monitor your sales, expenses, and overall profit/loss.


- **Balance Sheet**: View your assets, liabilities, and equity.


- **Cash Flow Analysis**: Analyze cash inflow and outflow.

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