# Testing Times and How to Fix Them (with Testing)

## Learning Intentions
- Be able to explain when and why a piece of code needs tests.
- Be able to structure tests using the Arrange-Act-Assert framework.
- Be able to write and run simple tests using pytest & ipytest.
- Understand that writing testable code requires a slightly different method of writing code.
- Have all the necessary understanding to be able to start writing tests on your own code **today**.

## Why pytest? Why ipytest?
- It's my preference & what I know best.
- Other tools exist and have different tradeoffs. I think pytest is super easy to get working immediately.
- ipytest allows us to write tests directly within Jupyter notebooks.

## What are we covering today?
- What is testing? Why do we write tests?
- What code requires tests? What code does not require tests?
- What is Arrange-Act-Assert? Simple examples of testing.
- Refactoring code to make it testable.
- Public & Private functions - what to test?
- Write a test on one of your own functions.

## What are we not covering today?
- Mocking functions and objects,
- Test-driven development,


## Installing packages and running the server

The below commands assume you are using Mac / Linux. If you're using windows these commands will need to be adjusted slightly. 

1. Clone the repository using "git clone <repo_url>"
2. Create a virtual environment using "python3 -m venv .venv". If using Windows you may need to use "python -m venv .venv"
3. Activate the virtual environment using "source .venv/bin/activate". If using Windows this will be ".venv/Scripts/activate".
4. Install UV - a fast replacement for pip "pip install uv".
5. Use UV to install the requirements "uv pip install -r requirements.txt".
6. Run the jupyter server with "jupyter lab". If you already have a jupyter server running - try a different port with "jupyter lab --port 8889" for example.

