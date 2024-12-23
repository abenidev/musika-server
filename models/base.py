from sqlalchemy.ext.declarative import declarative_base

# SQLAlchemy ORM setup
"""
This code snippet is using SQLAlchemy's declarative_base function to 
create a base class for declarative class definitions. 
The base class is typically used as the base class for 
other classes in the application to define the structure of database tables. 
In this case, the variable Base is assigned the base class.
"""
Base = declarative_base()
