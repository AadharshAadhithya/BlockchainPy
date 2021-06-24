# Simple Simulation of Blockchain in Python
_Aadharsh Aadhithya_

# Usage
 Install the dependencies
`pip install -r requirements.txt`
From the terminal fire the app
`python app.py`
python development server should be up and running

# Endpoints
- `{http://{localhost}/chain}`
    - Allowed methoeds:
        - 'GET' : Returns the chain of the blockchain
- `http://{localhost}/mine}`
    - Allowed methoeds:
        - 'POST':  POST `data` in JSON format. `data` is read to be the data of the newly mined block.Redirects to `{http://{localhost}/chain}`

## Get all Blocks in chain through GET request to `{http://{localhost}/chain}`
![image info](./chainroute.png) 

## MINE A BLOCK THROUGH POST REQUEST TO `{http://{localhost}/mine}`
![image info](./mineroute.png) 

# To Be Added
- P2P communication must be eshtablished.

