    # PIN Error Generator
    
    This Python script generates all possible combinations of PIN errors. It uses simple permutations and swaps, and simulates erroneous user input, such as swapping adjacent digits or inputting wrong digits.
    
    ## Prerequisites
    
    The script requires the `tqdm` library for displaying progress bars and the `itertools` library for generating combinations. If you don't have these libraries installed, you can do so by running the following command:
    
    ```
    pip install tqdm itertools
    ```
    
    ## Description
    
    The script provides various utility functions:
    
    1. `pin_rep(num, k)`: This function generates a PIN representation for a given number as a tuple.
    
    2. `swapPositions(list, pos1, pos2)`: This function swaps the positions of two digits in a given list. 
    
    3. `swapErrors(List)`: This function generates all possible swap error combinations for a given PIN.
    
    4. `WrongDigitErrors(List,i)`: This function generates all possible error combinations for just one wrong digit in the PIN.
    
    5. `WrongDigitErrorFull(List)`: This function generates all possible error combinations for all wrong digits in the PIN.
    
    6. `PinSpan(List)`: This function generates the union of swap errors and wrong digit errors for a given PIN.
    
    7. `findsubsets(s, n)`: This function finds all possible subsets of a given set.
    
    8. `ListPinSpan(List)`: This function checks whether all possible PINs can be generated from the errors of the given list of PINs.
    
    9. `Is_There_Good_Choice(n,k)`: This function checks if there exists a set of PINs such that all possible PINs can be generated from the errors of the PINs in the set. 
    
    ## Usage
    
    You can run this script by simply executing the Python file in your command line:
    
    ```
    python pin_error_generator.py
    ```
    
    You can also import this script as a module in another Python script and use the functions provided:
    
    ```python
    import pin_error_generator as peg
    
    pin = peg.pin_rep(1234, 4)
    errors = peg.PinSpan(list(pin))
    ```
    
    ## Contribution
    
    Feel free to submit pull requests for improvements or new features. Any contributions you make to this effort are of great value.
    
    ## License
    
    This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
