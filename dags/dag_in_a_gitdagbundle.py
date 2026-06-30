from airflow.sdk import dag, task 

@dag
def rerun_latest_bundle_version_dag():

    @task 
    def my_task():
        pass

    my_task()

rerun_latest_bundle_version_dag()
