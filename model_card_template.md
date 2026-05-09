# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details
    This model is a supervised machine learning classification model. It was trained to predict whether a person's income is less than $50,000 or greater than $50,000 based on census data. The model uses a Random Forest Classifier from scikit-learn.
    The model was trained using the provided census.csv dataset. Categorical variables were processed with one-hot encoding and the target label was converted into a binary label. The model and encoder were saved to be used by the API.
## Intended Use
    The intended use is to show how data can be processed to train a model for educational purposes only. It should not be used to make decisions.
## Training Data
    The training data is from the census.csv file. It includes demographic, work, education, and financial information, as well as categorical information. The data was split into a training dataset and a test dataset.The training set was used for the encoder, label binarizer and model. The categorical information was one-hot encoded. The salary column was used for the label.
## Evaluation Data
    The evaluation data was from the test split of the census.csv data. It was not used to train the model but was processed using the same label binarizer that the training data used.
    The model was evaluated on the full test data and slices of the test data. The slice evaluation was done for each unique value of the categorical features like education, race, sex, and native country. 
## Metrics
    The metrics used were precision, recall, and F1 score.
    Precision measures how many of the model's positive predictions were correct. Recall measures how many actual positive cases the model found. F1 score combines precision and recall.

    My model's overall performance was:
    Precision: 0.7949
    Recall: 0.5525
    F1: 0.6519

    The model also produced slice metrics shown in the slice_output.txt file. This shows that the model performace varies across categories, specifically when a slice has fewer records.

## Ethical Considerations
    This model includes sensitive data about the population and should not be used to make real life decisions.

## Caveats and Recommendations
    This model was created for educational purposes and should not be used in a production system. 
    A recommendation would be to compare this model to others, examine the slice results further and fine-tune the parameters further.