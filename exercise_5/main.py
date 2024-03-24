import numpy as np
import pandas as pd

import imageio.v3 as iio

from typing import List, Union, Tuple


#######################################################################
# Question 1 - numpy
def get_highest_weight_loss_participant(training_data: np.ndarray, participant_names: List[str]) -> str:
    return participant_names[
        np.apply_along_axis(lambda x: x[-1] - x[0], 1, training_data).argmin()
    ]


def get_diff_data(training_data: np.ndarray) -> np.ndarray:
    return np.apply_along_axis(lambda x: np.diff(x), 1, training_data)


def get_distance_from_linear_change(training_data) -> np.ndarray:
    expected_intervals = np.apply_along_axis(lambda x: np.linspace(x[0], x[-1], len(x)), 1, training_data)
    diffs_from_expected = np.apply_along_axis(lambda x: x[1:-1], 1, training_data.__sub__(expected_intervals))
    return diffs_from_expected


#######################################################################
# Question 2 - image processing
def np_array_to_ascii(darr: np.array) -> str:
    return ''.join([chr(item) for item in darr])


def ascii_to_np_array(s: str) -> np.array:
    return np.frombuffer(s.encode(), dtype=np.uint8)


def arr_dist(a1: np.array, a2: np.array) -> Union[int, float]:
    return a1.astype('int64').__sub__(a2.astype('int64')).__abs__().sum()


def find_best_place(im: np.ndarray, np_msg: np.array) -> Tuple[int, int]:
    best_place, smallest_delta = None, None

    for row_idx, row in enumerate(im):
        for value_idx in range(len(row) - len(np_msg) + 1):

            checked_arr = row[value_idx: value_idx + len(np_msg)]
            checked_arr_grade = arr_dist(checked_arr, np_msg)

            if smallest_delta is None or checked_arr_grade < smallest_delta:
                best_place, smallest_delta = (row_idx, value_idx), checked_arr_grade

    return best_place


def create_image_with_msg(im: np.ndarray, img_idx: Tuple[int, int], np_msg: np.array) -> np.ndarray:
    _im = im.copy()
    row_index, internal_row_index = img_idx
    msg_size = len(np_msg)

    _im[row_index][internal_row_index: internal_row_index + msg_size] = np_msg
    _im[0][0], _im[0][1], _im[0][2] = row_index, internal_row_index, msg_size

    return _im


def put_message(im: np.ndarray, msg: str) -> np.ndarray:
    np_msg = ascii_to_np_array(s=msg)
    best_index = find_best_place(im=im, np_msg=np_msg)
    new_im = create_image_with_msg(im=im, img_idx=best_index, np_msg=np_msg)

    return new_im


def get_message(im: np.ndarray) -> str:
    row_index, internal_row_index, msg_size = im[0][0], im[0][1], im[0][2]
    np_msg = im[row_index][internal_row_index: internal_row_index + msg_size]
    msg = np_array_to_ascii(darr=np_msg)

    return msg


#######################################################################
# Question 3 - pandas
def load_weather_csv(file_name: str) -> pd.DataFrame:
    return pd.read_csv(file_name)


def impute_to_mean(weather_data: pd.DataFrame) -> pd.DataFrame:
    return weather_data.apply(
        lambda x: x if x.name == 'day' else x.fillna(x.mean())
    )


def fix_to_celsius(weather_data: pd.DataFrame) -> pd.DataFrame:
    return weather_data.apply(
        lambda x: x.apply(lambda c: (c - 32) * 5 / 9) if x.min() > 40 else x
    )

# Helper function to run all Question 2 steps in one line.
# feel free to use, but don't change!


def clean_data(weather_data: pd.DataFrame) -> pd.DataFrame:
    return fix_to_celsius(impute_to_mean(weather_data))


def add_week_index(weather_data: pd.DataFrame) -> pd.DataFrame:
    weather_data.loc[:, 'week'] = weather_data.index // 7 + 1
    return weather_data


def get_weekly_mean(weather_data: pd.DataFrame) -> pd.DataFrame:
    prepared_data = clean_data(weather_data=weather_data)
    df_with_week_idx = add_week_index(weather_data=prepared_data)

    result = df_with_week_idx.drop('day', axis=1).groupby('week').mean()
    return result


def get_temperature_range(weather_data: pd.DataFrame) -> pd.Series:
    prepared_data = clean_data(weather_data=weather_data)
    result = prepared_data.drop('day', axis=1).apply(lambda x: x.max() - x.min())

    return result


def find_coastal_effect(weather_data: pd.DataFrame, coastal_cities: List[str]) -> Union[int, float]:
    temp_range_data = get_temperature_range(weather_data=weather_data)
    coastal_cities_mask = temp_range_data.index.isin(coastal_cities)

    coastal_cities_avg, non_coastal_cities_avg = (
        temp_range_data[coastal_cities_mask].mean(), temp_range_data[~coastal_cities_mask].mean()
    )

    return coastal_cities_avg - non_coastal_cities_avg


def add_rainy_days(weather_data: pd.DataFrame) -> pd.DataFrame:
    prepared_data = clean_data(weather_data=weather_data)

    added_row = prepared_data.apply(lambda x: 0 if x.name == 'day' else (x < 20).sum())
    added_row.name = 'Rainy Days'

    return prepared_data.append(added_row)


if __name__ == '__main__':
    def array_compare(a, b, threshold=1e-10):
        if a.shape != b.shape:
            return False
        return np.abs(a - b).max() < threshold

    def df_compare(a, b, threshold=1e-2):
        return array_compare(a.values, b.values, threshold=threshold)

    # Q1 checks
    training_data = np.loadtxt('training_data.csv', delimiter=',')
    participant_names = ['Tali', 'Avi', 'Naomi', 'Shlomi']
    study_months = ['November', 'December', 'January', 'February', 'March', 'April']

    diff_data_expected = np.array([[-2.7, 1.5, -2.7, -2.7, -2.2],
                                   [-4.4, -0.2, -0.7, -1.5, -1.4],
                                   [-1.0, -1.2, 0.6, -0.3, -1.6],
                                   [-2.5, -4.1, -3.1, -2.7, -2.8]])
    distance_from_linear_expected = np.array([[-0.94, 2.32, 1.38, 0.44],
                                              [-2.76, -1.32, -0.38, -0.24],
                                              [-0.3, -0.8, 0.5, 0.9],
                                              [0.54, -0.52, -0.58, -0.24]])

    print(get_highest_weight_loss_participant(training_data, participant_names) == 'Shlomi')
    print(array_compare(get_diff_data(training_data), diff_data_expected))
    print(array_compare(get_distance_from_linear_change(training_data), distance_from_linear_expected))

    # Q2 checks
    sent_message = "thats all folks"
    image_raw = iio.imread('parrot.png')  # read unencrypted image from file

    print(arr_dist(ascii_to_np_array(sent_message), ascii_to_np_array("gettin schwifty")) == 320)
    
    print(find_best_place(image_raw, ascii_to_np_array("Hello")) == (110, 121))

    image_enc = put_message(image_raw, sent_message)
    iio.imwrite('parrot_enc.png', image_enc)  # write encrypted image to file
    retrieved_message = get_message(iio.imread('parrot_enc.png'))
    print(retrieved_message == sent_message)

    # Q3 checks
    coastal_cities = ['haifa', 'zichron_yaakov', 'hadera', 'hakfar_hayarok', 'tel_aviv', 'ashdod', 'ashkelon', 'netanya']
    weather_data = load_weather_csv('weather_data_2023.csv')

    print(df_compare(impute_to_mean(weather_data), pd.read_csv('pandas_results/post_impute.csv')))
    print(df_compare(clean_data(weather_data), pd.read_csv('pandas_results/post_clean_data.csv')))

    weekly_mean = get_weekly_mean(weather_data)
    print(df_compare(weekly_mean, pd.read_csv('pandas_results/weekly_mean.csv', index_col=0)))
    print(weekly_mean.index.name == 'week')

    print(find_coastal_effect(weather_data, coastal_cities) - (-2.79714) < 1e-5)
    
    with_rainy_days = add_rainy_days(weather_data)
    print(df_compare(with_rainy_days, pd.read_csv('pandas_results/with_rainy_days.csv', index_col=0)))
    print(with_rainy_days.index[-1] == 'Rainy Days')
