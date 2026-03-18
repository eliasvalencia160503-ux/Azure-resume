import json
import os

import azure.functions as func
from azure.cosmos import CosmosClient, exceptions


def get_container():
    endpoint = os.environ["COSMOS_ENDPOINT"]
    key = os.environ["COSMOS_KEY"]
    database_name = os.environ["COSMOS_DATABASE_NAME"]
    container_name = os.environ["COSMOS_CONTAINER_NAME"]

    client = CosmosClient(endpoint, credential=key)
    database = client.get_database_client(database_name)
    container = database.get_container_client(container_name)
    return container


def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        container = get_container()
        item = container.read_item(item="1", partition_key="1")

        current_count = int(item.get("count", 0))
        new_count = current_count + 1
        item["count"] = new_count

        container.upsert_item(item)

        return func.HttpResponse(
            json.dumps({"count": new_count}),
            mimetype="application/json",
            status_code=200
        )

    except exceptions.CosmosResourceNotFoundError:
        return func.HttpResponse(
            json.dumps({"error": 'Counter item with id "1" was not found.'}),
            mimetype="application/json",
            status_code=404
        )
    except Exception as e:
        return func.HttpResponse(
            json.dumps({"error": str(e)}),
            mimetype="application/json",
            status_code=500
        )