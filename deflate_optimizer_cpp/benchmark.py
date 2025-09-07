import tqdm
import glob
import subprocess
import os
import matplotlib.pyplot as plt

def check_all_files():
    lis = []
    # fact_lis = []
    for path in tqdm.tqdm(glob.glob('../tmp/ziptext/*/*_deflated.txt')):
        # print(path)
        res = subprocess.run(['./a.out', path], stdout=subprocess.PIPE).stdout
        res = map(lambda x: int(x.split(':')[1]), res.decode().splitlines())
        # これのように出力させないといけないので注意（デバッグ出力を入れたり消したりしないと死ぬ）
        # bef_fact, bef_bit, aft_fact, aft_bit = res
        bef_bit, aft_bit = res
        # print('factor:', bef_fact, '->', aft_fact)
        # print('bit   :', bef_bit, '->', aft_bit)
        # print('factor_diff :', aft_fact - bef_fact)
        # print('bit_diff    :', aft_bit - bef_bit)
        # print('bit_ratio   :', aft_bit / bef_bit)
        if 0 <= bef_bit <= 10000 and 0 <= aft_bit <= 10000:
            # fact_lis.append((bef_fact, aft_fact))
            lis.append((bef_bit, aft_bit))            
        
    # factor_diffs = list(map(lambda x: x[1] - x[0], fact_lis))
    ratios = list(map(lambda x: x[1] / x[0], lis))
    diffs = list(map(lambda x: x[1] - x[0], lis))
    avg_diff = sum(diffs) / len(diffs)
    # avg_factor_diff = sum(factor_diffs) / len(factor_diffs)
    avg_ratio = sum(ratios) / len(ratios)
    bef_avg =  sum(map(lambda x: x[0], lis)) / len(lis)
    aft_avg =  sum(map(lambda x: x[1], lis)) / len(lis)
    # print(f'{avg_factor_diff = }')
    print(f'{avg_ratio = }')
    print(f'{avg_diff = }')
    print(f'{bef_avg = }')
    print(f'{aft_avg = }')


    plt.xlabel("Bit Difference (After - Before)")
    plt.ylabel("Frequency")
    plt.title("Histogram of Bit Differences")
    plt.hist(diffs, bins=50)
    plt.savefig('diff_histogram.png')
    plt.clf()
    plt.xlabel("Factor Difference (After - Before)")
    plt.ylabel("Frequency")
    plt.title("Histogram of Factor Differences")
    plt.hist(factor_diffs, bins=50)
    plt.savefig('factor_diff_histogram.png')
    plt.clf()
    plt.xlabel("Bit Ratio (After / Before)")
    plt.ylabel("Frequency")
    plt.title("Histogram of Bit Ratios")
    plt.hist(ratios, bins=50)
    plt.savefig('ratio_histogram.png')


if __name__ == '__main__':
    if os.path.dirname(__file__) != os.getcwd():
        raise Exception("Run this script from the directory it is in.")
    check_all_files()
