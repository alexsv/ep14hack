import os
import re
import json

def main():
    from_idx = 6
    base_path = os.path.join(os.path.dirname(os.path.realpath(__file__)),'../data/rk_berlin_routes/')
    path = os.path.join(base_path, 'all_points.txt')
    for line in open(path):
        jsonstr = re.match(r'(.*)var pointJson = (.*);', line).groups()[1]
        with open('route%s.json' % from_idx, 'w') as f: 
            f.write(jsonstr)
            from_idx += 1
    
if __name__ == "__main__":
    main()
