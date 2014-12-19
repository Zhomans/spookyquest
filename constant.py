#Idle Animations On/Off
ANIMATION = False

# Tile size of the level
LEVEL_WIDTH = 57
LEVEL_HEIGHT = 74

# Tile size of the viewport (through which you view the level)
VIEWPORT_WIDTH = 21
VIEWPORT_HEIGHT = 21   

VIEWPORT_WIDTH_RADIUS = (VIEWPORT_WIDTH-1)/2
VIEWPORT_HEIGHT_RADIUS = (VIEWPORT_HEIGHT-1)/2

#Offset of the screen
SCREEN_OFFSET = 1

# Pixel size of a tile (which gives you the size of the window)
TILE_SIZE = 32

# Pixel size of the viewport
WINDOW_WIDTH = TILE_SIZE * VIEWPORT_WIDTH
WINDOW_HEIGHT = TILE_SIZE * VIEWPORT_HEIGHT

# Pixel size of the panel on the right where you can display stuff
WINDOW_RIGHTPANEL = 296

#Types of Terrain
#Numbers used for simplicity
TYPE = {
    'Grass': 0,
    'Stone': 1,
    'Tree' : 2,
    'Grave': 3,
    'Wall' : 4
}

NUM_TO_TYPE = {
	0 : 'Grass',
	1 : 'Stone',
	2 : 'Tree',
    3 : 'Grave',
    4 : 'Wall'
}

#Mapping between movements and directions
DIR_TO_MOVE = {
    'Left': (-1,0),
    'Right': (1,0),
    'Up' : (0,-1),
    'Down' : (0,1)
}

MOVE_TO_DIR = {
    (-1,0): 'Left',
    (1,0): 'Right',
    (0,-1): 'Up',
    (0,1): 'Down'
}


#Character attributes
CHARACTER_HEALTH = 3
MAX_ACTIONS = 10

#Timestep of the Event Queue
QUEUE_TIMESTEP = .01

#Time waited after Grave summons a Mummy
GRAVE_WAIT_TIME = 1

#Divisions of movement when moving or switching
#Increase to make smoother
MOVEMENT_DIVISIONS = 10.0
SWITCH_DIVISIONS = 20.0

#Time in between idle animations
ANIMATION_TIME = 30

#Number of Graves
#Increase to increase difficulty
GRAVE_COUNT = 5 

#Hard-coded names
NAMES=[
"Delmar",
"Armand",
"Toby",
"Wally",
"Dominique",
"Antony",
"Doyle",
"Mauro",
"Raul",
"Kirk",
"Lonny",
"Sang",
"Fritz",
"Harry",
"Chuck",
"Pablo",
"Yong",
"Antonia",
"Issac",
"Scot",
"Luis",
"Branden",
"Stacey",
"Corey",
"Ezequiel",
"Marion",
"Nelson",
"Brady",
"Reggie",
"Dewayne",
"Napoleon",
"Parker",
"Lenard",
"Grady",
"Jamaal",
"Adalberto",
"Dominic",
"Claudio",
"Tad",
"Rufus",
"Hugo",
"Samuel",
"Robby",
"Ward",
"Russel",
"Israel",
"Damian",
"Zach",
"Moshe",
"Anderson",
"Rocky",
"Cody",
"Giovanni",
"Lucius",
"Dallas",
"Quinn",
"Edmond",
"Fausto",
"Rene",
"Gilberto",
"Frederic",
"Von",
"Miquel",
"Roman",
"Jarred",
"Jeffery",
"Kent",
"Willie",
"Foster",
"Rudy",
"Guadalupe",
"Daren",
"Sergio",
"Carroll",
"Cedrick",
"Silas",
"Rolland",
"Morton",
"John",
"Royce",
"Cleveland",
"Claud",
"Colton",
"Peter",
"Matthew",
"Kevin",
"Kenny",
"Olin",
"Bart",
"Collin",
"Erin",
"Gerald",
"Len",
"Aron",
"Laverne",
"Ernie",
"Gregg",
"Mario",
"Christian",
"Moises",
"Chauncey",
"Horacio",
"Drew",
"Trenton",
"Jessie",
"Hassan",
"Andrew",
"Vicente",
"Mel",
"Harris",
"Bernard",
"Mitchell",
"Pierre",
"Xavier",
"Osvaldo",
"Lupe",
"Samual",
"Newton",
"Edgar",
"Leopoldo",
"Warner",
"Travis",
"Leo",
"Stanford",
"Rupert",
"Donnie",
"Terrance",
"Bert",
"Jamal",
"Laurence",
"Rayford",
"Sherman",
"Quentin",
"Clemente",
"Neil",
"Reginald",
"Stewart",
"Terrell",
"Rodrigo",
"Omer",
"Chani",
"Luke",
"Chris",
"Louis",
"Derek",
"Kyle",
"Rene",
"Broderick",
"Willian",
"Herb",
"Werner",
"Zane",
"Rodger",
"Pasquale",
"Cesar",
"Augustus",
"Rey",
"Terrance",
"Randy",
"Emmitt",
"Elvin",
"Jayson",
"Ismael",
"Bennett",
"Kent",
"Irving",
"Delmer",
"Stacy",
"Korey",
"Louie",
"Elroy",
"Dan",
"Ron",
"Stanley",
"Edmund",
"Tracy",
"Alfredo",
"Lamar",
"Nathaniel",
"Chong",
"Lindsey",
"Palmer",
"Tyrell",
"Harland",
"Alfonzo",
"Brad",
"Rayford",
"Jerrod",
"Scotty",
"Rudy",
"Demetrius",
"Stacey",
"Delbert"
]