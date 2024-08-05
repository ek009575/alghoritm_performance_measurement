from multiprocessing import Pool

import time
#It is paralel computation function we called it inside of pool
def parallel_computation_cosine(unique_pairs):
    import multiprocessing
    import math
    import numpy as np
     # apply dot product
    
    def dot(v1, v2):
        total = 0
        for i in range(0, len(v1)):
            total += v1[i] * v2[i]
        return total
#Perform cosine similarity operation
    def cosine(v1, v2):
        dot_product = dot(v1, v2)
        magnitude_v1 = math.sqrt(dot(v1, v1))
        magnitude_v2 = math.sqrt(dot(v2, v2))

        if magnitude_v1 == 0 or magnitude_v2 == 0:
            return 0

        return dot_product / (magnitude_v1 * magnitude_v2)
# It iterates unique pair and use the fix size    
    startTime=time.time()
    for pair in unique_pairs:
        if isinstance(pair[0], list) and isinstance(pair[1], list):  #It checks type of vectors
            v1 = pair[0][:20000] 
            v2 = pair[1][:20000]
            cosine(v1, v2)
        else:
            pass
    print(multiprocessing.current_process()," took ", time.time()-startTime," seconds")     #Calculates time


    


# In[ ]:





# In[ ]:




