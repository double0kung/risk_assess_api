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

### Users

GET /users: Retrieve a list of all users
GET /users/{user_id}: Retrieve information about a specific user
POST /users: Create a new user
PUT /users/{user_id}: Update information about a specific user
DELETE /users/{user_id}: Delete a specific user

### Assets

GET /assets: Retrieve a list of all assets
GET /assets/{asset_id}: Retrieve information about a specific asset
POST /assets: Create a new asset
PUT /assets/{asset_id}: Update information about a specific asset
DELETE /assets/{asset_id}: Delete a specific asset

### Threats

GET /threats: Retrieve a list of all threats
GET /threats/{threat_id}: Retrieve information about a specific threat
POST /threats: Create a new threat
PUT /threats/{threat_id}: Update information about a specific threat
DELETE /threats/{threat_id}: Delete a specific threat

### Risks

GET /risks: Retrieve a list of all risks
GET /risks/{risk_id}: Retrieve information about a specific risk
POST /risks: Create a new risk
PUT /risks/{risk_id}: Update information about a specific risk
DELETE /risks/{risk_id}: Delete a specific risk

### Reports

GET /reports: Gnerate a report for specific user.



## App's ERD:
![DBeaver ERD RiskAssessAPI](https://user-images.githubusercontent.com/60038702/225978630-98a001cc-3b6f-482a-80bc-706fc89d2200.png)


## Detail any third party services:

POSTMAN
DBeaver
certifi==2022.12.7
charset-normalizer==3.1.0
click==8.1.3
colorama==0.4.6
Flask==2.2.2
Flask-JWT-Extended==4.4.4
flask-marshmallow==0.14.0
Flask-SQLAlchemy==3.0.3
greenlet==2.0.2
gunicorn==20.1.0
idna==3.4
itsdangerous==2.1.2
Jinja2==3.1.2
MarkupSafe==2.1.2
marshmallow==3.19.0
marshmallow-sqlalchemy==0.29.0
packaging==23.0
psycopg2-binary==2.9.5
PyJWT==2.6.0
python-dotenv==0.21.1
requests==2.28.2
six==1.16.0
SQLAlchemy==2.0.6
typing_extensions==4.4.0
urllib3==1.26.15
Werkzeug==2.2.2

POSTMAN - A tool used for testing API endpoints using CRUD methods (GET, POST, DELETE, PUT)
DBeaver - A database management tool used for connecting to various database systems, executing SQL queries, and viewing and modifying database structures and data.

The rest are Python packages used to build the Flask application and provide additional functionality like managing environment variables, managing database connections, serialization and deserialization of data, and managing web requests and responses.

## Project's models and relationships:

My project uses Flask SQLAlchemy to define several models, each representing a different data entity in my application. These models define the attributes and relationships of the entities with each other.

One of the models is the Asset model, which describes the assets in the system and includes attributes such as their name, type, owner, location, value, and description. Assets are linked to users through a foreign key relationship.

Another model is the Report model, which captures information about risk assessment reports. This includes asset details like name, type, owner, location, value, and description, as well as information about threats such as name, type, and description. Reports are also linked to users through a foreign key relationship.

The Risk model represents the risk scores associated with a specific asset and threat pair. It includes attributes such as impact, likelihood, risk score, and risk rating, and is linked to users, assets, and threats through foreign key relationships.

The Threat model captures information about the different types of threats in the system, including their name, type, and description.

Finally, the User model describes the user accounts in my application and includes attributes like email, first name, last name, and password. The User model is used to associate users with assets, reports, and risks through foreign key relationships.

Unfortunately, due to time constraints and distractions, I haven't been able to create additional models such as controls to be applied to risks.

## Database relations implementation:

Flask SQLAlchemy is used to create models that represent different data entities in the application. These models have attributes that describe their properties, and they also have relationships with other models.

For example, the User model describes the users in the application. The User model has attributes such as email, first name, last name, and password. There is also an Asset model that describes assets in the system, including attributes such as name, type, owner, location, value, and description.

To create a relationship between these two models, a foreign key constraint is used. Specifically, a user_id column is added to the Asset model, which references the id column of the User model. This creates a one-to-many relationship between users and assets, meaning that a user can have many assets, but an asset can only belong to one user.

Similarly, there is a Threat model that describes the different types of threats in the system. The Threat model has attributes such as name, type, and description. There is also a Risk model that represents the risk scores associated with a specific asset and threat pair, including attributes such as impact, likelihood, risk score, and risk rating.

To create relationships between these models, foreign key constraints are also used. Specifically, asset_id and threat_id columns are added to the Risk model, which reference the id columns of the Asset and Threat models, respectively. This creates a many-to-many relationship between assets and threats, meaning that an asset can be associated with many threats, and a threat can be associated with many assets.

Finally, there is a Report model that captures risk assessment reports, including information about assets and threats. To create relationships between the Report model and other models, nested fields in the schema are used. Specifically, the Nested() method is used to nest instances of the AssetSchema, ThreatSchema, and RiskSchema inside the ReportSchema. This allows information about the associated assets, threats, and risks to be included in the serialized output.

Overall, by using foreign key constraints and nested fields in the schema, a robust database relations implementation can be created that accurately reflects the relationships between the different data entities in the application.

## Describe the way tasks are allocated and tracked in your project:

To allocate and track tasks for this project, I am using [notion.io](https://imminent-trumpet-dda.notion.site/6a0e9bdb1c214401aaf38007c07028a0?v=533cd0ff09cd47a3baf2bf4798fcbee8). Specifically, I am including relevant URLs in task comments to provide additional context, and organizing the tasks on a kanban board to easily visualize their progress.


