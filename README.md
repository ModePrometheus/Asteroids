# Asteroids
A python project to recreate the game asteroids. This is for a guided project from the Boot.dev curriculum.
This will require installing dependencies, so navigate to the game folder either in a terminal or file explorer
and your OS specific option of open in terminal then:

// this installs the dependencies
pip install -r requirements.txt
// this will run the game from the command line
python3 main.py

Or if you want to install the dependencies exlusively in the game folder, you will need to create a virtual 
environment, so while in the game folder in the terminal:

// this creates the virtual environment
python3 -m venv venv
// this essentially "turns on" the environment
source venv/bin/activate
// now the dependency install
pip install -r requirements.txt
// lastly run the game
python3 main.py

Now keep in mind that if you create a virtual environment, you will need to activate it every time you want to open
the game unless you keep the terminal window open all the time.

Notes:
1. This is a W.I.P application
2. currently the only ways to open the game is through the command line or if you're on windows and installed the 
dependencies without a virtual environment you can probably open it with the GUI python interpreter on windows.