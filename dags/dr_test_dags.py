from airflow.sdk import dag, task, chain, Asset
from datetime import datetime

@dag(
    start_date=datetime(2026, 1, 1),
    schedule="@hourly",
)
def start_dag():

    @task 
    def upstream_dtm():
        import random
        return [random.randint(1, 100) for _ in range(random.randint(1, 10))]

    _upstream_dtm = upstream_dtm() 

    @task 
    def transform_dtm(num):
        return num ** 2

    _transform_dtm = transform_dtm.expand(num=_upstream_dtm)

    for i in range(30):

        @task(task_id=f"parallel_task_{i}")
        def parallel_task():
            import time
            import random
            time.sleep(random.randint(1, i))
            return f"Hello World {i}"

        _parallel_task = parallel_task()


    sequential_task_list = []

    for i in range(30):

        @task(task_id=f"sequential_task_{i}")
        def sequential_task():
            import time
            import random
            time.sleep(random.randint(1, i))
            return f"Hello World {i}"

        _sequential_task = sequential_task()
        sequential_task_list.append(_sequential_task)


    @task(outlets=[Asset(name="output_asset1")])
    def downstream_task():
        return "Hello World"

    chain(*sequential_task_list, downstream_task())


start_dag()


@dag(
    schedule=[Asset(name="output_asset1")]
)
def downstream_dag():
    @task(outlets=[Asset(name="output_asset2")])
    def d1():
        import time
        time.sleep(10)
        return "Hello World"

    d1()

downstream_dag()


@dag(
    schedule=[Asset(name="output_asset2")]
)
def downstream_dag2():
    @task(outlets=[Asset(name="output_asset3")])
    def d2():
        return "Hello World"

    d2()

downstream_dag2()


@dag(
    schedule=[Asset(name="output_asset3")]
)
def downstream_dag3():
    @task(outlets=[Asset(name="output_asset4")])
    def d3():
        return "Hello World"

    d3()

downstream_dag3()

@dag(
    schedule=[Asset(name="output_asset1"), Asset(name="output_asset2")]
)
def downstream_dag4():
    @task(outlets=[Asset(name="output_asset5")])
    def d4():
        return "Hello World"

    d4()

downstream_dag4()


@dag(
    schedule=[Asset(name="output_asset5"), Asset(name="output_asset3"), Asset(name="output_asset4")]
)
def downstream_dag5():
    @task(outlets=[Asset(name="output_asset6")])
    def d5():
        return "Hello World"

    d5()

downstream_dag5()