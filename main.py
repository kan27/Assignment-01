"""
CMPS 2200  Assignment 1.
See assignment-01.pdf for details.

Srikanya Balaji Garuda
"""
# no imports needed.

def foo(x):
    ### TODO
    def foo(x):
        if (x <=1):
            return x
        else:
            ra = foo(x-1)
            rb = foo(x-2)
            return ra + rb
    pass

def longest_run(mylist, key):
    ### TODO
    curr_seq = 0
    max_seq = 0
    for n in mylist:
        if (n == key):
            curr_seq += 1
            if curr_seq > max_seq:
                    max_seq = curr_seq
            else:
                curr_seq = 0
    return max_seq

    pass


class Result:
    """ done """
    def __init__(self, left_size, right_size, longest_size, is_entire_range):
        self.left_size = left_size              # the length of the longest run on left side of input
                                                # eg, with a key of 12, [12 12 3] has left_size of 2 
        self.right_size = right_size            # length of longest run on right side of input
                                                # eg, key 12, [3 12 12] has right_size of 2
        self.longest_size = longest_size        # length of longest run in input
                                                # eg, [12 12 4 12 12 12]: longest_size is 3
        self.is_entire_range = is_entire_range  # True if the entire input matches the key
        
    def __repr__(self):
        return('longest_size=%d left_size=%d right_size=%d is_entire_range=%s' %
              (self.longest_size, self.left_size, self.right_size, self.is_entire_range))
    
    
def longest_run_recursive(mylist, key):
    ### TODO
    pass