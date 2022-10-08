from hello import toyou, add, subtract

def setup_function(function):
    print("Running Setup: %s" % function.__name__)
    function.x = 10


def teardown_function(function):
<<<<<<< HEAD
    print("Running Teardown: %s" % function.__name__)
    del function.x

=======
	print("Running Teardown: %s" % function.__name__)
	del function.x
>>>>>>> 17f6648fab6521ad2df6f410ea249da4f0074799

def test_hello_subtract():
    assert subtract(test_hello_subtract.x) == 9
