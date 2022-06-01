from enum import Enum
from abc import ABC


class Rank(Enum):
    DIRECTOR = 1
    MANAGER = 2
    RESPONDER = 3


class Employee(ABC):
    def __init__(self):
        """
        Employee constructor.
        """
        self.current_call = None
        self.rank = None

    def receive_call(self, call):
        """
        Start the conversation.
        """
        pass

    def call_completed(self):
        """
        The issue is resolved, finish the call.
        """
        pass

    def escalate_and_reassign(self):
        """
        The issue has not been resolved. Escalate the call and assign_call new call to the employee.
        """
        pass

    def is_free(self):
        """
        Returns whether or not the employee is free.
        """
        return self.current_call == None


class Director(Employee):
    def __init__(self):
        """
        Director constructor.
        """
        super().__init__()
        self.rank = Rank.DIRECTOR


class Manager(Employee):
    def __init__(self):
        """
        Manager constructor.
        """
        super().__init__()
        self.rank = Rank.MANAGER


class Respondent(Employee):
    def __init__(self):
        """
        Respondent constructor.
        """
        super().__init__()
        self.rank = Rank.RESPONDER


class Caller:
    pass


class Call:
    def __init__(self, c: Caller):
        """
        Call constructor.
        """
        self.rank = Rank.RESPONDER
        self.caller = c
        self.handler = None

    def set_handler(self, e: Employee):
        """
        Set employee who is handling call.
        """
        self.handler = e

    def reply(self, message: str):
        """
        Send a message to the caller.
        """
        pass

    def increment_rank(self):
        """
        Increment the rank of the call.
        """
        pass

    def disconnect(self):
        """
        Disconnect from the call.
        """
        pass


class CallHandler:
    # 3 levels of employees
    LEVELS = 3

    # Initialize 10 respondents, 4 managers, and 2 directors
    NUM_RESPONDENTS = 10
    NUM_MANAGERS = 4
    NUM_DIRECTORS = 2

    def __init__(self):
        """
        CallHandler constructor.
        """
        # List of employees by level
        # employee_levels[0] = respondents
        # employee_levels[1] = managers
        # employee_levels[2] = directors
        self.employee_levels = []
        # queues for each call's rank
        self.call_queues = []

    def get_handler_for_call(self, call: Call) -> Employee:
        """
        Gets the first available employee who can handle this call.
        """
        pass

    def dispatch_caller(self, caller: Caller):
        """
        Routes the call to an available employee, or saves in a queue if no
        employee is available.
        """
        call = Call(caller)
        self.dispatch_call(call)

    def dispatch_call(self, call: Call):
        """
        Routes the call to an available employee, or saves in a queue if no
        employee is available.
        """
        # Try to route the call to an employee with minimal rank.
        emp = self.get_handler_for_call(call)
        if emp is not None:
            emp.receive_call(call)
            call.set_handler(emp)
        else:
            # Place the call into corresponding call queue according to its
            # rank.
            call.reply("Please wait for free emplyee to reply.")
            self.call_queues[call.rank.value].append(call)

    def assign_call(self, emp: Employee) -> bool:
        """
        An employee got free. Look for a waiting call that employee can serve.
        Return true if we assigned a call, false otherwise.
        """
        pass
