## Context

This repository has the artifacts related to the paper "Choosing the Right Git Workflow: A Comparative Analysis of Trunk-based vs. Branch-based Approaches" and has two folders. 

All materials related to our study, including the survey, interviews, and analysis scripts, are available in our replication package. The repository is structured as follows:

- **`survey_package/`**: Contains all artifacts related to the survey.
  - **`code/`**: Python scripts used to generate the graphs from the survey data.
  - **`graphs/`**: Graphs generated by the analysis scripts, available in PDF format.
  - **`anonymized_survey_answers.xlsx`**: The anonymized responses collected through the survey.
  - **`final_card_sorting.png`**: Output of the card sorting activity used to consolidate the factors.

- **`interviews_package/`**: Contains transcripts of the 22 interviews conducted in the study.
  - Each interview has its own folder, which includes a file with the transcription in Portuguese.


## How to Use

To reproduce the graphs, the data from `anonymized_survey_answers.xlsx` must first be preprocessed and saved as `survey.csv`. This CSV file should then be placed in the same directory as the scripts, in `survey_package/code/`. 
Each script will generate its corresponding graph in PNG format.

All other analyses were conducted manually and are described in Section 2 of the paper.
