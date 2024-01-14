import mindsdb_sdk
from decouple import config
import pandas as pd

server = mindsdb_sdk.connect('http://127.0.0.1:47334')

# Get all databases.
all_dbs = server.list_databases()
db_names = [i.name for i in all_dbs]
print(all_dbs)
print(db_names)

# Get the default project for creating a model
project = server.get_project('eduminds')


# create ml engine
try:
    server.ml_engines.create(
        'learning_path',
        'openai',
        connection_data={'api_key': config('OPENAI_API_KEY')},
    )
except RuntimeError:
    print('ML engine already exists')

try:
    # create model
    sentiment_classifier = project.models.create (
        name='sentiment_classifier',
        engine='learning_path', # alternatively: engine=server.ml_engines.openai
        predict='sentiment',
        options={
            'prompt_template':'answer this question: {{questions}}',
            'model_name':'gpt4'
        }
    )
except RuntimeError:
    print('Model already exists')

my_model = project.list_models()[0]

rs = server.get_database('files').query('SELECT * FROM file_name')
df = pd.DataFrame(rs.fetch())

prompt = f"With all the data in this database, can you create a learning path for this user. The learning path should fit to the users goals which are {df['goals'].iloc[0]} and information on the pandas dataframe. It should have links to resources and a max of 5 resources. The user's subjects of interest are {df['subjects_of_interest'].iloc[0]}."
print(prompt)
# my_model.predict({"text": question})




# List ML Engine
# print(server.ml_engines.list())
# print(dir(server.ml_engines))
"""
mindsdb = server.get_project('mindsdb')

# Show data handlers
data_handlers = mindsdb.query('SHOW HANDLERS WHERE type = \'data\'')
print(data_handlers.fetch())

# show all databases
print(server.list_databases())

# Show ML handlers
ml_handlers = mindsdb.query('SHOW HANDLERS WHERE type = \'ml\'')
print(ml_handlers.fetch())




"""