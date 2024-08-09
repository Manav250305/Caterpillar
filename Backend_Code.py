import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import seaborn as sb

data = pd.read_csv('Main Data Set.csv')

machine_name = input("Enter the machine name: ")
component_name = input("Enter the component name: ")

available_parameters = data[(data['Machine'] == machine_name) &
                            (data['Component'] == component_name)]['Parameter'].unique()
print(f"Available parameters for {component_name} in {machine_name}: {available_parameters}")

parameter_name = input("Enter the parameter name: ")

filtered_data = data[(data['Machine'] == machine_name) &
                     (data['Component'] == component_name) &
                     (data['Parameter'] == parameter_name)]

if not filtered_data.empty:
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=filtered_data, x='Time', y='Value', marker='o')
    plt.title(f'{parameter_name} over Time for {component_name} in {machine_name}')
    plt.xlabel('Time')
    plt.ylabel(parameter_name)
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.show()
else:
    print("No data found for the specified machine, component, and parameter.")
