# Pytest: What, Why, and How!

## Run using binder

I've set up a binder image at https://mybinder.org/v2/gh/jdgsmallwood/cookies-testing/2b87766b56389fae05d5acb904b0c61387dde0d0?urlpath=lab%2Ftree%2Fcookies_testing.ipynb

You should be able to open that link & get a Jupyter environment already set up!

## Installing packages and running the server locally

The below commands assume you are using Mac / Linux. If you're using windows these commands will need to be adjusted slightly. 

1. Clone the repository using "git clone https://github.com/jdgsmallwood/cookies-testing"
2. Run setup.sh to set up the environment. This will launch a JupyterLab session.

If the above script does not work for any reason, follow these steps:
1. Create a virtual environment using "python3 -m venv .venv". If using Windows you may need to use "python -m venv .venv"
2. Activate the virtual environment using "source .venv/bin/activate". If using Windows this will be ".venv/Scripts/activate".
3. Install UV - a fast replacement for pip "pip install uv".
4. Use UV to install the requirements "uv pip install -r requirements.txt".
5. Run the jupyter server with "jupyter lab". If you already have a jupyter server running - try a different port with "jupyter lab --port 8889" for example.

