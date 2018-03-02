import abc


class Operator(metaclass=abc.ABCMeta):

    def __init__(self):
        self.totalExpressions = None  # Number of expressions evaluated by the operator
        self.operandStack = []

    def push(self, token):
        self.operandStack.append(token)

        if len(self.operandStack) == self.totalExpressions:
            return self.eval()

    @abc.abstractmethod
    def eval(self):
        return


class PlusOp(Operator):

    def __init__(self):
        super().__init__()
        self.totalExpressions = 2

    def eval(self):
        return sum(self.operandStack)


class MinusOp(Operator):

    def __init__(self):
        super().__init__()
        self.totalExpressions = 2

    def eval(self):
        return self.operandStack[0] - self.operandStack[1]


def tokToNum(tok):
    try:
        return int(tok)
    except ValueError:
        return float(tok)


def evaluate(expr):
    token = ""
    operatorStack = []
    operatorMap = {"+": PlusOp, "-": MinusOp}

    for token in expr.split():

        try:
            operatorStack.append(operatorMap[token]())

        except KeyError:
            while operatorStack:
                result = operatorStack[-1].push(tokToNum(token))
                while result is not None:
                    if len(operatorStack) > 1:
                        operatorStack.pop()
                        result = operatorStack[-1].push(tokToNum(result))
                    else:
                        return result
                else:
                    break
    return token


def evaluateExpression(expr):
    # The coding challenges states that all inputs will be valid,
    # However there is some basic error checking

    if not isinstance(expr, str):
        print("Input must be a string")
        return

    try:
        return evaluate(expr)
    except:
        print("Invalid expression")


if __name__ == "__main__":
    # example usage
    print(evaluateExpression("+ 1 1"))
