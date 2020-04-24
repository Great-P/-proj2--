import os

# seq_file = "pigeon.fa"
seq_file = "pigeon.fa"
res_file = "results_cnn_pigeon.txt"
with open(seq_file, "r") as fp:
    while True:
        seq = fp.readline().strip()
        if seq:
            if seq.find(">") == 0:
                continue
            else:
                print(seq)
                os.system("python isPreMiR.py -s %s >> %s" % (seq, res_file))
        else:
            break

with open(res_file, "r") as fp:
    count = 0
    cur_count = 0
    while True:
        each_result = fp.readline().strip()
        if each_result:
            count += 1
            if each_result.find("Yes") != -1:
                cur_count += 1
        else:
            break

    accuracy = cur_count / (count / 2)
    print("accuracy:",accuracy)
