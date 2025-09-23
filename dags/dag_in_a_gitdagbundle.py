# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
"""Example DAG demonstrating the simplest use of the `@dag` decorator."""

from __future__ import annotations

from airflow.sdk import dag, task


@dag(
    schedule="@daily",
    tags=["gitdagbundle_example"]
)
def dag_in_a_gitdagbundle():
    @task
    def my_task1():
        print("hi")
        return {"a":23, "b":19}

    _my_task_1 = my_task1()

    @task
    def my_task2(my_dict={}):
        print(my_dict)

    my_task2(_my_task_1)


    # @task 
    # def my_task3():
    #     print("hello")

    # my_task3()





dag_in_a_gitdagbundle()
