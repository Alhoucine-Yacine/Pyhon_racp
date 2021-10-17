def what_dec(func):

    def func_wrapper():
        # before function
        print("What !!!")
        func()
        # after function
        print("serioussly !!!")

    return func_wrapper
        


@what_dec
def question():
    print("is this true ?")

question()