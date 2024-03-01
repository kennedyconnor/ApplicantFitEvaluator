# Compatibility Predictor

## Overview
- Python-based solution for evaluating applicant compatibility with a team.
- Uses statistical analysis on team and applicant attributes.

## How It Works
- Processes JSON input containing team and applicant data.
- Calculates mean, variance, and weighted importance of each attribute with the provided team.
- Scores applicants based on these generated weights.

## Input
- Reads JSON input from `test_data.json` (default). Can be changed in the `INPUT_FILE_PATH` variable.
- Format:
 ```json
  {
    "team": [
      {"name": "Member1", "attributes": {"intelligence": 5, "strength": 6, "endurance": 7, "spicyFoodTolerance": 8}},
      // ... more team members
    ],
    "applicants": [
      {"name": "Applicant1", "attributes": {"intelligence": 4, "strength": 5, "endurance": 6, "spicyFoodTolerance": 7}},
      // ... more applicants
    ]
  }
  ```

## Output
- Outputs to `output_data.json` (default). Can be changed in the `OUTPUT_FILE_PATH` variable.
- Format:
 ```json
  {
    "scoredApplicants": [
      {"name": "Applicant1", "score": 0.75},
      // ... more scored applicants
    ]
  }
  ```

## Running the Application
- Requires Python.
- Run `python solution.py`.
- Input and output file paths are configurable. By default, they are located in the same directory as solution.py

## Approach/Premise
I designed my approach to blend intuitive and statistical analysis of team members and applicants. The initial `WEIGHTS_DEFAULT` values set an intuitive benchmark for team analysis. Relying solely on statistical measures might disproportionately emphasize outliers (like Joe). These default weights serve as a balance, grounding the analysis in our understanding of what a 'strong' applicant generally is, and can be changed depending on recruiter needs.

The program then refines this approach by examining the team's data, guided by two assumptions:

1. A higher mean score in an attribute suggests its greater relative importance to the team.
2. Lower variance in an attribute suggests its significance.

A team characterized by a high average and low variance in intelligence would, in theory, be a team that priorites not only overall team intelligence, but intelligence in each member. Therefore intelligence will have its default weight increased accordingly. In contrast, a lower average and higher variance in an attribute like strength would signal its lesser relevance, and its weight would be decreased.

It's important to note that the solution is tailored to identify applicants who are most "compatible" with a team, interpreted as matching the team's existing scores. My assumption is that a given team already functions well, and we want an applicant who matches its members.

An alternative perspective, which could be interesting for further exploration, involves using applicants to "fill the gaps" in a team's skillset. This potential expansion of functionality would shift the focus from compatibility to complementarity.