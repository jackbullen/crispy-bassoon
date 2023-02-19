import os
import glob

pgn_files_path = 'SOME_SITE_URL'
pgn_output_dir = 'OUTPUT_DIR'

# Download all the pgn files from SOME_SITE_URL and save in OUTPUT_DIR
os.system(f'wget -r -np -nd --no-check-certificate -A pgn -P {pgn_output_dir} {pgn_files_path}')

# Get the path of all the downloaded pgn files
pgn_files = glob.glob(f'{pgn_output_dir}/*.pgn')

# Create the output pgn file and append all the pgn games into one pgn file
with open('games.pgn', 'w') as out_file:
    for pgn_file in pgn_files:
        with open(pgn_file, 'r') as in_file:
            out_file.write(in_file.read())
        out_file.write('\n\n') # add a blank line between games
