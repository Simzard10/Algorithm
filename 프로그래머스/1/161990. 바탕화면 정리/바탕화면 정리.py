def solution(wallpaper):
    rows = []
    cols = []
    
    for i, v1 in enumerate(wallpaper):
        for j, v2 in enumerate(v1):
            if v2 == '#':
                rows.append(i)
                cols.append(j)    

    lux, luy = min(rows), min(cols)
    rdx, rdy = max(rows), max(cols)
    
    return [lux, luy, rdx+1, rdy+1]