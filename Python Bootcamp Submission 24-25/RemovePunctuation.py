import string

test_str = 'here,is a little code! i wrote?&gt;) ;'

test_str = test_str.translate(str.maketrans('', '',
                                    string.punctuation))
print(test_str)
