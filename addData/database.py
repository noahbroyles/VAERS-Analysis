import os
import time
import pymysql


try:
    DBHOST = os.environ['DBHOST']
    DBUSER = os.environ['DBUSER']
    DBPASSWD = os.environ['DBPASSWD']
    DATABASE = os.environ['DATABASE']
except KeyError:
    DBHOST, DBUSER, DBPASSWD, DATABASE = None, None, None, None


class DatabaseError(Exception):
    pass


class Database:

    def __init__(self, server: str = DBHOST, port: int = 1433, database: str = DATABASE, username: str = DBUSER, password: str = DBPASSWD, charset: str = 'UTF-8'):
        self._connection = pymysql.connect(
            user=username,
            password=password,
            host=server,
            database=database,
            charset=charset
        )

    def __enter__(self):
        return self

    def __exit__(self):
        self.close()

    def _prepare_for_params(self, sqlString):
        return sqlString.replace('?', '%s')  # This shit is so old it should be discontinued. SMHHHHHHHHHH

    def query(self, sqlQuery: str, params: list = None, convert_blanks_to_nulls: bool = True):
        """
Parameterizes query and runs in the database, returning the results. Replaces ?'s in query with params in the proper order. Use
for SELECT and EXEC if the stored procedure is meant to return something.
        :param convert_blanks_to_nulls: Uses NULL as a substitute for blank strings ("") in the parameters
        :param sqlQuery: The query to run
        :param params: A list of parameter values to substitute for ?'s in the query
        """

        cursor = self._connection.cursor()

        if params:
            if convert_blanks_to_nulls:
                params = [p if p != "" else None for p in params]
            params = tuple(params)
            sqlQuery = self._prepare_for_params(sqlQuery)
            cursor.execute(sqlQuery, params)
        else:
            cursor.execute(sqlQuery)

        res = cursor.fetchall()
        cursor.close()
        return res

    def execute_proc(self, procCode: str, params: list, commit: bool = False, timeoutSeconds=200, convert_blanks_to_nulls: bool = True):
        """
Run a stored procedure in the database and wait for it to finish
        :param convert_blanks_to_nulls: Uses NULL as a substitute for blank strings ("") in the parameters
        :param procCode: The code to run the stored procedure
        :param params: Any parameters ya might want
        :param commit: Commits after running if True
        :param timeoutSeconds: The max number of seconds to wait
        """
        cursor = self._connection.cursor()
        if params:
            if convert_blanks_to_nulls:
                params = [p if p != "" else None for p in params]
            params = tuple(params)
            procCode = self._prepare_for_params(procCode)
            cursor.execute(procCode, params)

        else:
            cursor.execute(procCode)

        # Wait to finish
        slept = 0
        while cursor.nextset():
            if slept >= timeoutSeconds:
                break
            else:
                time.sleep(1)
                slept += 1

        cursor.close()
        if commit:
            self._connection.commit()

    def execute_stmt(self, sqlStmt: str, params: list = None, commit: bool = False, convert_blanks_to_nulls: bool = True):
        """
Parameterizes statement and runs in the database. Use for INSERT, UPDATE, and DROP commands where no results are expected to be returned.
        :param convert_blanks_to_nulls: Uses NULL as a substitute for blank strings ("") in the parameters
        :param commit: Commits after running if True
        :param sqlStmt: The statement to run
        :param params: Any parameters for the statement
        """

        cursor = self._connection.cursor()
        if params:
            if convert_blanks_to_nulls:
                params = [p if p != "" else None for p in params]
            params = tuple(params)
            sqlStmt = self._prepare_for_params(sqlStmt)
            cursor.execute(sqlStmt, params)
        else:
            cursor.execute(sqlStmt)

        cursor.close()
        if commit:
            self._connection.commit()

    def close(self):
        self._connection.commit()
        self._connection.close()
        del self


class ParameterMismatchError(Exception):
    pass


class PreparedStatement:
    """
    Please please PLEASE only use this class for debugging. It is NOT secure against SQL injections, since it simply substitutes
    parameter placeholders with whatever value they are assigned, with no data validation.
    DO NOT USE WITH UN-SANITIZED USER DATA!!!
    This class is very useful for debugging queries to see how they look with all their parameters in place. For huge SQL statements,
    performance is much slower than just executing the query with the params using Database.execute_stmt() or Database.query().
    """
    
    def __init__(self, sql: str, params: list, convert_blanks_to_nulls: bool = True):
        self._sql = sql
        self._params = params
        self._blank_conversion = convert_blanks_to_nulls
        self._finished_sql_statement: str = ''
        self._prepare()

    def _prepare(self):
        if not self._params:
            self._finished_sql_statement = self._sql
            return
        try:
            param_index = 0
            for char in self._sql:
                if char == '?':
                    if type(self._params[param_index]) == str:
                        if self._params[param_index] == '':
                            if self._blank_conversion:
                                self._finished_sql_statement += 'NULL'
                        else:
                            self._finished_sql_statement += f"""'{self._params[param_index].replace("'", "''")}'"""
                    else:
                        self._finished_sql_statement += str(self._params[param_index])
                    param_index += 1
                else:
                    self._finished_sql_statement += char
        except IndexError:
            raise ParameterMismatchError("The number of parameters in the SQL code did not match the params list")

        self.sql = self.get_finished_sql()

    def get_finished_sql(self):
        return self._finished_sql_statement

    def __str__(self):
        return self.sql

