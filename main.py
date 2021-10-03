from time import perf_counter
import config
import pandas as pd
import Levenshtein
import swifter
from multiprocessing import Pool

#collect vars and set up base dataframe
config.distance
config.in_list
main_df = pd.read_csv(config.trusted_domains_file)
main_df.columns = ['domain']

def calculate_distance(record):
    """Copy global dataframe, perform risk calculation"""
    df = main_df.copy(deep=True)
    df['distance'] = df['domain'].swifter.progress_bar(False).apply(lambda x: Levenshtein.distance(x, config.in_list[record]))
    #print(df)
    risk = ((df['distance'] <= config.distance) & (df['distance'] != 0)).any()
    #print(risk)
    return {"domain": config.in_list[record], "risky": risk}

def main():
    """Main function"""
    start = perf_counter()
    calc_pool = Pool(processes=len(config.in_list))
    risky = calc_pool.map(calculate_distance, range(len(config.in_list)))
    stop = perf_counter()
    print({
        "Performance": stop - start,
        "Input Metric": config.distance,
        "Risky Domains List": risky
    })

if __name__ == '__main__':
    main()
