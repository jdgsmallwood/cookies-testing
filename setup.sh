python3 -m venv .venv
source .venv/bin/activate
pip install uv
uv pip install -r requirements.txt
jupyter lab
