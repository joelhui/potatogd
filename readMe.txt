#Potato Gene-Disease Curation Platform

##Introduction
This system is a curation platform for potato gene-disease data, designed to provide efficient data storage and retrieval capabilities. All data is stored in a MySQL database, so it is necessary to ensure that MySQL is installed and configured before using this system.

#System Requirements
##Python 3.x
##MySQL Database
Installation Guide
Install Python Dependencies
Ensure Python is installed and install the required Python libraries with the following command:
>pip install pymysql flask

#MySQL Database Configuration
Install the MySQL database. Please refer to the MySQL official documentation for specific installation steps.
Configure the database connection information. Modify the database configuration in the db.py file, for example:

	host="localhost", 
	user="your_username", 
	password="your_password", 
	database="your_database"
	
#Data Format
The data format for this platform is as follows:

	data = {
    		'sub': sub,
    		'sub_type': sub_type,
    		'sc': subc,
    		'relation': relation,
    		'obj': obj,
    		'obj_type': ob_type,
    		'oc': 'oc',
    		'pmid': pmid,
    		'sentence': sentence
	}
	
	The meaning of each field is as follows:

		sub: Subject
		sub_type: Subject Type
		sc: Subcategory
		relation: Relation
		obj: Object
		obj_type: Object Type
		oc: Additional Information
		pmid: PubMed ID
		sentence: Sentence
	
#Running the Platform
After completing the above steps, you can start the platform for data curation operations. Ensure the database connection is correct and all dependencies are installed.
You can run python app.py directly in the console.
	> python app.py
License
This project follows the MIT License.

For further assistance or any questions, please contact the development team.