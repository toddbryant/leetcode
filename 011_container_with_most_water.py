# OK, as I learned from the solution, there is a magic trick 
# that does it much faster than this!

def isMatch(heights):
    first_geq = {}
    last_geq = {}
    unique_heights = sorted(set(heights))

    # first_geq[height] gives the index of the first line >= that height
    height_index = 0
    max_height = unique_heights[0]
    try:
        for ax, height in enumerate(heights, start=1):
            while height >= max_height:
                first_geq[max_height] = ax
                height_index += 1
                max_height = unique_heights[height_index]
    except IndexError:
        # We covered all unique heights
        pass

    # last_geq[height] gives the index of the last line >= that height
    height_index = 0
    max_height = unique_heights[0]
    try:
        for ax, height in enumerate(heights[::-1], start=0):
            while height >= max_height:
                last_geq[max_height] = len(heights)-ax
                height_index += 1
                max_height = unique_heights[height_index]
    except IndexError:
        # We covered all unique heights
        pass
    
    maxArea = 0
    for ax, height in enumerate(heights, start=1):
        maxArea = max(maxArea, (ax-first_geq[height])*height)
        maxArea = max(maxArea, (last_geq[height]-ax)*height)
                
    print(maxArea)

if __name__=='__main__':
    isMatch([1,8,6,2,5,4,8,3,7])
