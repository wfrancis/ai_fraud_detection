import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler


# Function to preprocess data
def preprocess_data(file_path, output_path):
    # Load Data
    data = pd.read_csv(file_path)

    # Feature Engineering
    # Convert trans_date_trans_time to datetime and extract new features
    data['trans_date_trans_time'] = pd.to_datetime(data['trans_date_trans_time'])
    data['trans_year'] = data['trans_date_trans_time'].dt.year
    data['trans_month'] = data['trans_date_trans_time'].dt.month
    data['trans_day'] = data['trans_date_trans_time'].dt.day
    data['trans_hour'] = data['trans_date_trans_time'].dt.hour
    data['trans_minute'] = data['trans_date_trans_time'].dt.minute
    data['trans_second'] = data['trans_date_trans_time'].dt.second

    # Drop the original datetime column
    data.drop(['trans_date_trans_time'], axis=1, inplace=True)

    # Convert categorical variables to numerical using Label Encoding
    label_encoders = {}
    for column in ['merchant', 'category', 'first', 'last', 'gender', 'street', 'city', 'state', 'job']:
        label_encoders[column] = LabelEncoder()
        data[column] = label_encoders[column].fit_transform(data[column])

    # Drop columns that may not be useful for the model directly or might lead to data leakage
    data.drop(['cc_num', 'dob', 'trans_num', 'unix_time'], axis=1, inplace=True)

    # Normalize numerical columns
    scaler = StandardScaler()
    numerical_columns = ['amt', 'lat', 'long', 'merch_lat', 'merch_long']
    data[numerical_columns] = scaler.fit_transform(data[numerical_columns])

    # Handling Missing Values (if any)
    data.ffill(inplace=True)

    # Save the preprocessed data to a new CSV file
    data.to_csv(output_path, index=False)
    print(f"Preprocessing completed. File saved as {output_path}.")


# Preprocess both training and test datasets
preprocess_data('fraudTrain.csv', 'fraudTrain_preprocessed.csv')
preprocess_data('fraudTest.csv', 'fraudTest_preprocessed.csv')
