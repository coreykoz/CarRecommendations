from sklearn.neighbors import NearestNeighbors
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import sys


def suggest_model_given_model(model, year, sugg_count, dataset):
    car_candidates = dataset.loc[(dataset['Model'] == model) & (dataset['Year'] == int(year))]
    if len(car_candidates) == 0:
        #if car cant be found in database, report error
        sys.exit("ERROR: Model not found in Database, check spelling.")

    #Since there are duplicates (read: different trim models but noted as separate rows), focus on the first result only
    car = car_candidates.iloc[0]

    return suggest_model_given_attributes(year, car['Engine HP'], car['Number of Doors'], car['MSRP'], sugg_count, dataset)


def suggest_model_given_attributes(year, hp, doors, msrp, suggestion_count, dataset):
    modified_data = dataset.copy(deep=True)
    del modified_data['Model']
    del modified_data['Make']
    del modified_data['Engine Fuel Type']
    del modified_data['Engine Cylinders']
    del modified_data['Market Category']
    del modified_data['Vehicle Size']
    del modified_data['highway MPG']
    del modified_data['city mpg']
    del modified_data['Popularity']
    del modified_data['Transmission Type']
    del modified_data['Driven_Wheels']
    del modified_data['Vehicle Style']

    #make sure all values are ints- had some weird data type issues
    modified_data['Engine HP'] = modified_data['Engine HP'].astype('int64')
    modified_data['Number of Doors'] = modified_data['Number of Doors'].astype('int64')

    #scale values
    scaler = MinMaxScaler()
    scaler.fit_transform(modified_data)

    #running NearestNeighbors
    nn_classifier = NearestNeighbors(n_neighbors=int(suggestion_count))
    nn_classifier.fit(modified_data)
    neighbors = nn_classifier.kneighbors([[year, hp, doors, msrp]], return_distance=False)

    return neighbors


def table_output(result_array, dataset):
    for index in result_array:
        print(dataset.iloc[index])


if __name__ == '__main__':
    car_data = pd.read_csv("car_data.csv", skip_blank_lines=True)
    car_data = car_data.dropna(axis=0, how ='any')

    if len(sys.argv) == 4:
        result = suggest_model_given_model(sys.argv[1], sys.argv[2], sys.argv[3], car_data)
    elif len(sys.argv) == 6:
        result = suggest_model_given_attributes(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], car_data)
    else:
        sys.exit("USAGE: " + sys.argv[0] + "model year suggestion_count OR year hp door_count msrp suggestion_count")

    print("Based on your input, here are some similar cars:")
    table_output(result, car_data)

