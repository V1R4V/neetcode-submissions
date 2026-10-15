class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators=['+', '-', '*', '/']
        stack=[]
        for i in tokens:
            if i in operators:

                if i == '+':
                    stack.append(stack.pop()+stack.pop())

                elif i== '-':
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(b-a)


                elif i== '*':
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(a*b)

                elif i== '/':
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(int(b/a))           
            else:
                stack.append(int(i))
        return stack[0]


        