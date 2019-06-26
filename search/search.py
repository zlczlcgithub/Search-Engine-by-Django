TEST_PATH = """test_data/"""
data_dict = {}
sentences = []

for index in ["000","100","200","300","400","500","600","700","800","900","1000","1100","1200","2000","2100"]:
    filename = TEST_PATH + "_test_data_"+ index + "s" + ".py"
    F = open(filename, "r", errors="ignore")
    lines = F.readlines()
    F.close()
    flag = False

    for id, line in enumerate(lines[:100]):
        if not line.strip():
            continue
        if flag:
            if line.strip().startswith("'positive"):
                flag = True
            elif line.strip().startswith("]"):
                flag = False
            # extract sentences
            elif line.strip()[0] in ['"', "'"]:
                # while extracting backslash
                sentences.append(line.strip()[1:-2].replace("\\", ""))
        else:
            if line.strip().startswith("'positive"):
                flag = True
            elif line.strip().startswith("# **Super category:**"):
                super_cat = line.strip().split("* ")[-1]
            elif line.strip().startswith("# **Sub category:**"):
                sub_cat = line.strip().split("* ")[-1]
