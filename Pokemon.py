import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial.polynomial import polyfit
import seaborn as sns

dataset = pd.read_csv(os.path.expanduser("~/Desktop/Pokemon/Pokemon.csv"))
data = dataset.loc[:, "Name":"Legendary"]
attack_by_type = {}


#Removes all entries of Pokemon with more an irregular name
def data_cleaner(df):

    names = df['Name']
    bool_mask = ~(names.str.contains(' '))
    cleaned_data = df[bool_mask]
    return cleaned_data


def attack_plotter():

    poke_types = data['Type 1'].unique()

    for type in poke_types:
        selected_rows = data[data['Type 1'] == type]
        mean = selected_rows['Attack'].mean()
        attack_by_type[type] = mean
    average_attack = pd.DataFrame().append(attack_by_type, ignore_index=True)

    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(1, 1, 1)

    bar_positions = np.arange(18) + 0.75
    bar_heights = average_attack.iloc[0].values
    ax.bar(bar_positions, bar_heights, 0.5)

    tick_positions = range(1,19)
    ax.set_xticks(tick_positions)

    ax.set_xticklabels(list(average_attack.columns.values), rotation=90)
    plt.legend(loc="upper left")
    ax.set_title("Pokemon Types vs. Attack")
    plt.show()


#Finding relationship between tankiness and damage output

def hp_vs_attack():
    attack = data['Attack']
    hp = data['HP']

    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(1, 1, 1)

    sns.regplot(attack, hp)
    ax.set_xlabel("Attack")
    ax.set_ylabel("Health Points")
    plt.show()


#Explores whether speed makes you stronger
def speed_vs_attack():

    defense = data['Defense']
    attack = data['Attack']

    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(1, 1, 1)

    ax.scatter(defense, attack)
    ax.set_xlabel("Defense")
    ax.set_ylabel("Attack")
    plt.show()








