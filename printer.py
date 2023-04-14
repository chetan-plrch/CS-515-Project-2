import re

# TODO create function which will take out variable and put it to dictionary which acts like independent stack like in os
# TODO create a function which will print the values of given command line
import doctest
# NOTE unary is failing 

class printer(object):
    def __init__(self) -> None:
        self.stacker_dict={}

    def  eprint(self,in_string):
        if self.in_string=="":
            raise SyntaxError
        if re.findall("\s*[1-9]*\s*"):
            pass #number
        if re.findall("\s*([a-bA-Z_])*\s*"):
            pass
        if re.findall("\s*[+-*%/\\()]*\s"):
            pass
    
    def __inside_stack_checker_pre(self,lookup,ops,operand,symbol):
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
        if symbol=="PRE_INCREMENT":    
            if ops=="++":
                if operand in self.stacker_dict :
                            self.stacker_dict[operand]=self.stacker_dict[operand]+1
                            if operand==lookup:
                                pass
                            else:
                                self.stacker_dict[lookup]=self.stacker_dict[operand] # can be redunant
                elif lookup in self.stacker_dict:# To increment the value if already declared previously
                            self.stacker_dict[lookup]=self.stacker_dict[lookup[0][0]]+1
                else: # To make value 1 if the variable is not declared in it 
                    self.stacker_dict[lookup]=1
                return self.stacker_dict[lookup]
            elif ops=="--":
                if operand in self.stacker_dict :
                            self.stacker_dict[operand]=self.stacker_dict[operand]-1
                            if operand==lookup:
                                pass
                            else:
                                self.stacker_dict[lookup]=self.stacker_dict[operand]
                elif lookup in self.stacker_dict:# 
                            self.stacker_dict[lookup]=self.stacker_dict[lookup[0][0]]-1
                else: # To make value 1 if the variable is not declared in it 
                    self.stacker_dict[lookup]=-1
                return self.stacker_dict[lookup]
        elif symbol=="POST_INCREMENT":
            if ops=="++":
                if operand in self.stacker_dict :
                    temp=self.stacker_dict[operand]
                    self.stacker_dict[operand]=self.stacker_dict[operand]+1
                    if operand==lookup:
                        pass
                    else:
                        self.stacker_dict[lookup]=self.stacker_dict[operand] # can be redunant
                elif lookup in self.stacker_dict:# To increment the value if already declared previously
                    temp=self.stacker_dict[operand]
                    self.stacker_dict[lookup]=self.stacker_dict[lookup[0][0]]+1
                else: # To make value 1 if the variable is not declared in it 
                    temp=0
                    self.stacker_dict[lookup]=1
                return temp
            elif ops=="--":
                if operand in self.stacker_dict :
                    temp=self.stacker_dict[operand]
                    self.stacker_dict[operand]=self.stacker_dict[operand]-1
                    if operand==lookup:
                        pass
                    else:
                        self.stacker_dict[lookup]=self.stacker_dict[operand]
                elif lookup in self.stacker_dict:# 
                    temp=self.stacker_dict[operand]
                    self.stacker_dict[lookup]=self.stacker_dict[lookup[0][0]]-1
                else: # To make value 1 if the variable is not declared in it 
                    temp=0
                    self.stacker_dict[lookup]=-1
                return temp

        elif ops=="-": # unary handling
            if operand in self.stacker_dict:
                # if lookup in self.stacker_dict:# To increment the value if already declared previously
                    self.stacker_dict[lookup]=self.stacker_dict[operand]*-1
            else: # To make value 1 if the variable is not declared in it 
                    self.stacker_dict[lookup]=0
                    # BUG not working 
            return self.stacker_dict[lookup]
        return False
        
    
# def stacker(self,liner):
    def stacker(self,liner):
    
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
        x=re.findall("([a-zA-Z_])*\s*=\s*(.+)",liner)# assigning a value
        if x:
            # TODO create a code for handling pre 
            
            # TODO create a code for handling the expression or not 
            if re.findall("^\s*(\+\+|--|-)\s*([a-zA-Z][\w]*)$",x[0][1]):# Code for handling ++,--,- value only
                after_equals=re.findall("^\s*(\+\+|--|-)\s*([a-zA-Z][\w]*)$",x[0][1])# after equals declared to get the ops and 
                ops=after_equals[0][0]
                operand=after_equals[0][1]
                result=self.__inside_stack_checker_pre(x[0][0],ops,operand,"PRE_INCREMENT")
                print(result)
                print(self.stacker_dict)

            # TODO create a code for handling post
            elif re.match("^\s*([a-zA-Z][\w]*)\s*(\+\+|--)$",x[0][1]):
                after_equals=re.findall("^\s*([a-zA-Z][\w]*)\s*(\+\+|--)$",x[0][1])# after equals declared to get the ops and 
                operand=after_equals[0][0]
                ops=after_equals[0][1]
                result=self.__inside_stack_checker_pre(x[0][0],ops,operand,"POST_INCREMENT")
                print(result)
                print(self.stacker_dict)
            
            



# creating a helper function which will be integrated in the project2.py
