import csv
# State Dictionary
state_dict = {}
# CDC Dictionary
cdc_dict = {}
# Open the state CSV file
with open('state.csv', newline='') as csvfile:
    # Create a CSV reader object
    reader = csv.DictReader(csvfile)
    # Loop through each row in the CSV file
    for row in reader:
        # Add the row as a dictionary to the list
        if row['case_id'] in state_dict:
            print("Duplicate case id found: " + row['case_id'])
        else:
            state_dict[row['case_id']] = row
# Open the cdc CSV file
with open('cdc.csv', newline='') as csvfile:
    # Create a CSV reader object
    reader = csv.DictReader(csvfile)
    # Loop through each row in the CSV file
    for row in reader:
        # Add the row as a dictionary to the list
        if row['case_id'] in cdc_dict:
            print("Duplicate case id found: " + row['case_id'])
        else: 
            cdc_dict[row['case_id']] = row
# Format of the state dictionary for case id's 1, 2, 3, 4, 5
# state_dict = {
#   "1": { caseid, disease, date },
#   "2": { caseid, disease, date },
#   "3": { caseid, disease, date },
#   "4": { caseid, disease, date },
#   "5": { caseid, disease, date },
# }