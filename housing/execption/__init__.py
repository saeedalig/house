import os
import sys

class HousingException(Exception):
    # Constructor
    def __init__(self, error_message:Exception, error_details:sys):
        super().__init__(error_message)  # inheriting info from parent class(Exception)
        self.error_message = HousingException.get_detailed_error_message(error_message=error_message, error_details=error_details)

    # Static methods to avoid creating obj of the class
    @staticmethod
    def get_detailed_error_message(error_message:Exception, error_details:sys) ->str:

        # Extract eroor info
        _, _, exec_tb = error_details.exc_info()
        file_name = exec_tb.tb_frame.f_code.co_filename  # file name causing ertor
        line_number = exec_tb.tb_frame.f_lineno
        error_message = f"Error occured in Script: [{file_name}] at line number: [{line_number}] error message: [{error_message}]"
        return error_message



    # Error Message that has to be displayed
    def __str__(self):
        return self.error_message
    
    def __repr__(self) -> str:
        return HousingException.__name__.str()
