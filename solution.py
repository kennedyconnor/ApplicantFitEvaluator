# Hello, my name is Connor Kennedy. Welcome to my solution for the Compatability Predictor.

import json
import statistics

INPUT_FILE_PATH = 'test_data.json'
OUTPUT_FILE_PATH = 'output_data.json'

def calculate_team_statistics(team_data):
    # Calculate the mean and variance for each attribute of the team
    # Attributes are dynamically pulled from the first team member (assumed to be constant across team)
    # return a List of two Dictionaries [means, variances]

    means = {}
    variances = {}
    # pull list of attributes from first team member
    attributes = team_data[0]['attributes'].keys()

    for att in attributes:
        att_values = []
        for tm in team_data:
            att_values.append(tm['attributes'][att])
        means[att] = statistics.mean(att_values)
        variances[att] = statistics.variance(att_values)

    return [means, variances]



def calculate_applicant_compatibility(team_stats, applicant_data):
    # Measure invididual applicant against team and compatibility
    pass


def main():

    # Open and read JSON File
    try:
        with open((INPUT_FILE_PATH), 'r') as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        print(f"{INPUT_FILE_PATH} was not found.")
        return None
    
    # Define key data for team and applicants
    team_data = data['team']
    team_stats = calculate_team_statistics(team_data)
    applicants_data = data['applicants'] 

    print("Team Data", team_data)
    print("Applicants Data", applicants_data)
    print("Team Stats", team_stats)


if __name__ == '__main__':
    main()