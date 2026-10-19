import json
import pathlib
import time
import ArrayUtil
import StringUtil


# Checks for any files in the directory
def check_for_files():
    file_dir = pathlib.Path.cwd() / "data"
    files_in_dir = list(file_dir.glob(r'*'))
    return [file_dir, files_in_dir]


# creates the filename for the JSON file
def filename(directory_path, data_source):
    # Unix Epoch time used to mark when the Json file was created
    current_time_epoch = str(time.time_ns())

    # Creates the name and directory path for the new file
    new_filename = current_time_epoch + "_" + "V-Tubers_on_" + data_source + ".json"
    new_filepath = str(directory_path) + "\\" + new_filename
    return new_filepath


# opens a JSON file, so it can read by the program
def open_json_file(incoming_data):
    # Load JSON data
    with open(incoming_data, "r") as json_file:
        return json.load(json_file)


# creates a new JSON file holding the specified data and with the specified filename.
def create_json_file(filename, data):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)


# DEBUG: appends new data to an existing JSON file, of a given datatype.
def append_json_file(filename, data_to_append):
    with open(filename) as json_file:
        temp_file_data = json.load(json_file)
        for data in data_to_append:
            temp_file_data.append(data)
    create_json_file(filename, temp_file_data)


# finds the newest datafile in a directory, by comparing when the datafile was created
def find_newest_datafile(files_in_dir):
    timecode_array = []
    file_paths = []
    for file in files_in_dir:
        file_paths.append(file)
        timecode_array.append(StringUtil.convert_chr_to_string(StringUtil.get_numbers_from_string(file.name)))

    newest_timecode_index = ArrayUtil.find_index_of_highest_value(timecode_array)
    return open_json_file(file_paths[newest_timecode_index])


# Appends a new set of data to a JSON file
def append_new_data(filename, new_datasource, files_in_dir):
    current_json_file = find_newest_datafile(files_in_dir)
    create_json_file(filename, current_json_file)
    append_json_file(filename, new_datasource)


# Create New JSON file
def new_json_file(incoming_data, data_source):
    # Load the data into a JSON datafile
    #incoming_data_unpacked = open_json_file(incoming_data)

    # Check filepath
    directory_path, files_in_dir = check_for_files()

    # create a name for the new file
    new_file = filename(directory_path, data_source)

    # if there are no Json files, Create a new one from scratch
    if not files_in_dir:
        print("no files in directory")
        create_json_file(new_file, incoming_data)

    # else, append the newest data to the newest file
    else:
        print("files in the directory")
        append_new_data(new_file, incoming_data, files_in_dir)


# debug command
#def debug_cmd():
#    loaded_json_file = "DebugJson.json"
#    new_json_file(loaded_json_file, "YouTube")

#Debug_cmd()
