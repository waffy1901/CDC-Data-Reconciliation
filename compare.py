import csv

def get_state_dict():
    state_dict = {}
    # Open the state CSV file
    with open('state.csv', newline='') as csvfile:
        # Create a CSV reader object
        reader = csv.DictReader(csvfile)
        # Loop through each row in the CSV file
        for row in reader:
            # Add the row as a dictionary to the list
            if row['case_id'] in state_dict:
                print("Duplicate case id found in state database: " + row['case_id'])
            else:
                state_dict[row['case_id']] = row
    return state_dict

def get_cdc_dict():
    cdc_dict = {}
    # Open the cdc CSV file
    with open('cdc.csv', newline='') as csvfile:
        # Create a CSV reader object
        reader = csv.DictReader(csvfile)
        # Loop through each row in the CSV file
        for row in reader:
            # Add the row as a dictionary to the list
            if row['case_id'] in cdc_dict:
                print("Duplicate case id found in CDC database: " + row['case_id'])
            else: 
                cdc_dict[row['case_id']] = row
    return cdc_dict

def comp(state_dict, cdc_dict):
    results = {
        'missing_case_in_cdc_ids': [],
        'different_attribute_ids': []
    }
    for state_case_id in state_dict:
        state_row = state_dict[state_case_id]
        # If a case ID is in the state DB but not the CDC DB, mark it as a missing case
        if state_case_id not in cdc_dict:
            results['missing_case_in_cdc_ids'].append(state_case_id)
        # If a case has different attributes between state and CDC DBs, mark it as such
        else:
            for attribute in state_row:
                # If an attribute is different and the case ID is not already flagged, flag it
                if state_row[attribute] != cdc_dict[state_case_id][attribute] and state_case_id not in results['different_attribute_ids']:
                    results['different_attribute_ids'].append(state_case_id)
    return results

def main():
    print(comp(get_state_dict(), get_cdc_dict()))

if __name__ == "__main__":
    main()
    
# Format of the state dictionary for case id's 1, 2, 3, 4, 5
# state_dict = {
#   "1": { caseid, disease, date },
#   "2": { caseid, disease, date },
#   "3": { caseid, disease, date },
#   "4": { caseid, disease, date },
#   "5": { caseid, disease, date },
# }