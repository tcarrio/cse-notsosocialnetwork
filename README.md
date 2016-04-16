# Please contact me at [tom@carrio.me](mailto:tom@carrio.me) when you have completed the application testing.

### Current Build Status [![Build Status](https://travis-ci.org/tcarrio/cse-notsosocialnetwork.svg?branch=master)](https://travis-ci.org/tcarrio/cse-notsosocialnetwork)

# Server Environment Configuration:
The requirements of the application are configured through either of the following:

* The provided `srv/setup_*` scripts. `srv/setup_srv.sh` is the initial script and installs all packages on a Debian or Ubuntu server.
* The provided `.travis.yml` file describes the required packages for the application. 

You can set this up on any operating system so long as the following is installed:

### Software Level:

* MySQL database
* Python
* Pip

### Python Packages:

* flask
* sqlalchemy
* pymysql
* [sqlalchemy-fulltext-search](https://github.com/mengzhuo/sqlalchemy-fulltext-search)([Clone URI](https://github.com/mengzhuo/sqlalchemy-fulltext-search.git))

### Configuration:

* `config/env_config.py` contains two subclasses that dictate configurations for the application. In latest testing, the MySQL server has been up and running at `nssn.carrio.me:3306`. This can be used for the time being with the following information:
	* **ssh**
		* u: `root`
		* p: `1bTpuZh0k4LPkf9J`
    * **mysql**
    	* u: `root @ localhost`
    	* p: `nssntest`
    	* u: `nssnuser @ %`
    	* p: `2rU9ZFnd2xYMilSb`
    * **folder structure:**
    	* `/opt/nssn/ -> /www2`
    	* Either of these folders are the root directory for the main application
    	* `python3 routes.py` launches the Python controller
* If running this application locally, the application config file **must** be adjusted accordingly. For now the easiest way to is to access the server online to view the application along with our source code. 
* The server is online at [nssn.carrio.me](http://nssn.carrio.me) to view and also connect with the credentials given above. Any further questions, please contact me at [tlcarrio@oakland.edu](tlcarrio@oakland.edu) or [tom@carrio.me](tom@carrio.me).

------------------------------

Members involved:

|Name|Github Username|
|----|---------------|
|Tom Carrio|[tcarrio](https://github.com/tcarrio)|
|Michael Atang|[maatang](https://github.com/maatang)|
|Jon Calvert|[jccalver](https://github.com/jccalver)|
|Wesley Austin|[wjaustin](https://github.com/wjaustin)|

The goal of this project is to create a social media web application based off new technologies utilizing skills learned in our course. The technology stack for our application consists of:

|Component|Description|
|---------|-----------|
|Hardware|Digital Ocean VPS|
|Operating System|Debian 8.3 (jessie)|
|Linux kernel|3.16.0-4 x86_64|
|Client Side Frameworks| Bootstrap 3.3.6|
||JQuery 1.12.0|
|Server Language|Python 3.4.2|
|Server Framework|Flask 0.10.1|
|Database Abstraction|SQLAlchemy 1.0.12|
|Database Server|MySQL 5.5.47|
|Web Design IDE|Adobe Brackets 1.6.1|
|Web Dev IDE|Adobe Brackets 1.6.1|

The running website can be visited at http://nssn.carrio.me
