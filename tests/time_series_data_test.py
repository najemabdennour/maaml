from maaml.Datasets.UAH_dataset.time_series import (
    PathBuilder,
    DataReader,
    DataCleaner,
    UAHDatasetBuilder,
)

data_dir_path = "/run/media/najem/34b207a8-0f0c-4398-bba2-f31339727706/home/stock/The_stock/dev & datasets/PhD/datasets/UAH-DRIVESET-v1/"


def indev_test(data_dir_path, conditions_vector=[1, 1, 1, 1]):
    driver1_normal_secondary_gps = PathBuilder(data_dir_path, conditions_vector, 1)
    driver1_normal_secondary_acc = PathBuilder(data_dir_path, conditions_vector, 2)
    reader_gps = DataReader(driver1_normal_secondary_gps.path, "UAHdataset").data
    reader_acc = DataReader(driver1_normal_secondary_acc.path, "UAHdataset").data
    print(f"\ndatset_dir value: \n{driver1_normal_secondary_gps.parent_dir}")
    print(f"\nconditions value: {driver1_normal_secondary_gps.conditions}")
    print(f"file type value: {driver1_normal_secondary_gps.filetype}")
    print(f"driver value: {driver1_normal_secondary_gps.driver}")
    print(f"path value: \n{driver1_normal_secondary_gps.path}")
    print("\nthe GPS reader : \n", reader_gps)
    print("\nWindow stepping static method test :")
    test = DataCleaner.window_stepping(
        data=reader_gps, window_size=60, step=10, average_window=False, verbose=1
    )
    print("\nGPS data preparation: \n")
    gps_data_cleaned = DataCleaner(
        reader_gps,
        average_window=False,
        window_size=0,
        step=0,
        uah_dataset_vector=conditions_vector,
        verbose=1,
    )
    print("\nAccelerometer data preparation: \n")
    acc_data_cleaned = DataCleaner(
        reader_acc,
        average_window=True,
        window_size=10,
        step=10,
        verbose=1,
    )
    print("\nCleaned GPS Data  \n", gps_data_cleaned.dataset)
    print("\nCleaned Accelerometer Data  \n", acc_data_cleaned.dataset)
    print("\nMerging data:\n")
    merged = DataCleaner(
        reader_gps,
        new_data=acc_data_cleaned.dataset,
        average_window=True,
        window_size=0,
        step=0,
        uah_dataset_vector=conditions_vector,
        verbose=1,
    )
    print("\n The merged dataset \n", merged.dataset)


def dataset_builder_test(data_dir_path):
    dataset = UAHDatasetBuilder(
        data_dir_path, 1, 2, window_size_dt2=10, step_dt2=10, verbose=1
    )
    print(
        "\n\033[1m",
        "The UAHDatasetbuilder can take less than 5 minutes to build the full dataset. \n Please wait ..",
        "\033[0m",
    )

    print("\nthe data chunk 1 from the UAHDatasetbuilder class\n", dataset.data_chunk1)
    print("\nthe data chunk 2 from the UAHDatasetbuilder class\n", dataset.data_chunk2)
    print(
        "\nthe data chunks merged from the UAHDatasetbuilder class\n",
        dataset.data_chunk_merged,
    )
    print("\nthe full data from the UAHDatasetbuilder class\n", dataset.data)
    print("\nlength of the path list: ", len(dataset.path_list))


if __name__ == "__main__":
    print("\n\033[1m", "******* BEGIN *******", "\033[0m")
    indev_test(data_dir_path, [6, 3, 2, 1])
    # dataset_builder_test(data_dir_path)
