## File: mymath.py##
def binhphuong(n):
    return n**2

def lapphuong(n):
    return n**3

def trbinh(values):
    nvals = len(values)
    sum = 0.0
    for v in values:
        sum += v
    return float(sum)/nvals
