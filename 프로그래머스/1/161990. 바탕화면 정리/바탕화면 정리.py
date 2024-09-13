def solution(wallpaper):
    answer = []
    stack = []
    uppy = len(wallpaper)
    downy = 0
    lefty = len(wallpaper[0])
    righty = 0
    
    for i in range(len(wallpaper)):
        for l in range(len(wallpaper[0])):
            if wallpaper[i][l] == "#":
                uppy = min(uppy, i)
                downy = max(downy, i)
                lefty = min(lefty, l)
                righty = max(righty, l)
                
        
    
    return [uppy, lefty, downy+1, righty+1]