import re

# TODO create function which will take out variable and put it to dictionary which acts like independent stack like in os
# TODO create a function which will print the values of given command line
import doctest
# NOTE unary is failing


class Printer(object):
    def __init__(self) -> None:
        self.stacker_dict = {}

    def eprint(self, in_string):
        if self.in_string == "":
            raise SyntaxError
        if re.findall("\s*[1-9]*\s*"):
            pass  # number
        if re.findall("\s*([a-bA-Z_])*\s*"):
            pass
        if re.findall("\s*[+-*%/\\()]*\s"):
            pass

    def __inside_stack_checker_pre(self, lookup, ops, operand, symbol):
        # TODO add check for operand = constant
        """
        ### Funtion to handle the pre TODO try to integrate post in one

        Args:
            lookup (string): the LHS side
            ops (string): the operator
            operand (string): the operand of the statement

        Returns:
            Bool: If correct then True else False


        unary single BUG facing problems
        >>> x=printer()
        >>> x.stacker("x=++x")
        {'x': 1}
        >>> x.stacker("z=-x")
        {'x': 1, 'z': -1}

        above is failing

        >>> x=printer()
        >>> x.stacker("x=--x")
        {'x': -1}
        >>> x.stacker("x=--x")
        {'x': -2}

        >>> x=printer()
        >>> x.stacker("z=-x")
        {'z': 0}
        """
        if symbol == "PRE_INCREMENT" or symbol=="PRE_DECREMENT":
            if ops == "++":
                if operand in self.stacker_dict:
                    self.stacker_dict[operand] = self.stacker_dict[operand]+1
                    if operand == lookup:
                        pass
                    else:
                        # can be redunant
                        self.stacker_dict[lookup] = self.stacker_dict[operand]
                elif lookup in self.stacker_dict:  # To increment the value if already declared previously
                    self.stacker_dict[lookup] = self.stacker_dict[lookup[0][0]]+1
                else:  # To make value 1 if the variable is not declared in it
                    self.stacker_dict[lookup] = 1
                return self.stacker_dict[lookup]
            elif ops == "--":
                if operand in self.stacker_dict:
                    self.stacker_dict[operand] = self.stacker_dict[operand]-1
                    if operand == lookup:
                        pass
                    else:
                        self.stacker_dict[lookup] = self.stacker_dict[operand]
                elif lookup in self.stacker_dict:
                    self.stacker_dict[lookup] = self.stacker_dict[lookup[0][0]]-1
                else:  # To make value 1 if the variable is not declared in it
                    self.stacker_dict[lookup] = -1
                return self.stacker_dict[lookup]
        elif symbol == "POST_INCREMENT" or symbol=="POST_DECREMENT":
            if ops == "++":
                if operand in self.stacker_dict:
                    temp = self.stacker_dict[operand]
                    self.stacker_dict[operand] = self.stacker_dict[operand]+1
                    if operand == lookup:
                        pass
                    else:
                        # can be redunant
                        self.stacker_dict[lookup] = self.stacker_dict[operand]
                elif lookup in self.stacker_dict:  # To increment the value if already declared previously
                    temp = self.stacker_dict[operand]
                    self.stacker_dict[lookup] = self.stacker_dict[lookup[0][0]]+1
                else:  # To make value 1 if the variable is not declared in it
                    temp = 0
                    self.stacker_dict[lookup] = 1
                return temp
            elif ops == "--":
                if operand in self.stacker_dict:
                    temp = self.stacker_dict[operand]
                    self.stacker_dict[operand] = self.stacker_dict[operand]-1
                    if operand == lookup:
                        pass
                    else:
                        self.stacker_dict[lookup] = self.stacker_dict[operand]
                elif lookup in self.stacker_dict:
                    temp = self.stacker_dict[operand]
                    self.stacker_dict[lookup] = self.stacker_dict[lookup[0][0]]-1
                else:  # To make value 1 if the variable is not declared in it
                    temp = 0
                    self.stacker_dict[lookup] = -1
                return temp
        elif symbol == "UNARY":
            if ops == "-":  # unary handling
                if operand in self.stacker_dict:
                    # if lookup in self.stacker_dict:# To increment the value if already declared previously
                    self.stacker_dict[lookup] = self.stacker_dict[operand]*-1
                else:  # To make value 1 if the variable is not declared in it
                    self.stacker_dict[lookup] = 0
                    # BUG not working
                return self.stacker_dict[lookup]
        return False


# def stacker(self,liner):

    def stacker(self, liner):
        """
        ### Keyword arguments:
        argument -- description
        Return: return_description

        >>> x=printer()
        >>> x.stacker("x=++x")
        {'x': 1}

        >>> x=printer()
        >>> x.stacker("x=x++")
        inside this

        """
        x = re.findall("([a-zA-Z_])*\s*=\s*(.+)", liner)  # assigning a value
        if x:
            # TODO create a code for handling pre

            # TODO create a code for handling the expression or not
            # Code for handling ++,--,- value only
            if re.findall("^\s*(\+\+|--|-)\s*([a-zA-Z][\w]*)$", x[0][1]):
                # after equals declared to get the ops and
                after_equals = re.findall(
                    "^\s*(\+\+|--|-)\s*([a-zA-Z][\w]*)$", x[0][1])
                ops = after_equals[0][0]
                operand = after_equals[0][1]
                result = self.__inside_stack_checker_pre(
                    x[0][0], ops, operand, "PRE_INCREMENT")
                print(result)
                print(self.stacker_dict)

            # TODO create a code for handling post
            elif re.match("^\s*([a-zA-Z][\w]*)\s*(\+\+|--)$", x[0][1]):
                # after equals declared to get the ops and
                after_equals = re.findall(
                    "^\s*([a-zA-Z][\w]*)\s*(\+\+|--)$", x[0][1])
                operand = after_equals[0][0]
                ops = after_equals[0][1]
                result = self.__inside_stack_checker_pre(
                    x[0][0], ops, operand, "POST_INCREMENT")
                print(result)
                print(self.stacker_dict)

            # Code for handling ++,--,- value only
            if re.findall("^\s*(-)\s*([a-zA-Z][\w]*)$", x[0][1]):
                # after equals declared to get the ops and
                after_equals = re.findall(
                    "^\s*(-)\s*([a-zA-Z][\w]*)$", x[0][1])
                ops = after_equals[0][0]
                operand = after_equals[0][1]
                result = self.__inside_stack_checker_pre(
                    x[0][0], ops, operand, "UNARY")
                print(result)
                print(self.stacker_dict)
        elif re.match("^\s*(\+\+|--|-)\s*([a-zA-Z][\w]*)$|^\s*([a-zA-Z][\w]*)\s*(\+\+|--)$", liner):
            y = re.findall(
                "^\s*(\+\+|--|-)\s*([a-zA-Z][\w]*)$|^\s*([a-zA-Z][\w]*)\s*(\+\+|--)$", liner)
            if y[0][0] and y[0][1]:
                ops = y[0][0]
                lookup = y[0][1]
                operand = y[0][1]
                if ops == "++":
                    result = self.__inside_stack_checker_pre(
                        lookup, ops, operand, "PRE_INCREMENT")
                elif ops == "--":
                    result = self.__inside_stack_checker_pre(
                        lookup, ops, operand, "PRE_INCREMENT")
                elif ops == "-":
                    pass  # TODO what to do in case of single unary ?
            elif y[0][2] and y[0][3]:
                ops = y[0][3]
                operand = y[0][2]
                lookup = y[0][2]
                if ops == "++":
                    result = self.__inside_stack_checker_pre(
                        lookup, ops, operand, "POST_INCREMENT")
                elif ops == "--":
                    result = self.__inside_stack_checker_pre(
                        lookup, ops, operand, "POST_INCREMENT")
            print(result)

    def token_helper_pre_post(self, list_of_tokens):
        """
        A function which will help the tokenizer.py

        Args:
            list_of_tokens (list): list of token in format
        [('POST_INCREMENT', 'x++'), ('PLUS', '+'), ('POST_INCREMENT', 'y++')]
        """
        count = 0
        # while(count<len(list_of_tokens)):
        #      print(list_of_tokens[count])

        while (count < len(list_of_tokens)):
            print(list_of_tokens[count])
            if list_of_tokens[count][0] == "POST_INCREMENT" or list_of_tokens[count][0]=="POST_DECREMENT":
                ops = list_of_tokens[count][1][1:]
                lookup = list_of_tokens[count][1][0]
                operand = lookup
                operation_system="POST_DECREMENT" if ops=="--" else "POST_INCREMENT"
                result = self.__inside_stack_checker_pre(
                    lookup, ops, operand, operation_system)
                list_of_tokens[count]=("NUMBER",result)

            if list_of_tokens[count][0]=="PRE_INCREMENT" or list_of_tokens[count][0]=="PRE_DECREMENT":
                ops=list_of_tokens[count][1]
                lookup=list_of_tokens[count+1][1]
                operand=lookup
                operation_system=list_of_tokens[count][0]
                print(ops,lookup,operation_system)
                result = self.__inside_stack_checker_pre(
                    lookup, ops, operand, operation_system)
                list_of_tokens.pop(count)
                list_of_tokens[count]=("NUMBER",result)
            if list_of_tokens[count][0]=="MINUS":
                # TODO case 1 : when there is number in front of the unary 
                # TODO case 2 : when there is a LPAREN in front of the unary
                # Case 1 : if there is + in front of unary convert + into -
                # and if there is - infront of then convert into + 
                if count==0:
                    #TODO pendingid: 37e6cf59-2005-4d99-a0c7-d16af26a72bb
                    pass
                elif list_of_tokens[count-1][0]=="NUMBER" or list_of_tokens[count-1][0]=="RPAREN":
                    pass
                elif list_of_tokens[count-1][0]=="PLUS":
                    list_of_tokens.pop(count-1)# poping out the plus 
                elif list_of_tokens[count-1][0]=="MINUS":
                    list_of_tokens[count-1]=("PLUS",'+')# converting - -() into + () 
                    list_of_tokens.pop(count)# poping it as redunant due to 
                elif list_of_tokens[count+1][0]=="LPAREN":
                    print(list_of_tokens)
                    print("Inside this")
                    list_of_tokens.insert(count,("NUMBER","-1"))
                    print(list_of_tokens.pop(count+1))
                    list_of_tokens.insert(count+1,("MULTIPLY","*"))
                    
                    # list_of_tokens.pop(count)

            count = count+1
        print(list_of_tokens)


# creating a helper function which will be integrated in the project2.py
