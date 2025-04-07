# Pytest: What, Why, and How!

## Installing packages and running the server

The below commands assume you are using Mac / Linux. If you're using windows these commands will need to be adjusted slightly. 

1. Clone the repository using "git clone https://github.com/jdgsmallwood/cookies-testing"
2. Run setup.sh to set up the environment. This will launch a JupyterLab session.

If the above script does not work for any reason, follow these steps:
1. Create a virtual environment using "python3 -m venv .venv". If using Windows you may need to use "python -m venv .venv"
2. Activate the virtual environment using "source .venv/bin/activate". If using Windows this will be ".venv/Scripts/activate".
3. Install UV - a fast replacement for pip "pip install uv".
4. Use UV to install the requirements "uv pip install -r requirements.txt".
5. Run the jupyter server with "jupyter lab". If you already have a jupyter server running - try a different port with "jupyter lab --port 8889" for example.

