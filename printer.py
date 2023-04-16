import re
import Tokenizer
import ExpressionEvaluation
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
        print(len(list_of_tokens))
        while (count < len(list_of_tokens)):
            print(list_of_tokens[count][0])
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
                  
                    list_of_tokens.insert(count,("NUMBER","-1"))
                    list_of_tokens.pop(count+1)
                    list_of_tokens.insert(count+1,("MULTIPLY","*"))

            if list_of_tokens[count][0]=="NAME":
                print("inside this ")
                if list_of_tokens[count][1] in self.stacker_dict.keys():
                    tempVar=self.stacker_dict[list_of_tokens[count][1]]
                else:
                    tempVar=0
                list_of_tokens[count]=("NUMBER",tempVar)
                    # list_of_tokens.pop(count)

            count = count+1
        return(list_of_tokens)
    
    # def printist(self,statement):
    #     if re.match("^\s*print\s*(.+)\s*$",statement):
    #         res_value=
    #     pass

    def ops_extension(self,statement: str):
        """code to handle the ops_extension

        Args:
            statement (str): this will be the command which will be given in the input

        Returns:
            _type_: either a the new statement or False ( False means the pattern did not match )
        """

        if re.match("^\s*([a-zA-Z][\w]*)\s*([\^|\+\-*\\\%])=(.+)$",statement):
            op_manager=re.findall("^\s*([a-zA-Z][\w]*)\s*([\^|\+\-*\\\%])=(.+)$",statement)
            res_value=op_manager[0][0]# LHS value
            operator=op_manager[0][1]# RHS Value
            new_statment=statement
            
            # removing previous values

            # Sanitizing the LHS
            for index,i in enumerate(statement):
                if i==operator:
                    position_at=index
                    new_statment=statement[:position_at]+statement[position_at+1:]
                    break
            print(new_statment)

            # Adding the operation to RHS

            # Adding parenthesis, res_value and operator 
            for index,i in enumerate(new_statment):
                if i=="=":
                    position_at=index
                    new_statment=new_statment[:position_at+1]+" "+res_value+" "+operator+" "+"("+new_statment[position_at+1:]+")"
                    return new_statment

           
        return False # if ops is not required

    def assigner(self,statement):
        spliter=statement.split("=")
        try:
            is_float=True if float(spliter[1]) or int(spliter[1]) else False
        except: 
            is_float=False
        if is_float:
       
            self.stacker_dict[spliter[0]]=spliter[1]
        else:
            ops=self.ops_extension(statement)
            if ops!=False:
                spliting_for_RHS_Eval=ops.split("=")
                print("inside the else")

                t= Tokenizer.Tokenizer(spliting_for_RHS_Eval[1])
                list_of_tokens=t.char_with_type_tokenized_lines()
                print("list of tokens",list_of_tokens)
                pre_post=self.token_helper_pre_post(list_of_tokens[0])
                evalu=ExpressionEvaluation.ExpressionEvaluation()
                result=evalu.evaluate_expression(pre_post)
                
            else:

            # TODO create the else
            





# creating a helper function which will be integrated in the project2.py


# DONE Extension
# I need to add brackets at 0 and -1
# I need add the op at 0 
# I need to add the LHS