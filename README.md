# openfisca-djangoapi-template

This is a template for a database and Django webserver layer for serving OpenFisca variables.


## Use Cases & Features
We import variables from an Openfisca Web API to the database and improve on the readability of the variables, link and display the dependencies of each variable. 



#### Monitor OpenFisca Variables and their dependencies
There are two visualisation tools that could be useful for monitoring the variables in the database.

**1. displaying all variables**
We summarise all variables in the database by a bar chart arranged by their total number of dependencies, i.e. the number of children (those variables needed to compute this variable) and the number of parents (i.e. variables depending on this variable)

   `</plots/id>` gives this arranges the barchart by variable name (id) and 
   `</plots/alias>` provides an alternative by a more readable form of variable name, i.e. after removing the undersores.

**2. displaying the dependency graph of a variable**
For each variable, one can display the entire dependency graph by searching through children by multiple depth. We further annotated the type of node in the graph by whether it is an input variable (i.e. requiring user input) or output variable (i.e. no parents) or intermediate variables (i.e. with both parents and children)
    
 `</plots/graph/<var:id>>` gives such a dependency graph of a variable with `<var:id>`




#### Injest OpenFisca Variables to Frontend UI

This database is ideal in further annotating the variables (e.g. making them more readable by giving proper alias name, regulation reference or other data structure for a particular legislation).

Here we have annotated each variable using a metadata tag.  You can download this version of Openfisca Core to enable this function in your OpenFisca Repo directly. [Reference Github Openfisca core metadata tag version](http://github.com/..) #TODO


Here is an example of a metadata tag, consisting of three attributes.
   
   `<variable-type>`: depending on the number of children and parents, it is one of input, output or intermediary type 
   `<alias>` : derived from the variable name by removing underscores
   `<input_offspring>`: a list of all input dependencies, can be rendered in an UI for user input. 

```
    "metadata": {
            "variable-type": "output",
            "alias": "Maternity Benefits Is Eligible For Maternity Benefit",
            "input_offspring": [
                "maternity_benefits__weeks_after_birth_of_child",
                "maternity_benefits__weeks_to_due_date"
            ]
        },
```
This is automatically generated based on input variables from OpenFisca Web API. These are then used in the visualisation component. 



#### Calculation API for variables with formulae




## Serving Locally and Deploying

#### Serving locally
This repo can be served in two ways:
1) Serve with a local development environment :heavy_check_mark:
   - Instructions in [local_deployment.md](docs/local_deployment.md)
2) Serve with Docker
   - Not recommended (this functionality is currently broken :warning:) :warning:
   - Instructions in [docker_deployment.md](docs/docker_deployment.md) 


#### Deploying
- This app can be deployed in a number of ways, we'll leave that up to you :wink:
- But, here are some considerations
   - This app uses a sqlite3 database. SQLite runs in memory, and backs up its data store in files on disk. Thus, a persistent filesystem is required - and platforms with ephemeral filesystems (such as Heroku) are not suitable.
   - The authors of this repo use AWS ElasticBeanstalk, because it has a persistent filesystem. AWS ElasticBeanstalk requires a few additional config files, located at `/.ebextensions` and `/.platform`. Additional info on ElasticBeanstalk can be found at [aws_elasticbeanstalk_instructions.md](docs/aws_elasticbeanstalk_instructions.md).
 

## Serve with a local development environment (recommended)
We recommend you build and serve this Django application locally.

To do this, follow these instructions: [local_deployment.md](docs/local_deployment.md).

## Serve with Docker
Not recommended (this functionality is currently broken :warning:)

To do this, follow these instructions: [docker_deployment.md](docs/docker_deployment.md).


## Awesome resources

See [additional_resources.md](docs/additional_resources.md) to learn more about all the different components used in this repository.
