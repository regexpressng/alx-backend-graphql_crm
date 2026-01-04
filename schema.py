# schema.py
import graphene
from django.contrib.auth.models import User



class Query(graphene.ObjectType):
    hello = graphene.String()

    def resolve_hello(root, info):
        return "Hello, GraphQL"
    
schema = graphene.Schema(query=Query)