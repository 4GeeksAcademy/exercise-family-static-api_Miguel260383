"""
Update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- get_member: Should return a member from the self._members list
"""


class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._next_id = 1
        self._members = [
            {
                "id": self._generate_id(),
                "first_name": "John",
                "last_name": last_name,
                "age": 33,
                "lucky_numbers": [7, 13, 22]
            },
            {
                "id": self._generate_id(),
                "first_name": "Jane",
                "last_name": last_name,
                "age": 35,
                "lucky_numbers": [10, 14, 3]
            },
            {
                "id": self._generate_id(),
                "first_name": "Jimmy",
                "last_name": last_name,
                "age": 10,
                "lucky_numbers": [1]
            }
        ]

  
    def _generate_id(self):
        generated_id = self._next_id
        self._next_id += 1
        return generated_id


  
    def add_member(self, member_data):
        new_member = {
            "id": self._generate_id(),   
            "first_name": member_data["first_name"],
            "last_name": self.last_name,
            "age": member_data["age"],
            "lucky_numbers": member_data["lucky_numbers"]
        }

        self._members.append(new_member)  
        return new_member


    def delete_member(self, member_id):
        member = self.get_member(member_id)

        if member:
            self._members.remove(member)   
            return True

        return False

    def get_member(self, member_id):
        for member in self._members:  
            if member["id"] == member_id:
                return member
        return None


    def get_all_members(self):
        return self._members
