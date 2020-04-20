# This is the main ATM program, this will call all other classes and modules.
import session as session_library
import card_reader as card_reader_library
import customer_console as customer_console_library
import operator_panel as operator_panel_library
import log as log
import account as acount_library
import network as network_library
import receipt as receipt_library

class Atm(object):
    _id = "12345"

    @property
    def id(self):
        return self._id

    def __init__(self):
        print("Atm initialized")

    def display_welcome(self):
        # console = console_library.Console()
        print("Welcome to our very expensive bank!")

    def read_card(self):
        self.card_number = card_reader_library.Get_Card()

    def start_session(self):
        self.session = session_library.Session(self._id, self.card_number)
        print("Session started.")

    def end_session(self):
        self.session.end_session(self.session)
        print("Session Ended.")
    
    def start_customer_console(self):
        self.customer_console = customer_console_library.Console()
        print("Console started.")
    
    def get_action(self):
        self.action = self.customer_console.get_action()

    def deposit_withdrawal_transfer(self):
        if self.action == "deposit":
            continue
        elif self.action == "withdrawal":
            continue
        elif self.actioin == "transfer":
            continue
        else:
            print("Invalid action, please try again.")
            


    
            


