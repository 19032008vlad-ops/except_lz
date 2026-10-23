import os
import pandas as pd

class Validator:
    def __init__(self, file_path):
        self.file_path = file_path
        self.expected_col = [
            'Участники гражданского оборота', 'Тип операции', 'Сумма операции', 
            'Вид расчета', 'Место оплаты', 'Терминал оплаты', 'Дата оплаты', 
            'Время оплаты', 'Результат операции', 'Cash-back', 'Сумма cash-back'
        ]
        self.expected_dtypes = {
            'Участники гражданского оборота': 'str', 'Тип операции': 'str', 
            'Сумма операции': 'float64', 'Вид расчета': 'str', 'Место оплаты': 'str', 
            'Терминал оплаты': 'str', 'Дата оплаты': 'str', 'Время оплаты': 'str', 
            'Результат операции': 'str', 'Cash-back': 'str', 'Сумма cash-back': 'float64'
        }

    def check_data(self):
        try:
            if not os.path.exists(self.file_path):
                raise FileNotFoundError(f"[Errno 2] No such file or directory: '{self.file_path}'")

            self.df = pd.read_csv(self.file_path, sep=',', index_col=0)
            
            if self.df.empty:
                raise ValueError("Dataframe is empty")

            errors = []
            
            col_now = list(self.df.columns)
            if col_now != self.expected_col:
                errors.append(f"  -Names of colls don't match.\n"
                              f"Expected: {self.expected_col}\n"
                              f"Actual: {col_now}")

            for col_name, expected_type in self.expected_dtypes.items():
                if col_name in self.df.columns:
                    actual_type = str(self.df[col_name].dtype)
                    
                    if expected_type == 'str' and actual_type == 'object':
                        continue 
                    if expected_type == 'float64' and actual_type in ('int64', 'float64'):
                        continue
                        
                    if actual_type != expected_type:
                        errors.append(f"  - In coll '{col_name}' data type is invalid.\n"
                                      f"Expected: {expected_type}, Actual: {actual_type}")

            if errors:
                full_error_msg = "Dataframe structure doesn't match to the expected:\n" + "\n".join(errors)
                raise TypeError(full_error_msg)

        except FileNotFoundError as e:
            print(f"There was an error: {e}")
            
        except ValueError as e:
            print(f"There was an error: {e}")
            
        except TypeError as e:
            print(f"{e}") 
            
        else:
            print("Reading completed successfully.")

