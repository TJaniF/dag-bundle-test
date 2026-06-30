from airflow.sdk import dag, task 

@dag(schedule="@daily",) #rerun_with_latest_version=False)
def rerun_latest_bundle_version_dag():

    @task 
    def my_task():
        print("hello")

    my_task()

rerun_latest_bundle_version_dag()
