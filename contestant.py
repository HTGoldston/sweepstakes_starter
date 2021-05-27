from sweepstake import Sweepstake




class Contestant(Sweepstake):
    def __init__(self):
        self.contestant = Contestant
        super(Contestant, self).__init__((self, self.first_name, self.last_name, self.email_address,
                                          self.registration_number))
        self.first_name = input("first_name")
        self.last_name = input("last_name")
        self.email_address = input("email_address")
        self.registration_number = 1 <= 10


