import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

TITLE = 'TOP front SIF values after branching'
SIMFOLDER = 'C:\\Users\\u1056\\Fracture_Project_simulations\\PULLING\\Classic_numerical_Example\\'
TOPORBOTTOM = 'TOP'
BOTTOM_simulations = ['Experiment_data_15_15_BOTTOM.SIF',
               'Experiment_data_45_45_BOTTOM.SIF',
               'Experiment_data_15_0_BOTTOM.SIF',
               'Experiment_data_30_0_BOTTOM.SIF',
               'Experiment_data_45_0_BOTTOM.SIF',
               'Experiment_data_MY_ANGLES_BOTTOM.SIF',
               'Experiment_data_TRUE_BRANCHES_BOTTOM.SIF']

TOP_simulations = ['Experiment_data_15_15_TOP.SIF',
               'Experiment_data_45_45_TOP.SIF',
               'Experiment_data_15_0_TOP.SIF',
               'Experiment_data_30_0_TOP.SIF',
               'Experiment_data_45_0_TOP.SIF',
               'Experiment_data_MY_ANGLES_TOP.SIF',
               'Experiment_data_TRUE_BRANCHES_TOP.SIF']

# simulations = ['example_analysis_data_initial_lower_insertion.SIF']

def get_sifs_from_simulations(simulations):
    KIs = {}
    KIIs = {}
    KIIIs = {}
    Js = {}
    for simulation in simulations:
        df = pd.read_csv(SIMFOLDER + simulation)

        print(df)
        print('hi')

        KI = []
        KII = []
        KIII = []
        J = []
        for i in range(1, len(df)):
            KI.append(df['KI'][i])
            KII.append(df['KII'][i])
            KIII.append(df['KIII'][i])
            J.append(float(df['J'][i]))
        KIs[simulation] = KI
        KIIs[simulation] = KII
        KIIIs[simulation] = KIII
        Js[simulation] = J
    nodes = np.arange(1,len(df))
    return KIs, KIIs, KIIIs, Js, nodes

def plot_KI(simulations, nodes, KIs):
    plt.figure(figsize=(10,10))

    for simulation in simulations:
        if(simulation.startswith("kink")):
            plt.plot(np.arange(0, len(KIs[simulation]), 1), KIs[simulation], label='Kink = ' + simulation.split('_')[-3])
        else:
            split = simulation.split('_')
            plt.plot(np.arange(0, len(KIs[simulation]), 1), KIs[simulation], label=split[-3] + "/" + split[-2])
    plt.legend(loc ='upper right')
    plt.xlabel("front nodes")
    plt.ylabel('KI (MPa sqrt(mm))')
    plt.title(TITLE.replace("SIF", "KI"))
    plt.savefig(SIMFOLDER + TOPORBOTTOM +"KI_plots.png")
    plt.close()

def plot_KII(simulations, nodes, KIIs):
    plt.figure(figsize=(10,10))

    for simulation in simulations:
        if(simulation.startswith("kink")):
            plt.plot(np.arange(0, len(KIIs[simulation]), 1), KIIs[simulation], label='Kink = ' + simulation.split('_')[-3])
        else:
            split = simulation.split('_')
            plt.plot(np.arange(0, len(KIIs[simulation]), 1), KIIs[simulation], label=split[-3] + "/" + split[-2])
    plt.legend(loc ='upper right')
    plt.xlabel("front nodes")
    plt.title(TITLE.replace("SIF", "KII"))
    plt.ylabel('KII (MPa sqrt(mm))')
    plt.savefig(SIMFOLDER + TOPORBOTTOM +"KII_plots.png")
    plt.close()


def plot_KIII(simulations, nodes, KIIIs):
    plt.figure(figsize=(10,10))

    for simulation in simulations:
        if(simulation.startswith("kink")):
            plt.plot(np.arange(0, len(KIIIs[simulation]), 1), KIIIs[simulation], label='Kink = ' + simulation.split('_')[-3])
        else:
            split = simulation.split('_')
            plt.plot(np.arange(0, len(KIIIs[simulation]), 1), KIIIs[simulation],  label=split[-3] + "/" + split[-2])
    plt.legend(loc ='upper right')
    plt.xlabel("front nodes")
    plt.ylabel('KIII (MPa sqrt(mm))')
    plt.title(TITLE.replace("SIF", "KIII"))
    plt.savefig(SIMFOLDER + TOPORBOTTOM +"KIII_plots.png")
    plt.close()

def plot_J(simulations, nodes, Js):
    plt.figure(figsize=(10,10))

    for simulation in simulations:
        if(simulation.startswith("kink")):
            plt.plot(np.arange(0, len(Js[simulation]), 1), Js[simulation], label='Kink = ' + simulation.split('_')[-3])
        else:
            split = simulation.split('_')
            plt.plot(np.arange(0, len(Js[simulation]), 1), Js[simulation],  label=split[-3] + "/" + split[-2])
    plt.legend(loc ='upper right')
    plt.xlabel("front nodes")
    plt.title(TITLE.replace("SIF", "J"))
    plt.ylabel('J')
    plt.savefig(SIMFOLDER + TOPORBOTTOM +"J_plots.png")
    plt.close()

def plot_combined_J_values(TOP_Js, BOTTOM_Js):
    plt.figure(figsize=(10,10))
    top_keys = list(TOP_Js.keys())
    for simulation in TOP_Js.keys():
        split = simulation.split('_')
        J_top = np.asarray(TOP_Js[simulation])
        J_bot = np.asarray(BOTTOM_Js[simulation.replace("TOP", "BOTTOM")])
        J_eq = np.abs(np.average(J_top)) + np.abs(np.average(J_bot))
        plt.bar(split[-3] + "/" + split[-2], J_eq)
    plt.title('Combined J for both crack fronts')
    plt.ylabel('absolute value of combined J averaged along crack front')
    plt.savefig(SIMFOLDER +"Combined_J_bar_graphs.png")

def plot_combined_KI_values(TOP_KIs, BOTTOM_KIs):
    plt.figure(figsize=(10,10))
    top_keys = list(TOP_KIs.keys())
    for simulation in TOP_KIs.keys():
        split = simulation.split('_')
        J_top = np.asarray(TOP_KIs[simulation])
        J_bot = np.asarray(BOTTOM_KIs[simulation.replace("TOP", "BOTTOM")])
        J_eq = np.abs(np.average(J_top)) + np.abs(np.average(J_bot))
        plt.bar(split[-3] + "/" + split[-2], J_eq)
    plt.title('Combined KI\'s for both crack fronts')
    plt.ylabel('absolute value of combined KI averaged along crack front')
    plt.savefig(SIMFOLDER +"Combined_KI_bar_graphs.png")

def plot_combined_KII_values(TOP_KIIs, BOTTOM_KIIs):
    plt.figure(figsize=(10,10))
    top_keys = list(TOP_KIIs.keys())
    for simulation in TOP_KIIs.keys():
        split = simulation.split('_')
        J_top = np.asarray(TOP_KIIs[simulation])
        J_bot = np.asarray(BOTTOM_KIIs[simulation.replace("TOP", "BOTTOM")])
        J_eq = np.abs(np.average(J_top)) + np.abs(np.average(J_bot))
        plt.bar(split[-3] + "/" + split[-2], J_eq)
    plt.title('Combined KII for both crack fronts')
    plt.ylabel('absolute value of combined KII averaged along crack front')
    plt.savefig(SIMFOLDER +"Combined_KII_bar_graphs.png")


# KIs, KIIs, KIIIs, Js, nodes = get_sifs_from_simulations(bottom_simulations)

# plot_KI(bottom_simulations, nodes, KIs)
# plot_KII(bottom_simulations, nodes, KIIs)
# plot_KIII(bottom_simulations, nodes, KIIIs)
# plot_J(bottom_simulations, nodes, Js)

TOP_KIs, TOP_KIIs, TOP_KIIIs, TOP_Js, nodes = get_sifs_from_simulations(TOP_simulations)
BOTTOM_KIs, BOTTOM_KIIs, BOTTOM_KIIIs, BOTTOM_Js, nodes = get_sifs_from_simulations(BOTTOM_simulations)
plot_combined_J_values(TOP_Js, BOTTOM_Js)
plot_combined_KI_values(TOP_KIs, BOTTOM_KIs)
plot_combined_KII_values(TOP_KIIs, BOTTOM_KIIs)
print("here")
# plot_KI(simulations, nodes, KIs)
# plot_KII(simulations, nodes, KIIs)
# plot_KIII(simulations, nodes, KIIIs)
# plot_J(simulations, nodes, Js)