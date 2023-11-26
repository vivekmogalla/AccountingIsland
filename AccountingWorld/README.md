# Accounting Web Application

This is an accounting web application designed to help users manage their financial transactions, track their profit and loss, and generate balance sheets and cash flow statements.

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

3. Install the required Python packages

        pip install -r requirements.txt

4. Run database migrations

        python manage.py migrate

5. Create a superuser accont (for admin access)

        python manage.py createsuperuser

6. Start the development server:

        python manage.py runserver
