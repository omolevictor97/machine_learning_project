import os
import sys

class HousingException(Exception):

    def __init__(self, error_message:Exception, error_detail:sys):

        """
        error_message: An Exception object
        error_detail: A sys module object
        """
        super().__init__(error_message)
        self.error_message = HousingException.get_detailed_error_message(
            error_message=error_message,
            error_detail=error_detail
        )

    @staticmethod

    def get_detailed_error_message(error_message:Exception, error_detail:sys) -> str:
        
        _, _, exec_tb = error_detail.exc_info()
        # The error_detail.exc_info() returns a tuple that contains:
        # A type, value and traceback object
        line_number = exec_tb.tb_frame.f_lineno
        file_name = exec_tb.tb_frame.f_code.co_filename
        error_message = f"""
        Error was found in script: [{file_name}] 
        and on line number: [{line_number}] 
        with error message: [{error_message}]"""

        return error_message
    

    def __str__(self):
        return self.get_detailed_error_message() #For display in print statement
    
    def __repr__(self) -> str:
        return HousingException.__name__.str() # Displays when the class object is called