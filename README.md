# CDC-Data-Reconciliation
Automating the reconciliation of case counts for infectious diseases between 50 state health departments and the CDC.

## Technologies used:

*Stack selection: Python FastAPI, React, SQLite*

For our backend selection, we have chosen to use a Python framework called FastAPI. We chose this backend because it is easy to use, creates automatic documentation, and will be able to run on basically any hardware that the state would like to use. Next, we chose to use React to create our user interface as it makes it easy to create a stateful UI and the component style makes it easy to reuse existing code. For our database component, we chose SQLite for a number of reasons: it requires no setup on the user side, it uses a file to keep its storage so it is easy to use between processes, database files can easily be transferred to another server, and the server can automatically create and set up the database. Notably, the client for this project requested that we use Python for our backend logic and also stated that using a SQL database would be preferred. The reasons for this are that these technologies are proven as well as familiar with existing employees.

## Rationale for coded portion:

*Coded portion: As a data scientist, I want to generate reports detailing differences between state and CDC case data so that I can remedy the discrepancies.*

We chose to implement this section of the program because it is the single most important and basic part of the application. Users need to be able to generate reports indicating the differences between two databases in order for any other part of the program to be useful.
