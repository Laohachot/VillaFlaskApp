import os 
import numpy as np 
from typing import Iterable
from re import findall

def read(f):
    with open(f, 'r') as f:
        return f.read()

def argsort_regex(pattern, x, cast=float):
    '''
    Uses re.findall and then argsorts results
    Regex pattern should have exactly have one group
    Returns argsort indices
    '''
    return np.argsort(np.array(findall(pattern, str(list(x)))).astype(cast))

def sort_regex(pattern, x, cast=float):
    '''
    Uses re.findall and then sorts results
    Regex pattern should have exactly have one group
    Returns np.ndarray sorted items
    '''
    return np.array(x)[argsort_regex(pattern, x, cast=cast)]

def interleave(A: Iterable, B: Iterable):
    '''
    Interleaves to iterables, returns tuple of interleaved 
    iterable items. 
    '''
    return reduce(tuple.__add__, [(a,b) for a,b in zip(A,B)])

if __name__ == '__main__':
    extensions = {'.jpg','.png','.jpeg'}
    static_dir = os.path.join('web','static')
    PATHS = sort_regex('\d+', [path for path in os.listdir(static_dir) if os.path.splitext(path)[1] in extensions])
    CAPTIONS = [read(os.path.join(static_dir,f)).strip() for f in [os.path.splitext(path)[0]+'.txt' for path in PATHS]]
    print(PATHS)
    
    
    