# Hello, my name is Connor Kennedy. Welcome to my solution for the Compatability Predictor.

import json
import statistics

INPUT_FILE_PATH = 'test_data.json'
OUTPUT_FILE_PATH = 'output_data.json'
WEIGHTS_DEFAULTS = {'intelligence': 0.25, 'endurance': 0.25, 'strength': 0.25, 'spicyFoodTolerance': 0.25}  # Can adjust base weight for each attribute by org needs

def calculate_team_statistics(team_data):
    # Calculate the mean and variance for each attribute of the team
    # Attributes are dynamically pulled from the first team member (assumed to be constant across team)
    # return a List with two dictionary entries for means and variances
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

def calculate_team_attribute_weights(team_stats):
    # Use the team's stats to calculate the weight given to each attribute when evaluating compatibility
    
    weights = WEIGHTS_DEFAULTS
    means = team_stats[0]
    variances = team_stats[1]
    mean_mid = 5.5                          # 5.5 is the middle of the attribute scale, 'normal' value
    var_avg = statistics.mean(variances.values())    # Average variance dictates "normal" variance for attr
    
    # Adjust weights based on mean and variance
    for attr in weights:    
        mean_diff = (means[attr] - mean_mid) / mean_mid      # Percent difference for mean
        var_diff = (variances[attr] - var_avg) / var_avg     # Percent difference for variance

        # Combine percent differences and adjust weights
        attr_adjustment = mean_diff - var_diff    # var_diff subtracted because lower variance = higher importance (weight)
        weights[attr] *= (1 + attr_adjustment)    # Multiply attr weight by 1 + adjustment_factor to get new weight

    # Renormalize weights to sum up to 1.0
    total_weight = sum(weights.values())
    for attr in weights:
        weights[attr] /= total_weight

    return weights

def calculate_applicant_compatibility(applicant_data, weights):
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
    team_weights = calculate_team_attribute_weights(team_stats)
    applicants_data = data['applicants'] 

    applicant_compatibility_scores = {"scoredApplicants":[]}

    #for applicant in applicants_data:
     #   c_score = calculate_applicant_compatibility(applicant, team_weights)
      #  scored_app = {'name':applicant['name'], 'score':[c_score]}
       # applicant_compatibility_scores['scoredApplicants'].append(scored_app)

    print("Team Data", team_data)
    print("Applicants Data", applicants_data)
    print("Team Stats", team_stats)
    print("Scored Applicants", applicant_compatibility_scores)

if __name__ == '__main__':
    main()