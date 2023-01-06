**Connect to MySQL** 

```mysql -u root -p```

-u: user 

root: the MySQL username 

-p: password 

**View Database** 

```mysql> SHOW DATABASES;```

**Create Databases** 


```mysql> CREATE DATABASE IF NOT EXISTS database_name;```

**Select a Database** 

```mysql > USE database_name```

**Create a Table**

    mysql> CREATE TABLE IF NOT EXISTS tb2 (

        col1 INT,

        col2 VARCHAR(20),

        PRIMARY KEY (col1)
        );

**View Tables** 

```mysql> SHOW TABLES;```

