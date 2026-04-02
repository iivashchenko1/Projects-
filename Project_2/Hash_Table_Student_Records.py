""""
Task

Design a student record system using a hash table (Python dictionary).

Required Operations
def insert(self, student_id, name, gpa):
def retrieve(self, student_id):
def delete(self, student_id):

Give Visualization of the output as much as possible in the Word document

Concepts to Demonstrate
• Hashing (dictionary)
• CRUD operations
• Data retrieval efficiency
"""

class Student_Records:
    def __init__(self):
        self.records = {}

    def insert(self, student_id, name, gpa):
        self.records[student_id] = {
            "Name": name, 
            "GPA": gpa
            }
        print(f'Inserted {student_id}:  {name}, GPA: {gpa}')

    def retrieve(self, student_id):
        if student_id in self.records:
            print(f'Record were found for {student_id}: {self.records[student_id]}') 
            return self.records[student_id]

        else: 
            print(f'No records were found for {student_id}')
            return None   
    
    def delete(self, student_id):
        if student_id in self.records:
            del self.records[student_id]
            print(f'Delete a record for {student_id}')
        
        else:
            print(f"Can not delete the records.{student_id} doesn't exist")

    def display_records(self):
        print('\nCurrent Student Records:')
        if len(self.records) == 0:
            print("No records are available to display.")
        else:
            for student_id, info in self.records.items():
                print(f'{student_id}: Name = {info["Name"]}, GPA: {info["GPA"]}')

def main():
    hash_table = Student_Records()

    hash_table.insert('S1', 'Illia', 3.5)
    hash_table.insert('S2', 'Mariia', 4)
    hash_table.insert('S3', 'Andrew', 2.8)
    
    hash_table.display_records()

    print('\nRetrieving one student records:')
    hash_table.retrieve('S1')

    print('\nDeleting one student records:')
    hash_table.delete('S2')

    hash_table.display_records()

    print('\nTrying to retrieve a deleted record:')
    hash_table.retrieve('S2')

    print('\nTrying to retrieve a deleted record:')
    hash_table.retrieve('S3')

if __name__ == "__main__":
    main()
