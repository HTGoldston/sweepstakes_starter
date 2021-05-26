from sweepstake import Sweepstake

class Contestant(Sweepstake):
    def __init__(self):
        self.contestant = Contestant
        super(Contestant, self).__init__((self, self.first_name, self.last_name, self.email_address,
                                          self.registration_number))
        self.first_name = "first_name"
        self.last_name = "last_name"
        self.email_address = "email_address"
        self.registration_number = []


