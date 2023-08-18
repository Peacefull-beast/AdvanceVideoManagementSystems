# Global variables
main_window_name = 'Main Window'
popup_window_name = 'Popup Window'
vedio_player_window = 'Video Player'
button_width = 200
button_height = 50
button_margin = 20
nummain = 0  # index of url passed
numpop = 0  # index of analytics applied
mbuttons = []
pbuttons = []

# calculation
num_cameras = 9
grid_cols = 3  # Number of columns in the grid
grid_rows = (num_cameras + grid_cols - 1) // grid_cols

# Define the gap size between grids
gap_size = 10  # Adjust the value to increase or decrease the gap size

# Calculate the frame dimensions for each camera
frame_width = 300
frame_height = 300

# url list of camera
urls = [
    0,0,0,0,0,0,0,0,0
]