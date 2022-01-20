# bloodtype
A data transformation of a blood groups' dataset by country. The original blood type dataset was created using web scraping in Python, more details are in [1]. Although the dataset is tidy, the column's type is not useful for data analysis and data visualization, so the goal of the present code is to change to numerical all data that is currently an object pandas type. Don't be misled by the seemingly simplicity of this task, because 'dataframe.pd.to_numeric' will not be enough.

[1] Original dataset page: https://www.kaggle.com/ricardopaula/blood-type-distribution-by-country
