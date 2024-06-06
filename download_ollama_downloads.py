import os

# Define the path to the configuration file
config_file_path = "../config/ollama_models.txt"

# Check if the configuration file exists
if not os.path.exists(config_file_path):
    print(f"Configuration file not found: {config_file_path}")
else:
    # Open and read the configuration file
    with open(config_file_path, 'r') as file:
        # Iterate through each line in the file
        for line in file:
            # Trim any whitespace from the model name
            ollama_model = line.strip()
            # Construct the CLI command
            command = f"ollama pull {ollama_model}"
            # Print the command (for debugging purposes, remove this line in production)
            print(f"Executing command: {command}")
            # Execute the command
            os.system(command)
