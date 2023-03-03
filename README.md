# risk_assess_api



## Identification of the problem you are trying to solve by building this particular app:

For this API web server project, I'm attempting to create a cyber security risk management API that allows users to manage and assess risks associated with their assets, controls, and threats. The goal is to help individuals and organisations better understand and mitigate the potential risks they face in the digital world. With this API, users can track and manage their assets, threats, and controls, as well as calculate risks and generate reports to help them make informed decisions about their cyber security.



## Why is it a problem that needs solving?

In recent years, there has been a significant increase in cyber attacks, especially with the rise of remote work due to the COVID-19 pandemic. As a result, the need for effective risk management and cybersecurity measures has become more important. Businesses are seeking solutions to mitigate cyber risks to protect their assets, data, and reputation. By creating this API, I aim to provide a tool that helps businesses manage their cybersecurity risks more effectively and efficiently.



## Database System:

For the Risk Assess API, I have chosen to use PostgreSQL as the database system. PostgreSQL is a popular and powerful open-source relational database system that provides robust features for data integrity and consistency. Compared to other database systems like MySQL and SQLite, PostgreSQL has better support for concurrency control and handling of complex queries, making it suitable for applications with heavy database usage.

MySQL is another popular open-source relational database system that is widely used in web applications. While it is known for its performance and scalability, MySQL has limitations in terms of data consistency and transactional support compared to PostgreSQL.

SQLite, on the other hand, is a lightweight and self-contained relational database system that requires no separate server process or setup. While it is suitable for small-scale applications that don't require complex queries or data consistency guarantees, it may not be a good fit for applications with larger data volumes or concurrent usage.

Overall, I have chosen PostgreSQL for the Risk Assess API due to its strong support for data integrity and concurrency control, making it a reliable choice for a risk management application that involves sensitive and critical data.



## Identify and discuss the key functionalities and benefits of an Object-Relational Mapping:
![image](https://user-images.githubusercontent.com/60038702/222720193-5e63eebb-0623-4de3-9122-2c766af4459d.png)
Reference: https://www.youtube.com/watch?v=0sOvCWFmrtA -Course from Sanjeev Thiyagarajan

ORM provides a way to interact with a database using object-oriented programming. This simplifies the code and reduces the need for complex SQL statements. Using an ORM such as SQLAlchemy allows us to map the database tables to classes, and perform CRUD (create, read, update, delete) operations on these objects. This provides benefits such as increased productivity, better code organization, and easier maintenance. Additionally, it can help with security by preventing SQL injection attacks.



## Endpoints:

GET /users: Retrieve a list of all users

GET /users/{user_id}: Retrieve information about a specific user

POST /users: Create a new user

PUT /users/{user_id}: Update information about a specific user

DELETE /users/{user_id}: Delete a specific user

GET /assets: Retrieve a list of all assets

GET /assets/{asset_id}: Retrieve information about a specific asset

POST /assets: Create a new asset

PUT /assets/{asset_id}: Update information about a specific asset

DELETE /assets/{asset_id}: Delete a specific asset

GET /controls: Retrieve a list of all controls

GET /controls/{control_id}: Retrieve information about a specific control

POST /controls: Create a new control

PUT /controls/{control_id}: Update information about a specific control

DELETE /controls/{control_id}: Delete a specific control

GET /threats: Retrieve a list of all threats

GET /threats/{threat_id}: Retrieve information about a specific threat

POST /threats: Create a new threat

PUT /threats/{threat_id}: Update information about a specific threat

DELETE /threats/{threat_id}: Delete a specific threat

GET /risks: Retrieve a list of all risks

GET /risks/{risk_id}: Retrieve information about a specific risk

POST /risks: Create a new risk

PUT /risks/{risk_id}: Update information about a specific risk

DELETE /risks/{risk_id}: Delete a specific risk

GET /reports: Retrieve a list of all reports

GET /reports/{report_id}: Retrieve information about a specific report

POST /reports: Create a new report

PUT /reports/{report_id}: Update information about a specific report

DELETE /reports/{report_id}: Delete a specific report

GET /risk_calculators: Retrieve a list of all risk calculators

GET /risk_calculators/{calculator_id}: Retrieve information about a specific risk calculator

POST /risk_calculators: Create a new risk calculator

PUT /risk_calculators/{calculator_id}: Update information about a specific risk calculator

DELETE /risk_calculators/{calculator_id}: Delete a specific risk calculator

GET /control_risks: Retrieve a list of all control risks

GET /control_risks/{control_risk_id}: Retrieve information about a specific control risk

POST /control_risks: Create a new control risk

PUT /control_risks/{control_risk_id}: Update information about a specific control risk

DELETE /control_risks/{control_risk_id}: Delete a specific control risk



## App's ERD:


##Detail any third party services:

Flask-RESTful

Flask-Security

Pytest



## Project's models and relationships:


## Database relations implementation:

## Describe the way tasks are allocated and tracked in your project:

To allocate and track tasks for this project, I am using [notion.io](https://imminent-trumpet-dda.notion.site/6a0e9bdb1c214401aaf38007c07028a0?v=533cd0ff09cd47a3baf2bf4798fcbee8). Specifically, I am including relevant URLs in task comments to provide additional context, and organizing the tasks on a kanban board to easily visualize their progress.


