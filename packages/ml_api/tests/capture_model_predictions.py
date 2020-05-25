"""
This script should only be run in CI.
Never run it locally or you will disrupt the
differential test versioning logic.
"""
from api import config


def capture_predictions(
        *,
        save_file: str = 'test_data_predictions.csv'):
    """Save the test data predictions to a CSV."""

    save_file = 'test_data_predictions.csv'
    test_data = load_dataset(file_name='test.csv')

    # we take a slice with no input validation issues
    multiple_test_json = test_data[99:600]
    multiple_test_input = test_data[99:600]

    predictions = make_prediction(input_data=multiple_test_json)
    predictions = make_prediction(input_data=multiple_test_input)

    # save predictions for the test dataset
    predictions_df = pd.DataFrame(predictions)

    # hack here to save the file to the regression model
    # package of the repo, not the installed package
    predictions_df.to_csv(
        f'{config.PACKAGE_ROOT.parent}/'
        f'regression_model/regression_model/datasets/{save_file}')
    predictions_df.to_csv(f'{config.PACKAGE_ROOT}/{save_file}')

    
if __name__ == '__main__':
    capture_predictions()