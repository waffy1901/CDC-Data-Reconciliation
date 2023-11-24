import csv
import argparse

class CaseResult:
    def __init__(self, caseID, eventName, state, eventDate, reason, reasonID) -> None:
        self.caseID = caseID
        self.eventName = eventName
        self.state = state
        self.eventDate = eventDate
        self.reason = reason
        self.reasonID = reasonID


results: list[CaseResult] = []


def get_state_dict(state_file):
    state_dict = {}
    # Open the state CSV file
    with open(state_file, newline='') as csvfile:
        # Create a CSV reader object
        reader = csv.DictReader(csvfile)
        # Loop through each row in the CSV file
        for row in reader:
            # Add the row as a dictionary to the list
            if row['CaseID'] in state_dict:
                results.append(CaseResult(row['CaseID'], row['EventName'], row['State'], row['EventDate'], "Duplicate Case ID found in State CSV File", "1"))
            else:
                state_dict[row['CaseID']] = row

    return state_dict

def get_cdc_dict(cdc_file):
    cdc_dict = {}
    # Open the cdc CSV file
    with open(cdc_file, newline='') as csvfile:
        # Create a CSV reader object
        reader = csv.DictReader(csvfile)
        # Loop through each row in the CSV file
        for row in reader:
            # Add the row as a dictionary to the list
            if row['CaseID'] in cdc_dict:
                results.append(CaseResult(row['CaseID'], row['EventName'], row['State'], row['EventDate'], "Duplicate Case ID found in CDC CSV File", "2"))
            else: 
                cdc_dict[row['CaseID']] = row

    return cdc_dict

def comp(state_dict, cdc_dict):
    for state_case_id in state_dict:
        state_row = state_dict[state_case_id]

        # If a case ID is in the state DB but not the CDC DB, mark it as a missing case
        if state_case_id not in cdc_dict:
            results.append(CaseResult(state_case_id, state_row['EventName'], state_row['State'], state_row['EventDate'], "Case ID not found in CDC CSV File", "3"))
        else:
            # If a case has different attributes between state and CDC DBs, mark it as such
            for attribute in state_row:
                if state_row[attribute] != cdc_dict[state_case_id][attribute]:
                    results.append(CaseResult(state_case_id, state_row['EventName'], state_row['State'], state_row['EventDate'], "Case has different attributes between State and CDC CSV Files", "4"))
                    break
            
            # Remove the case from the CDC dict so we can track what cases are missing from the state side
            del cdc_dict[state_case_id]

    # If there exists cases in the CDC dictionary still, mark it as a missing case on the state side
    for cdc_case_id in cdc_dict:
        cdc_row = cdc_dict[cdc_case_id]
        results.append(CaseResult(cdc_case_id, cdc_row['EventName'], cdc_row['State'], cdc_row['EventDate'], "Case ID not found in State CSV File", "5"))

def main():
    parser = argparse.ArgumentParser(prog="CompareCDCAndState", description='Compare CDC and State CSV files')
    parser.add_argument('-s', '--state', help='Local Path to State CSV file')
    parser.add_argument('-c', '--cdc', help='Local Path to CDC CSV file')
    parser.add_argument('-o', '--output', help='Local Path to Output CSV file')

    args = parser.parse_args()


    state_dict = get_state_dict(args.state)
    cdc_dict = get_cdc_dict(args.cdc)

    comp(state_dict, cdc_dict)

    # Create Results CSV File and write the results to it
    with open(args.output, 'w', newline='') as csvfile:
        fieldnames = ['CaseID', 'EventName', 'State', 'EventDate', 'Reason', 'ReasonID']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for result in results:
            writer.writerow({'CaseID': result.caseID, 'EventName': result.eventName, 'State': result.state, 'EventDate': result.eventDate, 'Reason': result.reason, 'ReasonID': result.reasonID})

if __name__ == "__main__":
    main()
    