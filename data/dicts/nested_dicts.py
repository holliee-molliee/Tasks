def short_pattern():
    pattern = {}
    pattern["sequence"]="101"
    pattern["occurences"]=5
    return pattern

def medium_pattern():
    pattern={}
    pattern["sequence"]="111000"
    pattern["occurences"]=25
    return pattern

def long_pattern():
    pattern={}
    pattern["sequence"]="1100110011001100"
    pattern["occurences"]=50
    return pattern

def run():
    print("Analysing patterns...")
    out={}
    out["short sequence"] = short_pattern()
    out["medium sequence"] = medium_pattern()
    out["long sequence"] = long_pattern()
    for key,value in out.items():
        print(f"{key}: {value}")

if __name__=="__main__":
    run()
